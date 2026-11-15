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
