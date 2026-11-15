# Source code

Python modules should be added here as the analytical workflow is specified.

Planned modules:
- `document_reader/`: PDF/text ingestion and evidence extraction.
- `amendment_reader/`: version comparison and legal amendment tracking.
- `policy_classifier/`: measure classification and R&D eligibility.
- `budget_reconstruction/`: annual budget and expenditure reconciliation.
- `rd_statistics/`: Eurostat/OECD retrieval and harmonisation.
- `additionality/`: parameter management and counterfactual estimation.
- `shock_estimation/`: annual scenario calculations and model exports.

Keep each module independently testable. Do not create speculative calculations before the input schema and evidence requirements are agreed.
