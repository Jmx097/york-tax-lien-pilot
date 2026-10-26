# Data contract

## Identity and lineage

| Entity | Identity and rule |
|---|---|
| Recording | Unique county plus instrument number; retain approved URL and document hash |
| Notice | Verified non-taxpayer notice reference and evidence; can span county recordings |
| Liability | Tax-period/form/assessment evidence within a notice; no blind summing |
| Prospect | Conservative name/address linkage with reviewer-confirmed aliases |
| Status event | Explicit notice reference and scope; material ambiguity held |
| Review | Decision, reviewer, timestamp, reason and evidence |
| Batch/member | Client, cutoff, policy/schema version and revision; stable lead ID |
| Delivery | Approved batch, destination, remote evidence and independent acknowledgement |
| Receipt | Unique actual payment ID, referral linkage and append-only adjustments |

Do not deduplicate on last name, ZIP or county alone. Same-name/different-address and joint-party cases require conservative review. Previously delivered taxpayers do not become new leads because of another county or notice. Approved updates are separate from new weekly lead counts.

## Amount and status

Store money as integer cents. Export fixed two-decimal USD text. The qualifying primary notice must have a documented amount of at least USD 10,000 (1,000,000 cents). Do not aggregate overlapping notices to reach the minimum; preserve supporting notices separately. Reconcile printed total with unique liability rows; redacted, uncertain or conflicting amounts stay held.

Use `amount_basis=primary_notice_not_current_balance` and `current_balance_verified=false`. Recording fees, OCR duplicates and unrelated dollar figures are not debt evidence.

The [IRS lien guidance](https://www.irs.gov/businesses/small-businesses-self-employed/understanding-a-federal-tax-lien) distinguishes release, withdrawal, property discharge and subordination. Linked full releases suppress the affected opportunity, not all unrelated liabilities. Withdrawal excludes the notice campaign without asserting debt paid. Partial releases, refiles, amendments, discharges, subordinations and uncertain links require scoped reconciliation or review. Report what was checked and when, not guaranteed current legal enforceability.

## Inclusion rules

Require approved county/type, instrument identity, traceable evidence, taxpayer name, exact approved contact fields, amount at or above the minimum, signed recency policy, reviewer approval, status checks, no prior delivery and no suppression. Additional entity/amount preferences are unset and cannot silently narrow the agreement.

Fifty is a conditional weekly target, not a mandatory selection cap or rolling-average definition. Agree whether to export all eligible rows or a capped selection; disclose actual counts and reasons. Recency, required contact fields, cutoff and acceptance deadline stay unset until agreed. Phone/email cannot be assumed or invented; paid enrichment is excluded.

## CSV contract

Ordered proposed headers: [weekly leads v1](../contracts/weekly-leads-v1.columns.txt). Final field acceptance and actual importer test version the schema before live delivery.

Use UTF-8, fixed order, RFC-style quoting, ISO dates, ZIP as text and deterministic ordering by recorded date descending then lead ID. No taxpayer IDs/fragments, birth dates, bank data, raw OCR, cookies, private download URLs or credentials. Non-taxpayer public notice references may be blank if a safe reference does not exist.

Treat strings as untrusted. [OWASP CSV injection guidance](https://community.owasp.org/attacks/CSV_Injection) explains formula risks; quoting alone is not a mitigation. Quarantine dangerous leading control/formula characters, including obscured variants, for safe reviewer resolution. Preserve original evidence and test actual importer behavior; do not silently mutate source facts.

## Manifest and delivery

Restricted manifest: batch/cutoff IDs, schema/policy/code versions, covered intervals, county counts, held/excluded counts, gaps, certified-through observations, checksum, byte size, approver and separate upload state. Public reports contain aggregates only.

Zero qualified rows require explicit shortfall handling and approval, not a successful fifty-lead label. Correction creates a new revision; records remain auditable. No email attachment or public-link fallback without separately approved policy.

## Acceptance and feedback

Use [referral log headers](../contracts/referral-log-v1.columns.txt). Separate delivery from pending/accepted/rejected/disputed referral acceptance. Activity states such as contacted, consultation_booked, consultation_paid and client_onboarded are not financial proof. Opt-outs and overlap findings update suppressions before subsequent export. Restrict access and minimize existing-client matching information.

## Collections ledger

Use [receipt log headers](../contracts/receipt-log-v1.columns.txt). A unique receipt records actual eligible collections in integer cents, currency, accepted referral, approved service category, date, terms version and restricted evidence reference. Booking, signed engagement or unpaid invoice alone is not a receipt. Count consultation credits only once; exclude unrelated services and separately charged taxes/third-party costs under the approved terms.

Refunds/chargebacks are append-only adjustments referencing the original receipt. Track service fees, setup recovery and remaining balance separately under privately approved lawful terms. Resolve attribution windows, disputes, cap and reversal behavior before billing; no fee percentage or tax rate is enabled by these headers.

Prepare one reconciled monthly hosted invoice under approved terms. The draft's review-before-charge interval and separate express card authorization remain restricted operating requirements; no stored card data or automatic charge is implemented. Client acceptance of supporting contact fields is a prerequisite to payment setup, not a promise that enrichment exists.
