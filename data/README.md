# Data assets and workbook register

## Current working workbook

**Local working file:** `Italy_RD_Investment_Shock_Database_v15.xlsx`  
**Version:** v15  
**Format:** Excel (.xlsx)  
**Role:** working analytical database and estimation workbench for the Italy R&D Investment Shock project.

The workbook currently contains the following sheets:

| Sheet | Purpose |
|---|---|
| START_HERE | Workbook navigation and usage notes |
| Eurostat_Macro | Macro/statistical source panel |
| Macro_Long | Long-format macro series |
| Policy_Measures | Policy-measure inventory |
| VC_Funds | Venture-capital fund evidence |
| PNRR_Economies | PNRR economy/reduction evidence |
| Ministry_Economies | Ministry-level economy evidence |
| Treasury_Flows | Treasury cash-flow snapshots |
| Historical_Policies | Historical R&D policy register |
| Macro_Transmission | Macro transmission channels |
| Annual_Exposure_Input | Annual measure exposure inputs |
| Shock_Estimation | Shock-estimation workspace |
| DATA_CATALOG | Dataset catalogue |
| Tax_Credit | R&D tax-credit evidence |
| Sources_Method | Sources and methodological notes |
| VC_Annual_Assumption | VC annualisation assumptions |
| MUR_Estimation | MUR funding estimates |
| M4C1_M4C2_Sensitivity | M4C1/M4C2 eligibility sensitivity |
| Budget_Law_Profile | Budget-law annual profiles |
| Budget_Law_Audit | Budget-law reconciliation/audit |
| Research_Funds_2026 | 2026 research-fund measures |
| Chapter_Mapping | State-budget chapter mapping |
| OpenBDAP_Extraction | OpenBDAP extraction workflow |
| OpenBDAP_API_Links | OpenBDAP API/export references |
| OpenBDAP_Manifest | CAP dataset manifest |
| PG_Extraction_Method | Piano gestionale extraction method |
| CAPPG_Manifest | CAPPG dataset manifest |

## Important data-status caveat

The OpenBDAP sheets document dataset identifiers, metadata and export/API routes. **They do not imply that the underlying raw CAP/CAPPG records have been downloaded, parsed and reconciled.** The repository's OpenBDAP register and this workbook must continue to distinguish:
1. dataset/metadata identified;
2. export URL verified;
3. raw data downloaded;
4. data parsed and normalised;
5. totals reconciled across CAP/CAPPG and official accounts;
6. chapter/PG mapped to policy measures.

Do not use metadata row counts or an export URL as evidence of actual budget execution.

## Accounting conventions

- Final competence appropriations are authorisations, not expenditure.
- Payments in competence (CP) and payments against residuals (RS) must be retained separately.
- Competence execution and cash expenditure are different views; do not add them.
- End-year unpaid residuals are stocks, not annual flows.
- CAP and CAPPG are overlapping views of the same budget perimeter; use CAPPG for detail and CAP for cross-checking, never sum them.
- Treasury transfers, ministry payments, implementing-body transfers and final-recipient expenditure are separate accounting layers. Reconcile them before aggregation.

## Analytical conventions

The workbook supports two distinct perimeters:
- **Strict Frascati/GERD:** eligible R&D expenditure performed in Italy, with gross and net additional values shown separately.
- **Broader innovation/technology:** financing and activity such as VC, technology adoption and scale-up that is not demonstrated to be Frascati R&D.

A public allocation, payment, VC commitment or investment by a fund is not automatically expenditure on R&D by the final performer.

## Versioning and repository status

The v15 workbook is the current local working artefact, but the binary workbook has **not yet been committed to this GitHub repository**. The repository contains related machine-readable CSV datasets, source registers and methodological documentation. When the workbook is added, record its version, date, checksum and relationship to the processed CSV files; do not silently replace earlier versions.

## Next data-engineering steps

1. Download and preserve the raw annual CAP/CAPPG extracts.
2. Parse the official fields using the year-specific data dictionary.
3. Reconcile CAP and CAPPG totals.
4. Map administration + chapter + PG to policy measure and funding source.
5. Link payments to implementing bodies and final recipients without double counting.
6. Build annual eligible recipient R&D expenditure and additionality profiles.
7. Export a model-ready annual shock table with scenario, price basis, sector and source identifiers.
