# Tests

Run the standard-library test suite from the repository root:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Current synthetic tests cover:
- HTTPS URL canonicalisation and rejection of non-HTTPS URLs;
- stable document identity versus content-specific version IDs;
- idempotent ingestion and preservation of revised source versions;
- checksum and version mismatch detection.

Planned test coverage:
- schema validation and source-locator completeness;
- unit and price-basis conversions;
- missing-value handling;
- annual aggregation and transaction-date allocation;
- PNRR/national funding overlap and double-counting checks;
- R&D eligibility and channel classification rules;
- additionality calculations and scenario bounds;
- statistical series transformations.

Use synthetic fixtures for unit tests. Never use fabricated data as empirical project evidence.
