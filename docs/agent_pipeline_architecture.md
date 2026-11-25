# Agent pipeline architecture and implementation sequence

**Status:** implementation foundation, 25 November 2026  
**Scope:** PNRR core. The national 2018–2025 fiscal-measures census remains a separate workstream.

## 1. Design rule

The project should use agents to reduce repetitive research and extraction work, not to delegate accounting judgement or causal identification to an opaque model.

The architecture separates four functions:

1. **Source and extraction agent (A01–A02, then A05–A07):** discovers official sources, records versions, downloads source bytes, extracts tables/text and proposes structured records.
2. **Reconciliation agent (A03–A04 and A08):** resolves measure/project/CUP/beneficiary identifiers, maps institutions and funding chains, and flags potential overlaps.
3. **R&D assessment and estimation agent (A07, A10–A12):** proposes Frascati classifications and evidence-based parameter candidates. It cannot promote assumptions to validated estimates or claim causal identification.
4. **Independent QA agent (A09 and review):** checks schemas, provenance, totals, dates, missingness, double counting and consistency with the approved methodology.

A workflow orchestrator coordinates tasks and routes uncertain or consequential cases to human review. The existing A01–A13 backlog in the PRIN 2022 pilot remains the authoritative workflow inventory; this document does not replace it.

## 2. Separation of responsibilities

| Layer | Permitted operations | Prohibited shortcut |
|---|---|---|
| Source catalogue | Discover, identify and version official sources | Treat a catalogue entry as a downloaded source |
| Raw ingestion | Download and preserve exact bytes, URL, timestamp and checksum | Rewrite or silently replace a prior source version |
| Extraction | Parse text/tables and retain page/table/row locators | Present extracted text as validated evidence |
| Structured evidence | Create candidate records with source lineage | Fill missing values with zero or infer unsupported fields |
| Reconciliation | Match stable IDs and expose conflicts | Match or merge solely by row counts or names |
| R&D assessment | Apply Frascati criteria and record rationale/uncertainty | Infer R&D from labels such as innovation, digital or technology |
| Financial reconstruction | Keep appropriations, commitments, payments, beneficiary costs and performance years separate | Equate cash disbursement with R&D performed |
| Additionality | Assemble evidence and scenario parameters | Present a model judgement as a causal estimate |
| Publishing | Produce versioned, validated datasets and run reports | Overwrite prior validated outputs |

Python should perform deterministic operations (hashing, parsing, joins, accounting checks, annual allocation and calculations). An LLM may propose extraction, classification and reconciliation candidates, each with evidence references and confidence. Human approval remains required for ambiguous Frascati boundaries, material financial conflicts, additionality assumptions and final validation.

## 3. First implemented component: immutable source provenance

The initial package `src/rd_engine/provenance.py` implements the raw-ingestion boundary:

- accepts absolute HTTPS URLs only and removes URL fragments while preserving query strings;
- creates a stable `document_id` from issuing institution + document title;
- creates a content-specific `version_id` and SHA-256 checksum from exact bytes;
- stores bytes below `data/raw/documents/<document_id>/<version_id>.<suffix>`;
- uses exclusive file creation: an existing version is never overwritten;
- treats identical bytes as an idempotent re-ingestion;
- records retrieval timestamp, URL, content type, byte size, raw path and run ID;
- validates that the stored bytes still match the recorded checksum and version ID;
- supports an append-only JSONL provenance event ledger.

The document identity and content version are deliberately different. A revised document should retain the same document identity where issuer and title are unchanged, but receive a new content version. If a source changes its title or issuer, any identity crosswalk must be reviewed rather than inferred.

Example (run from repository root):

```python
from rd_engine.provenance import download_and_ingest, append_jsonl_record

record = download_and_ingest(
    "https://example.gov.it/source.pdf",
    institution="Issuing public administration",
    document_title="Official source title",
    raw_root="data/raw",
    run_id="pnrr-source-ingestion-2026-11-25-001",
)
append_jsonl_record("data/intermediate/provenance/source_events.jsonl", record)
```

The example URL is illustrative only; it is not a project source. Actual ingestion must use a verified URL from the project source catalogue or an independently verified official source.

## 4. Data-layer contract

The pipeline must preserve the following progression:

- `data/raw/`: immutable source bytes and original source exports;
- `data/intermediate/`: extracted text/tables, candidate records, provenance events and reconciliation logs;
- `data/processed/`: validated analytical tables only;
- `outputs/`: versioned estimates, tables and reports.

Raw files are not committed automatically. Before committing a source, check licensing, confidentiality, file size and repository policy. A provenance record may point to an externally stored source where redistribution is not permitted.

An extracted observation must carry, at minimum, a source document/version reference and a precise locator (page, table, sheet, row, legal provision or API observation key). A model-generated value without a source locator must remain an assumption/candidate, not an extracted fact.

## 5. Implementation sequence

| Step | Existing workflow IDs | Deliverable | Acceptance gate |
|---|---|---|---|
| 1. Source provenance | A01–A02 | Immutable ingestion, document/version registry, extraction run IDs | Same bytes are idempotent; changed bytes create a new version; checksums validate |
| 2. Structured extraction | A02, A05 | PDF/HTML/XLSX/table extractors with page/sheet/row locators | Synthetic fixtures and source-specific QA pass |
| 3. Entity resolution | A03–A04 | CUP/project/beneficiary/institution crosswalks | Ambiguous matches remain unresolved and visible |
| 4. Financial reconciliation | A06, A08 | Transaction-date allocation, funding-chain and duplicate controls | Cash, commitments, beneficiary costs and R&D performance remain distinct |
| 5. Frascati assessment | A07 | Cost-category/activity crosswalk with evidence and reviewer state | No automatic inclusion of generic innovation or capital expenditure |
| 6. Independent QA | A09 | Automated checks and exception queue | No silent missing-to-zero conversions or unexplained reconciliation breaks |
| 7. Research and macro linkage | A10–A13 | Output linkage, additionality evidence, annual aggregation and publishing | Strict R&D and broad innovation proxy remain separate |

The first end-to-end pilot remains PRIN 2022 PNRR. It must not be scaled to the national portfolio until source ingestion, reporting periods, local-unit identification, cost classification and transaction-date allocation have passed the pilot acceptance gates.

## 6. Current limitations

- The current code implements raw-byte provenance only; it does not yet parse PDF/Excel files or call an LLM.
- The source catalogue in `config/sources.yaml` is the existing project catalogue; this first component does not rewrite or reinterpret it.
- A stable document ID based on issuer + title is a deterministic starting key, not a substitute for a reviewed document crosswalk.
- The ingestion function does not certify that a source is authoritative, that its contents are complete, or that an extracted amount is correct.
- Tests use synthetic byte fixtures. No empirical R&D figures are created by this module.

## 7. Reproducible test command

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

No API credentials or external Python packages are required for the provenance module.
