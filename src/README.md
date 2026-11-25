# Source code

The reusable Python package currently starts with `rd_engine.provenance`.

## Implemented
- `rd_engine/provenance.py`: HTTPS source URL canonicalisation, stable document identity, content-version hashing, immutable raw-byte ingestion, provenance records and checksum validation.

## Planned modules
- `document_reader/`: PDF/HTML/XLSX ingestion and page/sheet/table extraction.
- `entity_resolution/`: project, CUP, beneficiary and institutional-sector matching.
- `financial_reconciliation/`: funding-chain reconciliation and annual allocation.
- `frascati/`: evidence-based activity and cost classification.
- `additionality/`: parameter management and counterfactual estimation.
- `shock_estimation/`: annual scenarios and model exports.

Keep modules independently testable. Deterministic transformations belong in Python; LLM outputs are candidate evidence/classifications and must retain source locators and reviewer status. Do not create empirical calculations before the input schema and evidence requirements are agreed.
