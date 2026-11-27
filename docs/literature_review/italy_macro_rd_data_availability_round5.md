# Italy macro R&D input data availability — preliminary audit

**Run:** LR-2026-11-27-R5  
**Purpose:** identify official annual data series that can populate the literature-derived variable interface. This is a source-availability audit, not yet a downloaded/validated time series.

## 1. Confirmed official Eurostat/ISTAT anchors

| Required variable | Official source / code | Coverage / breakdown confirmed in source | Initial assessment |
|---|---|---|---|
| GERD by performing sector | Eurostat `rd_e_gerdtot` | Annual; business, government, higher education, private non-profit and total; latest metadata result covers 1980–2025 | Strong core aggregate |
| GERD by performer × funder | Eurostat `rd_e_gerdfund` | Annual; performance sector crossed with source of funds, including rest of world; metadata search result shows coverage 1980–2024 | Essential for public/private and domestic/foreign distinction |
| GERD by source of funds (aggregate) | Eurostat `rd_e_fundgerd` | Official Statistics Explained cites this code for source-of-funds series | Use as check; prefer cross-tab `rd_e_gerdfund` |
| Researchers / R&D personnel | Eurostat `rd_p_persocc` | Annual; professional position, sector, sex; FTE and headcount; latest metadata result covers 1980–2024 | Strong core labour series |
| Government budget allocations | Eurostat `gba_nabsfin07` | Annual; NABS objectives, total and subcategories; coverage 2004–2026 | Strong policy-budget series, but budget provisions not actual R&D |
| Tax support to business R&D | OECD R&D Tax Incentives Database / Corporate Tax Statistics; GTARD | OECD release June 2026 says fiscal-cost data cover 46 jurisdictions for 2000–2024; synthetic tax policy indicators cover 55 jurisdictions for 2019–2025 | Core but distinct source from Eurostat GERD; confirm Italy-specific observation availability |
| R&D type, cost and detailed performer/funder breakdowns | Eurostat R&D collection / national metadata and microdata | Metadata confirms availability by source, type (basic/applied/experimental), cost, NACE and NUTS2; odd-year/detail coverage and country-specific gaps must be checked | Potentially strong, but do not assume all cross-breakdowns are populated annually |
| Italian R&D totals and personnel | ISTAT, *La ricerca e lo sviluppo in Italia – Anni 2024–2025*, release 24 Sep 2026 | 2024 final/current-price results and preliminary 2025; detailed sector, type, personnel and GBARD reporting | High-value national validation source |

## 2. Important source-specific findings

### Eurostat / Frascati statistical system

The Eurostat reference metadata states that R&D expenditure is broken down by performing and funding sectors, type of costs, type of R&D, fields (FORD), socioeconomic objectives (NABS), regions (NUTS2) and, for business R&D, NACE industry, size class and industry orientation. Personnel is broken down by occupation, sector, qualification, sex and region. Annual reference period is the calendar year. This is a good conceptual match to the variable register.

The exact dataset identifiers confirmed in this audit are:
- `rd_e_gerdtot`: GERD by sector of performance;
- `rd_e_gerdfund`: GERD by sector of performance and source of funds;
- `rd_e_fundgerd`: GERD by source of funds;
- `rd_p_persocc`: R&D personnel by sector, professional position and sex;
- `gba_nabsfin07`: GBARD by NABS 2007 socioeconomic objectives.

No dataset identifier for the detailed type-of-R&D or cost cross-tabs is asserted here. Those identifiers must be confirmed from the live Eurostat data tree and metadata before extraction.

### GBARD versus realised R&D

Eurostat explicitly defines GBARD as budget provisions, not actual expenditure. It includes funding for R&D performed in business, higher education, government, private non-profit and the rest of the world. It must not be equated with GOVERD or GERD, and NABS reflects the intended socioeconomic objective when funds are committed rather than the ex-post project content.

### GTARD and B-index

OECD's June 2026 statistical release reports updated GTARD fiscal-cost indicators and synthetic tax policy indicators (including implied marginal subsidy rates) for different firm sizes and profitability statuses. These are separate measures:
- GTARD: foregone revenue and refundable amounts (fiscal cost);
- marginal tax subsidy/user-cost measures: expected reduction in the marginal cost of an additional unit of eligible R&D;
- BERD/GERD: R&D performed.

OECD notes that GTARD does not cover income-based provisions such as patent boxes in the same way as expenditure-based R&D incentives. The project's instrument taxonomy must preserve this distinction.

## 3. Latest Italian official R&D release — variables directly useful

ISTAT's release of 24 September 2026 covers 2024 and preliminary 2025:
- 2024 R&D expenditure grew 5.6% in current prices; university R&D expenditure rose 13.4%, public institutions 4.7%, and business R&D 2.4%.
- Preliminary 2025 business R&D expenditure fell 2.6% relative to 2024.
- 2024 R&D personnel: about 510,000 persons; 352,000 FTE; researchers about 179,000 FTE.
- R&D personnel FTE increased 1.2% overall, with a decline in business FTE (-5.9%) offset by increases in universities (+13.6%), public institutions (+5.6%) and non-profit (+7.1%).
- The share of researchers in business R&D personnel was 37.2%, compared with 68.2% in universities and 62.3% in public institutions.
- Universities allocated more than half of R&D spending to basic research; public institutions and non-profits concentrated more on applied research.
- ISTAT reports 2024 central-government, regional and autonomous-province R&D budget allocations of approximately EUR 13.5bn, broadly stable (+0.5%); 2025 initial allocations approximately EUR 13.1bn (-3.2%). This is a budget measure, not realised GERD.

These are published aggregate indicators, not yet a validated annual model-ready dataset. The full report and methodological annex should be extracted and reconciled to Eurostat vintages before modelling.

## 4. Data gaps and risks

1. **Time span:** the current project statistical baseline is 2015–2024. Eurostat GERD and personnel series can extend to 1980, so the baseline can potentially be extended backwards for a more credible macro time-series fit. Breaks in definition, sector coverage and revisions must be documented.
2. **Annual cross-tabulations:** source, type, costs and personnel breakdowns may have different availability and may not all be complete every year. Build a coverage matrix at the dimension-combination level.
3. **R&D deflators:** constant-price R&D capital stocks require a defensible price index; a single GDP deflator is not automatically valid for R&D labour/equipment. Keep nominal series and alternative deflations.
4. **GTARD:** confirm Italy-specific time coverage and the exact OECD indicator series; GTARD may be less current than GERD/GBARD, and tax timing differs from cash revenue.
5. **B-index:** requires tax law and firm characteristics (size, profitability, expenditure mix); not an administrative spending series.
6. **Microdata:** the public-support-to-BERD causal link requires secure matching of R&D surveys, company accounts, tax claims and support recipients. Public aggregate data cannot identify treatment effects.
7. **Regional and sectoral spillovers:** patent-class exposure, university proximity, high-tech trade and FDI require separate linked datasets and should remain optional satellite inputs.
8. **Revisions:** preserve download date, dataset code, dimensions, flags, unit, source vintage and original value. Never silently overwrite a series.

## 5. Recommended data assembly order

1. Download full `rd_e_gerdtot`, `rd_e_gerdfund`, `rd_p_persocc` and `gba_nabsfin07) for Italy and selected EU comparators, retaining all flags and dimensions.
2. Build a year × sector × funder × unit availability matrix and identify structural breaks.
3. Retrieve detailed R&D type/cost series only after exact identifiers and coverage are verified.
4. Retrieve OECD GTARD and implied marginal subsidy-rate series for Italy; preserve the distinction between fiscal cost and tax wedge.
5. Extract the ISTAT 2024–2025 release tables and reconcile totals, sector values, personnel and GBARD with Eurostat.
6. Extend historical macro series (TFP, GDP, physical capital, human capital) with compatible vintages and test break-adjusted comparability.
7. Only after the coverage audit, decide whether the Italian annual time series supports a VECM/BVAR benchmark or whether panel/QUEST calibration is required.

## 6. Sources reviewed

- Eurostat Data Browser: `rd_e_gerdtot`, `rd_e_gerdfund`, `rd_p_persocc`, `gba_nabsfin07`.
- Eurostat Statistics Explained: source-of-funds code `rd_e_fundgerd).
- Eurostat R&D reference metadata (ESMS): dimensions, units, reference periods and data-release/revision practices.
- Eurostat GBARD metadata: definition as budget provisions.
- OECD, *Government support for business R&D approaches record highs as R&D tax incentives expand across the OECD*, 25 June 2026 (updated 29 June 2026).
- OECD, Corporate Tax Statistics 2026, R&D tax incentives chapter.
- ISTAT, *La ricerca e lo sviluppo in Italia – Anni 2024–2025*, 24 September 2026.
