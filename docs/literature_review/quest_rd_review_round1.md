# Literature review — first execution round: QUEST-RD, policy entry points and data implications

**Run:** LR-2026-11-27-R1  
**Status:** First substantive round; not a completed literature review  
**Scope:** Macro model architecture, R&D policy entry points and first empirical evidence map  
**Project boundary:** PNRR plus directly associated national co-financing. The 2018–2025 national fiscal-measures census remains separate.

## Executive findings

1. **B3 does not model “R&D spending” through one generic variable.** Its R&D reform indicator maps directly to the exogenous wage-subsidy wedge \(s^{RD}\), while the research production block is endogenous and depends on high-skilled R&D labour, domestic and foreign knowledge stocks, and parameters governing productivity, spillovers and diminishing returns.
2. **The policy representation differs across QUEST-RD applications.** In Varga and in ’t Veld (2009), broad Cohesion Policy support to R&D/RTDI is represented as reductions in fixed costs and intangible-capital costs for intermediate-sector firms; the model separately contains tax subsidies for R&D investment and a fiscal subsidy instrument. This is not the same mapping as B3's \(s^{RD}\).
3. **A model may therefore need several policy levers, but the data engine should not impose a fixed number of R&D shocks.** It should preserve distinct fiscal and performance series and map them to the receiving model only after its equations and definitions are fixed.
4. **The PRIN pilot is not a direct observation of B3's \(s^{RD}\).** PRIN is a direct public research grant channel. It should first be measured as public funding and R&D actually performed by the recipient research organisations (often HERD, subject to performer evidence), not converted into a private R&D wage subsidy.
5. **The literature on additionality is heterogeneous.** Review evidence on R&D tax incentives and direct subsidies cannot justify one universal additionality coefficient. Meta-regression evidence finds that estimates vary with study design and treatment of firm heterogeneity. Additionality must remain instrument-specific and separately identified from gross realised R&D.

## 1. Corpus inventory and access status

The available Project/Library search and the repository materials were checked for the R&D literature and methodology relevant to this first assignment. This is an inventory of what was actually located, not a claim that every file in every Project folder has been exhaustively enumerated.

| ID | Source | Type / role | Access and review status |
|---|---|---|---|
| LR-P001 | Pfeiffer, Varga and in 't Veld (2024), “Unleashing potential: Model-based reform benchmarking for EU Member States”, *European Journal of Political Economy* 83, 102535, DOI 10.1016/j.ejpoleco.2024.102535; Project file b3 paper.pdf | Current anchor; QUEST-RD-based multi-country model | Full 22-page PDF text reviewed; model equations and mapping tables checked |
| LR-P002 | Project note, *R&D Policy-to-Macro Translation: Methodology note and PNRR direct-research pilot*, v0.1, 20 November 2026 | Project's existing data and model-interface methodology | Full 5-page note reviewed |
| LR-P003 | Roeger, Varga and in 't Veld (2008), *Structural Reforms in the EU: A simulation-based analysis using the QUEST model with endogenous growth*, European Economy Economic Paper 351 | Foundational QUEST endogenous-growth model | Official Commission publication page and bibliographic reference in B3 located; full paper not yet retrieved and read |
| LR-P004 | D'Auria, Pagano, Ratto and Varga (2009), *A comparison of structural reform scenarios across the EU member states*, European Economy Economic Paper 392 | Country-calibrated QUEST application | Official Commission PDF summary reviewed; confirms R&D-promoting tax credits and wage subsidies, but full technical paper not yet reviewed |
| LR-P005 | Varga and in 't Veld (2009), *A model-based analysis of the impact of Cohesion Policy expenditure 2000–06: simulations with the QUEST III endogenous R&D model*, European Economy Economic Paper 387, DOI 10.2765/28883 | QUEST-RD application with public capital, R&D and human capital policy channels | Full official Commission PDF text reviewed |
| LR-P006 | Roeger, Varga and in 't Veld (2009), “Modelling the Lisbon Strategy: Analysing Policies to Promote Knowledge Investment with an Endogenous Growth Model”, *Comparative Economic Studies* 51, 520–539, DOI 10.1057/ces.2009.13 | Related QUEST endogenous-growth policy application | Abstract and accessible full-text excerpt located; publisher full text access appears restricted; technical review pending |
| LR-P007 | Becker (2015; first published online 2014), “Public R&D Policies and Private R&D Investment: A Survey of the Empirical Evidence”, *Journal of Economic Surveys* 29(5), 917–942, DOI 10.1111/joes.12074 | Review of direct subsidies, tax credits, university research, human capital and cooperation | Abstract and review classification inspected; full article review pending |
| LR-P008 | Dimos and Pugh (2016), “The effectiveness of R&D subsidies: A meta-regression analysis of the evaluation literature”, *Research Policy* 45(4), 797–815, DOI 10.1016/j.respol.2016.01.002 | Meta-regression of micro-evaluations | Abstract and main conclusion inspected; full paper review pending |
| LR-P009 | Hall and Van Reenen (2000), “How effective are fiscal incentives for R&D? A review of the evidence”, *Research Policy* 29, 449–469, DOI 10.1016/S0048-7333(99)00085-2 | Foundational review of tax incentives | Abstract and accessible PDF excerpt inspected; full extraction pending |
| LR-P010 | Akcigit, Hanley and Stantcheva (NBER WP 22908; revised 2021), “Optimal Taxation and R&D Policies” | Firm heterogeneity, research productivity, information and spillovers | Abstract and research design inspected; full review pending |

**Corpus gap:** only B3 and the project methodology note were confirmed as directly available R&D-specific files in the search results. The other uploaded files in the current conversation concern continuation/extraction status, not additional macro literature. The inventory must be expanded if further R&D papers are found in Project storage.

## 2. Model architecture: what B3 actually uses

### 2.1 Model family and research production

B3 describes a multi-country New-Keynesian DSGE model based on the European Commission's QUEST-RD model. The model has endogenous innovation and semi-endogenous growth. New designs/patents are produced in a research sector using high-skilled labour and accumulated domestic and foreign knowledge (section 2.1, p. 3; section 2.3.3, pp. 5–6).

Its knowledge-production equation (8), p. 5, has the conceptual form:

\[
\Delta A_t = \upsilon A_{t-1}^{\phi}(A^*_{t-1})^{\psi}(L_t^{RD})^{\lambda}-\delta_A A_{t-1}
\]

The PDF's equation layout should be consulted for exact typesetting, but the paper's prose confirms the roles:
- \(L_t^{RD}\): high-skilled researchers employed in R&D;
- \(A_{t-1}\): accumulated domestic knowledge;
- \(A^*_{t-1}\): accumulated foreign knowledge;
- \(\upsilon\): total-factor efficiency of R&D production;
- \(\phi\) and \(\psi\): domestic and foreign knowledge spillover elasticities;
- \(\lambda\): elasticity of R&D production with respect to researchers;
- \(\delta_A\): knowledge depreciation/obsolescence.

The research institute chooses R&D labour and faces hiring adjustment costs. Its profit equation (10) includes the wage subsidy \(s_t^{RD}\) on high-skilled research labour. The public budget equation (11) records the direct fiscal cost of that subsidy (section 2.3.3 and 2.4, pp. 5–6).

### 2.2 Exact R&D policy mapping in B3

Table 2, p. 8, maps:

| Structural indicator | Mapping | Model counterpart | Timing |
|---|---|---|---|
| R&D subsidy (% GDP) | Direct | \(s_{RD}\) | 5 years |

This is a policy indicator mapped to a model subsidy wedge. It is not a measurement of total R&D expenditure. Section 4.5, p. 12, clarifies that the simulated policy channel is public subsidies on **private R&D**, including wage or tax incentives. The channel reduces the cost of R&D/intangible assets, stimulates research activity and reallocates high-skilled workers towards research.

Footnote 27, p. 12, explicitly cautions that subsidies to public research institutes or universities may have different transmission channels and less crowding-out; it distinguishes business applied research from basic research at universities/public institutes and notes potentially larger long-term spillovers from basic research.

**Conclusion for project mapping:** B3's \(s_{RD}\) is a private-R&D subsidy wedge. It cannot be used as a catch-all for PRIN, university grants, core funding to public research institutes, research infrastructure, doctoral programmes or public venture capital.

### 2.3 Calibration and data implications in B3

B3 reports EU calibration values in section 2.6, p. 7:
- \(\lambda=0.59\);
- \(\phi=0.44\);
- \(\psi=0.54\);
- knowledge obsolescence assumption of 5%.

These are model calibration values, not Italian observations and not coefficients to import automatically into an Italy-specific estimation. The paper's sensitivity section 6, pp. 18–20, varies the difficulty of finding ideas and foreign spillovers. It defines \(\beta_{RD}=1-\phi\) in its alternative representation and compares benchmark, “ideas getting harder to find”, and “additive growth” variants. The baseline and alternative assumptions materially change long-run output effects.

The research labour variable is endogenous in the model. R&D staff data may be needed to calibrate or validate the mechanism, but should not be confused with an exogenous fiscal input.

## 3. A second QUEST-RD policy mapping: Cohesion Policy (Varga and in 't Veld, 2009)

This paper is especially relevant because it explicitly maps broad public programme spending to several supply-side channels rather than using only the private wage-subsidy indicator in B3.

### 3.1 Model and channels

The paper uses a multi-country QUEST III extension with:
- semi-endogenous technological change following Jones (1995);
- endogenous R&D;
- endogenous human-capital accumulation;
- productive public infrastructure capital;
- cross-country trade and knowledge spillovers.

The model is described in section 4, especially:
- public capital in the final-goods production function (section 4.2, pp. 17–18);
- R&D production function (section 4.3, p. 18, equation 20);
- human-capital accumulation (section 4.4, pp. 19–20);
- government budget and subsidies (section 4.5, p. 20).

### 3.2 How public R&D support enters

The non-technical summary (printed pp. iii–iv) and the discussion in section 5.2 (around pp. 31–32) state that “Support to R&D” is defined broadly as spending on research, technological development and innovation (RTDI), including networks and partnerships between businesses and research institutes.

In the model, this programme category is captured through:
- reductions in fixed costs;
- reductions in intangible-capital costs for intermediate-sector firms, which use the output of the R&D sector.

The mechanism lowers barriers for start-ups/new product entry and reallocates high-skilled labour towards R&D. The authors explicitly report an initial negative effect on final-goods production from labour reallocation, followed by stronger productivity/output effects that persist after the programme spending ends.

This is a **broad RTDI policy mapping**, not a Frascati-pure R&D expenditure definition. The paper's programme category should not be copied into the project's strict R&D dataset without a Frascati eligibility assessment.

### 3.3 Separate policy and public-capital channels

The paper also represents:
- infrastructure spending through an exogenous government-investment share shock and productive public capital \(K^G\) in the production function (section 4.2);
- human-resource spending through human-capital accumulation/skill efficiency (section 4.4);
- R&D investment tax credits/depreciation allowances through exogenous fiscal subsidies in the government block (section 4.5).

Thus the model distinguishes R&D/RTDI support, infrastructure and human-capital spending. These channels should not be collapsed into one R&D shock. Public infrastructure investment is not R&D expenditure merely because it supports research capacity; its productivity channel is represented through public capital.

The model's R&D production function (equation 20, p. 18) is:

\[
\Delta A_t = \nu (A^*_{t-1})^{\omega} A_{t-1}^{\phi} L_{A,t}^{\lambda}
\]

where \(L_{A,t}\) is high-skilled R&D labour, \(A\) and \(A^*\) are domestic and foreign knowledge stocks, and \(\nu,\omega,\phi,\lambda\) govern productivity, spillovers and researcher elasticity.

### 3.4 Important caveat

The 2009 paper's RTDI expenditure category is much broader than the Frascati boundary and its model mapping is stylised. It is useful to identify macroeconomic channels, not to classify individual Italian measures as R&D or to infer their R&D expenditure share. The authors also stress that results depend on productive use/absorption of the transfers and should be complemented by project-level microdata (non-technical summary, pp. v–vi).

## 4. What the early QUEST literature implies

The official Commission summary of Roeger, Varga and in 't Veld (2008) describes a micro-founded DSGE model with endogenous growth and policy instruments including taxes, benefits, subsidies and education expenditure. D'Auria et al. (2009) applies the model to Member States and explicitly simulates knowledge-investment policies through tax credits and wage subsidies.

Roeger, Varga and in 't Veld (2009) also consider R&D tax incentives alongside other structural reforms, including entry barriers, service competition and high-skilled immigration. This reinforces that R&D policy can be represented through changes in the user cost of R&D and complementary conditions affecting the supply of research skills and entry/innovation.

The full technical review of the 2008 and 2009 foundational papers remains pending; the statements above are limited to the official Commission descriptions and accessible source material.

## 5. Empirical additionality: first evidence map

The first sources located do not support a universal additionality coefficient.

| Study | Instrument / scope | Main source-reported result | Implication |
|---|---|---|---|
| Hall & Van Reenen (2000) | Fiscal incentives / R&D tax credits; review of OECD evidence | Their review's then-current conclusion was approximately one unit of additional R&D per unit of tax credit | Historical benchmark only; not a universal coefficient for Italy or for grants |
| Becker (2015; online 2014) | Tax credits, direct subsidies, university research, high-skilled human capital, formal R&D cooperation | Review reports a shift in more recent literature towards positive private-R&D stimulation; university research and cooperation also typically increase private R&D | Public research can affect private R&D through spillovers/complementarity, not only through direct subsidies |
| Dimos & Pugh (2016) | Meta-regression of 52 micro-level subsidy evaluations since 2000 | After controls for publication selection and heterogeneity, crowding-out is rejected but substantial additionality is not evidenced; estimates depend on treatment of unobserved firm heterogeneity | Do not apply a positive uniform additionality factor to gross subsidies |
| Dimos et al. (2022) | Comparative meta-regression of R&D tax credits and subsidies | Reports input additionality for both, with estimated induced private R&D of 7.5 cents per dollar for either instrument; effects depend on firm/country heterogeneity and publication bias | The size and robustness of the effect remain contested; retain uncertainty and instrument heterogeneity |
| Akcigit, Hanley & Stantcheva (revised 2021) | Dynamic firm-level model of R&D policy, asymmetric information and technological spillovers | Optimal policy depends on research productivity heterogeneity, complementarity of observed/unobserved inputs, persistence and spillovers | Firm-level heterogeneity and spillovers matter for policy design and calibration |

These estimates are not directly comparable: they use different samples, periods, instruments, outcome definitions, identification strategies and meta-analytic methods. The 2022 result is an estimate from a particular comparative meta-regression, not a plug-in parameter for the Italian data engine.

## 5.1 Firm-level microfoundations: observable investment versus research effort

Akcigit, Hanley and Stantcheva (2021), in the full working-paper version reviewed for this round, provide a complementary firm-level model rather than an aggregate QUEST-type macro model.

Their framework explicitly separates:
- observable R&D investment (r_{t-1}): monetary resources spent on R&D, including scientists/researchers' pay, laboratory equipment, materials and research supplies (section 2.1, pp. 6–7);
- unobservable R&D effort (l_t): organisational/research effort that cannot be directly monitored or verified by government;
- firm research productivity (	heta_t): a heterogeneous, privately observed firm characteristic governing the efficiency with which observable investment and unobservable effort generate innovation.

The paper matches firm-level data to patent data and stresses that observed R&D expenditure is not a sufficient statistic for the full innovation-production process. Its policy design depends on complementarities among observable investment, unobservable effort and firm productivity, as well as the persistence of productivity and inter-firm spillovers (abstract and introduction, pp. 1–4; section 2.1, pp. 6–8).

**Data implication:** for business R&D measures, where firm-level data access permits, preserve at least eligible/actual R&D investment, researcher labour costs and firm/beneficiary characteristics separately. Patents and citations can provide innovation-output measures. Unobservable effort is not a directly extractable fiscal or accounting variable; it belongs to the behavioural model and must not be imputed as observed expenditure.

This reinforces the distinction between:
- public support received;
- observable R&D resources spent by the firm;
- the firm's latent research effort/productivity;
- innovation output (patents/citations);
- additional R&D relative to the counterfactual.

This firm-level structure is not a variable list to transplant wholesale into the macro dataset. It is useful for designing the microdata layer and identifying why a single subsidy amount or expenditure total cannot identify the behavioural response.

## 6. Preliminary model-to-data map for Italy

The evidence suggests maintaining separate **data blocks**, while postponing the decision on how many model shocks are ultimately needed.

| Data block | Candidate annual variables | Role | Initial relevance to PNRR |
|---|---|---|---|
| Business R&D policy support | Direct grants to firms; wage subsidies; R&D tax expenditure; eligible R&D base; tax/user-cost wedge | Fiscal observations and potential exogenous policy inputs (e.g. \(s_{RD}\) or user-cost wedge) | MIMIT business R&D grants, IPCEIs and tax incentives; requires eligible base and firm response evidence |
| Direct public research funding | Grants/operating funding by programme and performer; commitments/payments/accrual; beneficiary expenditure | Fiscal input to public research; not B3's private subsidy wedge | PRIN, FIS/FISA, young researchers, MUR research calls |
| R&D performed | Annual Frascati-eligible expenditure by performing entity, sector (HERD/GOVERD/BERD/PNP), funding source, R&D type and cost category | Realised economic-performance series; potential model input/validation series | Central to PRIN and other direct-research pilots |
| Research labour | R&D personnel/FTE, high-skilled researchers, researcher labour costs by sector | Endogenous mechanism / calibration or validation variable | Young researchers, doctoral programmes, research centres; distinguish training from R&D work |
| Research knowledge/output | Patent flows and stocks, publications or other knowledge measures where appropriate | Endogenous state/output proxy; calibration/validation, not fiscal input | Useful to test knowledge accumulation and spillovers; patent counts are not a substitute for R&D expenditure |
| Research infrastructure | Capital expenditure, asset completion/operational date, public capital stock and subsequent R&D use | Public-capital channel; separate from current R&D | M4C2 I3.1 and related infrastructure; count R&D only when research is performed |
| Human capital | Education/training, doctoral completion, skill composition and researcher supply | Human-capital state/mechanism; distinct from R&D expenditure | M4C1/M4C2 doctoral and skills measures; separate training costs from research activity |

### Minimum extraction requirements (proposed, not yet approved schema change)

For every in-scope measure and year, preserve:
- policy/measure/call IDs, legal basis, programme and funding source;
- financial stage (envelope, appropriation, commitment, payment, accrual, beneficiary expenditure, tax expenditure, equity/loan);
- recipient and actual R&D performer, including consortium members where available;
- performing sector and source of funds separately;
- Frascati activity/type, eligible cost category and evidence for the R&D share;
- current versus capital expenditure;
- annual performance-year allocation, not just payment year;
- nominal value, currency/unit, deflator and 2019-price transformation where applicable;
- source ID, page/table/paragraph, extraction date, original value, transformation and validation status;
- explicit missingness and uncertainty.

For business incentives, additionally collect eligible R&D expenditure, support received/tax relief, firm characteristics and treatment/control identifiers where available. For direct public research, collect grant-level budget and actual expenditure by project year, performer and cost category. For infrastructure, collect asset type, construction/commissioning date, operational status and subsequent R&D use.

## 7. What this means for the PRIN pilot

The project methodology note deliberately starts with PRIN because it is a competitive public research grant and permits a relatively direct grant → project expenditure → research-performing organisation chain. It also correctly insists on annualising multi-year projects and not equating award or payment with performance.

The literature review supports that sequence:
- **Do not map PRIN to \(s_{RD}\)**: B3's \(s_{RD}\) is a wage subsidy for private R&D.
- Measure PRIN as public research funding, preserving authorisations, commitments, payments and project-level expenditure.
- Identify the institution actually performing the research; a MUR-funded university project is generally a HERD candidate, not automatically GOVERD.
- Estimate R&D actually performed by year and Frascati category from project reporting; retain unknowns rather than assuming full grant equals performed R&D.
- Treat additionality separately. For public research, the counterfactual may involve continuation/replacement of existing national funding, projects-in-being, and research activity that would have occurred absent the PNRR award.

The first macro handoff from the PRIN pilot should therefore be a clean annual public-research funding/performance series with provenance, not a fabricated subsidy wedge. A later receiving model may require a fiscal spending shock, a public research input, a knowledge-production input or an empirically estimated additionality series; the correct mapping remains model-dependent.

## 8. Initial decisions and open questions

### Supported conclusions
- B3 has one direct R&D policy mapping in Table 2: R&D subsidy (% GDP) → \(s_{RD}\), with five-year implementation.
- \(s_{RD}\) operates on private research labour cost; it is not total R&D spending or public university funding.
- A different QUEST-RD application maps broad Cohesion RTDI support to fixed-cost and intangible-capital-cost reductions and separately models infrastructure, human capital and R&D tax subsidies.
- Therefore the data engine should preserve multiple distinct policy and performance blocks even if the eventual macro model aggregates some of them.
- Direct public research (PRIN) and private R&D incentives are distinct policy channels and should not be forced into one variable.

### Open questions for the next round
1. Retrieve and review the full Roeger et al. (2008) paper and reconstruct the exact QUEST-RD policy and research blocks.
2. Review the full D'Auria et al. (2009) country-calibration paper and the Roeger et al. (2009) *Modelling the Lisbon Strategy* paper.
3. Compare the 2009 Cohesion-policy RTDI mapping with B3's later \(s_{RD}\) mapping: are these model versions or policy experiments using different exogenous variables, and which are still present in the current QUEST-RD code?
4. Review public research funding models and evidence on university/public-institute research, including whether it enters as government expenditure, research labour, public knowledge production or an external knowledge stock.
5. Complete the review of empirical additionality evidence, prioritising meta-analyses, quasi-experimental tax-credit studies and public-research spillover studies.
6. Determine whether the project's minimum macro interface should include (i) public research funding/performance, (ii) business R&D support/user-cost wedge, and (iii) research labour/knowledge indicators as separate series.
7. Identify Italian data sources and coverage for each series before proposing schema changes.

## 9. Sources and locators

### Project sources
- Pfeiffer, P., Varga, J. and in 't Veld (2024), *Unleashing potential*, especially section 2.1 p. 3; section 2.3.3 and equations (8)–(10), pp. 5–6; section 2.6 p. 7; Table 2 p. 8; section 4.5 and footnote 27 p. 12; section 6 pp. 18–20. Project file: b3 paper.pdf.
- *R&D Policy-to-Macro Translation*, version 0.1, 20 November 2026, sections 1–11. Project file: RD_Policy_to_Macro_Methodology_v0.1.docx.

### External sources
- Roeger, Varga and in 't Veld (2008), European Commission, Economic Paper 351: https://ec.europa.eu/economy_finance/publications/pages/publication_summary13529_en.htm
- D'Auria, Pagano, Ratto and Varga (2009), European Commission, Economic Paper 392: https://publications.jrc.ec.europa.eu/repository/handle/JRC56221 and https://ec.europa.eu/economy_finance/publications/pages/publication16463_en.pdf
- Varga and in 't Veld (2009), European Commission, Economic Paper 387: https://ec.europa.eu/economy_finance/publications/pages/publication16016_en.pdf; DOI: 10.2765/28883
- Roeger, Varga and in 't Veld (2009), *Comparative Economic Studies* 51, 520–539: https://doi.org/10.1057/ces.2009.13
- Becker (2015), *Journal of Economic Surveys* 29(5), 917–942: https://doi.org/10.1111/joes.12074
- Dimos and Pugh (2016), *Research Policy* 45(4), 797–815: https://doi.org/10.1016/j.respol.2016.01.002
- Dimos et al. (2022), *Technovation* 115, 102450: https://doi.org/10.1016/j.technovation.2021.102450
- Hall and Van Reenen (2000), *Research Policy* 29, 449–469: https://doi.org/10.1016/S0048-7333(99)00085-2
- Akcigit, Hanley and Stantcheva, NBER Working Paper 22908 (revised 2021): https://www.nber.org/papers/w22908

---

**Run status:** substantive first round completed for B3, the project methodology note, and the Varga–in 't Veld (2009) Cohesion Policy model. Foundational QUEST-RD and empirical literature reviews remain in progress. No empirical data schema, project estimates or policy-perimeter decisions were changed.
