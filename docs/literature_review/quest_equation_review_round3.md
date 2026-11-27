# QUEST equation-level review — round 3 addendum

**Run:** LR-2026-11-27-R3  
**Sources:** Roeger, Varga and in 't Veld (2008), European Economy Economic Paper 351; D'Auria, Pagano, Ratto and Varga (2009), Economic Paper 392. Full official Commission PDFs reviewed.

## 1. QUEST endogenous-growth architecture: technical confirmation

Roeger et al. (2008) specify a micro-founded DSGE with investment in tangibles and intangibles, skill-disaggregated labour and a semi-endogenous Jones/Romer product-variety framework. The research sector employs high-skilled labour and produces new designs using existing domestic and foreign knowledge.

The research-production function (paper section 2; around p. 15) can be represented conceptually as:

\[
\Delta A_t = \nu (A_t)^{\phi}(A_t^*)^{\varpi}(L_{A,t})^{\lambda}
\]

where domestic and foreign knowledge stocks enter separately, (L_A) is research labour, and (
u,\phi,\varpi,\lambda) govern efficiency, spillovers and research-labour elasticity. The exact printed equation should be transcribed from the PDF if later implemented in code; the conceptual variable mapping is unambiguous.

The research institute chooses high-skilled labour and faces an adjustment cost of hiring. This makes the path of researcher employment gradual rather than instantaneous. A model-ready dataset therefore needs both annual R&D labour input and the policy timing profile; a one-year budget shock should not be mechanically equated to a one-year jump in FTE.

## 2. QUEST policy instruments are distinct

Section 3.1 of Roeger et al. (2008) compares two separate interventions, each calibrated to 0.1% of GDP:

1. A tax credit on returns from intangible capital, which lowers the cost/rental rate of intangible assets and reduces fixed costs faced by intermediate producers.
2. A wage subsidy paid to the R&D sector on researcher wages.

The paper's simulations report different transition paths. In the wage subsidy experiment, GDP initially falls as high-skilled workers move from production to research, before long-run gains emerge. In the tax-credit experiment, the mechanism operates through demand for patents, intangible investment and entry/fixed costs.

A particularly important model result is that about 25% of the increase in R&D spending in the tax-subsidy simulations is due to higher wages for high-skilled workers. This is a model-specific result, not a transferable Italian coefficient. It reinforces the need to distinguish:
- R&D labour expenditure;
- R&D headcount;
- R&D FTE/person-years;
- implied R&D unit labour cost.

The model explicitly warns that high-skilled labour supply constraints and wage inflation can absorb part of a fiscal incentive without an equivalent increase in real research labour input.

## 3. D'Auria et al. (2009): country calibration and Italy-specific lesson

D'Auria et al. calibrate the Roeger-Varga-Veld (2008) model separately for EU Member States using country-specific structural characteristics. The paper uses:
- Eurostat R&D intensity and researcher share of employment;
- the R&D labour elasticity, based on calibration/Bottazzi and Peri;
- Warda's B-index evidence for R&D subsidies;
- Eurostat skill composition and employment;
- EUKLEMS mark-ups;
- entry-cost and intangible risk-premium assumptions.

For Italy, Table 1 (average calibration inputs, generally 2003–2007) reports:
- researchers (L_A): 0.51% of employment;
- R&D intensity: 1.10% of GDP;
- R&D elasticity with respect to labour (lambda): 0.37.

These are historical calibration inputs from the paper's period and definitions, not current Italian statistics and not recommended present-day parameter values. They are useful as a documented historical model benchmark and a cross-check on the types of Italian inputs required.

The country-comparison exercise finds that less R&D-intensive countries tend to benefit more from R&D-promoting and skill-upgrading policies. This is partly a scale-of-shock result: a common 0.1%-of-GDP policy shock is proportionally larger relative to a small pre-existing R&D base. Other structural characteristics (mark-ups, entry barriers, risk premia, research efficiency and labour constraints) also explain differences.

## 4. Implications for the candidate variable interface

The equation-level review strengthens the following requirements:

- Keep tax credits/user-cost relief and researcher wage subsidies as separate policy wedges.
- Record the policy shock in model-consistent units (e.g. EUR/GDP or marginal subsidy rate), and retain both gross fiscal cost and effective wedge.
- Track research-labour expenditure, headcount and FTE separately to identify wage-price versus quantity responses.
- Preserve the high-skilled wage and researcher-labour supply/skill composition as calibration or endogenous labour-market variables.
- Include hiring adjustment/persistence parameters in the model-parameter register, not in the observed fiscal dataset.
- Where the receiving model has an intangible-capital/entry channel, retain intangible investment/user-cost and entry/fixed-cost variables; do not assume these are direct R&D expenditure.
- For Italy, historical QUEST calibration values can inform a starting benchmark only; current data and model re-estimation/calibration are required.

## 5. Model choice and fitting implications

The evidence now supports three viable but distinct routes:

**Route A — Structural QUEST/DSGE handoff.** Best if the receiving model equations are available. Inputs are policy wedges, public R&D/performance series, research-labour data and calibration parameters. TFP, GDP, wages, employment, patent/idea stocks and capital are largely endogenous states/outcomes, not all exogenous regressors.

**Route B — Reduced-form macro time-series (BVAR/VECM).** Use a parsimonious endogenous vector such as real GDP or TFP, public R&D stock/flow, private R&D stock/flow, researchers or FTE, and foreign R&D exposure. The annual Italian sample is short; a large unrestricted VAR is not credible without long historical data, panel information, quarterly indicators or strong Bayesian shrinkage.

**Route C — Production-function / panel benchmark.** Use output or TFP with physical capital, quality-adjusted labour/human capital, public/private/foreign R&D stocks or researcher counts, plus public capital, FDI and high-tech trade controls where data allow. Results are sensitive to specification and stock construction; use as a robustness/benchmark route, not an automatic causal PNRR estimator.

The PNRR policy-to-R&D causal estimation remains a separate first-stage exercise. The macro model should receive a measured/estimated annual R&D impulse with uncertainty, not be asked to infer from allocations what R&D occurred.

## 6. Open tasks

- Review Roeger et al. (2009), *Modelling the Lisbon Strategy*, or establish whether the QUEST 2008/2009 equations already cover the needed instrument channels.
- Complete the public-research spillover literature review, including university/basic research channels.
- Audit Italian annual series and vintages for GERD, GBARD, GTARD, researcher FTE, productivity and R&D deflators.
- Decide whether the eventual fitting route is a receiving QUEST model, BVAR/VECM or production-function benchmark only after the variable availability audit and model access.
