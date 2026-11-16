# First empirical diagnostic: Italian R&D intensity and the post-2020 period

**Status:** preliminary descriptive analysis, not a causal estimate  
**Reference date:** 16 November 2026  
**Primary macro source:** Eurostat `rd_e_gerdtot`, Italy, annual, 2010–2024 (repository extraction updated 11 November 2026)  
**Supplementary source:** ISTAT, *La ricerca e sviluppo in Italia – Anni 2024–2025*, published 24 September 2026.

## 1. Executive finding

The broad hypothesis that Italy experienced a sustained, system-wide R&D spending boost after the PNRR is **not supported by the aggregate R&D-intensity series through 2024**.

The data instead point to a more differentiated picture:

- Total GERD intensity rose from 1.46% of GDP in 2019 to 1.50% in 2020, then fell to 1.37% in 2022–2023 and recovered to 1.41% in 2024 (Eurostat vintage in the repository).
- Business-performed R&D intensity fell from 0.92% of GDP in 2019 to 0.80% in 2024.
- Government-performed R&D intensity rose from 0.18% to 0.21%.
- Higher-education-performed R&D intensity rose from 0.33% to 0.38%, although the series carries estimated (e) flags in the repository for several years.

This is consistent with a **public/university research expansion alongside weak business R&D intensity**, rather than an aggregate private-and-public R&D boom.

The 2020 increase must not be interpreted as a PNRR effect: the GDP denominator contracted sharply during the pandemic. RRF implementation and the two CDP-managed venture funds also began after the plan's initial approval and must be timed separately.

## 2. Observed macro series (% of GDP)

| Year | GERD total | Business (BES) | Government (GOV) | Higher education (HES) |
|---:|---:|---:|---:|---:|
| 2010 | 1.21 | 0.65 | 0.17 | 0.35 |
| 2015 | 1.33 | 0.77 | 0.17 | 0.34 |
| 2019 | 1.46 | 0.92 | 0.18 | 0.33 |
| 2020 | 1.50 | 0.93 | 0.20 | 0.35 |
| 2021 | 1.41 | 0.85 | 0.20 | 0.34 |
| 2022 | 1.37 | 0.81 | 0.19 | 0.34 |
| 2023 | 1.37 | 0.80 | 0.20 | 0.34 |
| 2024 | 1.41 | 0.80 | 0.21 | 0.38 |

**Important vintage note:** the Eurostat series in the repository reports 1.41% for 2024. ISTAT's September 2026 release reports 1.40%. Use the latest harmonised Eurostat extraction consistently for the main panel and retain ISTAT's national release as a cross-check; do not splice rounded values from different vintages.

## 3. What the latest ISTAT release adds

ISTAT reports for 2024:

- intra-muros R&D expenditure increased by 5.6% in current prices;
- expenditure by universities increased by 13.4%;
- expenditure by public institutions increased by 4.7%;
- expenditure by enterprises increased by 2.4%;
- public-sector funding of R&D increased by 10.6%, while business funding was broadly unchanged and foreign funding increased by 15.2%;
- enterprises accounted for 56.6% of total R&D performed; universities 26.9%; public institutions 14.7%; private non-profit 1.8%;
- the business-sector increase was concentrated in large firms (+6.4%); small firms fell 13.7% and medium firms 5.2%.

For 2025, ISTAT preliminary estimates indicate business-performed R&D fell by 2.6%, while public-institution R&D rose by 6.2% and private non-profit R&D by 6.4%. These preliminary sector growth rates are not a complete 2025 GERD/GDP observation and must not be used to manufacture one.

The latest Commission assessment reports that Italian authorities' preliminary estimate for public R&D expenditure in GERD terms was 0.59% of GDP in 2025, suggesting the relevant PNRR target was on track. This is a **public R&D component/target indicator**, not total GERD/GDP.

## 4. Preliminary interpretation

### Evidence consistent with a boost
- Public and university research expenditure grew strongly in 2024.
- Public funding of R&D rose 10.6% in 2024.
- The government and higher-education performance-sector shares of GDP in the Eurostat panel were above their 2019 levels in 2024.

### Evidence against a broad-based boost
- Total GERD/GDP in 2024 remained below its 2019 level in the repository's Eurostat vintage (1.41% versus 1.46%).
- Business-performed R&D/GDP fell materially (0.80% versus 0.92%).
- ISTAT's preliminary 2025 data point to another decline in business R&D expenditure.
- Small and medium-sized firms showed marked weakness in 2024.

### What cannot yet be inferred
- The aggregate data do not identify the causal contribution of the PNRR.
- A sector performing R&D is not the same as the sector financing it. The Eurostat performance-sector and source-of-funds dimensions must be analysed separately.
- Public funding is not automatically additional R&D: it can replace national funding, finance projects already planned, or pay for non-R&D components.
- R&D intensity can move because of both the numerator (R&D expenditure) and denominator (GDP).
- The venture-capital funds' investment amounts are not GERD. Only eligible R&D performed by portfolio companies in Italy can enter the R&D shock.

## 5. Identification strategy to implement

Do not estimate a single post-2020 dummy and call it the PNRR shock. Build a policy-timed, sector-specific design.

1. **Descriptive accounting bridge:** construct nominal GERD and GDP, then sector performance ratios and source-of-funds ratios. Keep current-price expenditure, constant-price expenditure and % GDP side by side.
2. **Policy chronology:** record policy origin, legal basis, first implementation, PNRR inclusion, RRF eligibility and actual R&D performance year separately. Pre-existing PRIN, Innovation Agreements and tax credits are not new PNRR shocks.
3. **Treatment intensity:** for each measure-year, derive verified eligible R&D performed in Italy, net of internal transfers and non-R&D costs. Distinguish grants, tax credits, loans, equity and infrastructure.
4. **Additionality:** apply evidence-based additionality/crowding-out adjustments only when supported by evaluations or credible project/company-level comparisons. Keep a range where evidence is incomplete.
5. **Counterfactual:** estimate pre-policy trends and use a synthetic-control / comparative-country or sectoral panel as robustness checks. A simple extrapolation of the 2010–2019 trend is a diagnostic only, not the central causal counterfactual.
6. **Transmission:** map contemporaneous R&D expenditure to GERD by performing sector; model researcher employment, private investment, productivity and TFP as separate outcomes with longer lags.
7. **VC channel:** use fund-level direct/indirect commitments and portfolio-company accounts to identify company R&D, Italian location, performance year, private co-investment and additionality. Do not assume a leverage multiplier not established in the relevant fund documents.

## 6. Immediate analytical priorities

1. Download and preserve the full Eurostat `rd_e_gerdtot` and `rd_e_gerdfund` extracts with flags and dimensions.
2. Reconcile the 2024 Eurostat/ISTAT vintage difference and update the macro baseline consistently.
3. Obtain 2025 national/Eurostat sector data when published; until then label sector growth rates as preliminary.
4. Reconstruct public R&D funding by source of funds and performing sector, not just public-sector GERD.
5. Populate annual measure-level eligible R&D expenditure for MUR and MIMIT measures, including national co-financing and tax expenditure.
6. Obtain DTF/GTF deployment by direct and indirect channel and portfolio-company R&D.
7. Only then estimate annual additional R&D in EUR and as percentage points of GDP.

## Sources

- Eurostat, *GERD by sector of performance*, dataset `rd_e_gerdtot`, data coverage 1980–2024, last update 29 September 2026: https://ec.europa.eu/eurostat/databrowser/view/rd_e_gerdtot/default/table
- Eurostat, *GERD by sector of performance and source of funds*, dataset `rd_e_gerdfund`, last update 29 September 2026: https://ec.europa.eu/eurostat/databrowser/view/rd_e_gerdfund/default/table
- ISTAT, *La ricerca e sviluppo in Italia – Anni 2024–2025*, 24 September 2026: https://www.istat.it/comunicato-stampa/la-ricerca-e-sviluppo-in-italia-anni-2024-2026/
- European Commission, 2026 assessment of Italy's progress report / RRF implementation, CELEX 52026DC0212: https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:52026DC0212

## Repository data used

- `data/processed/eurostat_macro_panel_italy_2010_2024.csv`
- `data/processed/eurostat_gdp_italy_2010_2024.csv`
- `data/processed/pnrr_measure_timeline.csv`
- `data/processed/pnrr_measure_year_macro_panel.csv`
- `data/processed/historical_rd_policy_register.csv`
- `data/processed/macro_transmission_matrix.csv`
- `data/processed/venture_capital_funds.csv`
