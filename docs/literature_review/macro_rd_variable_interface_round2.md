# Literature-based macro R&D variable interface — research round 2

**Run:** LR-2026-11-27-R2  
**Status:** candidate interface for model fitting; not a calibrated model specification  
**Perimeter:** PNRR plus directly associated national co-financing for the policy shock. The 2018–2025 national fiscal-measures census remains separate.  
**Price basis:** retain nominal and 2019-price EUR series, consistently deflated and versioned.

## 1. Purpose and conclusion

The literature does not support a universal single "R&D shock" variable. It supports a layered interface that can feed different model families (QUEST/DSGE, semi-endogenous growth, production-function/VECM/BVAR) without confusing policy instruments, realised R&D inputs, knowledge accumulation and macroeconomic outcomes.

The recommended starting point is a **minimum annual macro interface with six policy/performance blocks**, plus a separate satellite set for estimation and validation. The macro model should decide which blocks are exogenous shocks, endogenous variables, states or controls. Until the receiving model is specified, the repository should preserve the underlying dimensions and not collapse them into one scalar.

## 2. What the literature says

### 2.1 QUEST / semi-endogenous growth models

- Roeger, Varga and in 't Veld (2008), *Structural Reforms in the EU*, European Economy Economic Paper 351, describe a micro-founded DSGE with endogenous growth and policy instruments including taxes, benefits, subsidies and education expenditure. The Commission summary explicitly reports R&D subsidies, skill composition and adjustment lags as modelled reform channels. The full technical paper still needs equation-level extraction.
- Pfeiffer, Varga and in 't Veld (2024), B3, maps its R&D reform indicator directly to the private high-skilled R&D wage-subsidy wedge (s^{RD}). Its research-production mechanism separately uses R&D labour, domestic and foreign knowledge stocks, and productivity/spillover elasticities. This is not total R&D spending and not direct public research grants.
- Varga and in 't Veld (2009), QUEST III Cohesion Policy application, has separate channels for productive public capital, R&D/RTDI support and human capital. Its broad RTDI mapping includes innovation activities beyond strict Frascati R&D. It is useful for transmission architecture, not for classifying Italian spending.
- A later exposition of QUEST III specifies R&D investment subsidies through tax credits/depreciation allowances on R&D intangible investment, alongside physical-capital subsidies and a government budget constraint. Thus wage subsidies and user-cost/tax wedges are distinct policy representations, not interchangeable observations.

### 2.2 Public and private R&D and productivity

- Van Elk et al. (2015), CPB Discussion Paper 313, compare Cobb-Douglas, translog and augmented production functions for 22 OECD countries. Their abstract reports that baseline models controlling for private and foreign R&D and production factors often yield insignificant or negative public-R&D returns; more positive results emerge in models adding public capital, FDI stocks and high-tech trade shares. The paper's conclusion is explicitly context-dependent: public R&D does not automatically generate GDP/TFP growth.
- Herzer (2021/2022), *An Empirical Note on the Long-Run Effects of Public and Private R&D on TFP*, uses TFP, GDP, domestic public/private R&D capital and foreign public/private R&D capital. It also tests researcher counts as alternative activity measures, warning that PIM stocks can be sensitive to price-deflator assumptions. Its estimates find positive long-run effects using researcher counts, but the broader literature is mixed.
- The public/private/foreign R&D stock specification is a useful candidate for VECM/BVAR or production-function work, but stock construction, depreciation and deflators must be explicit. It is not itself a QUEST structural equation.

### 2.3 Tax and direct business R&D support

- OECD microBeRD (Appelt et al., 2020) uses business intramural R&D expenditure and B-Index/user-cost measures at country-industry-size-year level, with firm-level treatment uptake and support amounts where available. It examines R&D labour expenditure, headcount, FTE, implied unit labour cost, intensive/extensive margins, firm size, industry and type of R&D.
- The OECD report estimates a cross-country user-cost elasticity around -0.6 in its baseline micro-aggregated specification, but estimates vary by timing, cost category, firm size and industry. Treat this as a literature benchmark, not an Italy parameter.
- The OECD study distinguishes gross incrementality ratios from net additionality: ratios below one can indicate some crowding out; ratios above one net crowding-in. A tax-credit amount, B-index, direct grant and R&D expenditure are separate variables.
- The European Commission's 2014 *A Study on R&D Tax Incentives* notes the diversity of instrument design (volume/incremental, tax credits, allowances, accelerated depreciation, payroll tax incentives), heterogeneous firm responses and possible timing effects.
- Dimos and Pugh (2016) find strong heterogeneity across 52 micro-evaluation studies and warn that failure to address endogenous subsidy allocation exaggerates effects. Dimos et al. (2022) find both tax credits and grants can induce input additionality but stress country/firm heterogeneity and publication/power limitations. Neither justifies a single coefficient for all instruments.

### 2.4 Statistical measurement boundary

- OECD Frascati Manual 2015 §§4.7–4.8 defines GERD as intramural R&D expenditure performed in the national territory, regardless of funding source; it includes domestic performance funded from abroad and excludes funding for R&D performed abroad.
- Frascati Chapter 4 requires separate reporting of intramural performance, sources of funds and extramural funding flows. GERD can therefore be crossed by performing sector and funding source.
- Frascati Chapter 5 recommends both headcounts and FTE/person-years for R&D personnel. FTE measures actual time devoted to R&D and is preferable for labour-input mechanisms where available.
- GBARD (budget allocations) and GTARD (government tax relief) are government-support measures; neither is the same concept as realised GERD.

## 3. Recommended candidate variable architecture

### Layer A — policy shocks / exogenous policy inputs

These are the variables the PNRR evidence engine should try to construct, without assuming that the macro model uses all of them:

1. **Direct public R&D funding/performance impulse**: annual Frascati-eligible public funding and, separately, actual R&D expenditure performed by HERD/GOVERD/PNP recipients. The fiscal funding series and performance series must not be conflated.
2. **Business direct-support wedge/flow**: grants and other direct funding to business R&D, split between support amount, eligible base and actual recipient R&D. If the model has a grant wedge, construct it from recipient-level or sectoral data; do not use public grant allocations as BERD.
3. **R&D tax user-cost wedge**: annual B-index or a model-consistent marginal user cost of R&D, incorporating the tax treatment of labour and capital inputs. Retain GTARD/tax expenditure as a separate fiscal series.
4. **R&D labour-cost subsidy wedge**: only where a scheme demonstrably subsidises researcher wages/employment and the model contains a wage-subsidy instrument. This is the closest match to B3 (s^{RD}); it is not a generic public-research variable.
5. **R&D/RTDI fixed-cost or intangible-investment support**: optional model-specific wedge, only if the receiving model contains fixed-cost/intangible-cost channels. Keep broader RTDI separate from Frascati-eligible R&D.
6. **Research infrastructure/public capital impulse**: only the productive capital component and its commissioning/operational profile; not the construction allocation or full project value. It may be a public-capital input rather than R&D expenditure.
7. **Human-capital/researcher-supply impulse**: doctoral/researcher training or skill policies represented through additional qualified labour or human-capital efficiency, not automatically through R&D expenditure.

### Layer B — realised R&D inputs and state variables

8. **GERD by performing sector**: BERD, HERD, GOVERD and PNP, annual, nominal and constant-price.
9. **GERD by source of funds**: government, business, higher education, PNP, rest of world; retain cross-tabulation with performer sector where possible.
10. **R&D by type**: basic research, applied research, experimental development.
11. **R&D cost composition**: researcher labour costs, other current costs, capital expenditure; where possible distinguish equipment/software/IP products.
12. **R&D personnel by sector and function**: researchers and other R&D personnel, both headcount and FTE/person-years; qualification/skill mix where available.
13. **Private and public R&D capital stocks**: constructed from constant-price flows using a documented perpetual-inventory method and sensitivity to depreciation/deflators. Keep public and private stocks separate.
14. **Foreign public and private R&D stocks**: weighted foreign knowledge/R&D exposure, using explicit partner weights; do not treat foreign R&D as Italian domestic expenditure.

### Layer C — knowledge, transmission and macro outcomes

15. **Knowledge/innovation output**: patent applications/grants and citations, publications or other outputs as satellite measures; never use patents as a substitute for R&D expenditure.
16. **TFP / labour productivity**: macro outcome or endogenous state depending on model.
17. **GDP / value added**: macro outcome; for sectoral models retain industry value added.
18. **Physical capital and public capital**: productive capital stocks; separate research infrastructure where modelled.
19. **Human capital / skill composition**: education or skill-adjusted labour and high-skilled labour supply.
20. **International exposure**: foreign R&D stocks, high-tech imports/exports and FDI stocks as possible spillover/productivity controls where supported by the chosen model.

### Layer D — identification, estimation and validation variables

21. **Firm-level R&D expenditure and cost components**.
22. **Firm-level public grant receipt, amount, eligible costs and tax support uptake**.
23. **Firm size, industry, age, productivity, profitability/tax position and baseline R&D status**.
24. **University/research-institute exposure and formal R&D cooperation**.
25. **Treatment timing, eligibility thresholds, policy design changes and comparison-group identifiers**.
26. **Utilisation, R&D eligibility, domestic-performance, additionality and timing parameters**, stored separately with evidence and uncertainty.

These firm-level variables are not necessarily macro model inputs. They support causal estimation of the policy-to-R&D mapping and heterogeneity.

## 4. Minimum viable macro interface

The minimum interface to build first is:

| Block | Annual series to prepare | Why it is needed | Status |
|---|---|---|---|
| A. Public R&D | Public R&D funding by measure and performer; actual HERD/GOVERD/PNP performed | Direct public research channel | Core |
| B. Business incentives | Direct grants, GTARD/tax expenditure, B-index/user cost, eligible business R&D | Business cost/price channel | Core |
| C. Realised R&D | GERD by performer × funding source × R&D type; BERD/HERD/GOVERD | Outcome and consistency benchmark | Core |
| D. Research labour | Researchers FTE and headcount by sector; R&D labour costs | Production-function input and wage-subsidy transmission | Core |
| E. Knowledge capital | Public/private R&D stocks and foreign exposure | Growth mechanism/state; constructed with sensitivity | Core for growth/VECM models |
| F. Macro controls/outcomes | TFP, GDP/value added, physical capital, human capital, public capital | Fit and transmission | Core for macro estimation, model-specific |

A DSGE/QUEST implementation may instead treat several of these as endogenous states and require only policy wedges plus initial conditions/calibration. A reduced-form BVAR/VECM may include R&D stocks, TFP, GDP and foreign stocks as jointly endogenous variables. The interface should support both without deciding in advance.

## 5. Important modelling cautions

1. **Do not overfit a large BVAR to a short Italian annual sample.** The 2015–2024 statistical baseline is too short for a richly parameterised annual BVAR. Historical extensions, quarterly proxies, cross-country panels, Bayesian shrinkage or a structural calibration may be needed. Model choice must be driven by the receiving model and data coverage.
2. **Do not construct public/private R&D stocks with one unexamined GDP deflator.** R&D-specific price indices or labour/equipment cost deflators should be explored. Herzer documents sensitivity of PIM stocks to identical-deflator assumptions. Preserve alternative stocks and depreciation assumptions.
3. **Do not collapse public research and business incentives.** They affect different performers and may have different direct, spillover and crowding-out channels.
4. **Do not count researcher headcount as FTE.** Headcount and FTE measure different margins; OECD microBeRD shows why a policy can raise headcount more than R&D time actually devoted.
5. **Do not use a patent count as an R&D flow.** Patent output is a noisy, lagged knowledge outcome.
6. **Do not apply one additionality coefficient to grants, tax credits, public research, VC and infrastructure.** Use instrument-specific causal evidence and explicit counterfactuals.
7. **Do not insert broad DTF/GTF proxy into official GERD/BERD.** It remains a separate broad innovation proxy under the project's existing decision/methodology; company-level Frascati R&D is needed for the official-boundary series.
8. **Do not equate public R&D capital with government budget allocations.** Public R&D capital is a constructed knowledge stock; GBARD is a budget-support measure.

## 6. Mapping to the Italian PNRR work

- PRIN, FIS/FISA, research partnerships, national centres and research infrastructures: first trace public funding to recipient and performance year, identify performer (HERD/GOVERD/PNP as evidenced), and classify Frascati costs. Do not map to B3's private wage subsidy.
- Business R&D grants and tax incentives: construct direct-support and tax-user-cost variables separately; link beneficiaries to firm-level R&D and researcher employment; estimate additionality with selection/endogeneity controls.
- DTF/GTF and other VC instruments: keep fund commitments, capital calls, investment decisions and portfolio-company expenditure separate. Only portfolio-company R&D actually performed in Italy can enter BERD/GERD; retain the adopted broad proxy as a separate satellite series.
- Research infrastructure: distinguish construction/acquisition, R&D-specific equipment, commissioning and actual research use; model public capital only if the receiving model includes it.
- Doctoral and researcher programmes: track researchers/FTE and skill supply; classify actual R&D time separately from education/training.

## 7. Data extraction priorities before fitting

1. Consolidate Eurostat/OECD/ISTAT annual GERD by performer and funding source, R&D type and cost category, with vintage and metadata.
2. Extract GBARD and GTARD as separate government-support series.
3. Build sectoral R&D personnel headcount/FTE and researcher labour-cost series.
4. Build public/private R&D flow series and alternative knowledge stocks with transparent deflators and depreciation.
5. Construct the annual policy-instrument series from PNRR measures and directly associated national co-financing.
6. Locate firm-level microdata access pathways (ISTAT R&D survey, tax records, RNA/ReGiS beneficiary data, business accounts) and document access restrictions.
7. Identify Italian TFP, GDP/value-added, physical capital, public capital and human-capital series consistent with national accounts vintages.
8. Only then select candidate model(s), fit reduced-form diagnostics and map into the receiving model's equations.

## 8. Literature register and limits of this round

Reviewed in this round:
- OECD (2015), *Frascati Manual 2015*, especially §§4.7–4.8 and Chapter 5 §§5.46–5.50.
- Roeger, Varga and in 't Veld (2008), European Economy Economic Paper 351: Commission publication summary reviewed; full equations still pending.
- Pfeiffer, Varga and in 't Veld (2024), B3: technical review documented in round 1.
- Varga and in 't Veld (2009), QUEST III Cohesion Policy: technical review documented in round 1.
- Appelt, Bajgar, Criscuolo and Galindo-Rueda (2020), OECD microBeRD, No. 92.
- European Commission/CPB consortium (2014), *A Study on R&D Tax Incentives*, Taxation Paper 52.
- Dimos and Pugh (2016), meta-regression of R&D subsidy evaluations.
- Dimos et al. (2022), comparative meta-regression of tax credits and subsidies.
- van Elk et al. (2015), CPB Discussion Paper 313, public R&D returns.
- Herzer (2021 online; 2022 issue), public/private R&D and TFP.
- Akcigit, Hanley and Stantcheva (2021 revised; published 2022), optimal taxation and R&D, reviewed in round 1.

Not completed: full equation-level extraction of Roeger et al. (2008); full technical review of D'Auria et al. (2009); further public-research spillover and infrastructure literature; Italy-specific data availability audit; actual model fitting. This document is a candidate interface, not approval of a final model or numerical parameter set.
