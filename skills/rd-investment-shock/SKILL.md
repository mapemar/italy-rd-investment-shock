---
name: rd-investment-shock
description: Reconstruct R&D expenditure shocks from public budgets, administrative data and policy documents; assess Frascati eligibility, execution, additionality and macro-model inputs.
---

# R&D Investment Shock Skill

## Mission
Convert fragmented budgetary, legal, administrative and statistical evidence into a transparent annual estimate of R&D expenditure attributable to a policy or funding package, suitable for macroeconomic modelling.

Always distinguish:
1. Funding or budget authorisation.
2. Budget execution (commitments, payments and residuals).
3. Expenditure incurred by final recipients.
4. R&D expenditure eligible under the Frascati Manual.

A budget allocation or public payment is not automatically GERD.

## When to use
Use for PNRR/RRF and national R&D funding analysis; Italian MUR/MIMIT budget mapping; OpenBDAP extraction; Frascati classification; additionality assessment; R&D shock databases; and conversion of qualitative policy evidence into quantitative macro-model inputs.

## Core principles

### Frascati eligibility
Assess whether the activity is creative and systematic work that increases the stock of knowledge or devises new applications. Apply the five criteria: novelty, creativity, uncertainty, systematic nature, and transferability/reproducibility.

Classify each measure:
- **Strict R&D**: evidence supports Frascati eligibility.
- **Partially eligible**: mixed R&D and non-R&D activities; apply an evidenced coefficient.
- **Innovation only**: technology adoption, commercialisation, scale-up or innovation without demonstrated R&D; exclude from strict GERD but retain in a separate broad innovation series.
- **Not eligible**: no material R&D content.

Do not infer eligibility from labels such as innovation, digital, technology or startup alone. If evidence is incomplete, show low/central/high assumptions.

### Additionality
Separate gross eligible expenditure from net additional expenditure. Identify substitution, reallocation, acceleration, offsets, consolidation of legacy funds and crowding-in/out. A new budget line is not necessarily additional R&D.

### Two perimeters
Maintain two distinct annual series:
1. **Strict Frascati/GERD shock**: eligible R&D expenditure, ideally allocated to BERD, HERD, GOVERD and, where relevant, PNP. Show gross and net additional values separately.
2. **Broader innovation/technology shock**: innovation, technology adoption, VC and scale-up financing not demonstrated to be R&D. Never merge this into strict GERD.

### Double counting
Use unique IDs for measure, funding source, chapter, PG, beneficiary, project and year. Reconcile transfers through implementing bodies to final recipients. Do not add CAP and CAPPG records together: CAPPG is a more granular view of the same budget perimeter. Do not count both a fund investment and the recipient's R&D expenditure.

## Evidence hierarchy
Prioritise:
1. Official accounting and budget data (RGS, OpenBDAP, State budget, final accounts).
2. Legal acts and official technical/financial annexes (RT, DLB, CID, decrees).
3. Implementing-body monitoring and annual reports (MUR, MIMIT, CDP, Invitalia, CDP Venture Capital, EIB, universities and research bodies).
4. Eurostat, OECD, ISTAT and official evaluations.
5. Secondary sources for triangulation only.

For every figure record value, unit, year, accounting basis, source URL/title/date, page/table, whether it is an allocation/commitment/payment/residual/recipient expenditure/statistical R&D, confidence and limitations. Cite factual claims. Never invent values, UUIDs, URLs or chapter mappings.

## Italian budget and OpenBDAP workflow

### Dataset discovery
Identify official annual OpenBDAP datasets:
- CAP: Rendiconto elaborabile spese per capitolo.
- CAPPG: Rendiconto elaborabile spese per capitolo e piano gestionale.

Retrieve dataset IDs/UUIDs and CSV/OData export actions from official dataset pages. Record them in a manifest. Never infer a CAPPG UUID from a CAP dataset or another year.

Track separately: metadata verified; export URL verified; raw rows downloaded; parsed; totals reconciled; chapter/PG mapping completed. A verified endpoint does not mean data have been imported.

### Extraction and mapping
Prefer CAPPG for individual funding lines; use CAP for cross-checks and where PG detail is unavailable. Filter by administration, chapter, PG, mission/programme, economic classification and year. Build a mapping table from administration+chapter+PG to measure, source of funds, recipient sector, Frascati class, eligibility coefficient, additionality coefficient, evidence and confidence.

Investigate MUR lines such as FIS, FISA, FISR, FIRST, PRIN and FOE, and MIMIT lines such as the Fondo per la crescita sostenibile and industrial incentives. Verify year-specific chapter/PG descriptions; do not assume a chapter is homogeneous.

### Accounting variables
Always check the year-specific RGS data dictionary. Working interpretation for OpenBDAP rendiconto fields:

| Field | Meaning | Use |
|---|---|---|
| Previsioni definitive CP | Final competence appropriations | Authorisation, not expenditure |
| Pagato CP | Payments in competence account | Current-year cash execution component |
| Pagato RS | Payments against prior-year residuals | Keep separate |
| Totale CP | Paid plus remaining to pay in competence account | Competence execution/charged amount, subject to schema |
| Totale CS | Total cash expenditure | Cash-flow measure; verify schema |
| RS al 31/12 | End-year unpaid residual stock | Stock, not annual flow |

Do not add CP and CS. Do not add component payments to totals as if independent. Do not add residual stocks to annual flows. Do not call Totale CP a cash payment. Reconcile CAP and CAPPG for the same perimeter. Retain cash and competence series because payment timing may differ from the timing of R&D activity.

## Measure-level assessment
For each measure record: ID/name; legal basis; implementing authority; envelope and annual profile; funding source (RRF/national/other EU/private); allocation/commitment/payment status; beneficiary and performing sector; eligible cost categories; Frascati class and evidence; low/central/high eligible share; additionality/substitution; execution profile; expected performance year; overlap risks; source and confidence.

Decompose mixed measures where possible into research grants, researcher/PhD costs, training, infrastructure, equipment, technology adoption and commercialisation. Do not automatically count education, training, routine testing, ordinary software deployment, routine data collection or non-R&D infrastructure as R&D.

## Financial instruments and venture capital
Separate public fund commitment, capital paid into fund, investment by fund, final recipient expenditure, recipient R&D expenditure and private co-investment. A VC commitment is not GERD. It may be included in the broad innovation series as financing input. For strict GERD estimate the portfolio companies' actual R&D spending and timing. Eligibility rules for startups may support an assumption but do not prove that 100% of investment becomes R&D. If the user chooses a 100% scenario, preserve it as an explicit modelling assumption and show sensitivity.

## PNRR/RRF
For each measure identify CID milestone/target, national implementing act, EU and national financing, legal envelope, reprogramming/reductions, final recipients, commitments/disbursements/expenditure, Frascati eligibility, implementation delays and counterfactual baseline. Do not treat RRF transfers to the State as R&D expenditure. Measure recipient activity, not the EU cash receipt.

Classify M4C1/M4C2 sub-measures separately where possible: competitive projects, partnerships, national centres, ecosystems, infrastructure, PhDs and researcher recruitment can have different Frascati coverage and execution. If a 100% eligibility assumption is adopted for a defined perimeter, label it as an assumption and show sensitivity.

## Annual shock calculation
Funding-based proxy:
`Gross eligible R&D_t = funded amount_t × execution profile_t × Frascati share_t`
`Net additional R&D_t = Gross eligible R&D_t × additionality share_t`

Prefer observed recipient expenditure over funding proxies. For loans, guarantees, equity and fund-of-funds, do not use the nominal envelope as annual R&D expenditure. Model disbursement, investment and recipient R&D separately; add leverage only when attributable co-financing is observed.

Produce low/central/high scenarios. Allocate to BERD/HERD/GOVERD/PNP only when evidence supports the performing sector; otherwise leave unallocated.

### Macro-model handoff
Deliver annual nominal EUR million and specify price basis/base year. Include strict gross R&D, strict net additional R&D, sector split, broad innovation shock (separate), instrument, execution profile, scenario, source and assumption IDs. State whether input is a level, growth rate, GDP share or deviation from baseline. Deflate nominal values before using real-volume inputs. Do not apply a GDP multiplier to turn a budget into GERD.

## Workbook architecture
Maintain versioned Excel files and preserve raw data. Recommended sheets:
- START_HERE
- Policy_Measures
- Budget_Mapping
- OpenBDAP_Manifest
- Raw_CAP
- Raw_CAPPG
- Clean_Budget_Data
- Measure_Classification
- Recipient_Expenditure
- Annual_Shock_Input
- Sensitivity
- Macro_Transmission
- Sources_Method
- QA_Reconciliation

Keep raw extracts untouched; document all transformations and manual adjustments.

## Quality assurance
Before publishing:
- confirm year, accounting basis, dataset UUID and official export URL;
- distinguish metadata verification from raw extraction;
- reconcile CAP and CAPPG;
- check duplicate measure/chapter/PG records;
- do not add CP and CS;
- keep payments and residual stocks distinct;
- do not describe appropriations as actual expenditure;
- do not treat RRF transfers or VC commitments as GERD;
- evidence Frascati eligibility and additionality;
- reflect execution and recipient-spending timing;
- state nominal/real price basis;
- trace every figure to a source;
- disclose gaps and assumptions.

## Working style and response protocol
Work iteratively and preserve the existing database and version history. At each iteration state what was verified, what was extracted, what was calculated, and what remains uncertain. Never claim data were downloaded, parsed or calculated when only metadata or URLs were identified. If access fails, document the limitation and provide a reproducible extraction route rather than fabricating values. Proceed when scope is clear; ask one focused question only if essential.


## National Budget-Law Census (Italy, 2018–2025)

### Objective and perimeter
Build a comprehensive, auditable census of all Italian national-budget measures that finance, enable, reduce or otherwise affect R&D during 2018–2025. The census is distinct from the PNRR/RRF and PNC registers. Include:
- Budget Laws (Leggi di bilancio), both Section I (legal provisions) and Section II (state forecasts).
- Original and updated Technical Reports (Relazioni tecniche, RT), summary financial-effects tables (prospetti riepilogativi), and technical reports attached to government amendments.
- Parliamentary reading dossiers and verification-of-quantification dossiers (VQ).
- Ministry state-of-forecast volumes, budget tables, refinancing/definancing/reprogramming annexes and relevant final amendments.
- Where needed to understand the annual profile, subsequent allocation/repartition decrees, budget adjustments and final accounts. Keep these distinct from the Budget Law itself.

Include measures even where R&D is not explicit in the title. Screen all relevant ministries and policy areas, including MUR/MIUR, MIMIT/MISE, MEF, MASAF/MIPAAF, Health, Defence, Environment/Energy, Infrastructure/Transport, Space and other research-performing public bodies. Include tax expenditures, grants, institutional funding, researcher recruitment, research infrastructure, industrial research, public procurement with demonstrable R&D, public financial instruments and reductions/definancing. Include mixed measures in the broad register but do not automatically classify them as strict R&D.

### Document-by-document command protocol
Maintain a Document_Inventory with one record for every source document or coherent document package. Each record must include year, exact title, issuing institution, document type, official URL, version/date, relevant pages/tables, review status, extraction status, and notes.

Every document must have an explicit user instruction:
- **EXTRACT INFORMATION**: inspect the exact document; identify all relevant measures and extract all supported numerical information into the workbook, with page/table-level source references.
- **DISREGARD DOCUMENT**: exclude it from the requested extraction scope and record the exclusion and reason. Do not silently discard it.
- **PENDING**: no extraction decision has been made. Do not treat pending as disregard.

Do not ask the user to confirm again once a document has been marked EXTRACT. Continue through the approved queue. If a URL is broken or the document cannot be accessed, record ACCESS BLOCKED and the precise reason; do not substitute an unrelated source without noting the substitution. If a document is a duplicate, record DUPLICATE OF [document ID] and retain the canonical source.

### Required document sequence for each budget year
For each year 2018–2025, review in this order:
1. Enacted Budget Law and final consolidated legal text.
2. Section I parliamentary dossiers, all relevant volumes and sectoral dossiers.
3. Original Technical Report and summary financial-effects table.
4. Updated RTs attached to government amendments and the final parliamentary text.
5. VQ dossier(s), checking the measure-level calculations and assumptions.
6. Section II state forecasts and all relevant ministry tables.
7. Annexes listing refinancing, definancing and reprogramming.
8. Subsequent allocation/repartition decrees and adjustments where needed to identify the actual annual profile.
9. Final accounts / OpenBDAP CAP and CAPPG to assess execution, keeping these accounting stages separate from the ex-ante RT.

A parliamentary dossier is an aid to navigation and legal interpretation; it is not a substitute for the original RT or the state-forecast tables. Mark a document as fully reviewed only after the relevant pages, tables and annexes have been checked, not merely because it has been located or cited elsewhere.

### Measure discovery: exhaustive screening
Search for both explicit R&D provisions and adjacent measures. At minimum screen:
- R&D tax credits and related tax expenditures, including general and geographically enhanced schemes; separate R&D from innovation, design, digital/green transition and other eligible activities.
- University funding and research institutions: FFO, FOE, FIS, FISA, FISR, FIRST, PRIN, PNR (Programma Nazionale per la Ricerca), research infrastructures, competitive grants and institutional allocations.
- Research personnel: recruitment, stabilisation, career progression, PhD scholarships and researcher grants; distinguish researcher time from teaching, technical, administrative and training components.
- Industrial and applied research: Fondo per la crescita sostenibile, Accordi per l'innovazione, industrial biomedical research, aerospace, energy, agricultural and defence R&D.
- Research bodies and programmes: CNR, ENEA, INAF, INFN, INGV, ISS, CREA, ASI, CIRA, OGS and other public research performers.
- Technology transfer, venture capital, startup and scale-up schemes: retain in broad innovation unless final-recipient R&D performance is evidenced.
- Reductions, spending reviews, expiry, repeal, refinancing and reprogramming that change the baseline. Record negative measures as well as positive ones.
- Cross-ministry and multi-purpose funds. Do not classify an entire fund as R&D solely from its name; inspect calls, eligible costs, recipients and RT.

### Required numerical extraction: cell-by-cell annual data
The user’s objective is to quantify an annual impact, not merely compile a list of measures. For every measure and every year supported by the document, enter numerical values in the workbook at measure-year level. Never leave a known figure only in prose.

For each measure, extract where reported:
- annual legal authorisation / budget envelope;
- initial and final competence appropriations (competenza);
- initial and final cash appropriations (cassa);
- changes made by Section I and Section II;
- commitments (impegni), payments in competence account (pagato CP), payments against residuals (pagato RS), total competence execution and total cash payments, where the source provides them;
- residual stock at year-end, separately;
- RT effects on **saldo netto da finanziare (SNF)**, **fabbisogno**, and **indebitamento netto**, each in its own field and for each year;
- tax expenditure / revenue loss, including annual accrual or cash timing where available;
- coverage, offsets, reductions and compensatory revenue, separately from gross measure cost;
- EU financing, national co-financing and other funding sources, without double counting;
- beneficiary-level expenditure or R&D performed, when available.

Use EUR million consistently in presentation tables, but preserve original units and raw values in source/raw sheets. Record sign conventions explicitly: expenditure costs and revenue losses generally worsen balances, while offsets/improvements have the opposite sign; preserve the source's own sign and add a normalized-sign field rather than overwriting it. Do not infer a zero from a blank cell. Distinguish explicit zero from unavailable/not reported.

### RT and fiscal-balance interpretation
For every RT table, record the table title, page, measure reference and whether the profile is annual, cumulative, cohort-based or a change relative to a baseline. Preserve all years shown, including years outside 2018–2025 if they are needed to understand a multiannual profile.

Never collapse SNF, fabbisogno and indebitamento netto into one figure. They measure different accounting perspectives and must remain separate. Indebitamento netto is generally the closest of the three to the general-government net lending/borrowing concept, but do not automatically label it an ESA outturn or a measure-specific ESA impact. Explain the source's accounting perimeter and assumptions.

For tax credits, distinguish the statutory ceiling, RT forecast of tax expenditure, tax return accrued credit, credit used in compensation, and actual cash/revenue effect. A cohort-based RT profile may differ from the calendar-year amount of R&D performed. Do not add general and regional enhanced credits if the RT already accounts for interactions or if they apply to the same eligible cost.

For Section II, distinguish baseline forecasts, amendments, final approved appropriations and final accounts. A change in chapter allocation may be a transfer/reclassification rather than new policy. Reconcile chapter and PG totals to the relevant programme/mission and avoid adding control totals to their components.

### Workbook outputs for the national census
Maintain at least these linked sheets (names can be adapted to the current simplified workbook, but the functions must remain):
- **Document_Inventory**: document-level command, review and extraction status.
- **National_Measure_Census**: one row per measure, with legal basis, ministry, beneficiary, performer sector, strict/broad classification and source.
- **National_Annual_Profile**: one row per measure/metric and years in columns, with numeric cells, unit, basis and sign convention.
- **RT_Fiscal_Balances**: separate annual SNF, fabbisogno and indebitamento netto profiles, with page/table citations.
- **Section_II_Budget_Profile**: competence/cash appropriations by ministry, mission, programme, chapter and PG, with initial/final/revision status.
- **Execution_Profile**: commitments, CP payments, RS payments, total cash and residual stocks.
- **National_Measure_Mapping**: mapping from law provision and budget chapter/PG to measure, source of funds, recipient and performing sector.
- **Sources_Method**: source register, assumptions, transformations, confidence and limitations.
- **QA_Reconciliation**: checks between RT, legal authorisations, Section II, CAP/CAPPG and beneficiary-level records.

Keep raw extracts separate and immutable. Wide time-series views should have measures/metrics in rows and years in columns for readability. Do not delete raw source data or replace missing values with zero. Preserve a clear index and keep the user-facing workbook limited to essential sheets.

### Completeness and audit status
Use explicit status labels:
- NOT IDENTIFIED
- IDENTIFIED
- ACCESS BLOCKED
- QUEUED / PENDING USER COMMAND
- IN REVIEW
- PARTIALLY EXTRACTED
- EXTRACTED – NOT VERIFIED
- VERIFIED AGAINST SOURCE
- RECONCILED
- DISREGARDED BY USER
- DUPLICATE

A year is not complete until the document inventory is closed and all relevant Section I, RT, VQ, Section II and annex documents have either been extracted, explicitly disregarded by the user, or documented as inaccessible/duplicate. A measure census is not complete merely because the main headline funds have been found.

### Reporting to the user
When asked for progress, provide a year-by-year matrix listing:
- documents identified;
- documents fully inspected;
- documents partially inspected;
- documents not yet located;
- documents blocked by access;
- documents explicitly disregarded;
- measures identified;
- numerical profiles extracted;
- outstanding values and reasons.

Clearly distinguish **document located**, **document opened**, **document reviewed**, **data extracted**, **data verified**, and **data reconciled**. Do not claim “deep research”, “complete census” or “all measures” until the completeness criteria above are met.

When the user requests data, prioritise populated numeric cells and deliver the updated workbook. Explain the process only to the extent needed to interpret the numbers and their evidential status.
