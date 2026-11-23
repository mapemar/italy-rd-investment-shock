# Intermediate data and working artefacts

This directory stores extracted or harmonised working datasets that are not yet approved as validated analytical outputs.

## Structure

- `working_papers/`: scenario workbooks and analytical gap assessments.
- `pilots/`: bounded feasibility exercises and pilot datasets.
- `historical_census/`: if created, separate staging datasets for the 2018–2025 national fiscal measures census. Do not merge into the PNRR headline inventory automatically.

## Current artefacts

| Path | Version | Description | Status |
|---|---|---|---|
| `working_papers/RD_Quantification_Working_Paper_v0.1.xlsx` | v0.1 | MUR cumulative low/central/high estimates and annual-input gaps | Supplementary, not validated annual shock |
| `pilots/PRIN_2022_PNRR_Pilot_Final_v0.2.xlsx` | v0.2 | PRIN 2022 PNRR project-level pilot, includes ANVUR reference | Feasibility pilot; unresolved reconciliation/timing caveats |

## Rules

- Do not overwrite prior versions.
- Preserve formulas, original observations and source lineage.
- Do not label a pilot as nationally representative.
- Keep the historical national census distinct from the PNRR-only estimand.
- Missing observations remain missing, not zero.
