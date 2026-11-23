# Working-file and version register

**Updated:** 23 November 2026  
**Repository:** `mapemar/italy-rd-investment-shock`

This register prevents chat names, workbook vintages and analytical outputs from being confused. It supplements `data/README.md`; it does not replace the canonical methodology or decision log.

## Canonical repository documents

| Path | Role |
|---|---|
| `AGENTS.md` | Mandatory agent and data-integrity instructions |
| `docs/methodology.md` | Canonical analytical methodology |
| `docs/research_framework.md` | Research question, workstreams and staged gates |
| `docs/data_dictionary.md` | Dataset concepts and fields |
| `docs/decisions_log.md` | Adopted project decisions |
| `docs/project_status.md` | Live management status |
| `docs/first_quantitative_shock_estimate_nov2026.md` | Existing preliminary macro/R&D diagnostic; not a causal annual shock |
| `docs/chat_consolidation_2026-11-23.md` | Reconciliation of recent chat work with repository state |
| `docs/project_status_addendum_2026-11-23.md` | Supplementary status update from recent chat work |

## Text and data exports added in this update

| File | Source version | Role | Status / caveat |
|---|---|---|---|
| `data/intermediate/working_papers/RD_Quantification_Working_Paper_v0.1.json` | v0.1 XLSX export | Worksheet cell data and formula strings for MUR cumulative scenarios and annual-input gap | JSON export; formulas preserved as strings; not the original Excel binary |
| `data/intermediate/pilots/PRIN_2022_PNRR_Pilot_Final_v0.2.md` | v0.2 XLSX content note | Pilot award totals, CNR-IAC case study, Frascati crosswalk, automation backlog and source register | Text companion; not the original Excel binary |
| `documents/methodology/RD_Policy_to_Macro_Methodology_v0.1.md` | v0.1 DOCX transcription | 20 Nov 2026 methodology note and PRIN direct-research pilot protocol | Historical working note; canonical rules remain in `docs/methodology.md` |
| `documents/workstream_notes/historical_census/Continua Stima PNRR R&D.txt` | v18 notes | Chat extraction summary | Not the original v18 workbook or primary evidence |
| `documents/workstream_notes/historical_census/Continua lestrazione.txt` | v19 notes | Chat extraction summary | Not the original v19 workbook or primary evidence |

## Referenced but not uploaded as original binaries

| Artefact | Reason |
|---|---|
| `Italy_RD_Investment_Shock_Database_v15.xlsx` | Master workbook is referenced in the project Library, but its binary was not available in the current working directory. Existing repository CSVs and documentation remain in place. |
| `RD_National_Measures_Census_2018_2025_v18_extraction_round10.xlsx` | Original binary was not available; only the v18 chat-note text was available. |
| `RD_Italy_2018_2025_Extraction_Continuation_v19.xlsx` | Original binary was not available; only the v19 chat-note text was available. |
| `PRIN_2022_PNRR_Pilot_Final_v0.2.xlsx` | Its content is represented by the text companion above; the original Excel binary was not uploaded. |
| `RD_Quantification_Working_Paper_v0.1.xlsx` | Its worksheet cell content and formula strings are represented by the JSON export above; the original Excel binary was not uploaded. |
| `PRIN_2022_PNRR_Pilot_Agent_Backlog_v0.1.xlsx` | Earlier pilot workbook is superseded for current use by v0.2, which retains the Agent_Backlog sheet and adds ANVUR_Reference. |

## Versioning rules

1. Never overwrite a prior workbook vintage.
2. Record version, date, checksum, source lineage and relationship to processed CSVs for every binary workbook.
3. Treat chat summaries as work-history notes, not primary source evidence.
4. Reconcile records using stable identifiers such as `Measure_ID`, not row counts.
5. Keep the national 2018–2025 fiscal census separate from the default PNRR-only shock perimeter.
6. Keep observed values, official allocations, estimates, proxies and assumptions distinct.
7. Missing values remain missing; they are not zeros.
8. Do not describe a workbook as validated or reconciled unless those steps were actually completed.
