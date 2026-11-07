# Client charter

## Product and scope

Validate, then possibly produce, a reviewed CSV of unique eligible taxpayers associated with recorded IRS federal tax lien notices of at least USD 10,000 in the agreed New Jersey and Connecticut territory. A row is researched public-record information, not taxpayer interest, consent, a consultation or a sales-qualified opportunity. Recorded amount is not current payoff balance, and a source label of Active does not prove currently enforceable unpaid debt.

This client project is separate from Plinko's own B2B acquisition work and other clients. Taxpayer information never enters general acquisition lists, company-wide agent memory, public demos or unrelated CRM records.

| Dimension | Validation baseline | Required decision |
|---|---|---|
| Geography | NJ and CT only: CT statewide state lien sources and Bergen County, NJ; Essex optional and inactive | Agreed geographic rule; recording county is not automatically taxpayer residence |
| Counted unit | Unique eligible taxpayer, not a filing document or party-index row | Identity, joint-party and cross-filing rules |
| Amount | At least USD 10,000 with exact cents preserved; unknown amount is HOLD | Any additional restrictions require approval |
| Target | 50 unique eligible taxpayers/week, conditional | Lower target if supply cannot support it; shortfall reporting |
| Recency/contact | Unset | Written recency window and required-field checklist |
| Delivery | Local CSV draft and manifest only during validation | Restricted folder, recipients and import acceptance before any transfer |
| Tracking | Referral and collections log designed, not active | Owners, statuses and reconciliation cadence |
| Build | Bounded internal build/validation envelope, values held privately | Recommendation: GO TO AGREEMENT, NARROW SCOPE, NO-GO or NEEDS OWNER INPUT |
| Spending | No purchases, paid tooling or vendor sessions authorized | Explicit owner approval with a bounded cost ceiling |

Earlier four-county Texas scope, three-week agreed delivery framing, Monday/30-day defaults, rolling-average and mailbox-API assumptions are withdrawn.

## Ownership

| Accountable role | Responsibility |
|---|---|
| Product owner | Capacity, prioritization, restricted decision register, escalation and the final recommendation |
| Firm principal | Accepted business scope, contact expectations and launch acceptance |
| Firm operations contact | Delivery review, weekly status and receipt updates on the firm's behalf |
| Technical lead | State, qualification, contracts and recovery, adapted from the existing engine |
| Source engineer | Permitted NJ/CT access evidence and adapters |
| Reviewer/operator | Row verification, suppressions, approved upload and runbook execution |
| Qualified professional/tax reviewers | Resolve regulated compensation and applicable tax treatment |

The product owner is a solo founder who also handles fulfilment, so several roles may be held by one person. Roles are planning assignments, not engineering commitments. Ongoing fulfilment must fit a small, measured weekly founder-hour budget; parser runtime is not founder review time.

## Acceptance gates

Use [G01–G12](10-decisions-and-launch-gates.md). All begin pending. Internal sanctioned discovery may proceed only within its own approved access and data boundaries. Live transfer, spending and billing have separate approvals.

Every row requires human review, a supported initial IRS lien type, exact amount evidence, confirmed identity, the agreed geographic rule, conservative taxpayer matching, related-filing and release checks with stated coverage limits, prior-delivery exclusion and suppression checks. Machine eligibility is not the firm's written referral acceptance or a billing event.

## Non-goals and shortfalls

No autonomous taxpayer outreach, taxpayer representation, enrichment purchase, sending infrastructure, new CRM, dashboard, portal, conversion guarantee or geography beyond NJ/CT. Phone and email availability is not assumed or guaranteed. Optional later work needs a separate written scope and cost approval.

Report actual counts and explain source gaps, restrictions, processing failures or genuine supply. Never fill targets with duplicates, releases, stale backlog, Essex records of unverified origin or uncertain amounts. One viable state means NARROW SCOPE, not a claim of full coverage.

## Handoff

If the decision is to proceed, a named operator and backup must demonstrate review, delivery, suppression, restart and restore using the restricted runbook, with measured human effort. One successful demonstration does not establish recurring volume or conversion outcomes. Private commercial terms remain outside this repository.
