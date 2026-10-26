# [P07] Enforce suppression, overlap, and prior-delivery exclusion

## Assignment

Owner role: technical lead and firm coordinator. Target: days 6–8, and before every upload. Dependencies: stable state from P03 and reviewed identity from P05.

## Tasks

- [ ] Maintain stable lead IDs and a client-specific prior-delivery ledger.
- [ ] Securely import minimized existing-client, active-prospect, independent-source, and opt-out exclusions.
- [ ] Hold disputed overlap and invalid IDs, and audit corrections.
- [ ] Recheck suppression after batch approval and immediately before upload. Revise and reapprove a changed batch.

## Acceptance

- [ ] The same taxpayer in another county or notice is not a new weekly lead.
- [ ] An opt-out received before transfer prevents inclusion even if the row was previously approved.
- [ ] Delivery, client acceptance, and later activity remain separate statuses.

## Done and exclusions

Reviewer tests cover ambiguous identities, late feedback, and duplicate imports. Existing-client matching data stays private. No client roster or personal evidence belongs in GitHub. Recontact, campaigning, and CRM integration are out of scope.
