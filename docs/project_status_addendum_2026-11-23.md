# Project status addendum — 23 November 2026

This addendum records the integration of recent chat work into the existing repository. The canonical project status remains in `docs/project_status.md`; the current methodology, research perimeter and decisions in the repository take precedence.

## Newly registered evidence and working artefacts

- **Historical national fiscal census:** v18 and v19 chat extraction notes are archived under `documents/workstream_notes/historical_census/`. The original Excel workbooks were not available for upload. The census remains a separate 2018–2025 workstream and is not automatically part of the PNRR-only headline estimand.
- **MUR cumulative scenarios:** the review of master workbook v15 yielded preliminary low/central/high cumulative eligible-R&D scenarios of EUR 3,333.2m / EUR 4,084.3m / EUR 5,776.6m. These are cumulative gross scenario estimates based on provisional coefficients; not annual flows, not net additionality and not a replacement for the repository's first quantitative diagnostic.
- **PRIN 2022 PNRR pilot:** final pilot workbook v0.2 is archived under `data/intermediate/pilots/`. It remains a methodological feasibility test. The CNR-IAC expenditure/allocation discrepancy and calendar-year timing limitations are unresolved.
- **MUR quantification working paper:** v0.1 is archived under `data/intermediate/working_papers/` and supplements, rather than replaces, the master v15 workbook.

## Reconciliation with existing repository outputs

The repository already includes a first quantitative GERD/innovation diagnostic, processed macro datasets, PNRR execution evidence, measure-level data and budget/Treasury reconciliation. The cumulative MUR scenarios above are a separate calculation. The existing diagnostic and the new cumulative scenarios do not together establish a complete annual causal PNRR R&D shock.

## Data availability and validation

The master v15 workbook and original v18/v19 workbooks were not available as binary files in the current upload environment. Do not describe them as uploaded or consolidated. The archived chat notes are summaries, not primary evidence; opaque conversation citation IDs are not durable source references. Retrieve the original workbooks and source documents before record-level reconciliation.

## Immediate next actions

1. Retrieve the original v18/v19 workbooks and record version, date and checksum.
2. Create a separate national-census staging dataset; reconcile using stable `Measure_ID` values and preserve original observations.
3. Keep non-PNRR national measures outside the headline PNRR perimeter unless a documented perimeter decision changes it.
4. Reconcile aggregate PNR/PRIN M4C2I1.01 against the distinct PRIN 2022 PNRR pilot before combining amounts.
5. Continue annual measure/execution/performance-year reconstruction; do not annualise cumulative snapshots mechanically.
6. Estimate Frascati eligibility, domestic performance and additionality separately.
