# [P08] Deliver an immutable reviewed CSV through a restricted folder

## Assignment

Owner role: technical lead and operator. Target: a day-5 sample and a first approved batch around day 8, then repeat on the agreed cadence. Dependencies: P04, P05, P07, and the applicable launch gates, including professional and data-transfer approval.

## Tasks

- [ ] Produce a fixed schema, deterministic selection, content hash, and an aggregate coverage and shortfall manifest.
- [ ] Approve the exact batch and destination membership. A manual secure upload is sufficient.
- [ ] Recheck suppression, verify the remote object and content, and record operator, time, and version.
- [ ] Keep approval, upload verification, acknowledgement, and client acceptance distinct.
- [ ] Inspect the destination after an unknown upload outcome before any retry. Corrections use immutable revisions.

## Acceptance

- [ ] There is no unapproved recipient, public link, or email-attachment fallback.
- [ ] Approved does not mean delivered. Delivered does not mean accepted or billable.
- [ ] The real importer and upload-uncertainty tests pass. A zero or shortfall is explicitly disclosed.

## Done and exclusions

A second review and a restricted manifest are required. No mailbox or Drive API dependency and no automatic charge are included. Sharing a live sample that contains personal information requires the applicable approvals, not merely a completed coding milestone.
