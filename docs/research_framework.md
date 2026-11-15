# Research framework and workplan

## Research question

How much additional R&D expenditure in Italy has been generated, or is expected to be generated, by the PNRR and associated national policy interventions relative to a defined counterfactual?

## Workstreams

### WS1 — PNRR and policy inventory
- Original PNRR and 2021 Council Implementing Decision and annexes.
- Subsequent PNRR revisions, including the 2026 CID and annexes.
- Measure identifiers, milestones, targets, funding envelopes and implementation periods.
- Relevant Commission, Council and Italian Government implementation documents.

### WS2 — Legal and budgetary reconstruction
- Map each policy measure to its legal basis and implementing acts.
- Review annual Budget Laws and relevant budget annexes.
- Track initial and revised appropriations, reallocations, national co-financing, commitments and payments.
- Distinguish PNRR resources from national resources and avoid double counting.

### WS3 — Statistical baseline
- Eurostat and OECD historical R&D data.
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

### WS6 — Macroeconomic model interface
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

1. Confirm whether the repository is intended to cover only PNRR measures or also complementary national measures and non-PNRR policies introduced during 2021–2026.
2. Collect the original and revised CID documents and build a version-aware measure crosswalk.
3. Inventory the existing Eurostat workbook supplied by the project owner before downloading duplicate data.
4. Build a source register before bulk document extraction.
5. Agree the annual accounting basis and price basis before aggregation.
