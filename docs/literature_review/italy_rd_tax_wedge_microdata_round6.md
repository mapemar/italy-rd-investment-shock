# Italy R&D tax wedge and microdata access — round 6 addendum

**Run:** LR-2026-11-27-R6

## 1. Italy-specific OECD tax subsidy series confirmed

The OECD Data Explorer exposes the dataset **Implied tax subsidy rates on R&D expenditures**, identifier `DSD_RDTAX@DF_RDSUB`. The OECD metadata defines the implied marginal R&D tax subsidy as (1-BIndex). The measure is a synthetic tax-policy indicator based on headline tax credit and allowance rates; historical estimates are not adjusted for all ceilings and thresholds, and should be treated as an upper-bound measure of central-government marginal generosity rather than an observed fiscal expenditure.

The live OECD Data Explorer result includes Italy, with separate SME/large-firm and profitability dimensions. A large-firm profitable scenario series is shown for 2015–2025; values in the displayed table are:
- 2015: 0.04
- 2016: 0.04
- 2017: 0.09
- 2018: 0.09
- 2019: 0.07
- 2020: 0.11
- 2021: 0.20
- 2022: 0.20
- 2023: 0.09
- 2024: 0.09
- 2025: 0.09

These are the OECD's implied marginal tax subsidy rates for a representative firm under the selected scenario, not the amount of tax relief actually claimed or the effective support received by every Italian company. The displayed SME/large-firm breakdown and loss-making scenario should be separately extracted and validated before use.

The OECD Economic Survey of Italy 2026 also reports that:
- public support to R&D is 0.09% of GDP in Italy, versus 0.23% across OECD economies (survey's cited source: OECD R&D tax expenditure and direct government funding of BERD);
- tax incentives represented 64% of total government R&D support in Italy in 2023, versus 58% on average across OECD countries;
- business R&D tax incentives are predominantly expenditure-based and the Survey specifically discusses Transizione 4.0 and Transizione 5.0;
- the Survey notes that tax incentives tend to support expansion of existing processes/experimental development more than new applied research, which responds better to directed support.

Do not treat the 0.09% GDP aggregate public-support ratio, the 64% composition share, the 0.09 B-index-derived subsidy rate, or tax expenditure as the same statistic. They have different numerators, denominators and meanings.

## 2. Microdata access pathway confirmed

ISTAT's "Per la ricerca (MFR)" programme provides research microdata for some surveys on individuals, households and enterprises. The files are anonymised and subject to confidentiality controls. Access is restricted to a specific research project led by a researcher affiliated with an organisation recognised by Comstat or included in Eurostat's recognised research entities list. Requests are submitted through ISTAT's Contact Centre under "Rilascio di microdati"; project proposal and confidentiality documentation are required. Joint projects require recognition of all participating entities.

This establishes a potential formal route for research microdata, but **does not confirm that the specific ISTAT R&D survey file, tax microdata, RNA/ReGiS beneficiary identifiers or company accounts are jointly linkable or available under one access request**. The project must separately verify the relevant MFR catalogue entries, variables, identifiers, legal basis and linkage conditions. Eurostat European microdata access is also referenced by ISTAT.

## 3. Macro-interface consequences

1. Keep two distinct tax-policy series:
   - the OECD implied marginal tax subsidy rate (or B-index) as the model's policy/user-cost wedge;
   - GTARD as the fiscal-cost series.
2. Keep direct government funding of BERD separate from both tax measures.
3. For PNRR and other grants, construct recipient-level support separately and estimate the causal response of BERD; do not infer that from the national B-index.
4. Add firm size and profitability scenario to the tax-wedge data dimensions. These are important because the marginal incentive differs by firm type and because tax liability/refundability affects take-up.
5. Retain R&D type (basic/applied/experimental) in the microdata and aggregate data where available; the OECD Italy Survey identifies differences in the R&D activity induced by tax versus directed support.

## 4. Scope closure and remaining blockers

The literature-to-variable identification task is now sufficiently complete for a first macro-interface specification: the candidate register has 42 variables, source anchors, roles and data requirements. The next workstream is **data construction and model fitting**, not another open-ended literature search.

The following are explicitly outside the completed variable-identification task and remain dependent on data access/model availability:
- downloading and versioning all historical Eurostat/OECD series;
- verifying every detailed R&D type/cost/source cross-tab and its annual coverage;
- obtaining and validating Italy's GTARD fiscal-cost observations and all B-index scenario dimensions;
- confirming access/linkage for ISTAT R&D microdata and administrative treatment data;
- selecting the receiving macro model and its equations, priors/parameters and estimation strategy;
- estimating instrument-specific additionality and producing the annual PNRR R&D shock.

No macro model has been fitted and no additionality coefficient is recommended in this addendum.
