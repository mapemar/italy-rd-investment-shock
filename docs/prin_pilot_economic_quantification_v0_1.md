# PRIN PNRR pilot — preliminary economic quantification (v0.1)

**Status:** first quantified model input; provisional and reproducible.  
**Scope:** PRIN-funded projects within M4C2 Investment 1.1. The PRIN 2020 / PRIN 2022 "projects in being" cohort and the new PRIN 2022 PNRR call are kept distinct. The wider PNR/other M4C2-1.1 components are not silently counted as PRIN.

## 1. Executive result

The cleanest directly identifiable new PRIN PNRR cohort is the **DD 1409/2022 call**:
- Official MUR award table: **1,778 projects**, total awarded contribution **EUR 419,493,888** (EUR 419.5m), against the EUR 420m call envelope.
- Average award: **EUR 235,936 per project**.
- MUR/Corte dei conti report the broader M4C2-1.1 investment envelope at approximately **EUR 1.8bn**. This is broader than the new PRIN call and includes "projects in being"/other research components. Do not use EUR 1.8bn as if it were the DD 1409 call.

For the macro pilot, the baseline central estimate is:
- New PRIN PNRR grant envelope: EUR 420m.
- Assumed final expenditure execution: 97%.
- Assumed additionality against the no-PNRR counterfactual: 90%.
- **Central additional R&D expenditure over the full project life: EUR 366.7m.**
- **Additional R&D expenditure realised by August 2025 (proxy): EUR 334.6m**, using the observed aggregate execution profile described below.
- Low/high final scenarios: EUR 264.6m / EUR 420.0m.

These are model estimates, not official GERD observations. The project-level spend and additionality factors remain to be replaced by validated microdata when accessible.

## 2. Official award evidence: DD 1409/2022

MUR's official admission-to-funding page lists the number of projects and total grant by ERC sector. Transcription and arithmetic reconciliation:

| ERC macro-sector | Projects | Awarded EUR | Share of grant |
|---|---:|---:|---:|
| Life Sciences (LS) | 629 | 147,000,000 | 35.0% |
| Social Sciences & Humanities (SH) | 524 | 126,000,000 | 30.0% |
| Physical Sciences & Engineering (PE) | 625 | 146,493,888 | 34.9% |
| **Total** | **1,778** | **419,493,888** | **100.0%** |

The MUR portal lists 1,778 awards, while the MUR/Corte dei conti reporting describes the wider PRIN target/cohort as 1,780 or 5,533 total across windows. Preserve the two-project difference as a reconciliation flag; do not force the totals to match.

## 3. Perimeter and additionality treatment

| Cohort | Evidence / financial treatment | Central additionality treatment |
|---|---|---:|
| PRIN 2020 and PRIN 2022 "projects in being" | MUR DD 1567/2022, Annex 1, Table 7, groups these projects under EUR 550m of PNRR-backed projects in being. Later MUR reporting attributes EUR 550m to the DD 104/2022 window. Cohort attribution and CUP overlap need reconciliation. | **0%** in central case: these are treated as pre-existing projects / relabelled source of finance, not new activity. |
| PRIN 2022 PNRR, DD 1409/2022 | New call; EUR 420m envelope, EUR 419.494m awarded, 1,778 projects. | **90%** central; 70% low; 100% high. |
| National component of PRIN 2022 DD 104/2022 | MUR reporting describes EUR 741.8m total for the DD 104 window, including EUR 550m PNRR. The residual EUR 191.8m is not assumed to be incremental without a counterfactual. | Excluded from central additional shock pending budget-line tracing. |

**Interpretation:** PNRR funding of projects already underway can change the source of finance and the public budget profile without increasing total R&D performed. It is therefore excluded from the central additionality estimate. The DD 1409 new call is the cleanest first-pass treatment of incremental R&D.

## 4. Realisation profile and timing

Evidence:
- The Corte dei conti May 2025 report records **56.3%** expenditure against the EUR 1.8bn M4C2-1.1 envelope at 31 December 2024.
- The Corte dei conti December 2025 report attributes **EUR 580m** of additional expenditure to PRIN in the first eight months of 2025.
- The two observations concern the wider M4C2-1.1/PRIN investment reporting perimeter, not a separately published DD 1409-only expenditure series.

Proxy used until project-level ReGiS/PRIN spend is obtained:
- Apply the observed investment execution profile proportionally to the EUR 420m DD 1409 cohort.
- 2024 cumulative benchmark: 56.3%.
- Jan–Aug 2025 increment benchmark: EUR 580m / EUR 1.8bn = 32.22 percentage points.
- Cumulative execution proxy by August 2025: 88.52%.
- Final execution assumption: 97%; remaining 8.48 percentage points are spread across Sep 2025–Feb 2026.

For annual allocation only, the cumulative amount attributed to the new cohort by end-2024 is split 10% to Nov–Dec 2023 and 90% to 2024. The remaining post-August 2025 expenditure is split 4/6 to Sep–Dec 2025 and 2/6 to Jan–Feb 2026. This is a transparent timing assumption, not observed annual data.

## 5. Economic variables and central cost bridge

The MUR reporting guidelines identify six eligible cost categories: personnel; instruments/equipment; consultancy; licences/know-how/patents; other operating costs; and flat-rate general expenses. They also distinguish existing staff time from newly recruited project staff.

For macroeconomic classification, the central cost split uses the latest fully verified Istat higher-education R&D cost structure available in the extracted official table (2022):
- Personnel: EUR 4,899.432m / EUR 6,700.772m = **73.12%**.
- Goods and services: EUR 1,358.216m / EUR 6,700.772m = **20.27%**.
- Capital expenditure: EUR 443.124m / EUR 6,700.772m = **6.61%**.

Applied to EUR 366.66m central additional R&D:

| Economic variable | Share | EUR m | Treatment |
|---|---:|---:|---|
| Compensation / personnel cost (D.1 proxy) | 73.12% | 268.09 | Includes existing staff time allocated to research and new research staff; not all of it is net new employment. |
| Intermediate consumption (P.2 proxy) | 20.27% | 74.32 | Goods, materials, services, consultancy, licences, dissemination and general expenses, mapped approximately. |
| Equipment / other capital (GFCF proxy) | 6.61% | 24.25 | Equipment/software capital expenditure; MUR rules limit recognition to project use/depreciation where applicable. |
| **Total additional R&D expenditure** | **100%** | **366.66** | GERD-like project expenditure proxy, subject to Frascati and domestic-performance validation. |

Employment intensity proxy:
- Istat 2023 university R&D expenditure: EUR 7,362.530m; R&D staff: 95,558.6 FTE.
- Apply the 2022 personnel share above to 2023 university GERD, obtaining implied personnel cost of approximately EUR 5,382m and personnel cost per FTE of approximately **EUR 56,335**.
- EUR 268.09m / EUR 56,335 = approximately **4,759 R&D FTE-years** over the full project life.
- This is labour input equivalent, not an estimate of net additional jobs or permanent headcount.

R&D type and performing-sector allocation (assumptions for the model input, not observed project-level shares):
- **R&D type:** 55% basic research, 40% applied research and 5% experimental development. The 55% basic-research anchor reflects Istat's finding that more than half of university R&D expenditure is basic research; the applied/experimental split is a modelling assumption pending PRIN project classification.
- **Performing sector:** 90% higher education (HERD) and 10% government research institutes (GOVERD), reflecting the expected dominance of university-led PRIN consortia and the MUR eligibility of EPR. This is a provisional proxy, not a measured beneficiary share.
- **Domestic performance:** 100% is assumed for the first pass because funded research units are Italian eligible institutions; any foreign partner expenditure must be deducted when project-level accounts are available.


Import leakage (explicit assumption, not official data):
- 10% of intermediate consumption imported.
- 25% of equipment/capital expenditure imported.
- Implied direct imports: **EUR 13.49m**; domestic direct expenditure: **EUR 353.17m**.
- Sensitivity should test 5–15% for intermediate inputs and 15–35% for equipment.

## 6. Annual central additional R&D shock

EUR million, nominal project expenditure, central assumptions:

| Year | Additional R&D |
|---|---:|
| 2023 | 21.28 |
| 2024 | 191.53 |
| 2025 | 143.16 |
| 2026 | 10.68 |
| **Total** | **366.66** |

2025 includes the observed-proxy Jan–Aug profile plus the assumed Sep–Dec completion profile. 2026 covers Jan–Feb only.

### Scale check against national R&D

The 2024 central annual shock (EUR 191.5m) is approximately **0.62%** of Italy's total 2024 GERD (about EUR 31.0bn) and the assumed HERD component (EUR 172.4m) is approximately **2.1%** of 2024 university R&D expenditure (about EUR 8.35bn). This is a scale comparison, not an estimate of the observed contribution of PRIN to the national aggregate.

## 7. Scenario analysis

| Scenario | Final execution | Additionality | Additional R&D EUR m |
|---|---:|---:|---:|
| Low | 90% | 70% | 264.60 |
| Central | 97% | 90% | 366.66 |
| High | 100% | 100% | 420.00 |

No blanket additionality factor is applied to the EUR 550m projects-in-being cohort.

## 8. National-accounts and model-use cautions

- The output series is an **additional R&D expenditure shock**, not a direct GDP shock.
- Do not add GERD, compensation, intermediate consumption and equipment as separate shocks: the latter three are a decomposition of the same R&D expenditure.
- In ESA national accounts, R&D output/capitalisation and equipment GFCF require a bridge. Do not equate GERD with R&D GFCF or double count equipment.
- Imports are a leakage from domestic demand, not a deduction from GERD performed in Italy.
- Grants to universities/EPR are a funding-source observation; performing sector is predominantly higher education (HERD) and government research institutes (GOVERD). Exact shares require project-level beneficiary classification.
- The 90% additionality factor is an explicit judgement. It is not empirically identified. Low/high scenarios are mandatory until a counterfactual can be estimated.
- The project end date for DD 104/2022 and DD 1409/2022 was extended to 28 February 2026; the timing profile must be updated if final expenditure data show a different completion pattern.

## 9. Unresolved items (not blockers for v0.1)

1. Obtain complete project-level PRIN 2020 and DD 104/2022 CUP lists and reconcile against the EUR 550m projects-in-being allocation.
2. Obtain the final project/CUP register for DD 1409 and reconcile 1,778 awards against the 1,780 reported target.
3. Obtain project-level ReGiS / PRIN platform financial reporting, including cost-category detail and annual actuals.
4. Classify beneficiaries by HERD/GOVERD and performance location, including foreign partner expenditure.
5. Replace import shares and cost composition proxies with actual project and supply-use evidence.
6. Identify national co-financing and its additionality separately.
7. Build the ESA bridge to R&D GFCF, compensation, intermediate consumption and government final consumption as required by the target macro model.

## 10. Sources

1. MUR, official DD 1409/2022 award table (published 13 October 2023): https://www.mur.gov.it/it/atti-e-normativa/decreti-di-ammissione-al-finanziamento-bando-prin-pnrr-decreto-direttoriale-n-1409
2. MUR, PRIN 2022 PNRR call and documents: https://prin.mur.gov.it/Pages/Index/161
3. MUR, PRIN 2022 call DD 104/2022 and updated reporting guidance: https://prin.mur.gov.it/Pages/Index/119
4. MUR, PRIN reporting and expenditure monitoring documentation: https://prin.mur.gov.it/Pages/Index/221
5. MUR, PNRR reporting guidelines for M4C2-1.1, 8 February 2024, especially §§5–6: https://www.mur.gov.it/sites/default/files/2024-02/Linee%20Guida%20rendicontazione%20PRIN_prot.%28U%29.0000148%20del%2008-02-2024.pdf
6. Corte dei conti, PNRR implementation report, May 2025 (PRIN expenditure rate 56.3% at 31 December 2024): https://www.mur.gov.it/sites/default/files/2025-05/Quinta%20relazione.pdf
7. Corte dei conti, PNRR implementation report, December 2025, data available November 2025; § on financial progress and p.42/Tavola 7, including PRIN expenditure increase of EUR 580m in first eight months 2025: https://www.mur.gov.it/sites/default/files/2025-12/Sesta_Relazione_PNRR_Isem_2025.pdf
8. Istat, R&S in Italia 2023–2025, 25 September 2025, university R&D expenditure and FTE: https://www.istat.it/wp-content/uploads/2025/09/REPORT_RS_2025.pdf
9. Istat, ASI 2024, Table 21.2, 2022 R&D costs by performing sector and type of expenditure: https://www.istat.it/wp-content/uploads/2024/12/ASI_2024.pdf
10. Istat, R&S in Italia 2024–2025, 24 September 2026: https://www.istat.it/comunicato-stampa/la-ricerca-e-sviluppo-in-italia-anni-2024-2026/
11. Banca d'Italia, Ricerca, innovazione e trasferimento tecnologico in Italia, QEF 954 (national-accounts distinction between GERD and R&D investment): https://www.bancaditalia.it/pubblicazioni/qef/2025-0954/QEF_954.pdf

## 11. Reproducibility

The companion CSV `data/processed/prin_pnrr_macro_shock_v0_1.csv` stores the annual central series and the economic decomposition. All assumptions are explicit in the CSV and this note. Values are nominal EUR million unless otherwise stated.
