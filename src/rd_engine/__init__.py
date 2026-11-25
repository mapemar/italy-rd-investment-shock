"""Reusable ingestion and evidence-provenance primitives for the R&D engine."""

from .provenance import (
    append_jsonl_record,
    build_evidence_record,
    canonicalize_url,
    content_version_id,
    download_and_ingest,
    ingest_bytes,
    stable_document_id,
    validate_evidence_record,
)

__all__ = [
    "append_jsonl_record",
    "build_evidence_record",
    "canonicalize_url",
    "content_version_id",
    "download_and_ingest",
    "ingest_bytes",
    "stable_document_id",
    "validate_evidence_record",
]
