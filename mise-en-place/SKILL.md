---
name: mise-en-place
description: Run an evidence-backed preflight before a substantial build or delegated task. Check the ask, governing plan, work record, agents, environment, and budget; hold when a material prerequisite is unresolved.
---

# Mise en Place

Check that the work is ready before starting it. The name comes from preparing a kitchen before cooking.

Use this for substantial or risky work. A simple answer or routine reversible action does not need a full ceremony.

## Six checks

Use [TEMPLATE.md](TEMPLATE.md). Give each check a status and a short evidence reference.

1. **The ask:** State the intended outcome, who needs it, how success will be observed, and when to stop. Resolve ambiguity that could materially change the work.
2. **The plan:** Identify the governing specification or acceptance criteria. Check important claims against the current project. Name what is outside scope. No formal specification is required when a clear small work order is enough.
3. **The work record:** Confirm the correct ticket, task, or local record and its current state. Identify where the result and verification receipt will go. Do not create or update external tracker records without authorization.
4. **People and agents:** Assign clear responsibilities, inputs, outputs, and review ownership. Use only available capabilities. For consequential work, separate implementation from review where practical. Do not invent provider or model availability.
5. **The environment:** Confirm the intended repository, source revision, relevant local changes, dependencies, and preview or runtime provenance. A port answering does not prove which checkout it serves. Check for overlapping work before launching another run. For credentials, inspect only necessary metadata and perform a permitted least-privilege authentication check if the task needs one; never print values or broaden access. Preserve others' work.
6. **The budget:** Set a reasonable time or iteration limit, expected usage or cost when known, and the conditions for changing approach or stopping. Unknown cost is a decision point when spending could be material.

## Status and launch decision

- **PASS:** adequate evidence supports readiness.
- **HOLD:** a required prerequisite is missing, contradicted, or unverified.
- **N/A:** not relevant to this task; give the reason.

Any material HOLD blocks the affected work. Continue independent authorized preparation if useful. Fix the gap or obtain an explicit decision from the responsible person. A risk acceptance must state scope and reason; it cannot override permissions, safety requirements, or required approvals.

Once prerequisites are satisfied, proceed with the authorized task. Do not turn a green checklist into a second unnecessary approval ceremony.

## Close the loop

At completion, record the actual outcome, artifact/version, checks performed, remaining limitations, and any follow-up requiring a decision. Distinguish implementation, verification, publication, and production behavior.

## Limits

This is a procedure, not an automatic gate or a security certification. A PASS needs evidence. Recheck the affected station when the plan, code, runtime, permissions, or budget changes.
