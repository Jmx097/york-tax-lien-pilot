# Source validation

## Evidence baseline

Checked 2026-10-26. Published interfaces establish a starting point, not proof of working automation, current fees, document availability or permission. No live notice counts, PDFs or Droplet network traces were obtained during project setup.

| County | Portal | Visible department | Verified scope | Not yet verified |
|---|---|---|---|---|
| Dallas | [Official search](https://dallas.tx.publicsearch.us/) | Property Records | Search interface exists | NFTL code, pagination, permitted access, images, extraction, volume |
| Collin | [Official search](https://collin.tx.publicsearch.us/) | Property Records | Search interface exists | Same unknowns; redactions may affect fields |
| Denton | [Official search](https://denton.tx.publicsearch.us/) | Real Property | Search interface exists | Same unknowns; registration/download path needs particular review |
| Bexar | [Official search](https://bexar.tx.publicsearch.us/) | Land Records | Search interface exists | Same unknowns; test federal versus state lien mapping |

The department labels differ on the portals; do not substitute a universal department ID. The county's [Collin land recordings page](https://www.collincountytx.gov/county-clerk/land-recordings) warns about redacted instruments and incomplete online contents. The [Bexar clerk](https://www.bexar.org/2984/Public-Record-Search) describes free online search/viewing and printing uncertified copies; that does not prove the same conditions for every other county.

An older [Denton research guide](https://www.friscoheritage.org/media/Denton-County-Deed-Research.pdf) describes registration for downloads. Treat that as a discovery warning, not current authentication or pricing proof. Do not design around unrestricted PDF URLs until tested. The [Denton clerk](https://www.dentoncounty.gov/173/County-Clerk) links its publicsearch property-alert service.

## Discovery worksheet

Create one evidence record per county in a restricted operational folder, not a GitHub attachment containing names or addresses. Commit only redacted configuration and technical conclusions. Record the observation date and reviewer.

1. Confirm the official clerk-to-portal link and review terms, robots/access guidance, and vendor restrictions; request bulk/API access or written guidance if automated use is unclear. Stop rather than defeating denied access, login restrictions or payment controls.
2. Search one known recorded-date interval manually. Capture the exact department label and identifier, new NFTL types, refiles/amendments, releases/withdrawals, federal creditor names and excluded state/mechanics/medical types.
3. If ordinary browser requests expose usable JSON, document the permitted endpoint, request shape, pagination, session requirements and schema. An internal endpoint is not a public API entitlement.
4. Confirm result caps. Exhaust pagination; recursively split date windows when a cap prevents completeness. If a single day still caps, use a supported finer discriminator or mark incomplete and escalate. Never mark a clipped window complete.
5. Open real recent notices from each county. Confirm whether amount/address are in index, detail JSON, OCR text, permitted PDF or page image. Test actual born-digital versus scanned documents; no assumption that pdftotext is enough.
6. Determine viewing versus download versus certified-copy fees, authentication, permission and whether a lawful bulk export is cheaper than browser maintenance. Paid document purchase defaults to disabled.
7. Repeat a small approved test from the production Droplet IP. Record direct HTTP/local browser success, 403/429/challenge rates, bytes, runtime, image/text availability and manual review time.
8. Only if warranted, compare direct access with an approved Bright Data product using the same authorized scope. Do not automatically rotate IPs after denial. Verify vendor permission, domain pricing and account eligibility before enabling it.
9. Save a signed-off county mapping with version, retrieval date, accepted new-notice types, status-event types, allowed hosts, time basis, rate policy, fee policy and evidence reference. Source is enabled only after this evidence exists.

## Benchmark design

Measure four complete historical recorded-date weeks for every accessible county, not a population extrapolation. Retain counts for raw index hits, complete windows, true new federal notices, distinct federal notice identities, cross-county duplicates, distinct prospects, excluded status changes, qualified addresses, exact extracted amounts, reviewer holds and final accepted prospects.

Backfill and live supply use different cohorts: historical weeks group by recorded date; operational weekly delivery uses discovery/qualification state with freshness checks and excludes already delivered prospects. Cross-county duplication can reduce unique prospect volume. Never add four county averages without cross-county reconciliation.

Manual checks should cover page boundaries, empty dates, multiple liabilities, joint names, reused names, releases, partial releases, refiles, scanned images, redactions and missing addresses. If a case is not present in real available samples, record that coverage gap instead of fabricating source evidence.

## County go/no-go

A county is green only when both permitted index discovery and usable amount/address evidence work within budget. Index-only success is amber and cannot satisfy the qualified-delivery promise. A blocked or fee-heavy source is red until approved access or a lawful alternative is established.

Build Dallas as the reference implementation, then validate Collin, Denton and Bexar independently before reusing code. This order is an engineering starting point, not a claim about county conversion rates. The implementation may be one shared transport/parser plus four mappings, or a shared interface with county-specific overrides if evidence requires it.

## Assumptions explicitly withdrawn

The previous 84 notices/week estimate, claims that all four share identical request bodies, presumptions of free PDF downloads and claims that affluence predicts conversion are not accepted inputs. No verified current county count or fee data supports those guarantees. The fresh-client project begins with measurement.
