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

## 5. What is and is not estimated

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

## 6. Next calculation steps

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
- MIMIT, DTF and GTF reporting and control guidelines: https://www.mimit.gov.it/images/stories/documenti/allegati/LLGG_Rendicontazione_e_controllo_Investimenti_CDP_VC_PNRR_MIMIT_versione_2.pdf

