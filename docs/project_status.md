# Project status and next actions

**Project:** Italy R&D Investment Shock  
**Status date:** 15 November 2026  
**Purpose:** Single-page management summary. For live charts and CSV exploration, open the [Research Dashboard](../dashboard/index.html).

## Executive assessment

The project has moved beyond initial architecture and policy screening. It has a documented estimand and methodology, a substantial PNRR measure inventory, selected industrial project records, and a first set of budget/execution reconciliations.

It has **not yet produced an annual estimate of additional R&D expenditure**. The central remaining challenge is to connect policy measures to actual R&D performed in Italy, establish the counterfactual, and allocate expenditure to the year of performance.

## Workstream status

| Workstream | Status | Evidence / deliverable | Main remaining task |
|---|---|---|---|
| Research architecture | Established | Methodology, research framework, data dictionary and decision log | Maintain consistency |
| PNRR policy inventory | Substantial progress | MUR/MIMIT screening, CID history, industrial project register | Close gaps and validate scope |
| Legal and budget reconstruction | In progress | Treasury snapshots, OpenBDAP register, 2026 economy reconciliation | Build annual chapter-level panel and reconcile accounting layers |
| R&D statistical baseline | To consolidate | Eurostat/OECD/ISTAT source identification | Harmonise GERD/BERD/GOVERD/HERD and GBARD, 2015–2024 |
| R&D eligibility | Partial | Frascati screening and measure-level eligibility notes | Identify eligible R&D components |
| Additionality and counterfactual | Not yet estimated | Methodological framework | Gather evaluation evidence and define instrument-specific parameters |
| Annual shock and scenarios | Not yet produced | Output concepts and price base defined | Produce nominal and 2019-price annual series |
| Macro-model integration | Pending | Modular output concept | Obtain model equations, units and timing conventions |

Statuses are qualitative management judgements, not measured completion percentages.

## What is already established

- The primary estimand is **additional R&D expenditure performed in Italy**, attributable to PNRR measures and directly associated national co-financing, relative to a stated counterfactual.
- The public-financing view is a subset/view of domestic R&D, not an additional series to sum to it.
- R&D eligibility follows the Frascati Manual; generic digitalisation, machinery, infrastructure construction and ordinary capital formation do not automatically qualify.
- Appropriations, commitments, cash payments, beneficiary expenditure, ESA recording and R&D performance are separate accounting/timing concepts.
- Allocations and public support are not themselves evidence of additional R&D.
- The default policy perimeter excludes unrelated national measures. Cohesion Policy and EIC remain optional, separately identifiable extensions.

## Evidence milestones already reached

### Policy and programme mapping
- MUR M4C2 headline portfolio reconstructed at approximately **EUR 8.55bn**; this is an allocation envelope, not realised GERD.
- M4C2 I1.1 PRIN: EUR 1.8bn, with an explicit additionality issue for projects-in-being.
- Young researchers, extended partnerships, National Centres, innovation ecosystems, research/innovation infrastructures and doctoral programmes screened.
- MIMIT measures screened include IPCEIs, hydrogen R&D, innovation agreements, space, strategic supply chains, Net Zero, technology transfer, PoC and tax incentives.
- Industrial project register includes IPCEI participant/CUP records and selected industrial workstreams. A project/fund allocation is not automatically R&D performed.

### Budget and execution
- 2026 Budget Law Treasury returns: EUR 7.102bn over 2026–2028. This is a financing/budget operation, not negative R&D expenditure in those years.
- February 2026 central-administration economy cohort: EUR 1,587.510m. The published annex gives ministry totals, not individual measure attribution.
- September 2026 measure-level economy cohort: EUR 1,698m overall. The R&D-relevant extracted subset contains six MUR measures (EUR 8,040.9m budget; EUR 180.2m economies) and two hydrogen R&D measures (EUR 300m budget; EUR 21.9m economies).
- The cohorts must remain separately identified until their legal and accounting coverage is fully reconciled. Do not sum them mechanically.
- OpenBDAP catalogue was under extraordinary maintenance on 15 November 2026; the annual dataset register identifies sources but does not mean chapter-level data have been downloaded.

## Main analytical gaps

1. Annual State-budget chapter appropriations and final accounts, linked to PNRR measures and funding sources.
2. Consistent annual statistical baseline (GERD and sectors of performance; funding sources; GBARD as a distinct budget indicator).
3. Measure-level actual expenditure and the fraction that meets the Frascati R&D definition.
4. Additionality evidence and counterfactuals, especially for tax credits, projects-in-being, financial instruments and mixed industrial schemes.
5. Performance-year profiles and conversion to 2019 constant prices.
6. Model-specific variable mapping.

## Prioritised next actions

### Priority 1 — Build the analytical backbone
- Create a master measure table linking CID, national legal basis, budget chapters, implementing body and processed datasets.
- Consolidate a versioned annual financial profile: initial/revised allocations, commitments, payments, final beneficiary expenditure and identified economies. Keep accounting layers separate.
- Build the 2015–2024 statistical baseline from Eurostat/OECD and ISTAT GBARD, preserving dataset codes, units, metadata, vintages and breaks.

### Priority 2 — Move from financial support to R&D
- For each high-priority measure, identify eligible R&D activity, performing sector and domestic location.
- Retrieve beneficiary/project-level data only where it materially identifies eligible R&D cost, year of performance or additionality.
- Prioritise direct research funding and explicit R&D grants before mixed industrial instruments and venture-capital channels.
- Review evaluation literature and administrative evidence to define additionality ranges by instrument. Do not use a single coefficient for all measures.

### Priority 3 — Produce a first transparent estimate
- Build a pilot calculation for a small number of high-evidence measures.
- Show every step: eligible expenditure, R&D share, performance-year allocation, additionality and price conversion.
- Produce conservative/central/high scenarios only where parameter ranges are supported.
- Validate against official GERD/BERD/HERD/GOVERD trends and GBARD, without forcing accounting equality.

### Priority 4 — Prepare the macro interface
- Obtain the receiving model's equations, variable names, units, sectoral split and timing conventions.
- Export a modular annual shock dataset with source lineage and uncertainty.

## Decision rules / red lines

- Never present a PNRR allocation, fund commitment, Treasury transfer or economy as realised R&D expenditure.
- Never treat a Treasury return as negative GERD in the return year.
- Do not assign ministry-level economies to MUR/MIMIT measures without measure-level evidence.
- Do not infer that zero reported economies means full execution or full R&D performance.
- Do not count national expenditure relabelled as PNRR as newly additional at the date of relabelling.
- Do not add public-financed R&D to total domestic R&D.
- Keep unknowns explicit; no invented values or false precision.

## Key documents

- [Research framework](research_framework.md)
- [Methodology](methodology.md)
- [Policy measure screening](policy_measure_screening.md)
- [Budget and execution reconciliation](budget_execution_reconciliation.md)
- [2026 PNRR budget reconciliation](pnrr_2026_budget_reconciliation.md)
- [Data dictionary](data_dictionary.md)
- [Decision log](decisions_log.md)
- [Source catalogue](../config/sources.yaml)


## New quantitative work — M4C2 aggregate pilot (20 November 2026)

A preliminary aggregate model has been added on branch `m4c2-aggregate-quantification-v0-1`:

- Latest MUR Si.Ge.Co. v5.0 allocation perimeter: EUR 8,284.9m across seven research-oriented M4C2 investments.
- ANVUR cumulative execution base: EUR 5,459.8m (mostly October 2025; I3.1 updated to February 2026).
- Modelled R&D performed, including a separate provisional PRIN residual-financing line: EUR 3,156.2m low / EUR 3,763.7m central / EUR 4,354.7m high.
- Modelled additional R&D: EUR 575.4m low / EUR 1,374.5m central / EUR 2,243.4m high.
- Central annual profile (current prices): EUR 10.2m in 2021; EUR 36.8m in 2022; EUR 170.5m in 2023; EUR 422.3m in 2024; EUR 498.7m in 2025; EUR 236.1m in 2026.

The results are preliminary model outputs, not official R&D expenditure or causal estimates. The annual profile is assumed, the performing-sector and R&D-type splits are not yet estimated, private co-financing is not quantified, and final project-level rendiconti are still required. The M4C1 doctoral measures remain a separate extension. See [M4C2 aggregate quantification](m4c2_aggregate_rd_quantification_v0_1.md).


## New extension — doctoral programmes and co-financing (20 November 2026)

A versioned v0.2 extension has been added on branch `m4c2-aggregate-quantification-v0-1`:

- Adds M4C1 I4.1 doctoral programmes (EUR 504m allocation; EUR 316.8m reported expenditure) and the M4C1 I3.4 doctoral sub-line (EUR 34.5m allocation; doctoral-only expenditure estimated pro rata pending disaggregation).
- Reconstructs EUR 240.3m of approved project-cost gaps across 14 extended partnerships, 5 National Centres and 11 innovation ecosystems.
- Derives a minimum EUR 225.9m private co-financing requirement for ITEC from the 49% public funding cap.
- Reconstructs enterprise co-financing for I3.3 PhDs from DM352/2022, DM117/2023 and DM630/2024; central estimate EUR 127.4m, with the 2024 top-up explicitly assumed.
- Separately identifies EUR 31.7–42.4m university/host top-ups for PA and cultural-heritage doctoral scholarships in the DM118/2023 cohort; these are not classified as private.
- Central private/likely-private co-financing proxy: EUR 593.6m; strict private-only floor: EUR 328.4m.
- Combined central additional-R&D model output: EUR 1,575.3m (low EUR 629.7m; high EUR 2,658.5m).

These are preliminary model outputs, not official R&D expenditure or causal estimates. The private co-financing amount for I1.3/I1.4/I1.5 remains a proxy pending partner-level source classification; ITEC is a minimum implied by the call cap; DM630/2024 company top-ups are assumed centrally. M4C1 I3.4 doctoral-only execution is estimated pro rata. The M4C1 I4.1 and M4C2 I3.3 award-count discrepancies and the EUR 340.4m/360m I3.3 allocation vintage difference are documented in the v0.2 report.
