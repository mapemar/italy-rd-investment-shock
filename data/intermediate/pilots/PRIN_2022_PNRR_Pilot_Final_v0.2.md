# PRIN 2022 PNRR pilot — final v0.2 content note

**Reference version:** PRIN_2022_PNRR_Pilot_Final_v0.2.xlsx  
**Date:** 20 November 2026  
**Status:** methodological/feasibility pilot; not a national annual R&D estimate.

This note records the substantive content of the final pilot workbook. It is a text companion, not a byte-for-byte replacement for the Excel workbook.

## Scope

The pilot covers PRIN 2022 PNRR, DD 1409/2022, M4C2 Investment 1.1. It is distinct from:
- national PRIN 2022, DD 104/2022;
- the aggregate M4C2I1.01 PNR/PRIN measure with EUR 1.8bn envelope.

## MUR award totals

| ERC macrosector | Projects | Awarded contribution (EUR) | Share of projects | Share of awards | Average award (EUR) |
|---|---:|---:|---:|---:|---:|
| LS – Life Sciences | 629 | 147,000,000 | 35.38% | 35.04% | 233,704.29 |
| SH – Social Sciences and Humanities | 524 | 126,000,000 | 29.47% | 30.04% | 240,458.02 |
| PE – Physical Sciences and Engineering | 625 | 146,493,888 | 35.15% | 34.92% | 234,390.22 |
| **Total** | **1,778** | **419,493,888** | **100%** | **100%** | **235,935.82** |

The stated envelope is EUR 420m. The difference against published sector awards is EUR 506,112 (0.12%) and remains to be reconciled.

ERC macrosectors classify scientific fields, not institutional performing sectors. They must not be used as HERD/GOVERD/BERD codes.

## CNR-IAC local-unit case study

The technical report 04/2026 provides five project/local-unit participations. The reported amounts below are a case study, not a national execution sample.

| Project code | Funded amount EUR | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Reported total EUR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| P2022BLN38_002 | 91,250 | 7,273.75 | 10,562.75 | 8,602.00 | 21,036.41 | 23,325.88 | 24,262.16 | 95,063.00 |
| P2022XJ9SX_002 | 27,850 | 4,455.33 | 8,389.48 | 9,219.32 | 5,376.25 | 4,111.25 | 2,782.31 | 34,334.00 |
| P20228HZWR_002 | 56,500 | 3,560.98 | 16,924.16 | 16,853.66 | 13,191.48 | 3,289.00 | 12,776.30 | 66,595.60 |
| P2022AKRZ9_001 | 110,989 | 7,627.95 | 14,975.79 | 20,829.20 | 21,550.25 | 21,015.62 | 25,366.52 | 111,365.30 |
| P2022CMKHN_002 | 55,250 | 5,819.00 | 7,716.50 | 8,538.75 | 13,282.50 | 7,590.00 | 19,911.66 | 62,858.40 |
| **Total** | **341,839** | **28,737.01** | **58,568.68** | **64,042.93** | **74,436.89** | **59,331.75** | **85,098.95** | **370,216.21** |

The quarter/quadrimester sums are approximately EUR 370,216.21. The reported project row totals sum to EUR 370,216.30 due to rounding. Reported expenditure exceeds local-unit funded allocations by approximately EUR 28,377 (8.3%). The report does not reconcile the discrepancy; do not scale it to the national level or use it as an execution ratio.

The Q1–Q6 periods are quadrimesters, not calendar years, and cross calendar years. Exact transaction dates are required for annual allocation. A Q6bis extension (30 November 2025–28 February 2026) appears in university reporting but is not separately displayed in the CNR-IAC table.

## Frascati cost crosswalk

| Cost category | Initial treatment | Main validation issue |
|---|---|---|
| Personnel A1/A2 | Strong candidate for direct R&D labour; derive hours/FTE and annual costs | Verify tasks are R&D; avoid double counting salary and standard hourly cost |
| Equipment/instruments | Potential R&D capital expenditure if directly used for R&D | Identify acquisition year and R&D use; Frascati capital expenditure differs from depreciation |
| Consultancy/services | Include only services directly part of R&D | Exclude routine testing, legal/admin services; identify performer and location |
| Materials/consumables | Include if directly consumed in R&D | Exclude general-purpose items without project linkage |
| Travel/missions | Potential supporting R&D cost | Include only missions directly supporting R&D; distinguish dissemination |
| Dissemination/publications/open access | Not automatically R&D performance | Separate communication/dissemination from R&D activity |
| General costs / flat rate | Keep separate pending statistical treatment | The reported 15% flat rate must not be treated automatically as additional direct R&D |
| Doctoral/research contracts | Count actual research effort | Separate research task time from training/coursework |

## Automation backlog retained in the pilot

The final workbook contains an `Agent_Backlog` sheet with 13 workflows:
A01 source discovery; A02 PDF/ZIP extraction; A03 project entity resolution; A04 institution classification; A05 financial-report extraction; A06 date-to-year allocation; A07 cost classification; A08 double-counting/funding reconciliation; A09 QA/anomaly detection; A10 research-output linkage; A11 macro/statistical aggregation; A12 causal additionality; A13 database publishing.

Automatable tasks include source versioning, document/table extraction, project and CUP matching, institution mapping, rendiconti ingestion, transaction-date allocation, cost classification, reconciliation checks and versioned publishing. Human review remains necessary for source authority, ambiguous R&D classification, institutional edge cases, double-funding resolution and causal identification.

## Source register retained in the workbook

- MUR admission decrees PRIN 2022 PNRR: https://www.mur.gov.it/it/atti-e-normativa/decreti-di-ammissione-al-finanziamento-bando-prin-pnrr-decreto-direttoriale-n-1409
- MUR PRIN portal – reporting documentation: https://prin.mur.gov.it/Pages/Index/221
- MUR PRIN 2022 PNRR call: https://prin.mur.gov.it/Pages/Index/161
- MUR PNRR Investment 1.1: https://www.mur.gov.it/it/pnrr/misure-e-componenti/m4c2/investimento-11-fondo-il-programma-nazionale-della-ricerca
- CNR-IAC technical report 04/2026: https://iris.cnr.it/retrieve/ab633502-6780-4544-bada-8c57ff87d213/RT_Rendicontazione%20e%20monitoraggio%20dei%20progetti%20PRIN%202022%20PNRR%20firmato_signed_signed.pdf
- MUR reporting guidelines 08/02/2024: https://www.mur.gov.it/sites/default/files/2024-02/Linee%20Guida%20rendicontazione%20PRIN_prot.%28U%29.0000148%20del%2008-02-2024.pdf
- University of Chieti reporting page: https://www.dec.unich.it/pagina-rendicontazione-1487
- University of Cagliari performance report: https://performance.gov.it/performance/relazioni-performance/allegato/3145
- ANVUR 2026 report landing page: https://www.anvur.it/it/dati-e-pubblicazioni/rapporto-anvur
- ANVUR Focus 1 PDF: https://www.anvur.it/sites/default/files/2026-04/1-PNRR-e-Missione4-Rapporto-ANVUR-2026.pdf

## ANVUR provenance clarification added in v0.2

- Report: ANVUR, *Rapporto 2026 sul sistema della formazione superiore e della ricerca*.
- Publication date: 26 March 2026.
- Main financial-data vintage: October 2025.
- Exception: M4C2I3.01 research infrastructure observation updated to February 2026.
- Underlying sources cited by ANVUR include Italia Domani open data (October 2025) and the Government PNRR report at 31 December 2025.
- The EUR 1.8bn M4C2I1.01 PRIN measure is not the PRIN 2022 PNRR call alone.

## Use restrictions

This pilot is not a completed national expenditure estimate, not an official GERD series and not a causal/additionality estimate. The CNR-IAC values are a local-unit case study with an unresolved allocation discrepancy. Blank values must never be interpreted as zero.
