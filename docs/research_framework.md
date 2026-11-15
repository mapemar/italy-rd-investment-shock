# Research framework and workplan

## Research question

How much additional R&D expenditure in Italy has been generated, or is expected to be generated, by PNRR measures and their directly associated national co-financing, relative to a defined counterfactual? An optional, separately identifiable extension may include other EU programmes such as Cohesion Policy and the European Innovation Council (EIC).

## Workstreams

### WS1 — PNRR and policy inventory
- Original PNRR and 2021 Council Implementing Decision and annexes.
- Subsequent PNRR revisions, including the 2026 CID and annexes.
- Measure identifiers, milestones, targets, funding envelopes and implementation periods.
- Relevant Commission, Council and Italian Government implementation documents.

### WS2 — Legal and budgetary reconstruction
- Build a harmonised 2020–2026 State-budget panel from RGS OpenBDAP Budget Laws, notes of variation, approved adjustments and Rendiconti at chapter level.
- Reconstruct PNRR Treasury-account flows (accounts 25091/25092) and Group 286 special-account transfers separately from ordinary budget chapters.
- Reconcile transfers to implementing bodies with ReGiS expenditure declared and approved; eliminate internal transfers and transfers returned to the State budget.
- Keep State-budget accounting, Treasury cash movements and ESA 2010 general-government transactions distinct.
- Use ISTAT GBARD as an aggregate cross-check of public R&D budget allocations, not as realised GERD or a PNRR-only measure.
- Map each policy measure to its legal basis and implementing acts.
- Review annual Budget Laws and relevant budget annexes.
- Track initial and revised appropriations, reallocations, national co-financing, commitments and payments.
- Include national co-financing only where directly associated with an in-scope PNRR measure.
- Exclude unrelated national measures outside the PNRR.
- Avoid double counting between EU and national financing of the same intervention.

### WS3 — Statistical baseline
- Eurostat and OECD historical R&D data, targeting annual coverage from 2015 to 2024.
- Retain nominal values and derive constant-price values with 2019 as the reference year.
- GERD, BERD, GOVERD, HERD, funding sources and type of R&D.
- GBARD and relevant budget statistics.
- Metadata, revisions, units, prices, coverage and breaks.

### WS4 — Measure classification
Classify each intervention by policy channel, activity eligibility, performing sector, funding source, R&D type, directness and evidence quality.

### WS5 — Additionality and shock estimation
- Establish counterfactual for each instrument.
- Estimate utilisation, R&D relevance, additionality and timing separately.
- Develop conservative, central and high-impact scenarios.
- Run sensitivity and aggregation checks.

### WS6 — Programme perimeter and optional EU extension
- Default: PNRR measures plus directly associated national co-financing.
- Optional configuration switch to include Cohesion Policy programmes and EIC support.
- Keep programme-level outputs separately identifiable and provide PNRR-only and expanded-EU-programme totals.
- Do not include unrelated national measures outside the PNRR.

### WS7 — Macroeconomic model interface
- Obtain the model equations, variable definitions, units and timing conventions.
- Map the modular shock series to the required inputs.
- Document any mismatch between the evidence dataset and model requirements.

## Staged execution

| Stage | Deliverable | Gate |
|---|---|---|
| 0. Architecture | Methodology, schema, source catalogue, decision log | Review definitions and scope |
| 1. Source inventory | Document register and statistical source register | Confirm coverage |
| 2. Policy mapping | Measure-level PNRR and policy inventory | Validate measure list |
| 3. Legal/budget mapping | Legal chain and annual financial profiles | Reconcile funding sources |
| 4. Statistical baseline | Harmonised Eurostat/OECD dataset | Validate metadata and breaks |
| 5. Classification | R&D eligibility assessment by measure | Review Frascati boundary |
| 6. Estimation | Additionality assumptions and scenario outputs | Approve assumptions |
| 7. Model mapping | Model-ready shock inputs | Validate against model specification |

## Priority source families

1. Council Implementing Decisions and annexes for Italy's RRP.
2. European Commission RRP assessment, monitoring and payment documentation.
3. Official Italian PNRR portals and MEF/RGS monitoring information.
4. Italian Budget Laws, budget statements and official financial annexes.
5. Implementing legislation and ministerial decrees.
6. MIMIT, MUR and other implementing bodies' reports and administrative data.
7. CDP, CDP Venture Capital and EIB documentation for financial instruments.
8. Eurostat and OECD statistical datasets and metadata.
9. Evaluation studies and academic evidence on additionality of R&D grants, tax credits and public venture capital.

## Initial tasks

1. Download the original 2021 CID and annex and the latest 2026 adopted CID and annex from the Commission Italy country page; preserve intermediate revisions for change tracking.
2. Build a version-aware crosswalk of measure codes, descriptions, milestones, targets and financial envelopes between the 2021 and 2026 annexes.
3. Screen M4C1, M4C2, potentially R&D-relevant M6 measures, and M1C2 measures including the R&D tax credit and the Digital/Green Transition Funds.
4. Use Italia Domani open data, calls and notices, project records and financial-monitoring datasets to trace implementation and beneficiaries.
5. For every selected measure, reconstruct the legal and financial chain through all relevant annual Budget Laws and implementing acts.
6. Preserve cash payments, commitments, ESA accrual timing and beneficiary R&D performance as distinct concepts; do not apply a mechanical cash-to-accrual conversion.
7. Inventory the existing Eurostat workbook before downloading duplicate data.



### WS8 — Venture capital and start-up ecosystem
- Add the Digital Transition Fund (M4C2 I3.2) and Green Transition Fund (M2C2 I5.4), distinguishing direct investments from indirect fund commitments.
- Track fund commitments, capital calls, portfolio-company investment, private co-investment and leverage separately; avoid double counting fund-level and company-level flows.
- Add Law 193/2024 Article 33 as an institutional-capital mobilisation reform, not a direct R&D expenditure measure.
- Link portfolio companies to R&D actually performed in Italy and classify eligible costs using Frascati principles. Until such evidence is available, report VC deployment as innovation finance and leave its R&D contribution unquantified.
