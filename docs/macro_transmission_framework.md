# Macro transmission and annual shock estimation framework

## Purpose

This workstream extends the measure-level R&D shock framework into a broader macroeconomic transmission analysis. It does not replace the primary estimand (additional domestic R&D performed in Italy). It creates a separate, modular mapping from each PNRR measure and year to the macroeconomic variables it may affect.

## 1. Two distinct analytical outputs

1. **Policy impulse / expenditure shock:** measure-year values for appropriations, commitments, disbursements, beneficiary expenditure, eligible R&D expenditure and additional R&D. This is the evidence-based annual input.
2. **Macroeconomic effects:** changes in GDP/value added, gross fixed capital formation, employment, private investment, productivity, exports/imports, prices and public finances. These require an explicit transmission model or causal evaluation.

Do not treat a financing envelope, cash transfer or investment announcement as an observed macroeconomic effect. The macro transmission matrix is initially qualitative; it identifies plausible channels, lags, required evidence and quantification rules.

## 2. Annual unit of observation

The core panel is one row per PNRR measure per calendar year, extended to 2018–2030. It is a blank evidence-collection template, not an estimated dataset. 2018–2019 are the pre-RRF baseline; 2020–2026 are the RRF window subject to measure-specific eligibility; 2027–2030 capture persistence/spillovers and are not RRF-financed by default. Blank numeric fields mean not yet collected, not zero. See docs/policy_chronology_and_rrf_eligibility.md and data/processed/pnrr_measure_timeline.csv.

For each measure-year, collect separately:
- budget authorisations;
- legal/administrative commitments;
- cash payments/disbursements;
- final-beneficiary expenditure;
- Frascati-eligible R&D expenditure performed in Italy;
- additionality rate and resulting incremental R&D;
- public and private investment;
- employment/FTE and labour costs;
- value added, fixed investment, exports/imports;
- relevant price/cost indicators and fiscal cost.

The year assigned to the R&D shock is the year of actual R&D performance, not necessarily the year of allocation, commitment or cash transfer. Keep 2027+ only in a separately evidenced post-PNRR tail.

## 3. Macro variables and channels

| Variable | Main policy channels | Main evidence / identification requirement |
|---|---|---|
| GERD / BERD / HERD / GOVERD | Direct research, business R&D grants/tax incentives, portfolio-company R&D | Actual Frascati-eligible R&D by performing sector and performance year |
| GDP / value added | Direct demand, investment, R&D activity, productivity spillovers | National-accounts-consistent expenditure/output data or model multipliers |
| Gross fixed capital formation | Infrastructure, industrial capex, equipment and private co-investment | Realised domestic fixed assets; separate imported content |
| Employment / labour costs | Research hiring, project implementation, startup growth | FTE/payroll by occupation, net of substitution and temporary effects |
| Human capital | Doctorates, research training, skills and researcher mobility | Cohort outcomes, completion and employment follow-up |
| Private investment | Co-financing, venture capital crowding-in, firm capex | Actual private funds mobilised and counterfactual |
| Productivity / TFP | Knowledge creation, diffusion, innovation, scale-up | Firm/sector evaluation or calibrated macro model; long lags |
| Exports / competitiveness | Industrial innovation, technology adoption and scale-up | Firm-level exports, domestic value added and market share |
| Imports / external balance | Imported machinery, intermediate inputs, foreign investment leakage | Import content and input-output tables |
| Prices / costs | Demand pressure, wages, construction and input costs | Sectoral price indices and capacity constraints |
| Public balance | Grants, tax expenditures, loans, equity, guarantees and EU receipts | ESA 2010 treatment and fiscal-risk accounting |

## 4. Estimation sequence

1. Reconstruct measure-year financial execution; never allocate the full envelope evenly across years.
2. Trace payments to final beneficiaries and identify the year expenditure occurred.
3. Split each beneficiary expenditure into R&D, non-R&D investment, services, training and other categories.
4. Apply an evidence-based additionality/counterfactual parameter by instrument and year.
5. Produce the direct annual policy impulse (including additional R&D and, separately, non-R&D investment).
6. Map the impulse to macro variables using the actual receiving model equations or credible causal evaluations.
7. Report conservative/central/high scenarios only when parameter ranges have a defensible evidence base.

## 5. Accounting and causal safeguards

- Avoid double counting EU and national co-financing, transfers between intermediaries, and fund-level equity alongside the expenditure financed by portfolio companies.
- A venture-capital investment is a financial transaction; startup creation or business formation is not automatically R&D. Only actual eligible R&D performed in Italy enters the R&D shock.
- R&D spending and non-R&D capex are separate impulses. Do not count the same project euro in both.
- Employment, productivity, GDP and export impacts are not directly observable from an allocation. They require beneficiary data, a counterfactual, input-output analysis or the receiving macro model.
- Direction and lag labels in the transmission matrix are hypotheses for research design, not estimated causal effects.
- No model multiplier or elasticity is assigned until the model equations, units and timing conventions are available.

## 6. Current first-pass priorities

Prioritise measure-year reconstruction for:
- MUR direct research programmes (PRIN/PNR, young researchers, extended partnerships, National Centres, doctoral programmes);
- MIMIT business R&D instruments (IPCEI, Innovation Agreements, hydrogen R&D grants/loans);
- Digital and Green Transition Funds, with separate fund deployment, direct/indirect investment, private leverage and portfolio-company R&D;
- mixed industrial and infrastructure measures only after R&D/non-R&D expenditure can be separated.

The measure inventory contains other lower-relevance or enabling measures. Retain them in the database but do not force a quantified R&D or macro shock where evidence is absent.
