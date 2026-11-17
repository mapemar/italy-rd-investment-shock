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
