# Fieldhouse and Mertens (2026) — government R&D appropriations shocks and productivity

**Bibliographic record:** Andrew J. Fieldhouse and Karel Mertens (2026), “The Returns to Government R&D: Evidence from US Appropriations Shocks”, *American Economic Review*, 116(11), 3959–4002. DOI: 10.1257/aer.20231684.  
**Full text:** https://andrewjfieldhouse.com/wp-content/uploads/2026/10/Fieldhouse-and-Mertens-AER-2026.pdf  
**Replication package:** https://doi.org/10.3886/E246181V1  
**Review date:** 27 November 2026  
**Status:** full published article reviewed; US evidence, not an Italy calibration.

## 1. Research design and identification

The authors assemble a new postwar dataset of enacted R&D appropriations for major US federal agencies: Department of Defense, Department of Energy, NASA, NIH/HHS, NSF and historical precursors. They narratively classify significant changes in appropriations, identifying changes that are largely unanticipated and plausibly exogenous after conditioning on controls.

They estimate long-horizon Jordà local projections on quarterly US data from 1948Q1 to 2021Q4. They distinguish defense from nondefense appropriations shocks. This is important because appropriation, outlay/performance and capital accumulation occur at different times.

The second stage structurally estimates the production-function elasticity of government R&D capital using the SP-IV methodology of Lewis and Mertens (2024). The approach uses the estimated responses of government R&D capital and infrastructure-adjusted TFP to the narrative appropriations shocks as identifying moments in a GMM procedure.

## 2. Main findings

- A nondefense appropriations shock causes a delayed, gradual and persistent increase in business-sector TFP; the response becomes highly statistically significant at long horizons (8–15 years).
- A shock inducing a 1% increase in government R&D capital produces an eventual increase in TFP of about 0.2% in the baseline impulse responses.
- The production-function elasticity to total government R&D capital is approximately 0.11 in the preferred nondefense-shock specification (95% robust CI 0.09–0.15). Given the average nondefense share, the implied elasticity to nondefense R&D capital is about 0.06.
- Implied gross returns to nondefense government R&D are 140–210%, depending on specification and calculation.
- The authors' growth accounting attributes at least one-fifth of postwar business-sector TFP growth to government-funded R&D.
- Nondefense shocks increase patents, STEM doctoral recipients, R&D researchers and technology publications.
- Public and private R&D appear complementary: privately funded R&D capital increases following both defense and nondefense shocks, although the nondefense response is relatively small (peaking at around 20 cents per federally funded dollar). Defense-related private R&D responses are larger but later reverse.
- The paper finds little evidence of persistent productivity gains from defense R&D within 15 years; estimates for defense R&D productivity are imprecise/inconclusive. Do not interpret this as proof that all defense research has zero social return.
- Nondefense R&D appropriations also induce increases in nondefense public infrastructure, including education structures, roads, power, water and sewer systems. The authors therefore separate public infrastructure capital from government R&D capital in the production function.

## 3. Crucial measurement distinctions

The paper distinguishes:
1. R&D appropriations (budgetary authorisations);
2. actual R&D spending/outlays and the timing of performance;
3. government R&D capital stock;
4. business R&D capital stock;
5. public infrastructure capital stock;
6. innovation outputs (patents, STEM PhDs, researchers, technology publications);
7. business-sector TFP and real GDP.

Government R&D capital includes federally funded contract R&D performed outside government — by businesses, universities, non-profits and public-private R&D centres — as well as intramural government R&D. Funding source and performing sector are therefore distinct.

The BEA/NIPA government R&D capital concept capitalises software development and corresponds to government intellectual property in the US national accounts. It is not identical to a strict Frascati GERD series. The authors note differences between NIPA and NCSES expenditure data, including broader software-development treatment and classification of R&D plant, operational systems development, equipment and structures.

NCSES data permit breakdowns by funding agency, performing sector and type of research activity: basic research, applied research and experimental development. The paper shows that nondefense shocks disproportionately raise basic research and funding performed in government agencies and universities; defense shocks are more concentrated in development/product improvement and business performance. The majority of incremental publicly funded work is nevertheless extramural.

## 4. Model implications and candidate variables

This paper requires additions/refinements to the project's macro interface:

- Government R&D appropriations shock, ideally by instrument/measure, year and performer/funder.
- Actual government-financed R&D expenditure, by performing sector and R&D type.
- Government R&D capital stock, separately from public infrastructure capital.
- Nondefense/civilian and defense/security R&D stocks where a meaningful classification exists; for Italy, do not assume a direct US agency mapping.
- Business-funded R&D capital stock and response to public R&D shocks.
- Public infrastructure capital stock as a separate production-function input/control.
- Research outputs: patents, STEM doctoral completions, researchers/FTE, publications.
- Long lag/distributed response profile from appropriation to expenditure, capital accumulation and productivity.
- Narrative/exogenous policy-shock identification record and controls, if an Italian historical shock study is attempted.

The paper's production-function architecture has business-sector output/TFP as outcome and includes business factor inputs, public infrastructure capital and government R&D capital as separate arguments. The estimated government R&D elasticity is a structural production-function parameter; the 140–210% return is a derived gross-return concept, not an annual fiscal multiplier and not a PNRR additionality rate.

## 5. What transfers to the Italy/PNRR project — and what does not

**Transferable methodological lessons**
- Keep appropriations, commitments, cash outlays, beneficiary expenditure and R&D performance as separate stages.
- Separate government-funded R&D from R&D performed inside government: universities and firms can perform publicly financed R&D.
- Separate public R&D capital from public infrastructure capital.
- Preserve R&D type and performer-sector composition; public basic research and business development may have different spillover channels.
- Allow for long lags and persistent effects; annual PNRR expenditure should not be mapped into contemporaneous TFP.
- Estimate private-R&D crowd-in rather than assuming it; model public/private complementarity as an empirical mechanism.
- Treat innovation outputs as intermediate indicators, not substitutes for R&D inputs.

**Not transferable without further work**
- The numerical elasticities, returns and US long-run impulse responses.
- The defense/nondefense agency classification and historical US appropriations instrument.
- The US national-accounting definition of government R&D capital, including its software capitalisation.
- A causal interpretation of Italian PNRR allocations: the US narrative shock identification strategy does not automatically apply to PNRR programme allocations.

## 6. Data implications for Italy

The Italian dataset should retain a funding-source × performing-sector × R&D-type matrix. For public funding, the most important split is government-financed R&D performed by:
- government institutions (GOVERD);
- higher education (HERD);
- businesses (BERD);
- private non-profit (PNP).

The project should seek annual actual performance, not only GBARD or budget allocations. For capital-stock construction, develop alternative PIM series for public-financed R&D and public infrastructure separately, with documented deflators and depreciation assumptions. Publicly funded R&D performed in BERD/HERD should remain visible rather than being assigned to GOVERD.

Potential intermediate outcomes are patent applications/grants/citations, STEM doctoral completions, researchers FTE and scientific/technology publications. Their lags and measurement coverage need explicit treatment.

## 7. Relevance to model selection

This paper is particularly useful for a production-function / local-projection / structural-IV route. It is not a ready-made QUEST calibration. It suggests a potential empirical benchmark for the project:
- construct annual Italian government-financed R&D capital and public infrastructure capital;
- identify plausibly exogenous policy/funding shocks, if possible;
- estimate long-run productivity responses with local projections or a parsimonious time-series/panel design;
- use structural-IV or external instruments only if the identification assumptions and data support them.

Italy's annual sample is much shorter than the US quarterly postwar sample. A direct replication is not credible without a substantially longer series and defensible shock identification. The article should inform variable construction and mechanisms, not be used to mechanically calibrate the Italian model.

## 8. Source and traceability notes

Primary source: published AER PDF linked above. The article itself reports its replication package at DOI 10.3886/E246181V1. The full text and supplementary appendix should be used for any future extraction of exact variable definitions, depreciation rates, shock dates, agency-account mappings, local-projection controls and SP-IV moment conditions. This review summarises the published article's main text; no replication code or raw US data have been executed in this project.
