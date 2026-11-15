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

## Scope

- Geography: Italy.
- Historical statistical baseline: target 2015–2024, subject to source availability and methodological consistency.
- Policy focus: PNRR 2021, subsequent revisions including the 2026 revision, related national legislation and budget laws.
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
7. Produce scenarios and an annual shock dataset.
8. Map the resulting variables to the macroeconomic model once its specification is available.

## Evidence and traceability

Every material amount or legal claim should carry a source reference. Where feasible, record document title, issuing institution, date, URL, page, article/paragraph, quoted evidence, extraction date and the status of human validation.

Never fill gaps with invented values. Distinguish observed data, official allocations, estimates, forecasts and assumptions.

## Getting started

Read these files first:

- [Research methodology](docs/methodology.md)
- [Research framework](docs/research_framework.md)
- [Data dictionary](docs/data_dictionary.md)
- [Decision log](docs/decisions_log.md)
- [Source catalogue](config/sources.yaml)
- [Agent instructions](AGENTS.md)

## Reproducibility

Code should be modular, tested and deterministic where possible. Raw data should not be silently overwritten. Generated outputs should record input versions, parameters and execution date. Do not commit credentials, tokens, personal data or restricted institutional material.

## Status

**Stage 0 — Repository and research architecture.** No quantitative R&D shock estimate has yet been produced.
