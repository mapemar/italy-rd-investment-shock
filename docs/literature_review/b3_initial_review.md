# Initial literature review note — B3 (Pfeiffer, Varga and in 't Veld, 2024)

**Review status:** preliminary, source-grounded first pass  
**Source:** \`b3 paper.pdf\`, 22-page article  
**Citation:** Pfeiffer, P., Varga, J. and in 't Veld, J. (2024), “Unleashing potential: Model-based reform benchmarking for EU Member States”, *European Journal of Political Economy*, 83, 102535. DOI: 10.1016/j.ejpoleco.2024.102535.

This note records what the paper actually specifies. It is not yet a general literature conclusion.

## 1. Model architecture

The paper uses a multi-country macro model based on the European Commission's QUEST-RD model (section 2.1, p. 3). Its core contains optimising households and firms, monetary and fiscal policy, monopolistic competition, and real and nominal rigidities. The supply side includes endogenous innovation and semi-endogenous growth.

The model's R&D mechanism is not simply an exogenous R&D expenditure series:
- new patents/technologies are produced in research labs;
- research uses high-skilled labour;
- R&D production depends on accumulated domestic and foreign knowledge;
- R&D affects aggregate productivity and the creation of new product lines;
- research effort competes with production for high-skilled labour.

The paper describes the research institute as profit-maximising and employing high-skilled labour at the market wage. It can receive a wage subsidy denoted \(s^{RD}_t\) (section 2.3, pp. 4–5; equations 9–10). The fiscal debt equation also records the direct budgetary cost of the subsidy (section 2.4, p. 5, equation 11).

## 2. Exact policy input identified in the paper

Table 2 (p. 8), “Mapping of structural indicators into model variables”, maps:

| Structural indicator | Mapping type | Model variable | Implementation horizon |
|---|---|---|---|
| R&D subsidy (% GDP) | Direct | \(s_{RD}\) | 5 years |

The variable is a direct exogenous policy entry point in the paper's reform-benchmarking exercise. It is not a complete list of all variables governing R&D in the model.

Section 4.5 (p. 12) states that the model features public subsidies on private R&D, including wage or tax incentives. These reduce the cost of intangible assets/R&D and stimulate private R&D activity. The channel operates through patent creation and reallocation of high-skilled labour towards research.

**Interpretation:** \(s_{RD}\) is a policy subsidy wedge/input, expressed in the paper's benchmarking table as a percentage of GDP. It should not be interpreted as:
- total public R&D expenditure;
- total GERD;
- the value of public grants to universities or public research institutes;
- the amount of R&D actually performed;
- the net additional R&D induced by a policy.

The paper's five-year horizon is the implementation assumption in Table 2; it is not evidence that all effects disappear or are complete after five years.

## 3. Important boundary: private versus public research

Footnote 27 (p. 12) explicitly states that subsidies to public research institutes or universities could have different transmission channels and less crowding-out (citing Akcigit et al., 2021). The authors distinguish business-financed R&D, which they associate more with applied research, from basic research at public institutes and universities, which may be too costly or less profitable for private firms. They also note that long-term spillovers from basic research across firms and countries could be larger.

This is a strong reason not to use \(s_{RD}\) as a catch-all input for all PNRR/MUR/MIMIT measures. The paper itself flags the boundary but does not develop a separate public-research subsidy variable in its reform-benchmarking table.

## 4. R&D model mechanisms and parameters to extract from the paper

The paper's model discussion (section 2.3, pp. 4–5) identifies mechanisms/parameters including:

| Concept | Paper notation / description | Role in the model | Extraction implication |
|---|---|---|---|
| R&D subsidy | \(s^{RD}_t\) | Exogenous policy input; wage subsidy to research labour | Candidate policy input, but only for the private-R&D subsidy channel represented |
| High-skilled R&D labour | \(L^{RD}_t\) | Research input / endogenous choice | Not a fiscal series; may require R&D personnel or labour-cost evidence for calibration/validation |
| Domestic knowledge stock | \(A_{t-1}\) | Endogenous state inherited from prior innovation | Not directly an annual budget measure |
| Foreign knowledge stock | \(A^*_{t-1}\) | External knowledge stock / spillover source | Requires a model-specific foreign knowledge proxy if the model is to be replicated |
| R&D productivity | \(\upsilon\) | Efficiency of knowledge production | Calibration parameter |
| Domestic knowledge spillover | \(\phi\) | Elasticity associated with accumulated domestic knowledge | Calibration parameter |
| Foreign knowledge spillover | \(\psi\) | Elasticity associated with accumulated foreign knowledge | Calibration parameter |
| Research-lab hiring costs | \(\gamma^{LRD}\) | Adjustment/hiring cost parameter | Calibration parameter |
| Research-lab labour elasticity | \(\lambda\) | Elasticity of R&D production with respect to researchers | Calibration parameter |
| Knowledge depreciation | \(\delta_A\) | Depreciation/obsolescence of knowledge | Calibration parameter |
| Difficulty of finding ideas | \(\beta_{RD}\) | Parameter affecting R&D productivity / idea production | Calibration parameter |

Notation should be checked against the equations and Appendix A before being copied into a machine-readable variable dictionary. This table is a conceptual inventory, not an approved project schema.

## 5. What the paper does not give us

The paper does not provide a separate exogenous policy input for each of the following:
- direct grants to universities;
- core public research funding to government institutes;
- public competitive research grants such as PRIN;
- research infrastructure capital expenditure;
- doctoral funding or public research personnel programmes;
- public venture-capital funds or technology-transfer instruments.

It therefore does not establish that these measures should be added to \(s_{RD}\). Their model representation must be found in other papers/model versions or developed as a distinct extension.

The paper also cautions (p. 2) that stylised reform benchmarking is not directly applicable to concrete country measures without mapping the depth and scope of those measures into model variables.

## 6. Comparison with the project's current methodology

The project's \`RD_Policy_to_Macro_Methodology_v0.1.docx\` already distinguishes:
1. policy layer;
2. fiscal layer;
3. economic-performance layer;
4. macroeconomic/causal layer.

It also proposes separate annual PRIN series:
- \`PRIN_AUTHORISED_t\`;
- \`PRIN_COMMITTED_t\`;
- \`PRIN_PAID_t\`;
- \`PRIN_RD_PERFORMED_t\`;
- \`PRIN_HERD_t\`, \`PRIN_GOVERD_t\`, \`PRIN_BERD_t\);
- \`PRIN_ADDITIONAL_RD_t\`, only if a counterfactual estimate is available.

These are useful project-level evidence and handoff series. They are not all variables explicitly used by B3. In particular, the PRIN series may be needed to measure direct public research support and realised research activity, but the B3 \(s_{RD}\) channel represents subsidies to private R&D.

## 7. Preliminary model-to-data implications

Do not yet consolidate all measures into one R&D input. Maintain at least three distinct candidate data blocks while the literature is reviewed:

1. **Business R&D policy support:** annual public subsidy/tax support to business R&D, with instrument type and eligible R&D base. This is the closest current mapping to B3's \(s_{RD}\), subject to exact model definition and denominator.
2. **Direct public research funding and performance:** annual funding and actual R&D performed by universities and public research institutes, split by performing sector (HERD/GOVERD) and by current/capital expenditure. B3 flags this as a different channel but does not specify the input.
3. **Research capacity and enabling investment:** infrastructure, research personnel, doctoral capacity, technology transfer and financial instruments. Keep separate until the literature establishes whether they are direct model inputs, intermediate mechanisms or broader innovation indicators.

For each block, preserve both fiscal inputs and realised R&D performance where available. Additionality remains a separate estimate, not a synonym for the model's subsidy variable.

## 8. Questions for the next literature-review round

1. In the original QUEST-RD model (Roeger et al., 2008/2009), what is the precise definition and calibration of the R&D subsidy wedge? Is it an ad valorem wage subsidy, a broader subsidy rate or another cost wedge?
2. Does the model distinguish private and public research in its production/knowledge accumulation block, or is public research outside the model?
3. Which model variants introduce public R&D, government research capital, public knowledge production or basic research?
4. How should direct public research grants be mapped: as government expenditure, as a subsidy to the research-performing institution, as public R&D capital, or as an exogenous increase in research resources?
5. Which inputs are necessary for the model run, and which are only needed to estimate/calibrate the behavioural response?
6. Can R&D tax credits, direct grants, wage subsidies and public procurement be aggregated into a common subsidy wedge without losing important differences?
7. What is the appropriate timing convention: policy announcement, legal authorisation, cash payment, accrual expenditure or year of R&D performance?
8. Which empirical evidence can estimate additionality/crowding-out for each instrument, and how should uncertainty be carried into the macro scenarios?

## 9. Source locators

- Pfeiffer, Varga and in 't Veld (2024): model overview, section 2.1, p. 3.
- R&D knowledge-production mechanism and model parameters, section 2.3, pp. 4–5.
- Research-lab wage subsidy and fiscal cost, equations 9–11, pp. 5–6.
- Structural indicator to model-variable mapping, Table 2, p. 8.
- R&D policy transmission, section 4.5, p. 12.
- Public research caveat, footnote 27, p. 12.
- Knowledge depreciation and sensitivity to R&D productivity/spillovers, section 6.1, pp. 18–19.

**Review conclusion:** B3 supports one clear direct policy input for subsidised private R&D, \(s_{RD}\). It does not justify collapsing all public research, PNRR grants, tax incentives, infrastructure and innovation finance into that single variable. The next step is to review the underlying QUEST-RD model and literature on public research funding, then decide which separate inputs are genuinely required by the chosen macro model.
