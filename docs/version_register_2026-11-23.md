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

## Working artefacts added in this update

| File | Version | Role | Status / caveat |
|---|---|---|---|
| `data/intermediate/working_papers/RD_Quantification_Working_Paper_v0.1.xlsx` | v0.1 | MUR cumulative scenarios and annual-input gap | Supplementary; not a replacement for v15 |
| `data/intermediate/pilots/PRIN_2022_PNRR_Pilot_Final_v0.2.xlsx` | v0.2 | PRIN 2022 PNRR pilot, including ANVUR reference | Final pilot workbook; feasibility exercise, not annual national R&D |
| `documents/methodology/RD_Policy_to_Macro_Methodology_v0.1.md` | v0.1 | Text-preserving transcription of the 20 Nov 2026 methodology note | Historical working note; canonical rules remain in `docs/methodology.md` |
| `documents/workstream_notes/historical_census/Continua Stima PNRR R&D.txt` | v18 notes | Chat extraction summary | Not the original v18 workbook or primary evidence |
| `documents/workstream_notes/historical_census/Continua lestrazione.txt` | v19 notes | Chat extraction summary | Not the original v19 workbook or primary evidence |

## Referenced but not uploaded in this update

| Artefact | Reason |
|---|---|
| `Italy_RD_Investment_Shock_Database_v15.xlsx` | Existing master workbook is referenced in the project Library, but its binary was not available in the current working directory for upload. The repository's CSVs and documentation remain in place. |
| `RD_National_Measures_Census_2018_2025_v18_extraction_round10.xlsx` | Original binary was not available; only the v18 chat-note text was available. |
| `RD_Italy_2018_2025_Extraction_Continuation_v19.xlsx` | Original binary was not available; only the v19 chat-note text was available. |
| `PRIN_2022_PNRR_Pilot_Agent_Backlog_v0.1.xlsx` | Earlier pilot workbook is superseded for current use by v0.2, which retains the Agent_Backlog sheet and adds ANVUR_Reference. Keep v0.1 locally if historical comparison is required. |

## Versioning rules

1. Never overwrite a prior workbook vintage.
2. Record the version, date, checksum, source lineage and relationship to processed CSVs for every binary workbook.
3. Treat chat summaries as work-history notes, not primary source evidence.
4. Reconcile records using stable identifiers such as `Measure_ID`, not row counts.
5. Keep the national 2018–2025 fiscal census separate from the default PNRR-only shock perimeter.
6. Keep observed values, official allocations, estimates, proxies and assumptions distinct.
7. Missing values remain missing; they are not zeros.
8. Do not describe a workbook as validated or reconciled unless those steps were actually completed.
