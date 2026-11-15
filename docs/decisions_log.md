# Methodology and project decision log

Record durable decisions here so that work does not depend on conversation history. New entries should include date, decision, rationale, alternatives considered, implications and status.

## D001 — Separate policy allocation from additional R&D expenditure

- **Status:** Adopted as a core principle.
- **Decision:** A financial envelope or budget authorisation is not automatically an R&D expenditure shock.
- **Rationale:** Policy financing, realised beneficiary expenditure and statistically measured R&D are different concepts.
- **Implication:** Maintain separate accounting stages and estimate an R&D-relevant and additional component.

## D002 — Use four policy channels

- **Status:** Adopted as initial classification.
- **Decision:** Classify interventions as direct public R&D, business R&D incentives, venture capital/financial instruments, and R&D ecosystem/enabling measures.
- **Rationale:** The channels have different transmission mechanisms, data requirements and additionality problems.
- **Implication:** Keep channel-specific data and parameters before aggregation.

## D003 — Apply the Frascati boundary

- **Status:** Adopted as the R&D activity reference.
- **Decision:** Classify activities by whether they constitute basic research, applied research or experimental development, rather than relying on policy labels.
- **Rationale:** General innovation and capital expenditure are not necessarily R&D.
- **Implication:** Record evidence and eligibility status for each measure.

## D004 — Keep performance sector and funding source separate

- **Status:** Adopted.
- **Decision:** Maintain distinct dimensions for GERD by performing sector and GERD by source of funds.
- **Rationale:** Who performs research is not necessarily who finances it.
- **Implication:** Use separate fields in statistical and shock datasets.

## D005 — Keep the model interface modular

- **Status:** Adopted.
- **Decision:** Do not impose a macroeconomic model equation or elasticity before the receiving model is supplied.
- **Rationale:** The shock data should be adaptable to the model's actual definitions and input requirements.
- **Implication:** Produce a dimensional dataset and a documented mapping layer later.

## D006 — PNRR perimeter and directly associated national co-financing

- **Status:** Adopted.
- **Decision:** The core policy perimeter includes PNRR measures and national co-financing directly associated with those measures. It excludes unrelated national measures outside the PNRR.
- **Rationale:** The exercise aims to identify the R&D shock attributable to the PNRR intervention package without broadening the counterfactual to all national industrial and R&D policy.
- **Implication:** Track EU PNRR financing and directly associated national co-financing separately, while preventing double counting of the same intervention.

## D007 — Optional extension to other EU programmes

- **Status:** Adopted as an optional scope feature.
- **Decision:** Provide a configuration option to include other EU programmes, initially Cohesion Policy and the European Innovation Council (EIC), in an expanded scenario.
- **Rationale:** These programmes may provide relevant R&D support but should not contaminate the PNRR-only headline estimate.
- **Implication:** Keep programme-level identification and produce PNRR-core and expanded-EU-programme outputs separately.

## D008 — Two distinct R&D output concepts

- **Status:** Adopted.
- **Decision:** Produce both (i) additional domestic R&D performed in Italy and (ii) the publicly financed component of domestic R&D performed in Italy.
- **Rationale:** The first measures the additional R&D activity; the second identifies its public financing dimension.
- **Implication:** The publicly financed series is a subset/view of the domestic R&D performed series and must not be added to it.

## D009 — 2019 constant-price reference year

- **Status:** Adopted.
- **Decision:** Retain nominal values and express the constant-price series in 2019 euros.
- **Rationale:** A common pre-pandemic reference year provides a consistent price basis for the historical series and shock estimates.
- **Implication:** Document the selected deflator, source and vintage. 2019 is a price base, not the counterfactual baseline.

## Open decisions

- **OD001:** Select the preferred deflator for conversion to 2019 prices after reviewing Eurostat/OECD metadata and the macroeconomic model requirements.
- **OD002:** Confirm whether the model additionally requires funding-commitment series alongside expenditure-performed series.
