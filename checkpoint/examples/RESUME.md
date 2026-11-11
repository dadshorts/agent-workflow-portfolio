# Resume: equipment inventory CSV export

**Synthetic example.** All names, revisions, results, and dates below are invented to demonstrate the format. This is not a test receipt.

Updated: 2026-01-15T16:30:00Z
Revision: example-a1

## Mission
Let staff export the overdue inventory rows as a weekly CSV report, without adding a reporting dashboard.

## State
- Verified firsthand within this fictional scenario: the CSV formatter handles commas, quotes, and empty fields. The example unit-test report is 8 passed, 0 failed on example-a1.
- Reported, not independently verified: none.
- In progress: no background work is running.
- Not started: browser verification of the downloaded filename and row order.
- Blocked: the preview's checkout has not yet been verified.

## Next action
Confirm that the preview serves revision example-a1 from this project. If it matches, test the download using the synthetic fixture. If it does not, stop the browser test and identify the correct authorized preview; do not change another running server.

## Anchors
These paths belong to the fictional application, not this workflow package.
- `src/export_csv.py`: CSV formatting implementation.
- `tests/fixtures/inventory.csv`: invented equipment records for testing.
- `docs/export-decision.md`: why CSV was selected over a dashboard.

## Decisions and corrections
- Build the CSV export first. After the fictional sample-layout review, staff accepted a spreadsheet report. The two-day scope is a weekly overdue-items CSV, without a dashboard.
- Preserve the visible row order. Do not silently add sorting or analytics.
- Correction: “the export is complete” was premature. Unit checks do not establish browser download behavior.

## Constraints and authority
- Local implementation and testing are approved in this fictional scenario.
- No deployment, publication, new paid service, or production-data access is approved.
- Use the synthetic fixture only. Do not include real borrower contact details.

## Open questions and known dead ends
- Which checkout does the preview serve? This blocks browser verification.
- A full dashboard was considered and deferred because it exceeds the confirmed need. Revisit only if new requirements justify it.
