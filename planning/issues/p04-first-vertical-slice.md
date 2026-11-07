# [P04] Build the first permitted source-to-local-review slice

## Assignment

Owner role: technical lead and source engineer. Stage: 2–3, offline MVP to permitted integration. Dependencies: a green source from P02 and the adapted foundation from P03.

## Tasks

- [ ] Select the first source from observed permitted access (CT statewide or Bergen), not a fixed preference.
- [ ] Run date/state/source-filtered intake over a complete approved window. Retain restricted evidence and exact critical fields.
- [ ] Apply type, exact-amount, identity and geography checks, with explicit HOLD for uncertain amount, address or status.
- [ ] Produce a reviewed, formula-safe local CSV draft and manifest. External transfer stays disabled.

## Acceptance

- [ ] One real permitted source reaches a locally reviewed CSV draft, or the result is reported as a blocker.
- [ ] Every row has evidence, exact cents and a reviewer. No row asserts a current IRS balance.
- [ ] Synthetic fixtures are labelled synthetic and are not presented as live-source success.

## Done and exclusions

Sanitized demonstration evidence and a second review are required. Do not guess contact data, build universal OCR or reuse the earlier engine's sheet, email or scheduler paths. A live transfer requires a GO or NARROW SCOPE decision and the applicable launch gates.
