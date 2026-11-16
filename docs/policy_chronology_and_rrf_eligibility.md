# Policy chronology and RRF eligibility: data rules

## Purpose

The research window is extended to **2018–2030**. The panel distinguishes the pre-RRF baseline (2018–2019), the RRF implementation/eligibility window (2020–2026), and post-RRF persistence or spillovers (2027–2030). This is an analytical observation window, not a claim that the Italian RRP was approved in 2020 or that all measures started in that year.

## Legal and institutional dates

- NextGenerationEU and the political design of the recovery instrument developed in 2020.
- Italy formally submitted its initial RRP on 30 April 2021.
- The Commission endorsed it on 22 June 2021; the Council approved it on 13 July 2021.
- Article 17(2) of Regulation (EU) 2021/241 provides that measures started from 1 February 2020 may be eligible, subject to the Regulation's requirements.
- The Commission interprets 'started' as implementation on the ground, when economic value begins to be created. Preparation and initial phases launched before 1 February 2020 may only be included through clearly defined implementation phases/sub-projects whose entirety of costs are recorded after 1 February 2020 in ESA 2010 terms.
- The Italian PNRR Commission Staff Working Document states that the costs of measures financed by the Italian RRP refer to costs undertaken after 1 February 2020; where steps occurred earlier, only later-starting phases with all costs recorded after that date were included.

## Required chronology per measure

The pnrr_measure_timeline.csv file contains one record per inventory measure and deliberately leaves dates blank until documentary evidence is located. For every measure, distinguish:

1. **Policy origin date:** when the policy/programme was first announced or designed.
2. **Legal basis date:** law/decree/decision establishing the scheme.
3. **First implementation date:** first actual implementation on the ground (not merely announcement).
4. **PNRR inclusion date:** when the measure entered the Italian Plan/CID version.
5. **RRF eligibility start date:** start date of the eligible implementation phase under Article 17(2).
6. **Cost recording test:** evidence that the entirety of the costs assigned to the eligible phase is recorded after 1 February 2020 in ESA 2010 terms.
7. **Pre-existing policy/project flags:** identify schemes/projects that existed before PNRR, without assuming that their pre-existing costs are RRF eligible.

## Treatment of pre-existing measures

A policy may have a pre-2020 legal origin and still have a distinct later implementation phase. Conversely, inclusion in the PNRR does not make the entire historical spending of an existing programme eligible or additional.

For each measure, separate historical national-policy spending before PNRR; pre-1 February 2020 costs (exclude from RRF-eligible cost); eligible post-1 February 2020 implementation costs; pre-existing national appropriation relabelled or replaced by PNRR financing; genuinely additional expenditure induced by the measure; and later post-2026 persistence/spillovers.

Do not count relabelled national spending as additional merely because its funding source changed. Do not treat a pre-existing programme's entire baseline as a PNRR shock.

## Annual panel

pnrr_measure_year_macro_panel.csv is extended to 2018–2030 for every measure in the current inventory:
- 2018–2019: pre-RRF baseline;
- 2020–2026: RRF window, subject to measure-specific eligibility and cost tests;
- 2027–2030: post-RRF tail, not RRF-financed by default.

Blank values mean not collected, not zero. Annual observations must be assigned to the year of actual economic activity/expenditure, not mechanically to the year of allocation, PNRR inclusion or cash transfer.

## Sources

- Regulation (EU) 2021/241, Article 17(2): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02021R0241-20240301
- European Commission, COM(2024) 474 final, eligibility of measures under the RRF: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52024DC0474
- Commission Staff Working Document, analysis of Italy's RRP, SWD(2021) 165: https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:52021SC0165
- Italian Ministry of Health PNRR FAQ, questions 64–65: https://www.pnrr.salute.gov.it/it/pnrr-contenuti-di-sezione/faq/?faq.page=12&lingua=italiano
- European Commission country page, Italy's RRP and successive CID versions: https://reforms-investments.ec.europa.eu/recovery-and-resilience-facility-1/country-pages/italys-recovery-and-resilience-plan_en

## Historical programme evidence

MUR's PRIN series for 2007–2022 and the chronology of FCS/FIT, innovation agreements and R&D tax credits are now recorded separately in `data/processed/prin_historical_funding_2007_2022.csv` and `data/processed/historical_rd_policy_register.csv`. These are policy/budget history sources, not annual GERD expenditure. For PRIN, do not treat the MUR funding series as actual annual research performance; separate the national PRIN 2022 call from the PNRR-funded November 2022 call.
