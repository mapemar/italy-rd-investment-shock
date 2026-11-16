# First quantitative shock estimate — Italy R&D and innovation

**Status:** preliminary diagnostic and evidence-based VC proxy; not a causal estimate  
**Cut-off:** 16 November 2026  
**Statistical baseline:** Eurostat `rd_e_gerdtot` repository extraction, 2010–2024; Eurostat `nama_10_gdp` nominal GDP and GDP deflator proxy.

## Executive result

The available macro data do not show a broad-based increase in R&D intensity by 2024. They show a modest rise in real aggregate R&D expenditure since 2019, driven by government and higher education, offset by a decline in business-performed R&D.

- GERD/GDP: 1.46% (2019) to 1.41% (2024), -0.05 percentage points.
- Business R&D/GDP: 0.92% to 0.80%, -0.12 pp.
- Government R&D/GDP: 0.18% to 0.21%, +0.03 pp.
- Higher-education R&D/GDP: 0.33% to 0.38%, +0.05 pp (some observations carry Eurostat estimated flags).

Using the rounded intensity ratios and nominal GDP, and deflating with the GDP-wide deflator proxy (2019=100), approximate aggregate GERD increased from EUR 26.3bn in 2019 to EUR 27.1bn in 2019 prices in 2024 (+3.1%). Business R&D fell by approximately 7.2% in real terms; government-performed R&D rose by approximately 24.5%; higher-education R&D rose by approximately 22.9%. These are approximations because the intensity values are rounded and the deflator is a GDP-wide proxy, not an R&D-specific deflator.

## 1. Descriptive trend benchmark

An OLS linear trend fitted to Italy's GERD/GDP ratio over 2010–2019 and extrapolated to 2024 gives a benchmark of **1.581% of GDP**. The observed 2024 value is 1.41%, a gap of **-0.171 percentage points**.

This is deliberately labelled a *trend diagnostic*, not the causal no-policy counterfactual. It assumes the pre-2020 linear trend would have continued unchanged, ignores structural breaks, the pandemic, policy changes and cross-country convergence, and should not be interpreted as the amount of R&D “lost” because of or despite the PNRR. It does, however, show that there is no aggregate R&D-intensity overshoot relative to the pre-2020 trajectory in this simple benchmark.

## 2. Approximate expenditure bridge, 2019–2024

Calculations: GERD expenditure = GERD intensity × nominal GDP. 2024 values are deflated by the GDP-wide deflator proxy (2019=100; 2024=115.0252).

| Performing sector | 2019 current EUR bn | 2024 current EUR bn | 2024 in 2019 EUR bn | Real change |
|---|---:|---:|---:|---:|
| Total GERD | 26.28 | 31.17 | 27.10 | +3.1% |
| Business (BES) | 16.56 | 17.68 | 15.37 | -7.2% |
| Government (GOV) | 3.24 | 4.64 | 4.04 | +24.5% |
| Higher education (HES) | 5.94 | 8.40 | 7.30 | +22.9% |

Sector totals need not sum exactly because of rounding and the private non-profit sector is omitted from this compact table.

## 3. Cross-check with the latest ISTAT national vintage

The separate ISTAT national series reports GERD of EUR 26.260bn in 2019 and EUR 31.043bn in 2024, with 2024 intensity at 1.40% of GDP. Deflating the 2024 amount by the same GDP-wide deflator proxy (115.0252, 2019=100) gives approximately EUR 26.988bn in 2019 prices, around +2.8% relative to 2019. This is a separate national-statistics vintage and should not be spliced into the Eurostat panel. ISTAT reports 2024 nominal growth of 5.6%; its preliminary 2025 sector data show business R&D -2.6%, government institutions +6.2%, and private non-profit +6.4%, but do not provide a complete 2025 GERD estimate in this source.

## 4. Venture-capital component: now grounded in deployment evidence

The 100% coefficient agreed for DTF and GTF is retained as a **broad innovation-shock proxy**, not official GERD/BERD.

Verified evidence:
- Both funds became operational in 2023 (CDP Venture Capital Annual Financial Report 2024).
- At end-2024, CDP reported combined investment deliberations equal to 43% of the two funds' total investible capital. Applying 43% to the EUR 650m endowment gives a cumulative deliberated amount of approximately **EUR 279.5m**.
- CDP's 2025 Annual Financial Report reports that cumulative deliberations reached **74% of total investible resources** in 2025. Applying this percentage to EUR 650m gives approximately **EUR 481.0m cumulative deliberations** at end-2025.
- The implied increase in the cumulative deliberated amount between the two reporting dates is **EUR 201.5m** (EUR 481.0m minus EUR 279.5m). This is a derived annual proxy for new investment decisions in 2025, not a cash-disbursement or company R&D measure. It is the strongest annual VC innovation-shock proxy currently supported by the fund-level evidence.
- GTF's periodic disclosure reports **EUR 15.65m invested in seven companies** as at 31 December 2024.
- DTF's Annual Financial Report shows NAV of approximately EUR 16m and nine direct startup investments plus three VC funds (with seven underlying startups); NAV is not the same as gross deployment and is not used as an investment-flow proxy here.
- The same CDP annual report reports GTF NAV of approximately EUR 18m and seven direct startup investments plus three VC funds; the GTF SFDR disclosure says no indirect startup investments had yet occurred as at the reporting date.

**Quantification rule adopted for the extended innovation shock:** count 100% of fund-level deliberated investments as the VC-backed innovation proxy, in line with the user's explicit modelling assumption. Record EUR 279.5m cumulative by end-2024 and EUR 201.5m as the incremental 2025 proxy; cumulative end-2025 is EUR 481.0m. These are approvals/deliberations, not cash deployment. The EUR 15.65m GTF actual investment disclosure is a subset/validation point and must not be added again. DTF NAV is not used as a deployment measure. The proxy is kept outside official GERD/BERD.

## 5. New MIMIT implementation evidence at 31 December 2025

The MIMIT *PNRR Report – second semester 2025* adds a stronger operational picture for the venture-capital funds and financial progress indicators for other R&D-relevant measures.

### DTF and GTF

- GTF (EUR 250m): approx. 70% of total resources committed, including direct and indirect investments and costs; 8 direct start-ups, 3 third-party VC funds investing in 6 further start-ups, 14 investee companies in total, and 95 additional jobs relative to the investment date.
- DTF (EUR 400m): approx. 70% committed, including direct and indirect investments and costs; 16 direct start-ups, 6 third-party VC funds investing in 28 further start-ups, 44 investee companies in total, and 132 additional jobs relative to the investment date.
- Combined portfolio: 58 investee companies and 227 additional jobs.
- Applying 70% to the combined EUR 650m envelope gives EUR 455m indicative committed resources (EUR 175m GTF; EUR 280m DTF). This includes costs and is not cash deployed in companies.
- CDP's 74% deliberations figure is a separate indicator with a different scope; do not combine it with the MIMIT 70% commitment ratio.

The adopted 100% coefficient remains applicable to the broad innovation-shock proxy. For the present annual series, however, EUR 455m is a cumulative commitment indicator at end-2025, not an annual flow. The actual annual deployment profile remains to be obtained.

### Other MIMIT measures: financial progress snapshot

The MIMIT report's financial table at 31 December 2025 reports:
- IPCEI (EUR 1.5bn envelope): EUR 215.36m financial progress (14.67%).
- Innovation Agreements (EUR 164m): EUR 11.38m (6.94%).
- Technology Transfer Centres (EUR 350m): EUR 46.95m (13.41%); the report separately reports 6,500+ firms reached and 420+ R&D projects financed.
- Net Zero / strategic supply chains (EUR 3.5bn): EUR 698.87m (19.97%).

These are measure-level implementation indicators, not automatically R&D expenditure. IPCEI includes R&D, innovation and first industrial deployment; technology transfer includes services and centre operations; Net Zero is a mixed industrial investment programme. The R&D share must be isolated before including these amounts in official-boundary R&D.

## 6. What is and is not estimated

### Estimated / observed
- Historical GERD intensity and sector shares through 2024.
- Approximate real GERD expenditure bridge 2019–2024.
- Simple 2010–2019 linear trend benchmark and 2024 gap.
- Verified DTF/GTF cumulative deliberated amount at end-2024 and end-2025, with the 2025 incremental proxy.
- GTF's disclosed EUR 15.65m actual investment as a partial deployment validation point.

### Not yet estimable from the evidence in the repository
- Annual additional R&D expenditure caused by each MUR/MIMIT PNRR measure.
- Annual cash deployment by DTF/GTF and fund-by-fund direct/indirect transaction flows; the current annual proxy uses investment deliberations.
- Private capital mobilised by DTF/GTF, including direct/indirect channel split and the DTF 1:1 indirect leverage requirement's realised amount.
- Annual impact of Law 193/2024 Article 33 on institutional VC commitments.
- Additionality/crowding-in and the counterfactual for all measures.
- 2025 full GERD/GDP and sector performance series.

No annual PNRR R&D shock total or causal multiplier is published in this version. The data currently support a sectoral diagnostic and a partial VC proxy, not a complete causal estimate.

## 7. Next calculation steps

1. Obtain DTF/GTF transaction-level cash deployment by year and direct/indirect channel; replace the deliberation-based 2025 proxy when available.
2. Reconstruct annual expenditure profiles for the MUR measures from beneficiary expenditure / ReGiS / annual MUR reports; separate pre-existing PRIN and other programmes.
3. Reconstruct MIMIT R&D grant and tax-credit eligible expenditure, separating R&D from capital goods, innovation and training.
4. Build a country comparison panel (GERD, BES, GOV, HES, GDP) to assess whether Italy's sectoral changes differ from comparable EU countries.
5. Replace the simple trend benchmark with comparative-country / synthetic-control and sector-level robustness analyses.
6. Publish both the official-boundary additional domestic R&D series and the extended innovation shock including the agreed 100% DTF/GTF proxy.

## Sources

- Eurostat `rd_e_gerdtot`, repository extraction: `data/processed/eurostat_macro_panel_italy_2010_2024.csv`.
- Eurostat `nama_10_gdp`, repository extraction: `data/processed/eurostat_gdp_italy_2010_2024.csv`.
- CDP Venture Capital, *Relazione Finanziaria Annuale 2024*, especially pp. 66–67 and discussion of PNRR funds: https://cds.cdpventurecapital.it/cdpventurecapital/public/cms/documents/CDP_VC_Bilancio_2024.pdf
- CDP Venture Capital, *Relazione Finanziaria Annuale 2025*, especially pp. 69 and 100–101: https://cds.cdpventurecapital.it/cdpventurecapital/public/cms/documents/CDPVC_Relazione%20Finanziaria_Annuale_2025.pdf
- CDP Venture Capital, GTF periodic disclosure (as at 31 December 2024): https://cds.cdpventurecapital.it/cdpventurecapital/public/cms/documents/Estratto%20periodica%20per%20sitoweb_GTF_20250610_VENG_Final.pdf
- MIMIT, *PNRR Report – second semester 2025*, pp. 31, 77–80, 94 and 98–101: https://www.mimit.gov.it/images/stories/documenti/allegati/pnrr/31122025_Mimit_Report_Semestrale_DEF_.pdf
- MIMIT, DTF and GTF reporting and control guidelines: https://www.mimit.gov.it/images/stories/documenti/allegati/LLGG_Rendicontazione_e_controllo_Investimenti_CDP_VC_PNRR_MIMIT_versione_2.pdf



## 7. New execution evidence: Court of Auditors and ReGiS snapshots

### 7.1 PRIN — first measure-level expenditure observation

The Court of Auditors' May 2025 report, based on ReGiS, reports that the PRIN investment (EUR 1.8bn allocation) had recorded expenditure equal to **56.3%** of its allocation at 31 December 2024. This implies approximately **EUR 1,013.4m cumulative reported expenditure** (1,800 × 56.3%). This is the strongest measure-specific MUR expenditure observation identified so far.

It is a cumulative stock of reported expenditure by the snapshot date, not an annual 2024 flow. It must not be spread mechanically across 2022–2024. It also does not establish that the full amount is additional relative to pre-existing research funding: the PRIN investment included projects already in the pipeline and national co-financed lines.

The same Court of Auditors exercise selected EUR 19.16bn of PNRR R&D&I interventions across multiple missions and found EUR 6.16bn (32.2%) spent by 31 December 2024. This aggregate is a cross-check only; it includes PRIN and other measures and must not be added to the PRIN amount.

### 7.2 MUR — administration-level execution snapshot

The Government's Seventh PNRR Report reports, at 30 November 2025, MUR allocations of EUR 11,583.01m, of which EUR 599m relates to the student-housing financial instrument, and cumulative PNRR spending of EUR 7,343.19m. Excluding the student-housing instrument from the allocation denominator gives EUR 10,984.01m and a reported execution ratio of **66.9%**.

This is not an R&D-only figure: MUR's PNRR portfolio also includes education, scholarships, skills and other interventions. It is an administration-level execution control, not a direct estimate of M4C2 R&D expenditure.

### 7.3 MIMIT — financial-instrument execution at 30 November 2025

The Seventh PNRR Report's Table 28 provides cumulative ReGiS spending for financial instruments and similar measures. The relevant entries are:

| Measure | Budget (EUR m) | Reported spending (EUR m) | Ratio |
|---|---:|---:|---:|
| IPCEI | 1,500.00 | 269.44 | 17.96% |
| Digital Transition Fund | 400.00 | 66.05 | 16.51% |
| Green Transition Fund | 250.00 | 54.34 | 21.74% |
| DTF + GTF | 650.00 | 120.39 | 18.52% |
| Innovation agreements (territorialisation table) | 164.00 | 11.38 | 6.94% |

These are ReGiS financial execution values for the relevant instruments at the snapshot date. They are not a direct measure of portfolio-company R&D. For DTF/GTF, keep three separate concepts: (i) ReGiS spending recorded by the administration; (ii) CDP's fund-level investment deliberations; and (iii) cash actually invested in portfolio companies. The EUR 120.39m ReGiS figure and the EUR 481m CDP cumulative deliberations are different stages/definitions and must not be added together.

IPCEI is mixed: it includes R&D, innovation and first industrial deployment. Its reported spending cannot be classified 100% as R&D without project cost/work-package evidence.

### 7.4 Innovation agreements — 2026 signed-project pipeline

MIMIT's second four-monthly report for 1 May–31 August 2026 records **23 signed Innovation Agreements**. Across the 23 projects listed in the report, the stated total cost of R&D activities is approximately **EUR 166.57m**, while the administration's stated contribution is approximately **EUR 79.30m** (47.6% of total project R&D cost).

This is a project pipeline/approved R&D-cost measure, not expenditure performed in 2026. The published report includes agreements under more than one ministerial decree (including the 2022 and 2025 calls); do not attribute the entire EUR 166.57m to PNRR M4C2-I2.2bis until each agreement's legal funding source is matched. It is nevertheless a valuable source for project-level R&D cost and public contribution, and should be captured separately pending the legal crosswalk.

## 8. Updated interpretation of the shock

We now have three distinct quantitative anchors:
1. **PRIN:** EUR 1.013bn cumulative reported expenditure at 31 December 2024 (measure-specific, ReGiS-based).
2. **DTF/GTF:** EUR 120.39m cumulative reported ReGiS spending at 30 November 2025, alongside EUR 481m cumulative CDP investment deliberations at end-2025. These are separate implementation stages.
3. **Innovation agreements:** EUR 166.57m of R&D project costs across 23 agreements signed in May–August 2026, with EUR 79.30m stated public contribution; legal funding-source attribution and actual expenditure timing remain to be checked.

These amounts are **not additive**: they refer to different dates, stages, funding concepts and, in the case of the innovation-agreement pipeline, not yet a confirmed common PNRR funding perimeter.

No reliable annual 2020–2026 shock series can yet be constructed from these cumulative snapshots. The next step is to obtain annual transaction/project cash and cost profiles, not to allocate cumulative spending evenly across years. The current evidence does, however, show that the shock has several sizeable channels: direct university research (PRIN and other MUR measures), industrial R&D grants (IPCEI and Innovation Agreements), and VC-backed technology business creation (DTF/GTF).

## Sources added

- Court of Auditors, *Relazione sullo stato di attuazione del PNRR*, May 2025, p.185, PRIN expenditure and selected R&D&I cohort: https://www.mur.gov.it/sites/default/files/2025-05/Quinta%20relazione.pdf
- Presidency of the Council of Ministers, *Settima relazione sullo stato di attuazione del PNRR*, 22 December 2025, Tables 27–29, MUR and financial-instrument expenditure: https://www.mur.gov.it/sites/default/files/2026-01/Settima%20relazione%20-%20sezione%201.pdf
- MIMIT, *Report di monitoraggio del PNRR MIMIT – 2o semestre 2025*, including financial-instrument and territorialisation tables: https://www.mimit.gov.it/images/stories/documenti/allegati/pnrr/31122025_Mimit_Report_Semestrale_DEF_.pdf
- MIMIT, *Accordi per l'innovazione – Report secondo quadrimestre 2026*, 1 May–31 August 2026: https://www.mimit.gov.it/images/stories/documenti/allegati/31_08_26_accordi-innonvazione-2Q-2026.pdf
