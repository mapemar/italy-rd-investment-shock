# Methodology: estimating the incremental R&D investment shock

## 1. Estimand

The primary estimand is the annual additional R&D expenditure in Italy attributable to a defined set of policy interventions, relative to a clearly stated counterfactual in which those interventions did not occur (or occurred under a specified baseline policy).

The estimand is not:
- the total PNRR allocation;
- the total value of an incentive scheme;
- the total amount invested by venture capital funds;
- the total value of equipment or infrastructure classified as innovation-related.

The unit of analysis should initially be the policy measure by year, with aggregation to annual national totals only after measure-level validation.

### Policy perimeter
The default policy universe includes PNRR measures and the national co-financing directly attached to those measures. It excludes unrelated national R&D, innovation or industrial-policy measures outside the PNRR. The data model must nevertheless allow an optional extension to other EU programmes, initially Cohesion Policy and the European Innovation Council (EIC). These programmes must be switchable on/off through configuration and reported separately from the PNRR core. Do not include them in the headline PNRR-only result.

## 2. R&D definition and statistical boundary

Use the Frascati Manual definition of research and experimental development. Distinguish:
- basic research;
- applied research;
- experimental development.

Classify activities based on their substance, not merely their policy label. General digitalisation, machinery replacement, software adoption, routine engineering, technology deployment and ordinary capital formation are not automatically R&D.

Maintain separate dimensions for:
- **performing sector:** business enterprise, government, higher education, private non-profit;
- **funding source:** government, business, higher education, private non-profit, rest of the world, where available;
- **R&D type:** basic, applied, experimental development;
- **policy channel:** direct public R&D, business incentives, venture capital/financial instruments, ecosystem/enabling measures.

## 3. Four policy channels

### 3.1 Direct public R&D

Capture public grants, research programmes, university and public research activity, and the R&D component of research infrastructure. Separate research activity from non-R&D construction, generic equipment and administrative costs.

### 3.2 Business R&D incentives

Capture grants and tax incentives only to the extent that eligible activity is genuine R&D. Distinguish the fiscal cost from underlying eligible R&D expenditure and from the increment induced by the support. Consider deadweight, substitution, timing and beneficiary behaviour.

### 3.3 Venture capital and financial instruments

Track public commitments, fund-level investments, private co-investment and final company expenditure separately. The official GERD/Frascati statistical series should continue to include only R&D activity actually performed by resident units in Italy.

**Project-specific broad innovation-shock proxy (adopted D019):** for the Digital Transition Fund (DTF, M4C2 I3.2) and Green Transition Fund (GTF, M2C2 I5.4), count 100% of the two funds' deployed investment capital as a separate *VC-backed innovation and technology-business-creation proxy*. This is an explicit simplifying assumption motivated by the funds' targeted investment in start-ups/innovative companies and the Italian innovative-start-up eligibility framework. It is not a claim that every euro meets the Frascati definition or is recorded in GERD.

Apply the proxy to actual annual deployment/investment by the funds, not automatically to the full approved envelope in the year of allocation. Until annual deployment data are available, show the EUR 400m DTF and EUR 250m GTF envelopes as committed/potential proxy exposure, not as realised annual expenditure. Do not add private co-investment or a leverage multiplier to the proxy unless separately evidenced and explicitly reported; avoid double counting fund-level commitments and downstream company investments.

Report two parallel outputs:
1. **Official-boundary additional domestic R&D:** Frascati-eligible R&D actually performed in Italy, with additionality estimated separately.
2. **Broad innovation shock including VC proxy:** the official-boundary series plus the DTF/GTF proxy, clearly labelled as an extended innovation/technology-business-creation measure and never presented as official GERD or BERD.

The proxy should be shown in a separate component and sensitivity table so that users can see how much of the broad shock comes from this approximation. Where later portfolio-company data become available, replace or validate the proxy with company-level R&D and innovation expenditure, while retaining a bridge to the original 100% assumption.

### 3.4 Ecosystem and enabling measures

Track technology transfer, competence centres, research partnerships, doctoral programmes and innovation infrastructure. Quantify only a demonstrable R&D expenditure component. Otherwise retain these measures as enabling context, outside the quantified central shock.

## 4. Measure-level accounting bridge

For each measure and year, preserve separate fields for:

1. announced or approved envelope;
2. legal budget authorisation / appropriation;
3. commitments;
4. payments or disbursements;
5. expenditure by final beneficiaries;
6. share meeting the R&D definition;
7. estimated incremental share relative to counterfactual;
8. annual timing profile.

Do not assume these stages are equal or occur in the same year.

A useful decomposition is:

**Incremental R&D expenditure (measure, year)**

= R&D-eligible beneficiary expenditure in the year  
× estimated additionality share

Where beneficiary expenditure cannot be observed directly, estimate it transparently from earlier stages using separate utilisation, R&D-relevance and timing parameters:

**Estimated incremental R&D**  
= eligible public support × utilisation coefficient × R&D-relevance coefficient × additionality coefficient

For leveraged schemes, model private financing and beneficiary R&D expenditure explicitly. Do not apply a leverage multiplier mechanically to an entire fund or programme.

The formula is a bookkeeping framework, not a causal identification strategy. Each coefficient must have a documented definition, evidence base, range, year profile and validation status.

## 5. Counterfactual and additionality

For each instrument, specify what would likely have happened without the intervention. Potential approaches, depending on data availability, include:
- evaluation evidence from comparable schemes;
- beneficiary/non-beneficiary comparisons;
- difference-in-differences or matching studies;
- discontinuities around eligibility thresholds;
- firm-level panel analysis;
- structural or expert-informed assumptions where causal evidence is unavailable.

Assess:
- deadweight (activity that would have occurred anyway);
- substitution between supported and unsupported activity;
- crowding-in of additional private finance;
- crowding-out of private finance;
- displacement across firms, sectors or years;
- imports and foreign content, where relevant to the model's definition of domestic R&D;
- timing and persistence.

Do not label a scenario parameter as an empirical causal estimate unless a credible identification strategy supports it.

## 6. Timing

Distinguish the year of:
- budget authorisation;
- commitment;
- cash payment;
- investment by intermediary;
- R&D performance by beneficiary;
- statistical recording in GERD.

Use an explicit annual timing profile where policy support precedes the R&D activity. Avoid shifting expenditure to the year of the original PNRR allocation by default.

## 7. Scenarios and uncertainty

Produce conservative, central and high-impact scenarios only after defining evidence-based parameter ranges. For each parameter, record:
- definition;
- unit and bounds;
- source/evidence;
- method;
- applicable measure/channel;
- scenario value;
- uncertainty rating;
- reviewer status.

Use sensitivity analysis to show which assumptions drive the aggregate shock. Report ranges where precision is not justified.

## 8. Reconciliation with official statistics

Build the historical baseline from Eurostat and OECD series, retaining metadata and dataset identifiers. Distinguish:
- GERD by sector of performance;
- GERD by source of funds;
- GERD by type of R&D;
- GBARD, which captures government budget allocations/appropriations rather than the same concept as realised GERD.

Do not add measure allocations mechanically to GERD. Policy accounting and R&D statistics are distinct views of the economy. Use reconciliation to assess plausibility, coverage and overlaps, not to force equality.

Investigate current prices, constant prices and GDP ratios. Record the deflator, base year, GDP vintage and any series breaks. Do not splice Eurostat and OECD series without documenting differences.

## 9. Output concepts and price basis

Produce at least two distinct annual output series:

1. **Additional domestic R&D performed in Italy:** incremental R&D expenditure actually performed by resident units in Italy, regardless of whether it is financed by public or private sources.
2. **Publicly financed R&D performed in Italy:** the subset of domestic R&D expenditure financed by government/public sources, including the public financing component attributable to the interventions in scope.

The second series is a financing-source view of the first, not an additional amount to be added to it. Where public support induces private co-financing, classify the resulting R&D by both performing sector and funding source. Do not add the two output series together.

Retain nominal values and produce constant-price values using **2019 as the reference year**. Record the chosen deflator, source, vintage and conversion method. The 2019 reference year is a price base, not a counterfactual or policy baseline. Historical statistical coverage should target 2015–2024 where data are available.

## 10. Model interface

Keep the shock modular until the receiving macroeconomic model is supplied. Potential series include:
- direct public R&D performed;
- business R&D performed, split by funding source where possible;
- R&D financed through tax incentives;
- R&D linked to financial instruments;
- total incremental domestic R&D.

The model may require shocks by performing sector, funding source, type of R&D, price basis or timing. Map only after reviewing its equations and variable definitions.

## 11. Evidence and review

Every material input must be traceable to a source or explicitly labelled assumption. Keep extraction evidence, calculation lineage, parameter version and reviewer status. A result is not validated merely because an AI system extracted it.


## 12. Cash, commitments, accrual and the year of R&D performance

The project must preserve cash and accrual information, but must not treat the conversion of public cash expenditure into ESA accrual expenditure as equivalent to measuring R&D performed by the beneficiary.

Maintain separate annual dates/amounts for:
- budget appropriation and legal commitment;
- public cash payment/disbursement;
- recognition of the public-sector transaction under ESA 2010, where relevant;
- investment or eligible cost incurred by the final beneficiary;
- R&D activity actually performed and recorded in the relevant R&D statistics.

The primary shock for the macroeconomic R&D model should be assigned to the year in which the R&D activity is performed in Italy, insofar as the evidence permits. Cash payments and commitments remain essential explanatory and reconciliation variables.

ESA 2010 and Eurostat's Manual on Government Deficit and Debt are relevant for the government-accounting bridge, especially where national budget data are cash-based. However, ESA accrual rules are not a universal conversion formula for the timing of private or public-sector R&D performance. Apply transaction-specific rules and document the evidence used.

Specific cautions:
- **R&D tax credits:** distinguish payable/refundable from non-payable/non-refundable credits and record the fiscal cost according to the applicable ESA treatment. For the R&D shock, separately identify the year in which the eligible R&D costs are incurred/performed; do not use the later year of tax-credit utilisation as the R&D performance year. The Eurostat Manual on Government Deficit and Debt gives specific guidance on payable tax credits and the timing of recording.
- **Grants and subsidies:** cash disbursement may precede or follow eligible costs. Link payments to the period in which the beneficiary incurs eligible expenditure and performs R&D, where data allow.
- **Investment grants and infrastructure:** distinguish the timing of grant recognition/payment from construction, asset acquisition and the R&D services performed using the infrastructure. Only the R&D activity component enters GERD.
- **Venture capital/equity:** the public acquisition of an equity stake or a fund commitment is a financial investment, not R&D expenditure. Track fund deployment and portfolio-company R&D expenditure separately; the latter enters the R&D shock in the year performed.
- **Loans and guarantees:** neither loan disbursement nor guarantee exposure is itself R&D expenditure. Identify the additional R&D expenditure financed by the beneficiary and its timing.

Do not create a single mechanical cash-to-accrual multiplier. Build an event/timing bridge at measure or instrument level, with explicit treatment and evidence. If beneficiary-level timing is unavailable, report the proxy, uncertainty and sensitivity.

Useful official references:
- Eurostat, Government finance statistics methodology (ESA 2010 accrual principle): https://ec.europa.eu/eurostat/web/government-finance-statistics/methodology
- Eurostat, Manual on Government Deficit and Debt, 2022 edition: https://ec.europa.eu/eurostat/documents/3859598/16029761/KS-GQ-23-002-EN-N.pdf
- MEF-RGS OpenBDAP, national accounts and cash accounts: https://openbdap.rgs.mef.gov.it/Home/ContiPubbliciContabilitaNazionale


## 13. Expanded candidate universe and separate correction factors

The candidate universe is intentionally broader than the set of measures expected to contribute materially to R&D. Mixed industrial, technology, health-data, space, energy-transition and enabling measures are retained for screening where project-level R&D may exist. This is not a presumption that their full allocation is R&D.

For each measure/project/year, estimate separately:
- R&D eligibility share: share of beneficiary expenditure meeting the Frascati definition;
- domestic performance share: share of that R&D performed by resident units in Italy;
- additionality share: share of eligible domestic R&D attributable to the intervention relative to the counterfactual.

The preferred decomposition is:

`Incremental domestic R&D = beneficiary expenditure × R&D eligibility share × domestic performance share × additionality share`

Do not estimate one blanket haircut for a whole mission, component or instrument. A zero R&D eligibility share is appropriate for an activity such as routine equipment installation; it does not imply that every project within a mixed programme has zero R&D. Leave coefficients missing until evidence is available; missing is not zero. Where only aggregate evidence exists, show explicit low/central/high scenarios and uncertainty rather than a falsely precise point estimate.

The broad inventory includes boundary/control candidates such as Transition 5.0, standard SME renewable installations and hospital equipment replacement. Their presence is intentional: they document why ordinary capital expenditure, routine digitisation, training, energy deployment or clinical service provision should not be mistaken for R&D.


## 13. State-budget, Treasury and ESA reconciliation

The State Budget Law and the Rendiconto generale dello Stato are core sources for annual appropriations, commitments and cash payments recorded in the State budget. They are not, on their own, a complete record of PNRR implementation flows. PNRR funding also passes through dedicated Treasury accounts (including accounts 25091 and 25092) and special accounts in Group 286. Some flows are subsequently transferred into ordinary State-budget chapters; others are paid through dedicated implementation arrangements.

Maintain separate records for:
- annual budget-law appropriations by chapter (initial and final; competence and cash);
- budget adjustments and notes of variation;
- final-account commitments, payments and residuals by chapter;
- inflows and outflows from dedicated NGEU Treasury accounts;
- internal transfers within Treasury / Group 286;
- transfers to administrations and implementing bodies;
- project expenditure declared and approved in ReGiS;
- ESA 2010 transaction and institutional-sector classification;
- actual R&D expenditure performed in Italy.

Do not infer that a transaction is outside general-government expenditure merely because it is not visible as an ordinary ministry chapter at the point of cash movement. Conversely, do not infer that every Treasury transfer or budget appropriation is final public expenditure. ESA 2010 classification depends on the institutional unit and economic substance of the transaction; recording is accrual-based. Financial transactions, grants, tax credits, equity and loans require transaction-specific treatment.

Internal transfers and transfers returned to the State budget must be eliminated in consolidated flow reconciliations. Budget commitments, cash payments, final-beneficiary expenditure and R&D performance are distinct stages and must never be added together.

GBARD is the bridge to public R&D budget allocations: ISTAT derives central-government data using initial and adjusted State-budget forecasts acquired from RGS, while regional data are collected directly. GBARD is not realised GERD and is not a PNRR-only series. Use it as an aggregate allocation/plausibility check, not as a direct measure of PNRR-induced R&D.


## 14. PNRR budget-law revisions and economies

Record separately:
- national expenditure already financed under existing legislation and subsequently relabelled as PNRR following plan revision;
- resources returned from dedicated NGEU Treasury accounts to State-budget revenue;
- economies identified at ministry level;
- economies identified at individual-measure level;
- actual expenditure / R&D performance.

The November 2025 PNRR revision replaced approximately EUR 6.5bn of measures with nationally financed expenditure already provided for under existing legislation and largely incurred in previous years. This expenditure must not be treated as new PNRR-induced expenditure when relabelled. The 2026 Budget Law provides for EUR 7.102bn of returns from NGEU Treasury accounts over 2026–2028. Treat this as a financing/budget operation, not as new negative spending in the year of return.

The February 2026 ministry-level economy annex totals EUR 1,587.510m but does not identify individual measures. The September 2026 measure-level economy annex identifies a further EUR 1,698m cohort, with measure-level data. Keep the two cohorts separate until their relationship with the 2026 Budget Law return and the legal/accounting perimeter is reconciled. An economy is not a negative GERD observation; a zero economy does not prove full expenditure or R&D performance.


## 12. Temporal architecture: PNRR implementation versus post-2026 fiscal flows

The core PNRR implementation window is 2020–2026. Under Article 17(2) of Regulation (EU) 2021/241, measures initiated from 1 February 2020 may be eligible; the Facility's implementation deadline for milestones and targets was 31 August 2026, with final Commission payments due by 31 December 2026. The 2020–2026 window is therefore the principal policy and implementation period for the PNRR analysis.

Do not interpret every year appearing in a budget or Treasury dataset as a year of PNRR implementation or R&D performance. Maintain distinct time dimensions:

1. **Policy eligibility / implementation period:** normally 2020–2026 for PNRR measures, with measure-specific start and end dates.
2. **R&D performance year:** year in which Frascati-eligible R&D is actually performed in Italy. This is the year assigned to the R&D shock.
3. **Budget authorisation / commitment year:** year in which the relevant State-budget authorisation or commitment is recorded.
4. **Cash-flow / Treasury year:** year in which a transfer, payment, return or cash movement occurs.
5. **ESA recording year:** year in which the transaction is recorded under ESA 2010 rules.
6. **Post-2026 financial tail:** 2027 and later may appear in budget or cash records because of repayment/return profiles, financial instruments, guarantees, loan maturities, final accounting or other national-budget consequences. These years must not be automatically classified as new PNRR implementation or new R&D performance.

In particular, the EUR 7.102bn return of NGEU Treasury resources under the 2026 Budget Law (EUR 5.943bn in 2026, EUR 1.000bn in 2027 and EUR 0.159bn in 2028) is a budget/financing flow. The 2027–2028 amounts are not a continuation of the PNRR implementation period and must not be entered as negative R&D expenditure or new PNRR investment in those years.

The R&D shock dataset should initially report annual PNRR-attributable R&D performance for 2020–2026, and may extend beyond 2026 only where evidence shows that an in-scope financial instrument or project actually finances eligible R&D performed in Italy after the PNRR implementation deadline. Such post-2026 R&D must be identified as a separately evidenced tail, not assumed from a budget profile.


## R&D tax credit: measurement and current evidence

The tax-credit series must distinguish at least: (i) the eligible R&D expenditure performed in the tax year; (ii) the credit accrued/recognised by the beneficiary for that tax year; (iii) the amount offset in F24 in a later year; and (iv) the ESA tax expenditure/cash or accrual treatment. These are not interchangeable.

The incremental R&D credit applied from 2015 to 2019, based on eligible expenditure above a historical average. From 2020, Law 160/2019 introduced the volume-based regime and separately defined R&D, technological innovation and design. For the 2020–2022 official evaluation, the published R&D&I category is a combined aggregate and must not be treated as pure Frascati R&D.

The dataset `data/processed/rd_tax_credit_evidence_2020_2022.csv` records:
- exact tax credits accrued by companies limited by shares in the combined R&D&I category: EUR 1,183m in 2020, EUR 1,379m in 2021 and EUR 1,080m in 2022; beneficiary counts: 18,736, 15,768 and 12,517 respectively;
- approximate all-entity R&D&I amounts read from Figure 1 (EUR 1,200m, 1,050m and 850m), flagged as approximate and not to be combined with the corporate-only table;
- Istat's combined cumulative tax-relief indicator for R&D tax credit plus Patent Box (0.04% GDP in 2015, 0.28% in 2019, 0.18% in 2020), kept separate because it does not isolate the R&D credit.

The combined R&D&I grouping includes technological innovation and design, so the dataset is an upper-bound proxy for the relevant R&D tax expenditure, not the pure R&D amount. A pure annual series requires disaggregated tax return records or administrative data. The 2022 tax-return data are provisional. The MEF/Bank of Italy/MIMIT evaluation uses integrated tax-return, business-account and employment data for 2016–2022 and is a useful basis for impact evaluation; its public report does not expose the full microdata.

For annual R&D performance, use Istat's business R&D survey (intra-muros and extra-muros R&D) as the outcome series, not the credit accrued. The tax credit can influence private R&D but is not itself GERD.

Sources:
- Istat, *Gli incentivi alle imprese per la ricerca e sviluppo – Anni 2015–2020*: https://www.istat.it/comunicato-stampa/gli-incentivi-alle-imprese-per-la-ricerca-e-sviluppo-anni-2015-2020/
- MEF/Bank of Italy/MIMIT, *Gli incentivi in investimenti 4.0: una valutazione dell'impatto della misura* (2024): https://img.innovationpost.it/wp-content/uploads/2024/11/29161253/Gli-incentivi-in-investimenti-4.0-una-valutazione-dellimpatto-della-misura.pdf
- MIMIT, R&D tax credit legal and administrative overview: https://www.mimit.gov.it/it/incentivi/credito-d-imposta-r-s
- Istat business R&D survey: https://www.istat.it/informazioni-sulla-rilevazione/ricerca-imprese/


## 9. R&D tax-credit additionality: empirical evidence and transferability

A separate evidence table, `data/processed/rd_tax_credit_impact_evidence.csv`, records Italy-specific OECD microBeRD+ estimates and a 2023 policy-mix indicator reported in the OECD Economic Survey 2026.

### Historical causal estimates (OECD microBeRD+, 2023)

The OECD reports difference-in-differences estimates for two distinct Italian tax-credit regimes:

- **2007–2009 volume-based credit:** policy-change DiD; intramural R&D log ATT -0.061 (s.e. 0.032), reported incrementality ratio 0.59; sample 19,181 firm-years.
- **2015–2019 incremental credit:** policy-uptake DiD; intramural R&D log ATT 0.389 (s.e. 0.016), R&D employment log ATT 0.279 (s.e. 0.009), extramural R&D log ATT 0.144 (s.e. 0.060); reported incrementality ratio 2.24; respective samples 90,371, 89,128 and 24,512 firm-years.

These estimates are valuable Italy-specific evidence that tax-credit design and treatment matter. They are **not interchangeable**. In particular, the 2.24 ratio applies to the 2015–2019 incremental scheme, not automatically to the 2020-onward volume-based R&D&I tax credit. The 0.59 estimate concerns a different 2007–2009 regime. Do not use either as a point estimate for the 2020–2022 credit amounts. They may be used only as historical benchmark / sensitivity bounds, with an explicit transferability caveat.

The OECD Economic Survey: Italy 2026 reports that tax incentives represented 64% of total government support to business R&D in 2023 (OECD average: 58%). This is a composition statistic, not an additionality coefficient and not the share of BERD financed by government.

### Estimation design for the 2020-onward regime

Preferred strategy:
1. Obtain beneficiary-level administrative data on R&D, technological innovation and design tax-credit claims separately, ideally by firm, year and eligible cost category.
2. Link claims to firm-level Istat R&D survey outcomes (intramural R&D, extramural R&D, R&D personnel), financial statements, employment and productivity.
3. Construct treatment intensity from eligible credit actually accrued / eligible expenditure, not from the scheme's budget ceiling.
4. Use a firm-level panel with firm and year fixed effects, and exploit variation in treatment intensity / eligibility thresholds / rate changes. Test pre-trends and anticipation.
5. Where credible thresholds or eligibility discontinuities exist, use regression discontinuity or difference-in-discontinuities; otherwise use matched DiD / event-study and report identifying assumptions.
6. Estimate heterogeneity by firm size, age, sector, profitability/tax capacity, region and whether the firm is a startup.
7. Separate intramural R&D performed in Italy from extramural R&D purchased from providers; verify domestic location before including the latter in domestic R&D.
8. Convert estimated causal effects into additional R&D by year of performance. Keep fiscal cost, credit accrual, F24 offsets and actual R&D performance as distinct series.

### Interim modelling rule

Until a causal estimate for the 2020-onward regime is obtained, the annual incremental R&D shock attributable to the 2020–2022 R&D&I tax credit remains **not estimated**. Do not multiply the observed €1.183bn / €1.379bn / €1.080bn corporate R&D&I credit amounts by 2.24. The published amounts combine R&D with technological innovation and design and the 2.24 coefficient belongs to a different, incremental scheme.

Sources:
- OECD (2023), *The Impact of R&D Tax Incentives: Results from the OECD microBeRD+ Project*, Table 18: https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/10/the-impact-of-r-d-tax-incentives_bc42ab04/1937ac6b-en.pdf
- OECD (2026), *OECD Economic Surveys: Italy 2026*, section on business dynamism and public support to R&D: https://www.oecd.org/en/publications/oecd-economic-surveys-italy-2026_539538b2-en/full-report/enhancing-business-dynamism-to-raise-productivity_ec8ed53a.html
- Banca d'Italia (2024), *Innovation and public support policies: a comparative analysis*, QEF No. 898: https://www.bancaditalia.it/pubblicazioni/qef/2024-0898/


## 10. National R&D macro baseline (Istat)

The processed file `data/processed/italy_rd_macro_baseline_2019_2025.csv` records the official national outcome series, separated by indicator and observation status.

### Intra-muros GERD
- 2019: EUR 26,259.661 million; 1.46% GDP.
- 2020: EUR 25,028.257 million; 1.50% GDP.
- 2021: EUR 25,991.328 million; 1.41% GDP.
- 2022: EUR 27,286.216 million; 1.37% GDP.
- 2023: EUR 29,399.402 million; 1.37% GDP.
- 2024: EUR 31,043.211 million; 1.40% GDP (latest revised Istat September 2026 release).

The 2019–2023 figures come from Istat's 2025 Statistical Yearbook (national accounts vintage September 2025). The 2024 value is from the September 2026 Istat release. The latter is a revised vintage: do not treat the older 2024 preliminary estimate of EUR 30,414.964 million (1.38% GDP) as the current observation. The dashboard uses the 2026 vintage for 2024 and flags this break.

### 2024 performing-sector decomposition
- Business enterprises: EUR 17,565.795 million.
- Government institutions: EUR 4,575.193 million.
- Higher education: EUR 8,351.861 million.
- Private non-profit: EUR 550.362 million.
- Total: EUR 31,043.211 million.

R&D personnel amounted to 352,333.4 full-time equivalents, of which 188,317 in enterprises, 47,718.8 in government, 108,592 in higher education and 7,705.6 in private non-profit.

### Preliminary 2025 information
Istat reports preliminary sector-specific growth rates for 2025: business R&D -2.6%, government institutions +6.2%, and private non-profit +6.4%. No total GERD growth rate is inferred from these partial sector indicators. Do not extrapolate or sum them to construct a national total.

### Interpretation
The series measures R&D performed in Italy (intra-muros), irrespective of funding source. It is the macro outcome, not a measure of PNRR impact. Nominal values must be deflated before interpreting real growth or estimating a real R&D shock. Sector of performance and source of funds are distinct dimensions; public funding of business R&D does not mean the public sector performed that R&D.

Sources:
- Istat, *La ricerca e sviluppo in Italia – Anni 2024–2025*, 24 September 2026: https://www.istat.it/wp-content/uploads/2026/09/REPORT_RS_2026.pdf
- Istat, *Annuario Statistico Italiano 2025*, Chapter 21, Table 21.1: https://www.istat.it/storage/ASI/2025/capitoli/C21.pdf
- Eurostat, `rd_e_gerdtot`, GERD by sector of performance: https://ec.europa.eu/eurostat/databrowser/view/rd_e_gerdtot/default/table


## 11. Main macro outcome: R&D intensity as a share of GDP

The primary national outcome for the macro panel and the eventual model interface is **intra-muros GERD as a percentage of GDP** (R&D intensity). The nominal GERD level in EUR million remains a complementary series and must be retained in the database.

### Why use the GDP share as the headline series?

- It normalises R&D performance by the size of the economy and is the standard Eurostat indicator for cross-country comparison and national R&D intensity targets.
- The shock can be expressed transparently as an incremental contribution in percentage points of GDP.
- It avoids presenting nominal expenditure growth as an improvement in R&D effort when the change may partly reflect inflation or GDP growth.

### Important interpretation and modelling caveats

1. The ratio is not a real-volume measure. A rise in GERD/GDP can occur because GERD rises, GDP falls, or both. Retain nominal GERD and nominal GDP as companion series and, for real expenditure analysis, deflate the GERD numerator separately.
2. For a policy shock, calculate the additional GERD amount in constant prices first, then divide by the corresponding GDP in the same price basis (or use a consistent nominal numerator and nominal GDP for a current-price ratio). Do not divide constant-price GERD by current-price GDP.
3. Distinguish percentage points from percentage changes. An increase from 1.40% to 1.45% of GDP is +0.05 percentage points of GDP, not +0.05%.
4. Do not use the observed post-2020 change in GERD/GDP as the PNRR treatment effect. The counterfactual must account for pre-existing trends, the business cycle, other national and EU policies, and GDP denominator movements.
5. The present detailed Istat series combines the 2019–2023 vintage in the 2025 Statistical Yearbook with the revised 2024 observation published in September 2026. The vintage is explicitly recorded at observation level. For econometric work and international comparison, a fully harmonised Eurostat `rd_e_gerdtot` extraction should be the preferred master series; the Istat series is retained for detailed national consistency and sector decomposition.
6. The 2025 indicators are preliminary sector-specific growth rates, not a complete GERD/GDP observation. No total 2025 intensity is inferred.

### Proposed macro-model dependent variables

- Primary: GERD/GDP (percentage points), total and by sector of performance where available.
- Secondary: real GERD (2019 prices), total and by sector.
- Supporting outcomes: BERD/GDP, HERD/GDP, GOVERD/GDP, R&D personnel (FTE) and business R&D employment.
- Funding-source decomposition (government, business, abroad, higher education, private non-profit) is a separate dimension from sector of performance and must not be conflated with it.

Sources:
- Eurostat, *GERD by sector of performance*, dataset `rd_e_gerdtot`, unit percentage of GDP: https://ec.europa.eu/eurostat/databrowser/view/rd_e_gerdtot/default/table
- Eurostat, *GDP and main components*, dataset `nama_10_gdp`: https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table
- Eurostat metadata on current prices, chain-linked volumes and implicit deflators: https://ec.europa.eu/eurostat/cache/metadata/EN/nama_10_gdp_esms.htm


## 12. Eurostat master series and GDP deflator proxy

The Eurostat master outcome is `rd_e_gerdtot`, filtered to Italy, annual frequency, percentage of GDP and sectors TOTAL/BES/GOV/HES/PNP. The 2010–2024 extraction is stored in `data/processed/eurostat_rd_intensity_italy_2010_2024.csv`; nominal GDP and chain-linked GDP volume index from `nama_10_gdp` are stored in `data/processed/eurostat_gdp_italy_2010_2024.csv`. The merged panel is `data/processed/eurostat_macro_panel_italy_2010_2024.csv`.

A GDP-wide implicit-deflator proxy is derived from current-price GDP and the chain-linked volume index, then rebased to 2019=100. This proxy captures economy-wide price movements and must not be described as an observed R&D deflator. It may be used as a transparent provisional deflation assumption, with sensitivity analysis. The preferred approach for real R&D is an R&D-specific price index or cost deflator if a defensible source is identified.

The primary dependent variable is GERD/GDP in percentage points. Preserve nominal GERD, nominal GDP, chain-linked GDP volume index and the deflator proxy as companion series. Never combine constant-price R&D with current-price GDP when calculating a ratio.
