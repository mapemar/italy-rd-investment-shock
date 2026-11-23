# Chat-workstream consolidation — 23 November 2026

## Purpose

This note reconciles the work recorded in the recent ChatGPT conversations and locally available working files with the existing GitHub repository. It is an addendum, not a replacement for the repository's methodology, research framework, decision log or existing project status.

## Repository-first correction

The canonical repository is `mapemar/italy-rd-investment-shock`. It already contains a substantial research architecture, PNRR measure inventory, Eurostat/ISTAT macro datasets, MIMIT and ReGiS execution evidence, budget/Treasury reconciliation work, a dashboard, a first quantitative diagnostic and a reusable skill.

The recent chat work must therefore be integrated as a supplementary workstream. It must not be treated as a new project architecture or as a replacement for existing repository data.

## Four distinct analytical layers

1. **Policy:** legal measure, objective, eligibility, beneficiaries, implementation period and funding perimeter.
2. **Fiscal:** appropriations, commitments, payments, ESA treatment, tax expenditure, equity/loans/guarantees and transfers.
3. **R&D performance:** beneficiary expenditure that meets the Frascati definition, assigned to the year of performance, location and performing sector.
4. **Causal/macro:** additional R&D relative to an explicit counterfactual and the resulting model input.

The stages are linked but are not interchangeable. An allocation, payment, fund commitment or cumulative execution snapshot is not automatically R&D performed; gross R&D is not automatically additional R&D.

## Workstream A — historical national fiscal measures census (2018–2025)

This workstream is separate from the default PNRR-only headline estimand defined in the repository methodology and research framework. It is intended as a complementary evidence-building census, not an automatic expansion of the PNRR shock.

### v18 — Extraction Round 10

The chat notes report 106 records in `RT_Extracted_Data` and selected legal/budget extraction for 2018–2025. Examples include researcher recruitment, R&D tax credits, venture-capital funds, FOE, FISA, and MUR research appropriations.

Important caveats and corrections recorded in the notes:
- The EUR 227.1m profile for 2021–2023 is a combined R&D, technological innovation and ecological innovation profile, not pure R&D.
- The FOE 2022 increase must distinguish EUR 90m capital expenditure, EUR 62.5m current expenditure and EUR 30.3m increased revenue.
- The extraction is incomplete across years and ministries; it is not a complete or certified national census.

### v19 — supplementary extraction

The chat notes report 71 measure/intervention records, 236 annual-profile records, 20 fiscal-balance records, 18 document sources and 6 exclusions/qualitative measures.

The notes identify additional work on the National Research Fund, Technology Transfer Fund, FOE/FISA, CREA, ISPRA, IPCEI, NATO Innovation Fund and Green New Deal.

v19 is explicitly supplementary and was not merged with v18. Reconciliation must use stable `Measure_ID` values and must distinguish authorisations, annual fiscal profiles, financial transactions, intermediary flows and actual beneficiary expenditure.

### Repository integration rule

Do not append v18/v19 records directly to the PNRR measure inventory or the existing `historical_rd_policy_register.csv`. First create a separate, versioned national-census staging dataset, reconcile identifiers and scopes, and document any crosswalk. Measures outside the PNRR perimeter must remain separately tagged and excluded from the headline PNRR-only result unless the perimeter is explicitly changed.

**Availability limitation:** the original v18 and v19 Excel workbooks were not present in the working directory during this consolidation. Only their chat-note text files were available. The notes are archived in this repository; the original workbooks still need to be retrieved from their original project attachments before record-level reconciliation. The opaque chat citation IDs and sandbox download links in the archived notes are conversation artefacts, not durable source citations.

## Workstream B — MUR cumulative PNRR quantification in v15

The recent review of the v15 workbook identified a preliminary MUR cumulative scenario calculation based on ANVUR-reported expenditure snapshots and provisional R&D eligibility coefficients:

| Scenario | Cumulative eligible R&D estimate |
|---|---:|
| Low | EUR 3,333.2m |
| Central | EUR 4,084.3m |
| High | EUR 5,776.6m |

The reported cumulative expenditure was EUR 5,776.6m against EUR 8,904.9m of allocations (about 64.9%).

These are cumulative, gross, scenario-based estimates. They are not annual flows, not a Frascati-validated national total, and not net additional R&D. The coefficients are modelling assumptions, not official MUR/ANVUR shares. The broad high scenario should not be presented as strict GERD.

**Scope control:** the EUR 1.5931bn PNR/PRIN amount is the aggregate M4C2 I1.01 measure in the v15 calculation. Do not add the separate PRIN 2022 PNRR pilot's EUR 419.49m award total without reconciling scope; that would risk double counting.

## Workstream C — PRIN 2022 PNRR project-level pilot

The separate pilot covers PRIN 2022 PNRR, DD 1409/2022, M4C2 Investment 1.1. It is distinct from the national PRIN 2022 call and the aggregate PNR/PRIN measure.

Award data in the pilot:
- 1,778 projects;
- EUR 419,493,888 total awards;
- EUR 506,112 difference from the EUR 420m envelope, still to reconcile.

The CNR-IAC case study covers five projects/local units. Its reported expenditure totals approximately EUR 370,216.21 against EUR 341,839 of local-unit allocations, an unreconciled difference of about EUR 28,377. The reporting periods are quadrimestral and cross calendar years; exact transaction dates were not available in the pilot evidence, so the amounts cannot be reliably allocated to calendar years.

The pilot is a methodological feasibility exercise, not a national execution ratio or an annual R&D estimate. The final v0.2 workbook includes the ANVUR reference sheet and supersedes the earlier pilot workbook for current use; the earlier v0.1 backlog workbook is retained as a historical version where available.

## Workstream D — quantification working paper

`RD_Quantification_Working_Paper_v0.1.xlsx` is a separate addendum with four sheets:
- `MUR_Cumulative`;
- `Scenario_Summary`;
- `Annual_Input_Gap`;
- `Extraction_Progress`.

It organises the preliminary MUR scenarios and the annual-data gaps. It does not replace the master v15 workbook or the repository's first quantitative shock diagnostic.

## Reconciliation with the repository's existing first quantitative diagnostic

The repository already contains `docs/first_quantitative_shock_estimate_nov2026.md` and `data/processed/first_shock_estimate.csv`. That work provides a descriptive GERD/GDP and sectoral trend diagnostic, a trend benchmark, evidence on DTF/GTF deliberations and implementation snapshots, and selected MUR/MIMIT cumulative execution evidence.

It explicitly does **not** provide a complete annual causal PNRR R&D shock. The new MUR cumulative scenario calculation is a separate calculation and must not overwrite or be conflated with the repository's existing diagnostic. In particular:
- cumulative snapshots are not annual flows;
- DTF/GTF deliberations, ReGiS spending, commitments and company-level cash deployment are different stages;
- the agreed DTF/GTF 100% coefficient belongs only to the separately labelled broad innovation proxy, not official GERD/BERD;
- the trend diagnostic is not a causal no-policy counterfactual.

## Current state after consolidation

- The repository's core PNRR architecture and existing analytical assets remain authoritative.
- The national 2018–2025 fiscal census is a distinct, not-yet-reconciled workstream.
- The MUR v15 low/central/high cumulative estimates are preliminary and not annual.
- The PRIN 2022 PNRR pilot is complete as a feasibility test, with unresolved financial and timing reconciliations.
- The quantification workbook is an addendum.
- No complete annual additional domestic R&D shock has been established.

## Next actions

1. Retrieve original v18 and v19 workbooks; archive immutable copies and record checksums.
2. Create a separate historical-census staging schema and reconcile v18/v19 using `Measure_ID`.
3. Keep national non-PNRR measures outside the PNRR headline perimeter.
4. Reconcile the v15 MUR aggregate PNR/PRIN scope against the PRIN 2022 PNRR pilot before any aggregation.
5. Continue the repository's existing measure-year and budget/execution work; do not treat cumulative observations as annual performance.
6. Obtain beneficiary-level project costs and transaction/performance dates for the PRIN pilot where possible.
7. Estimate Frascati eligibility, domestic performance and additionality as separate parameters.
8. Produce annual gross R&D and net additional R&D only after the evidence and counterfactual gates are met.

## Version hierarchy

| Artefact | Role | Treatment |
|---|---|---|
| Repository methodology, research framework and decision log | Canonical project rules | Authoritative |
| Repository first shock diagnostic and processed datasets | Existing project evidence | Preserve; do not replace |
| Master workbook v15 | Existing working analytical workbook | Preserve as its own vintage |
| National census v18 | Historical fiscal extraction | Separate staging vintage; original workbook not currently available here |
| National census v19 | Supplementary historical fiscal extraction | Separate staging vintage; original workbook not currently available here |
| PRIN pilot v0.2 | Final pilot workbook | Current pilot artefact |
| Quantification working paper v0.1 | MUR cumulative scenarios and annual data gaps | Supplementary addendum |
| Chat notes | Work history and extraction summaries | Archive only; not primary evidence |

**Controlling principle:** preserve the existing repository's approved PNRR perimeter and decisions. Keep raw/extracted/validated data separate, retain original observations, and never convert allocations or cumulative snapshots into annual additional R&D without evidence.
