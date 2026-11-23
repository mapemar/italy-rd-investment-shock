# Intermediate data and working artefacts

This directory stores extracted or harmonised working datasets that are not yet approved as validated analytical outputs.

## Structure

- `working_papers/`: scenario workbooks and analytical gap assessments.
- `pilots/`: bounded feasibility exercises and pilot datasets.
- `historical_census/`: if created, separate staging datasets for the 2018–2025 national fiscal measures census. Do not merge into the PNRR headline inventory automatically.

## Current artefacts

| Path | Source version | Description | Status |
|---|---|---|---|
| `working_papers/RD_Quantification_Working_Paper_v0.1.json` | v0.1 XLSX export | MUR cumulative low/central/high scenarios, annual-input gap and extraction progress; formulas preserved as strings | Worksheet-level JSON export; original Excel binary not uploaded |
| `pilots/PRIN_2022_PNRR_Pilot_Final_v0.2.md` | v0.2 XLSX content note | PRIN awards, CNR-IAC sample, Frascati crosswalk, agent backlog and source register | Text companion; original Excel binary not uploaded |

## Rules

- Do not overwrite prior versions.
- Preserve formulas, original observations and source lineage.
- Do not label a pilot as nationally representative.
- Keep the historical national census distinct from the PNRR-only estimand.
- Missing observations remain missing, not zero.
- Text/JSON exports are not byte-equivalent replacements for source workbooks; retain the original binary in the Project Library until it can be uploaded.
