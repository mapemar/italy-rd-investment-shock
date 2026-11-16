# Italy R&D Investment Shock

**From PNRR policy measures to an evidence-based estimate of incremental R&D expenditure.**

## Objective

This project develops a reproducible framework to translate Italian public policy interventions—starting with the National Recovery and Resilience Plan (PNRR)—into an annual estimate of additional research and development (R&D) expenditure.

The intended final output is a modular time series that can be mapped to an externally supplied macroeconomic R&D model.

The project distinguishes four policy channels:

1. **Direct public R&D expenditure** — universities, public research institutions, research infrastructure and research programmes.
2. **Business R&D incentives** — grants and tax incentives that may induce private R&D expenditure.
3. **Venture capital and financial instruments** — public and private capital supporting firms, of which only the demonstrably R&D-related component can enter the R&D shock.
4. **R&D ecosystem and enabling measures** — technology transfer, innovation ecosystems, competence centres, doctoral programmes and other enabling interventions.

## Core principle

**A policy allocation is not automatically additional R&D expenditure.**

The analysis must distinguish policy commitments, budget appropriations, commitments, disbursements, beneficiary expenditure and measured R&D activity. Additionality must be estimated against an explicit counterfactual, and uncertainty must be reported.

## Research window and chronology

The observation window is 2018–2030: 2018–2019 establish the pre-RRF baseline, 2020–2026 cover the RRF implementation window (subject to the measure-specific 1 February 2020 eligibility test), and 2027–2030 capture persistence and spillovers. Policy origin, legal basis, first implementation, PNRR inclusion and RRF eligibility are recorded separately. See [policy chronology and RRF eligibility](docs/policy_chronology_and_rrf_eligibility.md) and the [measure timeline register](data/processed/pnrr_measure_timeline.csv).

## Scope

- Geography: Italy.
- Historical statistical coverage: target 2015–2024, subject to source availability and methodological consistency.
- Constant-price reference year: 2019 (nominal series will also be retained).
- Policy focus: PNRR 2021 and subsequent revisions, including national co-financing directly associated with PNRR measures.
- Optional extension: other EU programmes, initially Cohesion Policy and the European Innovation Council (EIC), controlled through an explicit inclusion setting.
- Exclusion: national measures outside the PNRR are outside the default scope.
- Projection / shock horizon: target 2025–2030, with observed and estimated values clearly separated.
- Statistical framework: Eurostat and OECD, with Frascati Manual definitions as the reference for R&D classification.

## Repository map

| Path | Purpose |
|---|---|
| `docs/` | Research design, methodology, data dictionary and decision log |
| `config/` | Reproducible settings and source catalogue |
| `data/raw/` | Immutable source files, where licensing and size permit |
| `data/intermediate/` | Extracted and harmonised intermediate data |
| `data/processed/` | Validated analytical datasets |
| `documents/` | Document inventory and locally stored source documents, where appropriate |
| `src/` | Reusable Python modules and pipelines |
| `notebooks/` | Exploratory and analytical notebooks |
| `outputs/` | Generated tables, charts and reports |
| `tests/` | Automated tests and data-quality checks |

## Workflow

1. Establish the analytical framework and data model.
2. Inventory primary policy, legislative, budgetary and statistical sources.
3. Map PNRR measures to legislation, budget lines and implementing instruments.
4. Reconstruct the annual financial profile of each intervention.
5. Build and validate the official R&D statistical baseline.
6. Estimate the R&D-relevant and additional components using transparent assumptions.
7. Produce separate annual series for additional domestic R&D performed in Italy and the publicly financed component, with no double counting.
8. Produce scenarios and an annual shock dataset.
9. Map the resulting variables to the macroeconomic model once its specification is available.

## Evidence and traceability

Every material amount or legal claim should carry a source reference. Where feasible, record document title, issuing institution, date, URL, page, article/paragraph, quoted evidence, extraction date and the status of human validation.

Never fill gaps with invented values. Distinguish observed data, official allocations, estimates, forecasts and assumptions.

## Getting started

Read these files first:

- [Research methodology](docs/methodology.md)
- [Research framework](docs/research_framework.md)
- [Initial PNRR R&D measure screening](docs/policy_measure_screening.md)
- [CID version history and measure crosswalk](docs/cid_comparison.md)
- [Raw CID measure history](data/raw/cid_measure_history.csv)
- [Processed PNRR R&D measure inventory](data/processed/pnrr_rd_measure_inventory.csv)
- [Data dictionary](docs/data_dictionary.md)
- [Decision log](docs/decisions_log.md)
- [Source catalogue](config/sources.yaml)
- [Agent instructions](AGENTS.md)

## Reproducibility

Code should be modular, tested and deterministic where possible. Raw data should not be silently overwritten. Generated outputs should record input versions, parameters and execution date. Do not commit credentials, tokens, personal data or restricted institutional material.

## Project overview and dashboard

- [Interactive Research Dashboard](dashboard/index.html) — project status, workstream overview, selected PNRR economy charts, Treasury return profile, measure table and local CSV explorer.
- [Project status and next actions](docs/project_status.md) — management summary of completed work, evidence milestones, analytical gaps and priorities.

## Status

**Research architecture and substantial policy screening completed; budget reconstruction and statistical baseline in progress. No annual estimate of additional R&D expenditure has yet been produced.**


## 2026 Budget Law and PNRR economies

- [2026 Budget Law and PNRR economy reconciliation](docs/pnrr_2026_budget_reconciliation.md) — €7.102bn Treasury return, ministry-level and measure-level PNRR economies, and the double-counting implications.
- [Ministry-level economies, February 2026](data/processed/pnrr_ministry_economies_feb2026.csv) — €1.588bn by administration; measure attribution not disclosed in the annex.
- [Measure-level economies, September 2026](data/processed/pnrr_measure_economies_sep2026.csv) — ReGiS budgets and economies for eight R&D-relevant measures.

## Budget and execution reconciliation

- [Budget and PNRR execution reconciliation](docs/budget_execution_reconciliation.md) — State-budget chapter datasets, Treasury-account flows, ReGiS reporting and the GBARD bridge.
- [PNRR Treasury-flow snapshots](data/processed/pnrr_treasury_flow_snapshots.csv) — sourced cumulative snapshots; not annual expenditure estimates.
- [OpenBDAP budget dataset register](data/processed/openbdap_budget_dataset_register.csv) — identified RGS chapter-level and historical datasets.

## Industrial project-level register

- [Industrial R&D project register](data/processed/industrial_rd_project_register.csv) — 24 IPCEI participant/CUP records plus implementation records for space, strategic supply chains, net-zero, technology transfer and PoC.
- [Expanded policy measure screening](docs/policy_measure_screening.md) — source-backed eligibility/exclusion decisions and project-level data priorities.


## Venture capital and institutional-investor reform

- [DTF and GTF fund-level evidence register](data/processed/venture_capital_funds.csv) — direct/indirect channels, envelope status, leverage and R&D evidence gaps.
- [Venture capital and start-up finance methodology](docs/venture_capital_and_startup_finance.md) — treatment of DTF/GTF, portfolio-company R&D and Law 193/2024 Article 33.


## Historical national R&D policy baseline

- [Historical PRIN funding, 2007–2022](data/processed/prin_historical_funding_2007_2022.csv) — MUR-reported annual funding allocations.
- [Historical R&D policy register](data/processed/historical_rd_policy_register.csv) — PRIN, FCS/FIT, innovation agreements, R&D tax credits, DTF/GTF and institutional VC reform.

- [R&D tax credit evidence 2020–2022](data/processed/rd_tax_credit_evidence_2020_2022.csv) — accrued R&D&I credits and Istat tax-relief indicators, with scope caveats.

- [OECD R&D tax-credit impact evidence](data/processed/rd_tax_credit_impact_evidence.csv) — Italy-specific causal estimates for 2007–09 and 2015–19, plus 2023 policy-mix statistic; not directly transferable to 2020–22.
