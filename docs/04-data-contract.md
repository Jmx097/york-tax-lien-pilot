# Data contract

## Record layers

Keep county recording, federal notice, liability, prospect, status event and delivery as different entities. A county filing number identifies a recording, not necessarily a unique taxpayer or distinct IRS debt. One notice may contain several liability rows, and the same notice may be recorded in more than one county.

| Entity | Identity policy | Notes |
|---|---|---|
| Recording | Unique `(county, instrument_number)` | Preserve source URL and document hash |
| Federal notice | Exact public notice serial/certificate reference where present, verified with party/evidence | Cross-county notice link; do not use taxpayer ID |
| Liability | Notice plus normalized tax form/period/assessment evidence | Do not sum refiles or overlapping liabilities blindly |
| Prospect | Conservative normalized name + complete mailing address, reviewer-confirmed aliases | Ambiguous matches held, not auto-merged |
| Status event | Event recording and explicit referenced notice/covered scope | Unknown reference requires review |
| Delivery batch | Client + cutoff + schema/policy version + revision | Immutable after approval |
| Delivery member | Batch + prospect; supporting notice links | Stable lead_id returned in feedback |

For uncertain same-name/different-address cases, flag potential duplicate for review. Do not deduplicate by last name, ZIP or county alone. Maintain a prior-delivered-prospect ledger for this client; do not re-send the same prospect on another county filing. A genuinely new service opportunity for an already-delivered prospect is a separately approved update, not a new lead toward the quota.

## Amount semantics

`recorded_notice_amount_usd` is the documented sum of unique liability rows on the selected notice as of that notice, not a live IRS balance. Use integer cents internally. Store parsed text evidence or approved restricted evidence pointer, extraction method/version, document hash and reviewer decision. Avoid binary floating point for money.

Never choose the largest dollar figure anywhere on a PDF. Do not confuse recording fees, dates, tax periods, penalty text or duplicate OCR lines with the lien amount. If both a printed total and rows exist, reconcile them; conflicting totals require review. Unclear decimal placement and redacted amounts must never be guessed.

When several notices belong to one prospect, retain each amount and covered periods internally. Export the amount from a designated primary eligible notice and include supporting-notice count; do not sum overlapping notice totals to manufacture a large lead. Set `amount_basis=primary_notice_not_current_balance` and `current_balance_verified=false`.

## Event semantics

The IRS [distinguishes withdrawal, release, discharge and subordination](https://www.irs.gov/businesses/small-businesses-self-employed/understanding-a-federal-tax-lien). Use that distinction in the pipeline:

- New federal notice: potential lead after qualification.
- Full release tied to the same notice/covered liabilities: suppress it from this lien-driven lead campaign and retain evidence; do not infer every other liability is satisfied.
- Partial release: reconcile only covered liabilities; review unresolved scope.
- Withdrawal: remove from the active-notice campaign, without asserting that the underlying debt is paid.
- Refile or amendment: update lineage and reassess freshness/amount; not automatically a new lead.
- Discharge of specific property or subordination: status/review event, not an automatic taxpayer-wide release.
- Unknown event or unmatched reference: hold the affected candidate where material; no affirmative claim that a lien remains legally enforceable.

The pipeline reports `no_disqualifying_event_found_as_of` and `status_checked_at`, not a guaranteed legal status. Same-name fuzzy searches alone cannot prove a release relationship. Reviewer-approved links and suppression always override ranking.

## Weekly inclusion

A deliverable prospect must have an allowed county, verified federal-new-notice classification, source identity/URL, name, required mailing-address fields, exact amount evidence, approved business-fit band, acceptable recorded-date age, no known disqualifying linked event, no prior delivery and no opt-out. Missing critical fields or unresolved identity/status are held, not silently ranked lower.

Client-approved amount bands and entity preferences start unset. Do not hard-code a wealth-based county preference or a dollar minimum until kickoff. Older-but-newly-indexed records may be included only within the approved age and flagged late. A target of fifty is a selection limit only if the client requests exactly fifty; otherwise deliver all eligible rows, ranked, with count disclosed.

## CSV v1

Ordered headers are defined in `contracts/weekly-leads-v1.columns.txt`. One row is one prospect, not one county hit. Core fields:

| Field group | Fields and semantics |
|---|---|
| Identifiers | lead_id, batch_id, schema_version, county, state, instrument_number |
| Evidence | public_notice_reference, source_record_url, recorded_date, first_seen_at_utc, status_checked_at_utc |
| Prospect | taxpayer_name, entity_type, mailing_street, mailing_city, mailing_state, mailing_zip |
| Amount | recorded_notice_amount_usd as fixed two-decimal text; amount_basis; current_balance_verified |
| Qualification | priority_score, priority_reasons, extraction_method, reviewer_verified, late_indexed, supporting_notice_count |

Never export taxpayer identifiers, SSN/EIN fragments, DOB, bank information, raw OCR, cookies or assumed phone/email. `public_notice_reference` must be a non-taxpayer recording/notice reference; if it contains sensitive identifiers, leave it blank and use internal lineage instead. Public source links must be stable approved record-view links, not session tokens, credentials or expiring private downloads.

CSV uses UTF-8, RFC-style quoting, embedded quote escaping, fixed column order, ISO dates, ZIP as text and stable ordering by priority descending then recorded_date descending then lead_id. The client must test ZIPs with leading zeros in its actual importer.

Treat all sourced strings as untrusted. Formula-triggering cells can execute in spreadsheet software; [OWASP describes CSV injection risks and application differences](https://community.owasp.org/attacks/CSV_Injection). For this MVP, quarantine unsafe leading control/formula characters (including whitespace-obscured or full-width variants) in free-text values for reviewer correction. Never mutate an evidence record silently or rely solely on CSV quotes. Add importer-specific tests before signoff; numeric amount columns are validated nonnegative numbers, not formulas.

## Manifest and delivery audit

Internal manifest: batch ID, cutoff, generated timestamp, client ID, schema/policy/config versions, git commit, eligible/exported/held counts by county, known coverage gaps, source-certified-through observations, byte size, SHA-256, approval identity/time and delivery state. Store names/addresses only in the protected CSV/database, not logs or alerts.

Create a header-only artifact plus explicit zero/shortfall notification if no records qualify, subject to approval. Never send an empty file as a successful fifty-lead run. Revisions require a new manifest revision and disclosure, not overwrite of a previously delivered CSV.

## Feedback contract

A minimal client feedback file contains `lead_id`, `outcome`, `outcome_date`, `fee_collected_usd`, `outreach_cost_usd`, `client_rejection_reason`, `do_not_contact`. Allow outcomes unworked, attempted, reached, consultation, qualified, engaged, lost, opt_out and invalid. Feedback can be manually imported weekly; no CRM service is needed initially.

Validate IDs, transitions, duplicates and money fields. Retain raw client feedback only in the restricted operational store. Opt-outs immediately update the suppression table and win over any prior qualification.
