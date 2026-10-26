# ROI and operating cost

## Optimize real business value

High notice amounts are not verified high conversion, present ability to pay, current IRS debt or professional fees. Do not rank counties by household income or assume larger debt increases service margin monotonically. County is initially a source dimension for measurement, not a conversion multiplier.

Expected net value per prospect should eventually use measured engagement probability, collected professional-fee contribution, acquisition/review/enrichment cost and outreach cost. These quantities are currently unknown. Start with transparent business-fit heuristics and a feedback loop, not invented conversion probabilities.

## Proposed initial ranking

Apply hard eligibility gates before scoring. No score can rescue missing source evidence, uncertain amount, known suppression, prior delivery or unapproved freshness. The following weights are proposed policy, not empirically validated performance:

| Component | Maximum points | Initial rule |
|---|---|---|
| Client service fit | 30 | Approved debt band, entity type and service scope; no automatic reward above preferred band |
| Freshness | 25 | Days since recorded date within client-approved bands; late indexing disclosed |
| Reachability | 20 | Complete required mailing address; channel is mailing unless lawful verified channel is separately approved |
| Evidence quality | 15 | Exact amount reconciliation and validated source classification; manual-reviewed confidence wins |
| Novelty | 10 | First delivered prospect and clear notice lineage; never count duplicate counties as added value |

All approved leads are novel; this component is intentionally a gate-like indicator rather than fabricated statistical separation. Store component values and reasons. Configuration remains delivery-disabled until client bands and thresholds are signed. Every policy change is versioned and tested on prior batches without re-sending them.

For the first delivery cycles, do not discard available valid leads just to maximize average amount. If oversubscribed, select by approved fit/freshness/quality and preserve an unselected queue without allowing it to age beyond policy. Report median and distribution of notice amount alongside lead count; one extreme amount should not make the cohort look better than it is.

## Measurement loop

Weekly, capture new federal notices, unique prospects, accepted prospects, rejected reasons, address/amount completeness, status matches, captured-to-delivered lag, county contribution, operating spend and manual review hours. Record client contact, consultation, engagement, collected fees, opt-outs and complaints by stable lead_id.

Report cost per accepted lead and cost per engaged client only when denominators exist. Separate cash infrastructure cost from engineering maintenance, review labor, outreach and service delivery. At least several delivery cohorts and a meaningful number of actual outcomes are needed before claiming any county or amount band converts better; report sample size and uncertainty, not a precise-looking score without evidence.

## Vendor pricing baseline

As of the research baseline, Bright Data's [residential offer](https://brightdata.com/solutions/premium-proxy) shows $8/GB pay-as-you-go and a promotional $4/GB rate. Treat the promotion, duration, account eligibility, domain treatment, minimum deposit and taxes as items to confirm in the actual account; do not bake a coupon into the business case.

Bright Data advertises [managed browsers at $8/GB](https://brightdata.com/pricing/mcp-server). Its [Browser API FAQ](https://docs.brightdata.com/products/scraping-browser/faqs) describes 5,000 shared monthly credits, at five credits per MB for Browser API, equivalent to about 1,000 MB if the whole allowance goes to that product. This is not a residential-proxy bandwidth allowance, not an automatic entitlement for an existing account and not proof that publicsearch domains are standard-priced.

The [billing FAQ](https://docs.brightdata.com/general/account/billing-and-pricing/faqs) describes pay-as-you-go and daily byte/spend limits, with delayed enforcement. Verify the account's actual product, available credits and billed-domain treatment before approval. No Bright Data account, subscription or purchase is created by this project setup.

## Cost scenarios

These are arithmetic planning scenarios, **not measured traffic forecasts**. Count browser bootstrapping, scripts, detail views, documents, retries, failed requests as billed under the selected product, and overhead. Use provider statistics for reconciliation; application bytes are only a conservative control estimate.

| Measured billable traffic/month | At $8/GB | Interpretation |
|---|---|---|
| 0.25 GB | $2 | Small traffic scenario, no free credit assumed |
| 1 GB | $8 | Near the proposed proxy budget |
| 3 GB | $24 | Requires approval or access optimization |

Existing Droplet cash increment is zero only while available CPU/RAM/disk/bandwidth remain sufficient. Local SQLite, CLI scheduling and local OCR introduce no new vendor line item by design, but do use host resources and engineering time. Existing mailbox API, off-host backup and GitHub CI are zero-increment assumptions only if current licensing/storage/usage permits; verify instead of promising free capacity.

Document charges are the largest unknown. Set paid purchases to zero by default and stop at a fee gate. Confirm real source costs before committing to full automation. A paid bulk extract may eventually be cheaper than per-document copies or brittle browser work, but requires a separate approved decision.

## Guardrails

- Proposed total incremental cash operating budget: $10/month; warn at estimated $5 and require explicit approval to resume paid retrieval at the budget threshold. Hosting increases, document fees, paid enrichment and new subscriptions are never automatic.
- Use a dedicated vendor zone/credential for this client, daily provider limits and local persisted monthly usage reservations. Rate assumptions must include premium-domain risk; a local dollar estimate is not a guaranteed invoice cap.
- Start with 200 network operations/day across all four counties, 45 minutes/run, maximum 5 MB/document and 10 pages/document, one browser/worker and initial plus two transient retries. These are protective proposed ceilings, adjustable only after measurement; exceeding one marks incomplete work and alerts, never silently drops remaining records.
- Before each paid session reserve a conservative traffic allowance, cap navigation count/time, record bytes and reconcile against vendor usage. Provider caps may lag by roughly 15 minutes according to its billing documentation, so do not rely on them alone.
- Cache unchanged document hashes; extract all fields from one permitted retrieval; do not re-download a document every overlap scan. Fetch needed document images even when decorative assets are blocked.
- No paid model calls, automatic skip tracing or unlimited retries. Stop on schema drift, permission denial, fee gates or budget exhaustion. Spending more cannot fix a true supply shortage.

## Expansion decision

After measured quality-adjusted supply is known, investigate only client-approved counties from the original requested list. Score each expansion candidate on incremental unique accepted prospects, document/access cost, development/review hours and prospective service fit. Do not declare Cook, Harris or any other county guaranteed to meet fifty without actual observations.
