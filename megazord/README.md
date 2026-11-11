# Megazord: two reviews, one decision

A small Python workflow for comparing independent Grok and Codex opinions before asking Grok to synthesize the evidence. It turns a vague second-opinion request into inspectable review files and a status that does not hide failed stages.

**Engineering highlights:** parallel independent reviews; separate synthesis; a recursion brake; atomic singleton lock; per-stage failure reporting; no automatic installation; configurable models; standard-library tests with no model calls.

## Try it without accounts

Requires Python 3.10+. From this folder:

```sh
python -B scripts/megazord.py --demo
python -B -m unittest discover -s tests -v
```

The demo replays `examples/` fixtures about an equipment-checkout app choosing a CSV export or reporting dashboard. Every response is authored synthetic data. It does not call an installed CLI, authenticate, or evaluate a model. A successful demo verifies orchestration and artifact creation, not live integration quality.

## Live setup

Install and authenticate Grok CLI and Codex CLI yourself using their official instructions. Review their data handling, current flags, local configuration, and billing before use. This package neither installs software nor promises a particular payment method or cost.

```sh
python -B scripts/megazord.py --prompt-file problem.txt --grok-cli /path/to/grok --codex-cli /path/to/codex
```

CLI names on PATH also work. Windows users must select native executables, not .cmd/.bat/.ps1 launchers. No shell launcher or npx fallback is provided. Optional `--grok-model` and `--codex-model` select models supported by your installations; otherwise their configured defaults apply. `--timeout 180` bounds each model subprocess, not the entire run.

Help-output checks reject missing required flags before model requests. They do not prove compatible semantics. The Grok adapter expects one JSON object with a nonempty `text` string. Codex must write `--output-last-message`. Live CLI compatibility and authentication have not been tested for this cleaned package.

## What you get

`megazord-runs/<UTC timestamp>-<random id>/` contains:

- `00-problem.txt`: supplied problem.
- `grok.md`, `codex.md`: independent reviews or explicit failure notices.
- `synthesis.md`: decision, agreement, conflict, one next action and risks.
- `meta.json`: mode, overall status and stage outcomes.
- Live runs also retain each stage's prompt or last-message file in its own subfolder.

The prompt and outputs may contain sensitive information. Choose an appropriate local output directory, inspect artifacts before sharing, and do not commit generated runs. Raw CLI diagnostics and session identifiers are not saved by this runner. Model text is untrusted and is not automatically redacted.

| Status | Meaning | Exit |
| --- | --- | --- |
| complete | Both reviews and synthesis succeeded | 0 |
| partial | At least one review succeeded, but not every stage did | 1 |
| failed | Both reviews failed; synthesis skipped | 1 |
| blocked | Setup, file, lock or CLI-contract failure | 2 |
| blocked | Recursive invocation refused | 3 |

## Boundaries and tradeoffs

- Two providers receive the same problem without seeing each other's review. Synthesis uses Grok, so it is not an independent third vote or a guarantee against shared errors.
- Codex is invoked read-only. Grok receives a tool deny list, no-memory/no-subagent flags and text-only instructions. These restrictions, a clean stage working directory and the recursion variable are **not a complete security boundary**. Installed CLI configuration, global instructions, plugins and account stores may still be accessible. Use a separately isolated OS/container environment for untrusted or sensitive work.
- Child environments forward only a small operating-system variable allowlist. API keys and arbitrary inherited variables are not forwarded; existing CLI account/configuration stores remain available. Environment-only authentication may therefore fail.
- Locks are scoped to the chosen output root. A crash can leave `.megazord.lock`; inspect for active runs before manually removing it. Different output roots are not mutually locked. The recursion brake is inherited-process protection, not tamper resistance.
- Python kills the immediate subprocess on timeout; descendant processes may survive. Inspect before retrying. Output is buffered in memory, so use bounded prompts and trusted CLI installations.
- No code is applied and no publication is performed. Human review remains required.
- Local verification is Windows/Python 3.13.7 unit tests and synthetic demo only. Paths use pathlib and no platform-specific install paths, but macOS/Linux runtime support is not verified.

## Provenance

Adapted from the owner's existing local Megazord Python runner and skill instructions. The design retained parallel Grok/Codex reviews, synthesis, recursion protection, locking and review artifacts. This cleanup replaced machine-specific paths, fixed model names, auto-install fallback, permissive execution modes and ambiguous success reporting. The supplied source directories contained no license or attribution file; authorship and redistribution rights still require owner review before publication. No license is assigned here.
