# Claude Code instructions

Read and follow the repository-wide instructions in [AGENTS.md](AGENTS.md). This file adds project-specific guidance for Claude Code.

## Working style

- Start each task by identifying the requested deliverable and inspecting only the relevant files.
- Before changing code, explain briefly which files you expect to modify and why.
- Prefer small, reviewable changes over broad rewrites.
- Do not invent source evidence, financial amounts, legal references or statistical observations.
- Keep the analytical distinction between financial inputs and additional R&D expenditure visible in code, schemas and outputs.
- Ask for clarification only when a missing choice materially blocks safe progress; otherwise document a conservative assumption and flag it.

## Methodological guardrails

- Direct public R&D, private R&D incentives, venture capital and enabling measures must remain separate channels.
- The R&D relevance coefficient and additionality coefficient are distinct.
- Implementation/utilisation, leverage and time profile are separate parameters; do not collapse them into one unexplained multiplier.
- Prevent double counting across PNRR resources, national co-financing, tax expenditure, intermediaries and final beneficiaries.
- Preserve uncertainty and scenario ranges.

## Before finishing

1. Run relevant tests and report the exact command and result.
2. Update the relevant documentation and decision log.
3. Summarise changed files and assumptions.
4. List unresolved data or methodological issues.
5. Do not claim that code or estimates have been validated unless tests or source checks were actually performed.
