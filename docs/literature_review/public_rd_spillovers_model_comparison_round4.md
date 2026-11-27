# Public research, spillovers and model-family comparison — round 4

**Run:** LR-2026-11-27-R4  
**New anchor:** Di Comite and Kancs (2015), JRC Technical Report EUR 27080 EN, *Macro-Economic Models for R&D and Innovation Policies: A Comparison of QUEST, RHOMOLO, GEM-E3 and NEMESIS*; Soete, Verspagen and Ziesemer (2022), *Economic impact of public R&D: an international perspective*; Dyèvre (2024), *Public R&D Spillovers and Productivity Growth* (ECB Forum paper).

## 1. The most useful finding: model choice changes the required variables

Di Comite and Kancs compare four models used by the Commission for ex-ante R&D policy assessment:

- **QUEST:** fully dynamic DSGE with intertemporal optimisation, explicit research industry, high-skilled R&D labour, patent/intangible assets, domestic and foreign knowledge spillovers, tax/subsidy instruments and adjustment paths.
- **RHOMOLO:** recursive spatial CGE with regional economies and geographical knowledge spillovers; R&D is a national sector selling R&D services to firms and using high-skilled labour. It has a spatial advantage, but in the reviewed version does not distinguish public and private R&D.
- **GEM-E3:** CGE with detailed sectoral/energy/environmental structure; R&D services and knowledge stocks can be linked to sector-specific learning-by-searching and learning-by-doing. Useful if the policy question is green/energy technology and sectoral reallocation.
- **NEMESIS:** macro-econometric, sectorally detailed model with richer econometrically estimated innovation elasticities and distinct process/product innovation channels; less fully micro-founded and with adaptive rather than forward-looking expectations in the reviewed version.

The report's key warning is that the reviewed versions of QUEST, RHOMOLO and GEM-E3 do not endogenously model the interaction between public and private R&D investments. NEMESIS distinguishes their impacts more explicitly. The report recommends improving empirical and country/sector specificity of R&D elasticities, accounting for non-linearities and heterogeneity.

**Implication:** our data interface must retain separate public and private R&D series and their interaction, even if the receiving model ultimately aggregates them. Do not pre-aggregate public and private R&D into one knowledge input.

## 2. Public R&D and private R&D may be complements

Soete, Verspagen and Ziesemer (2022) estimate country-specific VECMs for 17 OECD economies over 1975–2014. Their candidate endogenous vector includes:
- TFP;
- GDP;
- domestic public R&D capital stock;
- domestic private R&D capital stock;
- foreign public R&D capital stock;
- foreign private R&D capital stock.

They find a positive effect of public R&D on TFP growth in most, but not all, countries and strong dynamic complementarity between public and private R&D stocks in several countries. The productivity effect of public R&D is stronger where public investment induces additional private R&D.

Their cross-country discriminant analysis associates stronger public-private complementarity with:
- lower foreign funding share of business R&D (combined with high BERD intensity);
- higher basic-research share in BERD;
- higher public R&D intensity.

These are empirical associations, not universal causal rules. They nevertheless justify retaining source-of-funds and R&D-type composition, not only total expenditure.

## 3. Public-to-private spillovers: exposure and absorptive capacity

Dyèvre (2024 working paper, ECB Forum) combines US firm-level patents and balance-sheet information (1950–2020) and uses historical shift-share and patent-examiner-leniency IV strategies. The paper reports that public R&D spillovers raise firm productivity and innovative effort, with heterogeneous effects and stronger gains for smaller firms. It measures firms' exposure to public R&D through technological overlap between public agencies' and firms' patent classes.

This suggests a useful *satellite* exposure measure for micro-level work:
- public research knowledge exposure by technology/industry;
- geographic proximity to universities/research organisations;
- firm absorptive capacity (own R&D, skilled researchers and prior knowledge base);
- patent-to-scientific-publication links or cross-field patent citations.

Do not add these as mandatory national aggregate inputs if the receiving macro model does not model them. They are primarily useful for identifying and estimating spillover channels.

Salter and Martin (2001) review econometric, survey and case-study evidence on publicly funded basic research. They identify multiple routes to economic benefit and localisation effects, and conclude that no single simple model captures all benefits. This reinforces the need to keep basic research, applied research and experimental development separate where data permit.

## 4. Additional variables justified by this literature

The 34-variable core register should be supplemented with the following optional variables:

1. **Public-private R&D interaction/complementarity:** interaction term or jointly modelled public/private R&D stocks; estimated, not observed as a standalone series.
2. **Basic research share in BERD and public R&D:** composition of R&D by Frascati type, relevant to complementarity and knowledge spillovers.
3. **Foreign funding share of BERD:** business R&D financed from abroad divided by BERD; helps describe domestic capture and internationalisation.
4. **Sectoral R&D intensity and sector-specific R&D stocks:** useful for NEMESIS/CGE or panel estimation and for non-linear returns.
5. **Absorptive capacity:** firm/sector own R&D, researcher FTE and skill base; not a generic exogenous policy variable.
6. **Public research exposure:** technology-field and geographic exposure to public research, built from patent-class overlap, co-publication/co-patenting or distance; micro/satellite only.
7. **High-tech trade and FDI exposure:** possible international knowledge transmission/control variables in production-function or VECM models, not part of domestic R&D expenditure.

## 5. Updated model-fitting decision logic

- If the objective is **dynamic macro transmission of a time-profiled PNRR shock**, QUEST/DSGE is a natural structural candidate, provided the actual model equations and calibration interface can be obtained.
- If the objective is **regional allocation and spatial knowledge spillovers**, RHOMOLO-type structures require NUTS2 performer, funding, labour and exposure data.
- If the objective is **green/energy technology and sectoral effects**, GEM-E3-type structures need R&D/innovation inputs by sector and learning-by-doing/searching indicators.
- If the objective is **empirical sectoral innovation elasticities and fit to observed data**, NEMESIS-type macro-econometric approaches require sector-level R&D, innovation outputs, productivity and policy variables.
- If the objective is a **reduced-form country time-series analysis**, the Soete et al. six-variable VECM is a candidate benchmark, but an Italian annual sample must be tested for length, integration, breaks and stability before any fit. Do not fit a six-variable unrestricted VAR/BVAR to a short 2015–2024 panel.

## 6. Additional open tasks

- Audit the Italian historical series and identify which dimensions are actually available, by sector and year, including pre-2015 coverage.
- Check whether ISTAT/OECD/Eurostat provide consistent annual breakdowns by source of funds, R&D type, costs and personnel.
- Determine the feasibility of firm-level matching between public support, R&D surveys, patents and company accounts, including legal/access constraints.
- Continue the public research literature review with Italian institutional and sectoral evidence.
