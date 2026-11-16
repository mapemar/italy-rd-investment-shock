# Eurostat macro-data refresh

Run locally with Python 3.12:
```bash
python scripts/refresh_eurostat_macro.py
```

Or run the GitHub Actions workflow **Refresh Eurostat macro data** manually. It also runs monthly.

Outputs:
- `data/processed/eurostat_rd_intensity_italy_2010_2024.csv`: GERD/GDP by sector of performance (TOTAL, BES, GOV, HES, PNP), 2010–2024, with Eurostat flags and extraction vintage.
- `data/processed/eurostat_gdp_italy_2010_2024.csv`: nominal GDP (MIO_EUR) and chain-linked volume index (CLV_I20), with flags and vintage.

GDP implicit deflator may be derived as a GDP price proxy from current-price GDP and chain-linked volume data, normalised to 2019=100. It is not an R&D-specific deflator. Do not use the GDP deflator as if it were an observed R&D price index. The chain-linked volume index is non-additive and is not a constant-price euro level; use growth rates or derive a rebased index carefully.

Primary source: Eurostat dissemination API, datasets `rd_e_gerdtot` and `nama_10_gdp`.
