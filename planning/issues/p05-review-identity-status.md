# [P05] Implement row review, identity, and status safeguards

## Assignment

Owner role: technical lead and reviewer. Stage: 2, offline MVP. Dependencies: the P03 data model and P02 field evidence.

## Tasks

- [ ] Implement auditable hold, approve, reject, and correct decisions with reviewer, time, reason, and evidence.
- [ ] Conservatively link recordings, notices and taxpayers across filings and sources; the counted unit is a unique eligible taxpayer. Hold ambiguous and joint-party matches.
- [ ] Reconcile releases, withdrawals, partial scopes, and refiles without treating every event as debt paid.
- [ ] Preserve exact amounts with cents and apply the minimum, the NJ/CT geographic rule (recording county is not residence) and approved recency, contact and entity rules before deterministic ordering.

## Acceptance

- [ ] Every included pilot row is reviewed. Missing, conflicting, or redacted amounts stay held.
- [ ] A cross-filing duplicate is not counted as a new taxpayer. Same-name uncertainty cannot auto-merge. An Active label alone is not treated as enforceable debt.
- [ ] A material unmatched status event remains held. Actual correction rate and sample limits are disclosed.

## Done and exclusions

Real permitted evidence stays restricted. Tests and a second reviewer are required. Do not invent a current debt, sum overlapping notices, rank by inferred wealth, or add a conversion model. Aggregate accuracy never authorizes a known bad row.
