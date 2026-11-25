"""Immutable source ingestion and evidence provenance.

This module deliberately handles bytes and provenance only. It does not interpret
source content, classify R&D, or convert financial observations into expenditure.
Those tasks belong to downstream, separately reviewable stages.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


REQUIRED_RECORD_FIELDS = (
    "document_id",
    "version_id",
    "document_title",
    "institution",
    "source_url",
    "retrieved_at_utc",
    "sha256",
    "raw_path",
    "ingestion_status",
    "run_id",
)


def canonicalize_url(url: str) -> str:
    """Return a conservative canonical form for an HTTPS source URL.

    Query parameters are preserved as supplied: changing their order can change
    semantics on some public data portals. Fragments are removed because they
    do not identify a different downloadable resource.
    """
    parsed = urllib.parse.urlsplit(url.strip())
    if parsed.scheme.lower() != "https" or not parsed.hostname:
        raise ValueError("Only absolute HTTPS source URLs are accepted.")
    if parsed.username or parsed.password:
        raise ValueError("URLs containing embedded credentials are not accepted.")
    host = parsed.hostname.lower()
    port = parsed.port
    netloc = host if port in (None, 443) else f"{host}:{port}"
    path = parsed.path or "/"
    return urllib.parse.urlunsplit(("https", netloc, path, parsed.query, ""))


def _normalise_identity_part(value: str) -> str:
    value = re.sub(r"\s+", " ", value.strip().casefold())
    if not value:
        raise ValueError("Institution and title must be non-empty.")
    return value


def stable_document_id(institution: str, document_title: str) -> str:
    """Create a stable identity from issuer + title, not from file contents.

    If an issuer changes the title materially, the crosswalk must be reviewed;
    do not silently infer that two differently titled documents are identical.
    """
    identity = "\x1f".join(
        (_normalise_identity_part(institution), _normalise_identity_part(document_title))
    )
    digest = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:20]
    return f"doc_{digest}"


def content_version_id(content: bytes) -> str:
    """Identify an exact byte version; identical bytes yield the same ID."""
    return f"ver_sha256_{hashlib.sha256(content).hexdigest()}"


def _safe_suffix(filename: str | None, content_type: str | None) -> str:
    suffix = Path(filename or "").suffix.lower()
    if suffix and re.fullmatch(r"\.[a-z0-9]{1,8}", suffix):
        return suffix
    guessed = (content_type or "").split(";", 1)[0].strip().lower()
    return {
        "application/pdf": ".pdf",
        "text/plain": ".txt",
        "text/html": ".html",
        "application/json": ".json",
        "application/zip": ".zip",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": ".xlsx",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ".docx",
    }.get(guessed, ".bin")


def ingest_bytes(
    content: bytes,
    *,
    institution: str,
    document_title: str,
    source_url: str,
    raw_root: str | Path,
    run_id: str,
    retrieved_at: datetime | None = None,
    filename: str | None = None,
    content_type: str | None = None,
) -> dict[str, Any]:
    """Store a source version under a content-addressed immutable path.

    Re-ingesting identical bytes is idempotent. A prior file is never replaced.
    """
    if not isinstance(content, bytes) or not content:
        raise ValueError("Source content must be non-empty bytes.")
    if not run_id.strip():
        raise ValueError("run_id must be non-empty.")

    timestamp = retrieved_at or datetime.now(timezone.utc)
    if timestamp.tzinfo is None:
        raise ValueError("retrieved_at must be timezone-aware.")
    timestamp = timestamp.astimezone(timezone.utc)

    canonical_url = canonicalize_url(source_url)
    document_id = stable_document_id(institution, document_title)
    version_id = content_version_id(content)
    digest = hashlib.sha256(content).hexdigest()
    suffix = _safe_suffix(filename, content_type)
    relative_path = Path("documents") / document_id / f"{version_id}{suffix}"
    destination = Path(raw_root) / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)

    try:
        fd = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o444)
    except FileExistsError:
        existing_digest = hashlib.sha256(destination.read_bytes()).hexdigest()
        if existing_digest != digest:
            raise RuntimeError(f"Immutable raw-file collision at {destination}")
    else:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        destination.chmod(0o444)

    return {
        "document_id": document_id,
        "version_id": version_id,
        "document_title": document_title.strip(),
        "institution": institution.strip(),
        "source_url": canonical_url,
        "retrieved_at_utc": timestamp.isoformat(),
        "sha256": digest,
        "raw_path": relative_path.as_posix(),
        "content_type": content_type,
        "byte_size": len(content),
        "ingestion_status": "raw_ingested",
        "run_id": run_id,
    }


def download_and_ingest(
    source_url: str,
    *,
    institution: str,
    document_title: str,
    raw_root: str | Path,
    run_id: str,
    timeout_seconds: int = 60,
    max_bytes: int = 100_000_000,
) -> dict[str, Any]:
    """Download one HTTPS source and preserve its exact bytes and provenance."""
    canonical_url = canonicalize_url(source_url)
    request = urllib.request.Request(
        canonical_url,
        headers={"User-Agent": "italy-rd-investment-shock/0.1 (research provenance)"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            content = response.read(max_bytes + 1)
            if len(content) > max_bytes:
                raise ValueError(f"Source exceeds configured limit of {max_bytes} bytes.")
            content_type = response.headers.get("Content-Type")
            disposition = response.headers.get("Content-Disposition", "")
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not retrieve source URL: {canonical_url}") from exc

    filename = None
    match = re.search(r'filename\*?=(?:UTF-8\'\')?"?([^";]+)', disposition, re.I)
    if match:
        filename = urllib.parse.unquote(match.group(1).strip().strip('"'))

    return ingest_bytes(
        content,
        institution=institution,
        document_title=document_title,
        source_url=canonical_url,
        raw_root=raw_root,
        run_id=run_id,
        filename=filename,
        content_type=content_type,
    )


def build_evidence_record(**fields: Any) -> dict[str, Any]:
    """Validate and return a JSON-serialisable provenance record."""
    missing = [field for field in REQUIRED_RECORD_FIELDS if not fields.get(field)]
    if missing:
        raise ValueError(f"Evidence record missing required fields: {', '.join(missing)}")
    record = dict(fields)
    record["source_url"] = canonicalize_url(str(record["source_url"]))
    return record


def validate_evidence_record(record: Mapping[str, Any], raw_root: str | Path) -> list[str]:
    """Return validation errors; an empty list means the record passes basic QA."""
    errors = [f"missing:{key}" for key in REQUIRED_RECORD_FIELDS if not record.get(key)]
    if errors:
        return errors
    try:
        canonical = canonicalize_url(str(record["source_url"]))
        if canonical != record["source_url"]:
            errors.append("source_url_not_canonical")
    except ValueError:
        errors.append("invalid_source_url")
    path = Path(raw_root) / str(record["raw_path"])
    if not path.is_file():
        errors.append("raw_file_missing")
        return errors
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != record["sha256"]:
        errors.append("sha256_mismatch")
    if content_version_id(path.read_bytes()) != record["version_id"]:
        errors.append("version_id_mismatch")
    return errors


def append_jsonl_record(path: str | Path, record: Mapping[str, Any]) -> None:
    """Append one provenance event to an append-only JSONL ledger."""
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(dict(record), ensure_ascii=False, sort_keys=True)
    with destination.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")
        handle.flush()
        os.fsync(handle.fileno())
