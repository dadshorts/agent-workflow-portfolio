# Practical AI Workflows

Three reusable workflows for making AI-assisted work easier to review, hand off, and finish.

AI can produce a convincing answer before anyone checks the assumptions. It can also lose the reasons behind a decision when a session ends. These workflows address those everyday problems with independent review, written handoffs, and evidence before execution.

## Start here

| Workflow | What it does | What it demonstrates |
| --- | --- | --- |
| [Megazord](megazord/README.md) | Gets two independent AI reviews and brings them together into one decision record. | Multi-model orchestration, failure handling, and traceable decisions. |
| [Checkpoint](checkpoint/SKILL.md) | Saves the state, decisions, evidence, and next step so a fresh session can continue. | Reliable handoffs and honest reporting of what is verified. |
| [Mise en Place](mise-en-place/SKILL.md) | Checks the goal, plan, work record, people, environment, and budget before a substantial run. | Practical governance and risk-aware delivery. |

**If you have two minutes:** read the [example decision](megazord/examples/synthesis.md), the [example handoff](checkpoint/examples/RESUME.md), and the [preflight that catches a problem](mise-en-place/examples/preflight-hold.md).

## One example, three points in the work

The examples use a fictional equipment-checkout app. Three staff users need a weekly overdue-items report for 120 items, with two development days available. The team is deciding whether a CSV export is enough or whether to build a dashboard.

1. **Before work:** Mise en Place catches that the preview's source checkout is unverified. The run stays on hold until the intended code is verified.
2. **At a design choice:** Megazord compares independent opinions and records the decision, remaining disagreement, and next action.
3. **At a handoff:** Checkpoint preserves the decision to build the CSV export, the tests already completed, and the precise first step for the next session.

The example records are deliberately synthetic. They are not customer data, production evidence, or results from a live model run.

## What is implemented

- **Megazord:** a Python command-line runner, offline demonstration, and automated tests. Live use requires compatible, separately installed and authenticated provider CLIs.
- **Checkpoint and Mise en Place:** portable instruction files, templates, and worked examples. Their checks depend on the person or agent following them; they are not automated enforcement systems.

The [verification record](docs/VERIFICATION.md) separates tested behavior from remaining limits. The [design notes](docs/DESIGN.md) explain the choices and tradeoffs.

## Use the workflows

Start with each workflow's README or SKILL.md. Checkpoint and Mise en Place can be used as written procedures, or installed in an agent tool that supports SKILL.md files. Confirm that tool's current installation instructions rather than copying them into every runtime.

For Megazord, follow its [setup and demo instructions](megazord/README.md). The offline demo does not require an account or make provider requests. Review the data-sharing and command-execution limits before enabling live calls.

## Boundaries

These workflows support human judgment. Two models can share the same mistake, a saved handoff can become stale, and a checklist can be filled in without real evidence. Keep source references, verify material claims, and retain human control over publishing, permissions, spending, and other consequential actions.

See [provenance and licensing](docs/PROVENANCE.md) before redistribution. Only reusable workflow material and synthetic examples are included. Review any real inputs or outputs separately before sharing.
