# Operations

## Scope and access

This is an intended runbook, not installed services. Dedicated non-root identity, isolated release/config/state paths and restricted permissions are required. Verify host capacity before deployment. No public app port or changes to the earlier deployment. Store secrets outside Git; rotate using the approved owner process, never in issues.

Example paths: `/opt/york-tax-lien-pilot`, `/etc/york-tax-lien-pilot`, `/var/lib/york-tax-lien-pilot`. Database, evidence, exports and delivery history persist across releases. Encrypt approved storage/backup as required; document access roster, recipients, retention and deletion exceptions before personal-data transfer.

## Daily operation

1. Confirm applicable approvals, configuration version and county enablement.
2. Acquire application lock; enumerate incomplete/missed permitted windows.
3. Collect with bounded requests, retries and spending limits; record actual source coverage.
4. Extract/reconcile; route uncertain fields and status to restricted review.
5. Record real counts, holds, gaps, lag, failures and costs; investigate unexpected zero.
6. Review alerts and queue backlog with named operator/backup.

Never treat HTTP success alone as usable results. Detect login/challenge/error pages, schema drift, caps and missing evidence. A county failure cannot disappear into an aggregate success flag.

## Weekly transfer

1. Import feedback, overlap exclusions and opt-outs.
2. Review row evidence and source coverage; select eligible never-delivered prospects.
3. Generate fixed-schema CSV and restricted manifest with hash, cutoff and policy version.
4. Approve batch, destination membership and genuine shortfall report.
5. Recheck suppression immediately before upload; revise/reapprove if changed.
6. Upload manually to the agreed restricted folder; verify actual content and remote object/version.
7. Record uploaded status separately from acknowledgement and client acceptance.
8. On uncertain upload inspect remote state before retrying; retain correction history.

No public-link or email fallback, extra recipient or new purchase without approval. A missed cadence is reported, not silently backdated.

## Deployment and recovery

Review PR and tests, create a versioned release, pause affected jobs, take consistent backup, apply compatible migrations and no-transfer smoke tests, then explicitly authorize activation. Record code/config versions and operator. Rollback must account for data/schema compatibility; reverting code alone is insufficient.

Use an application-consistent SQLite backup mechanism rather than blindly copying an active database. Include required evidence, manifests and delivery/suppression history. Encrypt off-host backups with approved key access, retention and deletion policy. Restore into isolation with transfers/spending disabled; verify integrity, prior-delivery exclusions and checkpoints before resuming. Actual recovery objectives remain pending client/operations approval; do not invent an SLA.

## Incidents

| Incident | Immediate action | Resume condition |
|---|---|---|
| Denied/paid source access | Stop affected county | Approved permitted resolution |
| Parser drift/amount errors | Hold affected rows/batches | Evidence-backed correction and regression review |
| Unexpected zero/cap | Mark incomplete, investigate | Complete-window evidence |
| Budget/capacity limit | Stop affected work, notify | Explicit approved adjustment |
| Uncertain upload | Mark unknown, inspect destination | Reconciled artifact evidence before retry |
| Suppression/privacy incident | Stop affected transfer, secure access | Owner-approved incident response and any required notices |
| Genuine shortage | Report actual count and reasons | No padding; revised scope only by approval |

Maintain restricted incident timeline, impacted batches, operator actions and resolution. Public issues contain sanitized descriptions only.

## Handoff

Operator and backup demonstrate collection, review, transfer, receipt/feedback reconciliation, stop/resume and restore without builder intervention. Record contacts privately, support limits, renewal/expansion process and next review date. Ongoing support and third-party spend are not implicitly authorized by handoff.
