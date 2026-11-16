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

Track public commitments, fund-level investments, private co-investment and final company expenditure separately. Estimate the R&D component using defensible company- or portfolio-level evidence. Financing is not itself R&D expenditure; the same euro must not be counted both as an investment and again as the activity financed.

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
