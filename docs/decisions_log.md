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


## D010 — Measure screening must be broader than explicit R&D labels

- **Status:** Adopted.
- **Decision:** Initial screening covers M4C1, M4C2, potentially R&D-relevant measures in M6, and M1C2 measures such as R&D tax credits and the Digital and Green Transition Funds. The screening is not a presumption that every euro in these components is R&D.
- **Rationale:** Relevant research activity may be embedded in education, health, business incentives and financial instruments.
- **Implication:** Assess each investment/measure and, where necessary, each eligible activity or beneficiary expenditure line against the Frascati definition.

## D011 — Version-aware CID comparison

- **Status:** Adopted.
- **Decision:** Use the original 2021 CID and annex as the starting point and the latest adopted 2026 CID and annex as the end point, while retaining intermediate adopted revisions for change tracking.
- **Rationale:** The annex has been replaced/amended multiple times; a simple comparison of two files may conceal when and why a measure changed.
- **Implication:** Build a measure crosswalk with stable IDs, version-specific codes, descriptions, envelopes, milestones, targets and status. Do not assume measure codes or descriptions remain unchanged.

## D012 — Italia Domani as implementation and project-level source

- **Status:** Adopted.
- **Decision:** Use Italia Domani, including its open-data catalogue, calls/notices and project/financial monitoring information, to complement CID and legal sources.
- **Rationale:** CID defines the approved plan, while implementation data and calls provide information on beneficiaries, procedures, projects and actual progress.
- **Implication:** Record dataset version, extraction date, project/measure identifiers and coverage limitations; do not treat portal data as a substitute for primary legal or accounting evidence.

## D013 — Preserve cash, ESA accrual and R&D performance timing separately

- **Status:** Adopted.
- **Decision:** Record appropriations, commitments, cash payments, ESA accrual recognition where relevant, beneficiary eligible expenditure and the year of R&D performance as distinct time dimensions.
- **Rationale:** ESA 2010 accrual accounting supports government fiscal statistics, but it does not provide a universal conversion of cash disbursements into the year in which firms, universities or hospitals perform R&D.
- **Implication:** The macroeconomic R&D shock is assigned to the year of R&D performance where observable. Apply transaction-specific ESA rules for fiscal reconciliation, particularly for tax credits, grants and financial instruments. Never use a mechanical cash-to-accrual multiplier.
