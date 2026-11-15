# Data dictionary

This document defines the initial logical data model. Physical schemas may be refined as source files are inspected. Do not silently rename or repurpose fields; record schema changes in the decision log.

## 1. Core entities and identifiers

| Entity | Primary key | Description |
|---|---|---|
| Policy measure | `measure_id` | Stable identifier for a policy intervention |
| Document | `document_id` | Stable identifier for a source document/version |
| Legal act | `legal_act_id` | Stable identifier for legislation or implementing act |
| Budget record | `budget_record_id` | Measure- and year-specific financial observation |
| Statistical observation | `observation_id` | Official R&D statistical observation |
| Parameter | `parameter_id` | Estimation coefficient or assumption |
| Shock observation | `shock_id` | Estimated additional R&D value by year and dimension |

## 2. Policy measure table — proposed fields

| Field | Type | Meaning |
|---|---|---|
| measure_id | string | Stable internal ID |
| measure_name | string | Official/common measure name |
| pnrr_measure_code | string, nullable | CID/PNRR identifier |
| programme | category | PNRR / Cohesion Policy / EIC / other explicitly approved EU programme |
| funding_origin | category | EU / national co-financing / mixed |
| in_core_scope | boolean | Whether included in the PNRR-plus-associated-co-financing core |
| optional_programme_enabled | boolean | Whether an optional EU programme is enabled for the run |
| component | string, nullable | PNRR component |
| subcomponent | string, nullable | PNRR subcomponent |
| channel | category | direct_public_rd / business_rd_incentive / venture_finance / enabling |
| implementing_body | string, nullable | Responsible administration |
| start_year | integer, nullable | Expected/actual start |
| end_year | integer, nullable | Expected/actual end |
| r_and_d_eligibility | category | confirmed / partial / indirect / not_established |
| performing_sector | category, nullable | Business / Government / Higher education / PNP |
| funding_source | category, nullable | Government / Business / Higher education / PNP / Rest of world / mixed |
| evidence_status | category | extracted / source_checked / validated / disputed |

## 3. Document register — proposed fields

- `document_id`
- `document_title`
- `institution`
- `document_type`
- `document_date`
- `version_or_status`
- `url`
- `local_path` (optional)
- `language`
- `relevant_pages`
- `retrieved_at`
- `checksum_sha256` (where locally stored)
- `access_or_licence_notes`

## 4. Legal evidence table — proposed fields

- `legal_act_id`
- `document_id`
- `act_type`
- `act_number`
- `act_date`
- `article`
- `paragraph`
- `annex_or_table`
- `effective_date`
- `amends_or_implements`
- `measure_id`
- `evidence_excerpt`
- `page_number`
- `source_url`
- `validation_status`

## 5. Budget and expenditure table — proposed fields

All monetary observations must include currency, unit, price basis, reference year and accounting stage.

- `budget_record_id`
- `measure_id`
- `legal_act_id` (nullable)
- `document_id`
- `financial_year`
- `amount`
- `currency`
- `unit` (EUR / thousand EUR / million EUR)
- `price_basis` (current / constant)
- `price_base_year` (nullable)
- `financial_stage` (envelope / appropriation / commitment / payment / beneficiary_expenditure / tax_expenditure)
- `funding_source`
- `funding_programme`
- `national_or_eu`
- `funding_origin_detail` (PNRR EU contribution / directly associated national co-financing / Cohesion Policy / EIC / other)
- `programme`
- `in_core_scope`
- `gross_or_net`
- `reallocation_or_revision_flag`
- `source_reference`
- `evidence_status`

## 6. Statistical observation table — proposed fields

- `observation_id`
- `geo`
- `year`
- `dataset_code`
- `indicator_code`
- `performing_sector`
- `funding_source`
- `rd_type`
- `unit`
- `price_basis`
- `value`
- `currency_or_ppp`
- `constant_price_base_year` (2019 for the project's constant-price series)
- `metadata_url`
- `extraction_date`
- `revision_or_break_note`

## 7. Additionality parameter table — proposed fields

- `parameter_id`
- `measure_id` (nullable if channel-level)
- `parameter_name` (utilisation / rd_relevance / additionality / leverage / timing)
- `scenario` (low / central / high, with interpretation documented)
- `value`
- `unit`
- `lower_bound`
- `upper_bound`
- `method`
- `evidence_document_id`
- `rationale`
- `uncertainty_rating`
- `review_status`

## 8. Shock output table — proposed fields

- `shock_id`
- `year`
- `scenario`
- `channel`
- `performing_sector`
- `funding_source`
- `rd_type`
- `amount_eur_mn_current`
- `amount_eur_mn_constant_2019`
- `constant_price_base_year` (2019)
- `output_concept` (additional_domestic_rd_performed / publicly_financed_rd_performed)
- `programme_scope` (pnrr_core / expanded_eu_programmes)
- `share_of_gdp`
- `observed_or_estimated`
- `method_version`
- `run_id`

## 9. Controlled vocabularies

Use controlled values and document extensions. For output concepts, publicly financed R&D is a subset/view of domestic R&D performed and must not be added to it. Do not mix sector of performance and funding source in one field. Null means unknown/not available; zero means an observed or estimated zero and must not be used as a missing-value substitute.


## 10. Candidate screening and correction factors

The expanded policy inventory includes broad candidates and boundary/control measures. Inclusion in the inventory is not equivalent to inclusion in the quantified R&D shock.

The inventory schema includes the following screening fields:
- `rd_eligibility_share_factor`: share of the relevant beneficiary expenditure that meets the Frascati definition and is performed in Italy (0–1; estimate at project/activity level where possible).
- `additionality_share_factor`: share of eligible R&D that is additional relative to the specified counterfactual (0–1).
- `factor_status`: evidence status, estimation method and validation note.

A blank factor is **not estimated**, not zero. Do not fill factors with generic coefficients across heterogeneous measures. Store low/central/high estimates, evidence, method and uncertainty in the separate Additionality parameter table. For mixed instruments, estimate the R&D eligibility share from project work packages and cost categories; estimate additionality separately. Where relevant, add a domestic-performance share and timing profile rather than embedding these concepts in a single haircut.


## 11. Industrial R&D project register

File: `data/processed/industrial_rd_project_register.csv`.

One row represents either a beneficiary-level IPCEI participant or an aggregate project/workstream record where public sources do not disclose individual beneficiaries. Fields:
- `record_type`: beneficiary, subinvestment, project_aggregate or programme_aggregate.
- `pnrr_measure`, `submeasure_or_ipcei`: current measure and workstream identifier.
- `beneficiary_or_project`, `CUP`: legal entity/project name and unique project code where disclosed.
- `status_or_evidence_as_of`: status/vintage of public evidence.
- `amount_eur`, `amount_type`: amount and its meaning (allocation, activated resources, concession, project value, sub-line budget). Never aggregate different amount types.
- `R&D_relevance`: qualitative eligibility classification, not a numerical factor.
- `additionality_and_accounting_note`: counterfactual, double-counting and accounting caveats.
- `source_url`, `source_reference`: provenance.

The current register has 36 records: 24 IPCEI participant/CUP records plus 12 workstream/aggregate records, including a Q4 2024 aggregate concession record. A participant or selected project is not proof of final concession, payment, eligible R&D or additionality.


## Budget and execution datasets

### `pnrr_treasury_flow_snapshots.csv`

Cumulative public-source snapshots of PNRR Treasury movements and implementation transfers. These are not annual time series and must not be summed across snapshot dates.

- `snapshot_date`: date to which the cumulative amount refers.
- `reference_period`: period covered by the cumulative snapshot.
- `flow_level`: Treasury accounts, implementation transfers, implementation reporting or PNC.
- `indicator`: reported financial-flow concept.
- `amount_eur_bn`: amount in EUR billions.
- `source_url`, `source_note`: traceability and interpretation.
- `status`: reported or approximate reported value.

### `openbdap_budget_dataset_register.csv`

Register of identified RGS OpenBDAP datasets for annual budget-law and final-account expenditure by chapter, plus a historical aggregate series. Dataset IDs and URLs are source identifiers; the annual panel must be extracted and harmonised before analysis.

### Reconciliation principles

- Do not sum Budget Law appropriations, Treasury transfers, ReGiS reported expenditure and ESA expenditure.
- Competence, cash and residuals are separate fields.
- Internal transfers and transfers returned to the State budget are not final expenditure.
- A budget chapter is not R&D solely because its title contains research/innovation terminology.
- GBARD is a budget-allocation measure, not realised GERD.


## PNRR economy datasets

### `pnrr_ministry_economies_feb2026.csv`

Ministry-level economies identified under Article 30(1) of DL 19/2026, based on the annex reported in the parliamentary dossier. The amounts total EUR 1,587.510m. The source does not allocate these amounts to individual measures; do not infer measure-level R&D economies from ministry totals.

### `pnrr_measure_economies_sep2026.csv`

Measure-level ReGiS budgets and economies reported in the parliamentary dossier for DL 162/2026, Article 7(1), at 10 September 2026. Values are in EUR millions. The economy share is the reported economy divided by the reported ReGiS measure budget. The eight rows are the R&D-relevant subset, not the complete list of measures in the annex.

### Interpretation

Economies are not negative R&D spending observations. Zero economies do not prove full expenditure or Frascati eligibility. Keep February ministry-level and September measure-level cohorts distinct pending legal/accounting reconciliation with the 2026 Budget Law return.
