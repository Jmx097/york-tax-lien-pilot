# Solution architecture

## Architecture decision

Use one isolated batch application, one persistent SQLite database and systemd schedules on the existing Droplet. Prefer a TypeScript CLI over an always-on web API. No new public HTTP service, distributed queue, Redis, managed database, Kubernetes, CRM or runtime LLM is required for the pilot design.

Choose Node 24 LTS and pin an approved patched release and dependency lockfile during implementation. Node publishes an [LTS release record](https://nodejs.org/en/blog/release/v24.22.0); the old project's [manifest](https://github.com/Jmx097/lien-automation-v2/blob/main/package.json) already uses TypeScript, Playwright and better-sqlite3. These are compatibility inputs, not reasons to copy its architecture wholesale.

## Logical modules

| Module | Responsibility | Durable output |
|---|---|---|
| County adapter | Permitted query, all pages, detail/document retrieval | Recording identity, source evidence metadata |
| Access transport | Direct HTTP, local browser, explicitly enabled vendor mode | Sanitized request metrics and costs |
| Discovery runner | Date windows, overlap, checkpoints, partial-run detection | Search windows and upserted recordings |
| Job runner | Single-worker leases, retry policy and durable state | Extraction and reconciliation jobs |
| Extractor | Text layer first; local OCR if necessary | Field evidence, normalized liabilities and confidence |
| Status resolver | Link releases/refiles/withdrawals with careful scope | Reviewable status events and suppressions |
| Entity resolver | Conservative notice/prospect linkage | Canonical prospect and duplicate decisions |
| Qualifier/ranker | Client business rules, freshness and explainable rank | Eligible/held/rejected status with reasons |
| Exporter | Stable selection, safe CSV, manifest and checksum | Immutable batch and lead membership |
| Delivery outbox | Approval, HTTPS send, retry and audit | Delivery state and provider message ID |
| Feedback importer | Client outcomes keyed by lead_id | Status, revenue and suppression updates |

Proposed interfaces: `discover(window, cursor) -> page`; `getDetail(recordingId)`; `getDocument(recordingId)`; `extract(evidence)`; `qualify(prospect, policyVersion)`; `buildBatch(cutoff, policyVersion)`; `send(batch, recipient)`. Source config includes its own departments/types; transport mode does not alter business rules.

## Processing sequence

1. Acquire a process-level flock shared by collection, export and maintenance. Start a run with a configuration hash and source version. If a prior lock is held, skip and alert when repeated; never start competing writers.
2. Discover each enabled county serially. Search from the last successful window minus a proposed seven-day overlap. Respect source-certified-through date and record observed index lag. Use bounded historical reconciliation separately.
3. Insert/update recording rows and enqueue needed jobs in one transaction. Checkpoints advance only after complete pagination/window persistence. A protective request/time cap marks the window incomplete rather than complete.
4. Process durable jobs with one worker and expiring leases. Skip unchanged document hashes. Fetch only evidence required for missing fields/status. Persist accepted output and evidence metadata atomically; failures requeue with bounded backoff.
5. Parse liability rows and address; run status/entity reconciliation and qualification. Quarantine uncertain amounts, identities, joint recipients or redacted fields for review. Human approval is recorded with reviewer and time.
6. On Monday, select never-delivered qualified prospects through the cutoff, including newly discovered late-indexed notices that pass freshness. Recheck suppression and known status events. Create an immutable batch, member rows, CSV and internal manifest; write temp files then atomically rename.
7. During pilot, an operator approves the batch and exact recipient. Delivery outbox sends through the selected existing HTTPS mailbox API, stores the provider ID and reconciles uncertain outcomes before retrying. A successful API call proves provider acceptance, not recipient reading.
8. Import feedback and suppressions before the next export. Store lineage from each delivered lead to source recording, evidence, extraction version, policy and batch.

## Scheduling and windows

Proposed collection schedule: daily at 06:30 America/Chicago. Monthly reconciliation: first successful run of each month rechecks the previous 30 recorded-date days, under its own bounded budget. Initial four-week historical benchmark is explicitly labeled non-recurring backfill.

Proposed delivery schedule: Monday 09:00 America/New_York, after a 07:30 Eastern validation/export attempt. Monday's collection in Central time is not required to race the export: the export uses the prior completed discovery state and Sunday cutoff. A stale collection watermark blocks normal approval or requires a clearly labeled partial delivery approved by the product owner. Store instants in UTC; preserve original county date and interpret date-only records in America/Chicago.

Use persistent calendar timers and validate exact expressions on the deployed host. systemd's [timer documentation](https://www.freedesktop.org/software/systemd/man/systemd.timer.html) describes catch-up after downtime; catch-up activates a service, not a replay of every missed business export. The application enumerates uncompleted windows/batches explicitly and never sends multiple stale weeks without approval.

## Access strategy

Start with permitted direct HTTP where a stable request is verified. Use local Playwright if interaction is required. Add residential proxy routing or Bright Data Browser API only after measurements show a reliability or labor advantage, source/vendor permissions are reviewed and the product owner approves the cost. Neither vendor mode repairs a wrong selector or creates more filings.

A hosted browser may be cheaper overall than hours of anti-bot maintenance; compare engineer time as well as bandwidth. Bright Data distinguishes a [managed browser from plain proxies](https://docs.brightdata.com/products/scraping-browser/faqs). Do not categorically ban browser fallback or assume a residential IP solves access.

Limit one browser/one county at a time. Cache unchanged assets/documents, suppress analytics/fonts/video, but allow document page images required for OCR. Reuse only valid authorized sessions, never put cookies in source control, and do not route login-only content through a product that prohibits it.

## State and resilience

SQLite uses WAL, foreign keys, busy timeout, migrations and a single application writer. Keep the database on local disk, not a network share. A durable jobs table replaces a queue service; one job state transition and its results commit together. Renew long-job leases and cap attempts. Separate transient network failures from schema drift, permission denial, paid-content gates and validation errors.

Use three attempts maximum per transient operation (initial plus two retries), exponential backoff with jitter and Retry-After handling. Stop a county on unresolved authorization/challenge restrictions, unknown schemas or mapping drift; do not cycle providers indefinitely. County failures do not erase other completed counties, but mark the overall export coverage incomplete.

Protect against false zero: a successful HTTP 200 is insufficient. Validate response shape, department/type mappings, pagination and source availability before accepting an empty result. Alert on zero new hits for multiple runs, unusual rejection rate or lag beyond the agreed threshold; compare to historical source behavior, not a fabricated minimum.

## Deployment boundary

Run under a dedicated non-root service user with its own `/opt/york-tax-lien-pilot` code, `/etc/york-tax-lien-pilot` secrets and `/var/lib/york-tax-lien-pilot` state. Keep it separate from OpenClaw/other jobs, their volumes, credentials and timers. Prefer native systemd isolation for MVP; a Docker image may be added if it matches team operations, but never place SQLite inside an ephemeral container layer.

Initial resource guardrail: one worker/browser, 1 GiB memory budget subject to measured capacity, CPUQuota 50%, 45-minute collection timeout. These are proposed starting limits, not verified Droplet capacity. Inventory RAM, disk and existing load first; disable OCR/browser concurrency if the host cannot sustain it. A remote browser can reduce local RAM pressure without increasing Droplet size.

## Delivery boundary

Choose exactly one approved existing sender API at kickoff: Microsoft Graph for an existing Microsoft 365 mailbox or Gmail API for an existing Google mailbox. Implement only the selected provider. Keep credentials server-side, scoped as narrowly as supported; use delegated permission where suitable, or mailbox-scoped application access with tenant admin approval. No email address has been inferred, and no messages are sent during setup.

Use HTTPS on port 443 rather than assuming SMTP works: DigitalOcean [blocks SMTP ports by default](https://docs.digitalocean.com/support/why-is-smtp-blocked/). Send the approved minimal CSV attachment to the allowlisted recipient, with counts, coverage, source lag and shortfall disclaimer. If the client rejects attachments, switch by explicit scope decision to its existing restricted folder and a notification link; do not build both routes initially.

Use a deterministic batch ID, unique batch-recipient outbox row, content hash and provider ID. On timeout after possible acceptance, set delivery state `unknown`, look up provider evidence and require human reconciliation before resending. Do not claim exactly-once delivery over email.
