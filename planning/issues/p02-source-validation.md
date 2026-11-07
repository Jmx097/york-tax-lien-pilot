# [P02] Validate permitted NJ/CT access and exact-amount evidence

## Assignment

Owner role: source engineer. Stage: 1, source feasibility, inside a short time-boxed checkpoint. This comes before all other build work. Dependency: applicable access and data authorization from the product owner.

## Tasks

- [ ] Assess Connecticut statewide sources: the public index has no amount field, so find a permitted document or amount path. The linked automated-document route stopped at an observed restriction; do not bypass it.
- [ ] Assess Bergen County, NJ: supported labelled amount with cents, taxpayer mailing-field association and a permitted recurring access method.
- [ ] Leave Essex County inactive unless the product owner activates it; never count it as verified IRS supply.
- [ ] Inspect a handful of actual permitted documents for exact amount with cents, name, mailing address, recorded date and instrument identity.
- [ ] Record a pending, green, amber or red decision per source, with references, allowed method, limits and manual effort.

## Acceptance

- [ ] Dated CT statewide and Bergen decisions and evidence references exist.
- [ ] Denied, paid, challenged, capped or incomplete paths stop or escalate. They are not bypassed and are not reported as a successful zero.
- [ ] No permitted exact-amount path in either state is reported as NO-GO or NEEDS OWNER INPUT; one state is reported as NARROW SCOPE.

## Done and exclusions

Technical findings stay sanitized. Source documents, taxpayer information, cookies and approvals stay restricted. Do not rotate addresses, switch browsers or use a paid vendor to get around a restriction, and do not retry vendor authentication without a genuine credential change and owner approval.
