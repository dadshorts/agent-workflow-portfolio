# Preflight: equipment inventory CSV export

**Synthetic example.** This fictional record demonstrates a blocked launch. It does not describe a real system or test run.

Date/time: 2026-01-15T16:35:00Z
Target: equipment-checkout project, revision example-a1

| Check | Status | Evidence or gap |
| --- | --- | --- |
| Ask | PASS | Export the overdue inventory rows as a weekly CSV report. A correct file must preserve field values and row order. |
| Plan | PASS | The fictional export decision specifies CSV only, with browser filename and ordering checks still outstanding. No dashboard. |
| Work record | PASS | The fictional local task record names the next browser checks and the destination for their receipt. |
| People and agents | PASS | An implementer prepared the formatter. A separate reviewer will check the browser result against the fixture. |
| Environment | HOLD | A preview responds, but its source checkout and revision have not been established. A responding port alone is insufficient. |
| Budget | PASS | Twenty minutes for verification, one repair pass, no paid services or live model calls. Stop on an environment mismatch. |

Decision: HOLD browser verification. Reviewing the synthetic expected output can continue.

Next action: identify the preview's source checkout and revision using read-only evidence. If it is not example-a1, do not touch that server; find or request the correct authorized preview.

Authority: local testing only in this fictional scenario. No deployment, production-data access, permission change, or publication is approved.

Recheck if: the checkout, source revision, preview, acceptance criteria, or reviewer changes.
