# Client charter

## Product objective

Deliver a source-backed, deduplicated weekly CSV of qualified federal tax lien prospects to Christopher York using the already-paid Droplet and a proposed $10/month incremental operating budget. This is a proposed operating ceiling, excluding existing hosting, engineering labor, outreach and any unapproved document fees. It is not a claim that the workflow is currently running or can generate fifty qualified prospects.

## Initial scope

| Dimension | Planning default | Required client decision |
|---|---|---|
| Geography | Dallas, Collin, Denton, Bexar, Texas | Approve all four; no California or NYC |
| Instrument | New Notice of Federal Tax Lien, with original source evidence | Confirm business and individual coverage |
| Lead unit | Unique prospect with at least one eligible notice; supporting notices retained | Confirm prospect-based versus filing-based contract |
| Volume | Target 50 qualified new prospects/week on a four-week rolling average | Agree whether target is average or weekly minimum |
| Freshness | Notice recorded within 30 days; late discoveries separately flagged | Approve maximum age and backlog handling |
| Delivery | Monday 09:00 America/New_York; data cutoff Sunday 23:59:59 America/Chicago | Confirm timezone, holidays and late-arrival policy |
| Format | UTF-8 CSV, fixed schema; client-facing summary and internal manifest | Approve headers and import behavior |
| Distribution | One explicitly allowlisted recipient and approved sender API | Obtain actual email; do not infer it |
| Spending | Direct access first, optional Bright Data, no paid copies by default | Approve products and spend controls |
| Outreach | Client-managed; no automatic calls, texts, email campaigns or mailings | Client compliance owner approves use |

## Non-goals

No multi-client SaaS, website, public dashboard, tax advice, legal lien-status guarantee, current-payoff calculation, automatic skip tracing, property-equity modeling, machine-learning conversion prediction, or unrelated geography in the MVP. A CSV delivery is not permission to contact a prospect.

## Stakeholders and accountability

| Role | Responsibility | Approval authority |
|---|---|---|
| Jonathan / product owner | Scope, technical budget, prioritization, escalation | Go/no-go and spend exceptions |
| Christopher / client owner | Ideal client, accepted leads, format and recipient | Commercial acceptance and business-fit rules |
| Giovanni / coordinator | Requirements and weekly feedback logistics | Coordination; not assumed to authorize system credentials |
| Engineering lead | Architecture, implementation, pull-request quality | Technical release recommendation |
| Source engineer | County mappings, access evidence, adapters | County validation evidence |
| QA/data reviewer | Ground truth, exception queue, weekly sample | Data-quality gate |
| Operations owner | Droplet isolation, schedules, backup and incidents | Deployment and operational readiness |
| Client compliance owner | Source permissions and intended outreach | Compliance gate; obtain counsel as needed |

Named engineers must be assigned during kickoff; do not assume GitHub handles or add outside collaborators automatically. One person may fill several roles but code/data review must have a second reviewer.

## Acceptance gates

**Gate A — Requirements:** signed lead definition, amount band, entity preference, mail-address requirement, sender/recipient, freshness, retention, spend limit, lawful-use review and expansion rules. A missing field blocks delivery, not silent defaulting.

**Gate B — Access:** each included county has proven index pagination, exact document-type mapping, permitted detail/image access, fees, authentication requirements, sample extraction and rate-limit behavior from the actual Droplet. Unsupported counties stay disabled.

**Gate C — Quality:** proposed release targets are at least 98% correct included instrument classification and 98% exact amount extraction on a reviewer-labeled set of at least 50 real available notices, or all available if fewer, with per-county coverage. An included row's amount/address/status ambiguity is resolved by manual review; aggregate accuracy is not permission to export known errors.

**Gate D — Reliability:** deterministic replay, crash recovery, suppression updates, budget-stop behavior, restore drill, approved test-recipient delivery and false-zero alarm verified. No public production port or PII in GitHub artifacts.

**Gate E — Supply:** four complete historical recorded-date weeks and at least two scheduled live delivery cycles measured. The four-week average target is not achieved until qualified, first-delivered unique prospects average 50; backfill supply is not recurring supply. Historical results are indicative, not guaranteed.

## Shortfall policy

Deliver the actual approved count and an explicit reason-coded shortfall. Do not substitute releases, duplicates, unverified amounts, stale records or unrelated counties. Determine whether the cause is source incompleteness, parser/reviewer throughput, client restrictions, or genuine supply. Fix technical loss first; request approval before widening freshness or adding another originally requested county. No automatic commitment to Cook or Harris without a comparative access/volume spike.

## Client handoff requirements

Obtain a client-owned or explicitly authorized sender credential, verified recipient, mailbox permission, sample import confirmation and an agreed contact method for failed deliveries. Use approved HTTPS email delivery or an approved existing restricted shared folder if email attachments are rejected. No new paid vendor is authorized by this plan.

The lead record must identify public-record sourcing and avoid implying a current verified tax balance. The IRS distinguishes notice withdrawal, release, discharge and subordination; the pipeline must not collapse these into one debt-paid flag. [IRS lien guidance](https://www.irs.gov/businesses/small-businesses-self-employed/understanding-a-federal-tax-lien)
