# Budget and execution reconciliation: Italy, 2020–2026

**Status: source architecture and first cumulative PNRR reconciliation completed; annual measure-level extraction remains in progress.**  
**Last reviewed: 15 November 2026.**

## 1. Why the budget-law cross-check is necessary — and why it is not sufficient

The annual State Budget Laws and the General State Accounts (Rendiconto generale dello Stato) are essential sources for appropriations, commitments and cash payments recorded in the State budget. RGS OpenBDAP publishes downloadable/open-data tables at chapter level, including forecast and final accounts.

However, PNRR implementation also uses dedicated Treasury accounts and special accounting arrangements. The relevant PNRR flows are therefore not necessarily visible as a single, directly identifiable line of final expenditure in the annual Budget Law. Some flows are transferred into ordinary State-budget chapters; others move through dedicated Treasury accounts and special accounts for PNRR implementation.

This is **not** evidence that the expenditure is outside public expenditure or outside the general-government perimeter. The State-budget perimeter, Treasury cash flows, and ESA 2010 general-government accounts are distinct statistical/accounting views. ESA classification depends on the institutional unit and economic substance of the transaction; ESA transactions are recorded on an accrual basis, not simply when cash moves.

The project must therefore reconcile three linked but non-identical layers:

1. **State budget:** appropriations, commitments and payments by chapter, administration, mission/programme and economic category.
2. **PNRR Treasury / implementation system:** transfers between accounts, advances, intermediate payments, balances, amounts declared by implementing bodies and expenditure reports.
3. **National accounts / R&D statistics:** ESA 2010 general-government transactions and the actual R&D performed in Italy, by performing sector and funding source.

## 2. Official RGS/OpenBDAP data discovered

The RGS OpenBDAP open-data catalogue provides the following useful datasets. The catalogue states that State-budget expenditure data are published by chapter, with administration, mission, programme, economic category and COFOG information, in reusable open formats.

| Dataset | Identifier | Coverage / use |
|---|---|---|
| 2020 Budget Law, expenditure by chapter | `2020_LBF_SPE_ELB_CAP_001` | 2020 baseline; 5,404 rows |
| 2021 Budget Law, expenditure by chapter | `2021_LBF_SPE_ELB_CAP_001` | 2021 baseline; 5,848 rows |
| 2023 final accounts, expenditure by chapter | `2023_RND_SPE_ELB_CAP_001` | 2023 outturn; 5,331 rows |
| 2024 final accounts, expenditure by chapter | `2024_RND_SPE_ELB_CAP_001` | 2024 outturn; 5,362 rows |
| 2025 final accounts, expenditure by chapter | `2025_RND_SPE_ELB_CAP_001` | 2025 outturn; 5,395 rows |
| 2026 Budget Law, expenditure by chapter | `2026_LBF_SPE_ELB_CAP_001` | 2026 appropriations; 7,035 rows |
| Historical final accounts, expenditure by mission/programme/macro-aggregate | `RND_SPE_CRU_MPMAC_001` | 2008–2025; 10,889 rows |

The annual 2022 and 2025 Budget Law / 2026 final-account datasets, and the 2020–2022 and 2024 final-account datasets, should be retrieved from the same OpenBDAP catalogue using the corresponding year and document type. The 2008–2025 historical aggregate series is useful for continuity checks, but it is not a substitute for chapter-level annual data.

The 2025 chapter-level final-account dataset exposes 41 fields, including administration, chapter number and description, mission, programme, economic category, initial and final estimates, variations, amounts paid and amounts remaining to be paid. These field definitions must be checked against the dataset metadata before aggregation. The 2026 Budget Law chapter dataset exposes 27 fields, including the three-year competence and cash estimates.

**Important:** a chapter name containing “research”, “innovation” or “PNRR” is not sufficient to classify the full amount as R&D. Each chapter must be linked to the underlying legal measure and its eligible activity. Conversely, a PNRR-financed measure may not be identifiable from the chapter description alone.

Primary catalogue links:
- [OpenBDAP catalogue — expenditure by chapter](https://bdap-opendata.rgs.mef.gov.it/parola-chiave/capitolo)
- [2025 final accounts — expenditure by chapter](https://bdap-opendata.rgs.mef.gov.it/content/2025-rendiconto-pubblicato-elaborabile-spese-capitolo?metadati=showall)
- [2026 Budget Law — expenditure by chapter](https://bdap-opendata.rgs.mef.gov.it/content/2026-legge-di-bilancio-pubblicata-elaborabile-spese-capitolo?metadati=showall)
- [Historical final accounts — mission/programme/macro-aggregate](https://bdap-opendata.rgs.mef.gov.it/content/rendiconto-pubblicato-serie-storica-spese-aggregato-missione-programma-e-macroaggregato-0?metadati=showall)
- [OpenBDAP transparency requirements](https://openbdap.rgs.mef.gov.it/it/Home/AdempimentiDecreto)

## 3. First PNRR Treasury-flow reconciliation

The September 2026 Chamber of Deputies monitoring dossier, summarising the relevant reporting and Court of Auditors information, provides a first high-value quantitative bridge.

### 3.1 Cumulative Treasury movements at 31 December 2025

| Flow | EUR bn | Interpretation |
|---|---:|---|
| Inflows into PNRR Treasury accounts 25091 and 25092 | 299.2 | Cumulative movements, not expenditure |
| Of which: contributions from State budget | 143.6 | National budget-side funding into the dedicated accounts |
| Of which: European Commission instalments | 140.4 | EU financing received |
| Outflows from the two central accounts | 204.9 | Gross outflows, not final expenditure |
| Of which: transfers back into State-budget revenue | 139.2 | Mainly related to EU instalments; must not be counted as final project spending |
| Of which: transfers for implementation | 65.7 | Transfers to central administrations and other implementing arrangements |
| Payments reaching entities outside the central Treasury-account perimeter, net of internal Group 286 transfers | 51.55 | Cash reaching external recipients; still not proof of R&D performance |

The arithmetic is a useful control: 204.9 = 139.2 + 65.7 (rounded). The 51.55bn external-payment figure is a narrower net-flow measure and must not be added to the 65.7bn.

### 3.2 Implementation transfers and expenditure reporting, March 2026

| Indicator | EUR bn / count | Meaning |
|---|---:|---|
| Advances paid | 28.6 | Liquidity advances |
| Intermediate transfers | 16.2 | Intermediate funding |
| Final balances | 3.8 | Final transfers |
| Total advances, intermediate transfers and balances | 48.7 | Transfers, not necessarily expenditure in the same year |
| Financing of projects receiving transfers | approx. 110 | Denominator used in the report |
| Transfers as a share of this financing | 44% | Coverage of project financing |
| Project expenditure declared by implementing bodies | approx. 20.5 | Reported expenditure, not all approved |
| Project expenditure reports approved | just under 6 | Approved amount |
| Reports submitted | more than 74,000 | 63% approved by number |
| Approved amount / amount reported | 29.1% | Financial approval ratio |
| Reported expenditure / transfers for projects receiving transfers | 38.5% | Reporting progress |
| Reported expenditure / expenditure declared by implementing bodies | 30.9% | Reporting progress |

The report also notes that the aggregate transfers covered almost 80% of expenditure declared by implementing bodies. These ratios have different denominators and must not be combined.

**Analytical implication:** the gap between Treasury funding, transfers to implementing bodies, declared expenditure and approved expenditure is large. It would be incorrect to use the PNRR allocation, the Treasury outflow, or even the transfer to the final implementing body as a proxy for realised expenditure, let alone R&D.

### 3.3 National Complementary Plan (PNC)

The same dossier reports, for the PNC through 2025:
- total planned resources for 2021–2032: EUR 27.2bn;
- resources available through 2025: EUR 21.7bn;
- commitments: EUR 21.4bn;
- payments: EUR 18.1bn.

PNC is not the same as PNRR. Include it only where a specific PNC allocation is directly co-financing an in-scope PNRR R&D measure, and maintain a separate funding-source field.

## 4. What the annual budget-law cross-check can and cannot establish

For each in-scope measure, construct a legal-financial crosswalk:

- PNRR measure code and version;
- implementing administration and legal basis;
- annual budget-law chapter(s), article(s), and plan(s) of management, if any;
- annual appropriations (initial and final; competence and cash);
- commitments and payments in the State-budget accounts;
- dedicated NGEU Treasury account / special-account references;
- transfers to administrations and implementing bodies;
- project expenditure declared and approved;
- national co-financing and PNC, separately;
- ESA transaction / general-government treatment, where identifiable;
- R&D eligibility and actual R&D performance.

The annual Budget Law is a **budget authorisation snapshot**, not a complete record of actual spending. The Rendiconto is the ex-post State-budget source for commitments and payments. Treasury and ReGiS data are needed for flows and execution that do not map directly onto a single budget chapter. ESA 2010 is needed to assess the general-government transaction and its timing.

The State-budget final accounts report competence, cash and residuals. Do not mix:
- appropriations (initial/final);
- commitments;
- cash paid;
- unpaid commitments/residuals;
- transfers between Treasury accounts;
- final expenditure by beneficiaries.

Internal transfers and transfers back into the State budget must be eliminated in any consolidated flow reconciliation.

## 5. GBARD bridge to R&D appropriations

ISTAT's GBARD is the best official bridge between the budget system and public R&D allocations. For central-government administrations, ISTAT estimates GBARD using the initial and adjusted State-budget expenditure forecasts acquired from RGS; regional and autonomous-province data are collected directly.

Latest official figures found:
- 2023 adjusted forecasts: approximately EUR 13.5bn;
- 2024 adjusted forecasts: approximately EUR 13.5bn;
- 2025 initial forecasts: approximately EUR 13.1bn.

The 2023 distribution includes a substantial university component through the ordinary university funding (FFO), as well as space, health and industrial production/technology objectives. GBARD is an allocation measure, not realised GERD and not a PNRR-only measure. It can be used as an aggregate plausibility check and to identify the evolution of public R&D appropriations, but not as a direct measure of additional PNRR-funded R&D.

Sources:
- [ISTAT, R&S in Italia 2023–2025, 25 September 2025](https://www.istat.it/wp-content/uploads/2025/09/REPORT_RS_2025.pdf)
- [ISTAT, R&S in Italia 2024–2026, latest release](https://www.istat.it/comunicato-stampa/la-ricerca-e-lo-sviluppo-in-italia-anni-2024-2026/)

## 6. ESA 2010 and the meaning of “public expenditure”

Do not infer that a flow is outside public expenditure because it is not shown as a conventional ministry spending chapter at the moment it moves through Treasury accounts. The ESA 2010 general-government perimeter is based on institutional-sector classification and the economic substance of transactions. ESA records transactions on an accrual basis, i.e. when the economic activity occurs, rather than when cash is paid. It also distinguishes non-financial transactions (which affect the deficit) from financial transactions (which do not directly affect the deficit).

This distinction matters especially for:
- grants and investment contributions;
- tax credits;
- loans and equity investments;
- financial instruments / fund-of-funds;
- transfers between units inside general government;
- transfers between central Treasury accounts and ordinary budget chapters.

The project should not attempt to derive ESA expenditure mechanically from Treasury cash. Instead, it should identify the relevant transaction and institutional units, then reconcile with published general-government accounts and the applicable Eurostat rules.

## 7. Immediate extraction sequence

1. Download the annual OpenBDAP datasets for Budget Laws, notes of variation, approved adjustments and Rendiconti for 2020–2026 (latest available vintage for each).
2. Create a harmonised chapter-level panel, preserving chapter number, administration, mission, programme, action, economic category, competence/cash and the source vintage.
3. Identify candidate chapters using legal measure crosswalks, PNRR labels, responsible administrations and budget documentation. Use text search only as a discovery aid, not as final classification.
4. Reconstruct dedicated Treasury flows separately, beginning with accounts 25091/25092 and Group 286 special accounts.
5. Reconcile PNRR measure allocations with national co-financing and the PNC, removing internal transfers and double counting.
6. Compare annual public R&D appropriations with ISTAT GBARD and the historical RGS series.
7. Only then map the R&D-eligible component to GERD by performing sector and source of funds.

## 8. Key sources

- [Camera dei deputati, Monitoraggio e controllo — Relazioni da obbligo di legge, September 2026](https://documenti.camera.it/leg19/dossier/testi/CP0926R.htm), especially the sections on Treasury flows, transfers and expenditure reporting.
- [Camera dei deputati, Rendiconto 2025 — Assestamento 2026](https://documenti.camera.it/leg19/dossier/testi/BI0295.htm), for the structure of State-budget outturns, competence, cash, residuals and chapter-level accounts.
- [RGS OpenBDAP — expenditure datasets by chapter](https://bdap-opendata.rgs.mef.gov.it/parola-chiave/capitolo).
- [RGS OpenBDAP — historical expenditure by mission/programme/macro-aggregate](https://bdap-opendata.rgs.mef.gov.it/content/rendiconto-pubblicato-serie-storica-spese-aggregato-missione-programma-e-macroaggregato-0?metadati=showall).
- [ISTAT — GBARD / R&D expenditure report](https://www.istat.it/wp-content/uploads/2025/09/REPORT_RS_2025.pdf).
- [Eurostat — Government Finance Statistics methodology](https://ec.europa.eu/eurostat/web/government-finance-statistics/methodology).
- [Eurostat — Manual on Government Deficit and Debt, ESA 2010 implementation](https://ec.europa.eu/eurostat/documents/3859598/16029761/KS-GQ-23-002-EN-N.pdf).

## 9. Limitations and next validation gate

This first pass establishes that the data architecture exists and that the PNRR cash-to-reporting chain can be quantified from public parliamentary material. It does **not** yet provide a complete annual 2020–2026 measure-level series, nor does it prove the ESA classification of each PNRR transaction.

The next validation gate is the extraction of the actual OpenBDAP annual files and the mapping of relevant chapters and treasury flows to the existing PNRR measure inventory. No R&D shock coefficient or annual R&D expenditure estimate should be produced until this reconciliation and the Frascati eligibility assessment are complete.
