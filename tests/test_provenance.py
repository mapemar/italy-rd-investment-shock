from __future__ import annotations

import hashlib
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from rd_engine.provenance import (
    canonicalize_url,
    content_version_id,
    ingest_bytes,
    stable_document_id,
    validate_evidence_record,
)


class ProvenanceTests(unittest.TestCase):
    def test_canonicalize_url_preserves_query_and_removes_fragment(self) -> None:
        self.assertEqual(
            canonicalize_url("HTTPS://Example.COM:443/a?b=2#page=3"),
            "https://example.com/a?b=2",
        )

    def test_non_https_url_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            canonicalize_url("http://example.com/document.pdf")

    def test_document_identity_is_independent_of_file_version(self) -> None:
        first = stable_document_id(" Ministry of Research ", "Annual report 2025")
        second = stable_document_id("ministry of research", "Annual   report 2025")
        self.assertEqual(first, second)
        self.assertNotEqual(content_version_id(b"version 1"), content_version_id(b"version 2"))

    def test_ingestion_is_idempotent_and_preserves_versions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            timestamp = datetime(2026, 11, 25, tzinfo=timezone.utc)
            first = ingest_bytes(
                b"official source bytes",
                institution="MUR",
                document_title="PRIN report",
                source_url="https://example.gov.it/report.pdf#page=1",
                raw_root=root,
                run_id="test-run-001",
                retrieved_at=timestamp,
                filename="report.pdf",
                content_type="application/pdf",
            )
            repeated = ingest_bytes(
                b"official source bytes",
                institution="MUR",
                document_title="PRIN report",
                source_url="https://example.gov.it/report.pdf",
                raw_root=root,
                run_id="test-run-002",
                retrieved_at=timestamp,
                filename="report.pdf",
                content_type="application/pdf",
            )
            revised = ingest_bytes(
                b"revised official source bytes",
                institution="MUR",
                document_title="PRIN report",
                source_url="https://example.gov.it/report.pdf",
                raw_root=root,
                run_id="test-run-003",
                retrieved_at=timestamp,
                filename="report.pdf",
                content_type="application/pdf",
            )
            self.assertEqual(first["raw_path"], repeated["raw_path"])
            self.assertEqual(first["version_id"], repeated["version_id"])
            self.assertNotEqual(first["version_id"], revised["version_id"])
            self.assertTrue((root / first["raw_path"]).is_file())
            self.assertTrue((root / revised["raw_path"]).is_file())
            self.assertEqual(validate_evidence_record(first, root), [])

    def test_validation_detects_tampered_raw_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            record = ingest_bytes(
                b"source bytes",
                institution="MIMIT",
                document_title="Measure decree",
                source_url="https://example.gov.it/decree.pdf",
                raw_root=root,
                run_id="test-run",
            )
            raw_file = root / record["raw_path"]
            raw_file.chmod(0o644)
            raw_file.write_bytes(b"changed bytes")
            errors = validate_evidence_record(record, root)
            self.assertIn("sha256_mismatch", errors)
            self.assertIn("version_id_mismatch", errors)


if __name__ == "__main__":
    unittest.main()
