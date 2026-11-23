# R&D Policy-to-Macro Translation

**Methodology note and PNRR direct-research pilot**  
**Version 0.1 | 20 November 2026**

> Historical working note. The canonical project methodology is `docs/methodology.md`; this document preserves the separate PRIN pilot protocol as drafted on 20 November 2026.

## 1. Purpose and status

This note records the methodology and reasoning developed for the Italy R&D project. The objective is to translate public policy measures into traceable annual economic inputs that can subsequently be used in macroeconomic analysis and econometric models. This is a working protocol, not a completed empirical estimate. It should evolve through documented, version-controlled decisions.

The first pilot will focus on direct public funding of research under the Italian PNRR, starting with PRIN and then extending to comparable MUR measures. This choice deliberately avoids beginning with demand-driven business incentives, where the key challenge is to estimate the behavioural response of firms.

## 2. Core conceptual architecture

Keep four layers separate. They are linked, but must never be collapsed into one number:

- **Policy layer:** what the legal or administrative measure authorises, funds or requires; its objective, beneficiaries, eligibility and timetable.
- **Fiscal layer:** the public-finance transaction and its annual profile (appropriations, commitments, payments, accrual expenditure, tax expenditure, equity or loans).
- **Economic-performance layer:** the R&D activity actually performed, by whom, where, and in which year; classify under Frascati and by performing sector.
- **Macroeconomic / causal layer:** the model input and, separately, any estimated additionality or macroeconomic effect. These are analytical estimates, not observed facts.

The key distinction is between funding sector and performing sector. A grant financed by the MUR and executed by a university is public funding of Higher Education R&D (HERD), not automatically Government intramural R&D (GOVERD). The classification follows the performer and the actual activity.

## 3. Why start with PRIN

PRIN is a suitable first case because it is a competitive grant scheme financing research projects. The initial translation is relatively direct: public grant → project expenditure → R&D actually performed by the beneficiary research organisations. The pilot can test the extraction of legal and financial data, the annualisation of multiannual projects, Frascati eligibility and the mapping to HERD/GOVERD/BERD without first having to estimate a private firm's demand response.

PRIN is not automatically equal to R&D expenditure in the year in which the call is announced or the grant is awarded. Awards, commitments, cash payments and project execution can occur in different years. Nor should the full grant be assumed to be R&D if any non-R&D or indirect-cost components are present: eligibility and actual use must be checked against the call rules and reporting evidence.

## 4. PNRR measures to include in the direct-research pilot

The first perimeter should be M4C2 measures managed by MUR that directly finance research projects or research capacity. The official MUR PNRR overview lists Investments 1.1–1.5, 3.1 and 3.3. These measures are not homogeneous; retain separate sub-types rather than treating the whole M4C2 envelope as one R&D shock.

- **Core pilot – PRIN (M4C2, Investment 1.1):** Competitive project grants. Separate PRIN from the broader National Research Programme (PNR) funding line and distinguish PNRR-financed calls from nationally financed PRIN rounds. Closest comparator for a clean grant-to-research translation.
- **Core extension – Young researchers (M4C2, Investment 1.2):** Researcher-led projects and research grants. Map the grant/contract and the actual research performed; distinguish research expenditure from the labour-market or retention objective.
- **Core extension, mixed network – Extended Partnerships (M4C2, Investment 1.3):** Research programmes delivered by networks of universities, public research bodies and firms. Split expenditure by performing entity and activity; do not classify the whole partnership as HERD or BERD by default.
- **Mixed research capacity – National Research Centres (M4C2, Investment 1.4):** Funding for national R&D centres and facilities in key enabling technologies. Separate operating research expenditure, research personnel, equipment/infrastructure and technology-transfer activity.
- **Mixed / territorial – Innovation Ecosystems (M4C2, Investment 1.5):** Networks involving universities, research organisations, firms and territorial actors. Include only the Frascati-eligible research component in the strict R&D series; track technology transfer, entrepreneurship and broader innovation separately.
- **Research infrastructure – M4C2, Investment 3.1:** Capital investment in research and innovation infrastructure. Record public investment/capital formation separately from current R&D expenditure. Add annual R&D performance only when the infrastructure is operational and research is actually carried out.

## 5. Adjacent measures: record separately, do not merge into the core grant series

- **Innovative PhDs (M4C2, Investment 3.3):** Research training and doctoral contracts linked to firms' innovation needs. Potentially supports research labour and R&D capacity, but the policy objective and eligible cost base are not identical to project grants. Separate doctoral/research-personnel input; count in HERD/BERD only where the actual activity qualifies as R&D and the performing sector is known.
- **Research doctorates and related university measures under M4C1:** Potentially relevant to research capacity, but classify separately from M4C2 direct research grants. Distinguish education/training expenditure from R&D performed.
- **IPCEI and MIMIT industrial R&D measures under M4C2 / related PNRR lines:** Potentially substantial industrial research and experimental development, but business-oriented and often co-financed. Treat as a second pilot family, with BERD as the likely performer-side variable and a separate additionality/crowding-in question.
- **Technology-transfer, venture-capital and start-up measures:** Enabling or financial instruments. Do not count the fund allocation or equity investment itself as GERD. Track downstream R&D performed by investee firms only when evidence exists.

## 6. Measure-level translation protocol

1. Identify the policy object: stable Measure_ID; PNRR mission/component/investment; call or sub-measure; legal basis; managing authority; implementing entities; start/end dates; funding source.
2. Reconstruct the fiscal profile: for each year, collect appropriations, commitments, payments, recoveries/reallocations and any accrual expenditure separately. Identify EU/PNRR and national co-financing and prevent double counting.
3. Identify recipients and performers: record grant recipient, consortium members, subcontractors where available, and the entity actually performing the research. Preserve institution-level detail where possible.
4. Apply Frascati classification: classify activity as basic research, applied research or experimental development; assess whether the activity meets the Frascati criteria. Record eligibility share and evidence, not just the programme label.
5. Map the performing sector: HERD, GOVERD, BERD or PNP according to the performing organisation. If mixed, split using reported expenditure or a documented allocation key; do not assign the entire award to one sector.
6. Build annual economic execution: construct annual R&D performed in Italy, based on project reporting/expenditure. If unavailable, create explicitly labelled proxies or scenarios; do not equate payments with performance without justification.
7. Create the macro handoff: produce annual nominal and real EUR series, and optionally ratios to GDP. Preserve the underlying component series and metadata. Avoid premature aggregation across grants, infrastructure and financial instruments.
8. Assess additionality separately: only estimate additional R&D relative to a counterfactual where evaluation evidence or a defensible identification strategy exists. Gross publicly funded R&D is not the same as additional R&D.

## 7. Minimum data model

- Measure_ID; parent_investment_ID; call_ID; funding_source (RRF grant/loan, national); legal_basis; managing_authority; beneficiary; performer; project_ID.
- Year; appropriations; commitments; payments; accrual expenditure; beneficiary expenditure; R&D expenditure performed; amount/unit/currency/price basis.
- Frascati_type; Frascati_eligibility_share; performing_sector (HERD/GOVERD/BERD/PNP); geography; current vs capital expenditure.
- Source_ID; document title; URL; page/article/table/paragraph; extraction date; original value; transformation; confidence; validation status.
- Observation_status: observed / administrative / derived / proxy / model-estimated. Missing values remain blank, never silently set to zero.

## 8. Annual variables and model interface

For the first pilot, retain separate annual series:

- PRIN_AUTHORISED_t – authorised resources by year/call.
- PRIN_COMMITTED_t – commitments/contracted grants.
- PRIN_PAID_t – cash paid by year.
- PRIN_RD_PERFORMED_t – actual R&D expenditure performed in the year, where observed or transparently proxied.
- PRIN_HERD_t / PRIN_GOVERD_t / PRIN_BERD_t – split by performing sector where evidence permits.
- PRIN_ADDITIONAL_RD_t – only if a counterfactual estimate is available; otherwise leave unestimated.

For a BVAR or related model, the preferred economic input is not the initial appropriation or grant award by itself, but a well-defined annual series of public R&D funding or R&D actually performed. A separate policy-shock series requires identification of the unexpected component of policy changes. Annual observations should not be mechanically interpolated into quarterly data.

## 9. Quality controls and non-negotiable rules

- No invented values. A missing observation is blank and accompanied by a reason.
- Never conflate appropriation, commitment, payment, ESA accrual, beneficiary expenditure and R&D performed.
- Do not double count EU funding, national co-financing, transfers to intermediaries and downstream expenditure.
- Do not classify all M4C2 spending as R&D or all MUR-funded R&D as HERD/GOVERD without checking performers.
- Keep capital infrastructure separate from current research expenditure; record research services generated later.
- Keep broad innovation and technology transfer separate from strict Frascati R&D.
- Separate extraction confidence from the confidence of economic attribution and causal identification.
- All assumptions, coefficients and revisions must be versioned with source, rationale and approval status.

## 10. Work sequence

1. Pilot 1: PRIN, including separation of PNRR and national financing and annual project execution.
2. Pilot 2: M4C2 Investment 1.2 – young researchers.
3. Pilot 3: M4C2 Investment 1.3 – Extended Partnerships, with performer-level split.
4. Pilot 4: M4C2 Investments 1.4 and 1.5 – mixed research-centre/ecosystem programmes.
5. Pilot 5: M4C2 Investment 3.1 – research infrastructure, with separate capital and operating/R&D flows.
6. Adjacent module: Investment 3.3 and M4C1 doctoral measures.
7. Second family: MIMIT industrial R&D grants, IPCEI and tax incentives; only then test business-demand and additionality mechanisms.

## 11. Official starting references

- MUR – PNRR, Dalla ricerca all'impresa: https://www.mur.gov.it/it/pnrr/misure-e-componenti/dalla-ricerca-allimpresa
- MUR – PNRR measures and components: https://www.mur.gov.it/it/pnrr/pnrr-misure-e-componenti
- MUR – Implementation documents and investment calls: https://www.mur.gov.it/it/pnrr/attuazione-misure-pnrr/investimenti
- MUR – Reporting and control guidance for implementing entities: https://www.mur.gov.it/it/pnrr/strumenti-di-attuazione/Sigeco-e-linee-guida/Linee-Guida-Soggetti-Attuatori/rendicontazione-e-controllo
- MUR – Guidelines for M4C2 system initiatives (DM 1141/2021): https://www.mur.gov.it/sites/default/files/2021-10/Decreto%20Ministeriale%20n.1141%20del%2007-10-2021%20-%20Linee%20Guida_MUR_PNRR_M4C2.pdf
- Senato della Repubblica – Dossier on PNRR research investments: https://www.senato.it/show-doc?id=1487590&leg=19&part=dossier_dossier1-sezione_sezione12-h2_h294&tipodoc=DOSSIER

**Status:** Methodology agreed in principle; measure inventory is a structured starting perimeter, not yet a verified exhaustive census. Individual calls, financial profiles and R&D execution data remain to be extracted and validated.
