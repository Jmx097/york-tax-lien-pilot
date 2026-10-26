# Client charter

## Product and scope

Produce a weekly reviewed CSV of unique taxpayer leads associated with recent recorded federal tax lien notices of at least USD 10,000 in Dallas, Collin, Denton and Bexar, Texas. A lead is researched public-record information, not taxpayer interest, consent, a consultation or a sales-qualified opportunity. Recorded amount is not current payoff balance.

| Dimension | Three-week baseline | Required decision |
|---|---|---|
| Geography | All four counties; no fixed county allocation | Accept coverage method or explicit written scope amendment |
| Lead unit | Unique taxpayer/prospect, not filing | Identity, joint-party and overlap rules |
| Amount | At least USD 10,000 recorded notice amount | Any additional restrictions require approval |
| Target | 50 unique reviewable taxpayers/week, conditional | Shortfall reporting and selection/cap policy |
| Recency/contact | Unset | Written age window and exact required fields |
| Delivery | One weekly CSV in approved restricted folder | Weekday, cutoff, timezone, permissions and import acceptance |
| Tracking | Restricted shared acceptance/activity/receipt log | Owners, statuses, evidence and reconciliation cadence |
| Build | Three-week planning allowance, not guaranteed launch | Executed start, staffing and working calendar |
| Spending | No new purchases authorized | Internal capacity, vendor/document and storage caps |

The earlier Monday, 30-day recency, rolling-average and mailbox-API defaults are withdrawn. Neither an assumed USD 10/month ceiling nor a 2–4 hour optional integration estimate is a validated budget or estimate for the whole build.

## Ownership

| Accountable role | Responsibility |
|---|---|
| Product owner / Jonathan | Capacity, prioritization, restricted decision register and escalation |
| Firm approver / Christopher | Accepted business scope, contact expectations and launch acceptance |
| Firm coordinator / Giovanni | Delivery review, campaign tag, weekly status and receipt updates |
| Technical lead | State, qualification, contracts and recovery implementation |
| Source engineer | Independent county access evidence and adapters |
| Reviewer/operator | Row verification, suppressions, approved upload and runbook execution |
| Operations owner | Host isolation, access control, alerts and restore drill |
| Qualified professional/tax reviewers | Resolve regulated compensation and applicable tax treatment |

Roles are planning assignments, not named engineering commitments or automatic GitHub assignees. Two focused technical contributors plus daily review capacity is an assumption. One engineer requires a smaller explicitly agreed scope; one county is not silently substituted for four.

## Acceptance gates

Use [G01–G12](10-decisions-and-launch-gates.md). Applicable gates must be approved before activation; all begin pending. Internal sanctioned discovery may proceed only within its own approved access/data boundaries. Live transfer, spending and billing have separate approvals.

Every pilot row requires human review, exact amount evidence, required approved contact fields, conservative identity linkage, status review, prior-delivery exclusion and suppression checks. Known unsupported rows remain held irrespective of aggregate parser accuracy. Observe actual sample size and per-county gaps; no fabricated accuracy or capacity guarantees.

## Non-goals and shortfalls

No automated outreach, taxpayer representation, enrichment purchase, new sending infrastructure, API integration, CRM migration, dashboard, conversion guarantee or expanded geography. Optional later work needs a separate written scope and cost approval. The firm owns outreach, suitability and professional verification.

Deliver actual approved counts and explain source gaps, restrictions, processing failures or genuine supply. Never fill targets with duplicates, releases, stale backlog or uncertain amounts. Missing county access means escalation and an approved change or pause, not a claim of complete fulfillment.

## Handoff

A named operator and backup must demonstrate review, delivery, suppression, restart and restore using the restricted runbook. Client import and field acceptance must be documented. One successful demonstration does not establish recurring volume or conversion outcomes. No minimum setup recovery or financial return is assumed; private commercial terms remain outside this repository.
