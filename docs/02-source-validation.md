# Source validation

## Evidence baseline

All sources begin **pending**. Portal URLs are research starting points, not proof of permitted automated access, usable documents, completeness, fees, extraction quality or recurring volume.

| Source | Official starting point | Must prove |
|---|---|---|
| Connecticut statewide (primary) | [CT UCC lien filings dataset](https://data.ct.gov/Business/Uniform-Commercial-Code-UCC-Lien-Filings/xfev-8smz/about_data) and [CT online inquiry](https://service.ct.gov/business/s/onlineenquiry) | A permitted document path with exact lien amount; the public index has no amount field |
| Bergen County, NJ (primary) | [Bergen land records](https://bclrs.co.bergen.nj.us/browserview/) | Labelled amount with cents, taxpayer mailing-field association and a permitted recurring access method |
| Essex County, NJ (optional, inactive) | [Essex register](https://press.essexregister.com/prodpress/clerk/ClerkHome.aspx?op=basic) | IRS origin per record; not an automatic fallback and not verified IRS supply |

## Historical observation

A stored live-browser report covering 2026-10-05 to 2026-11-01 recorded these aggregate counts. They are historical observations, not fresh queries, and not delivery proof.

| Source | Observed count | What it establishes |
|---|---:|---|
| Connecticut statewide | 206 | Currently Active original IRS filing numbers with CT debtor addresses |
| Bergen County, NJ | 55 | Distinct IRS-linked instruments |
| Essex County, NJ | 55 | Broader federal lien category; IRS origin not individually verified |

These counts do not establish fifty eligible unique USD 10,000+ taxpayers per week. They have not been reduced by amount checks, taxpayer dedupe, releases, recency, suppressions or previous delivery. Weekly filing patterns are uneven. Essex must not be added as verified IRS supply.

## Known hard gaps

- **Connecticut amount.** The public index has no lien-dollar amount field, so a permitted document or amount path is essential. The linked automated-document route stopped at an observed access restriction. A different browser, proxy or vendor does not authorize bypassing it.
- **Bergen evidence.** Ordinary interface inspection obtained image pages, but supported labelled amount with cents, mailing-field association and a permitted recurring method remain unproved.
- **Vendor transport.** A paid browser/proxy vendor preflight did not authenticate, and no vendor sessions or source requests were run. Its effect on amount extraction or source legality is untested. Do not retry without a genuine credential change and owner approval, and do not send taxpayer documents to a third party without resolved data-handling scope.

## Investigation worksheet

1. Record observation date, owner, official source link, terms, access restrictions and approved use. Stop on denied access, challenges or unclear terms; seek guidance or approved bulk access.
2. Capture exact initial-notice, refile, release and withdrawal mappings. Exclude state and unrelated liens.
3. Establish authentication, viewing/download fees and lawful document access. Internal browser endpoints do not confer an API entitlement. No IP rotation or bypass after denial.
4. Exhaust pagination; detect caps and split windows where permitted. A capped day is incomplete, not a zero result.
5. Inspect real permitted documents for name, mailing address, exact amount with cents, recorded date and stable instrument identity. Test text PDFs, scanned images and redactions.
6. Run a small authorized test from the intended host; record blocking, rate limits, runtime, cost and reviewer minutes.
7. Sign off a versioned mapping with allowed hosts, access basis, evidence references, types, time semantics, limits and source decision.

Keep real records and session details restricted. Only sanitized technical findings and aggregate counts belong in GitHub.

## Supply measurement

Count raw hits, true notices, distinct notice identities, cross-filing duplicates, unique taxpayers, holds, exclusions, eligible taxpayers and client-accepted rows. Never add source totals before cross-source reconciliation. Historical backfill and new weekly supply are separate cohorts.

## Validation timing

- **Source feasibility checkpoint first.** A short, time-boxed check of the permitted amount path for CT and Bergen comes before any other build work. Stop or narrow if neither source yields exact amounts through a permitted method.
- **Offline MVP next.** Adapt the existing engine against permitted evidence only.
- **Integration only after permission.** No recurring collection until the source decision is green.

## Source decision

| Status | Meaning | Action |
|---|---|---|
| Pending | Evidence not reviewed | Disabled |
| Green | Permitted usable discovery and required evidence within approved limits | Eligible for testing, not automatic launch |
| Amber | Partial access or required evidence/capacity missing | No claim of eligible coverage; resolve or narrow |
| Red | Permission, access or cost blocker | Disabled; escalate |

Full NJ/CT scope preferably requires a viable source in each state. One viable state means NARROW SCOPE.
