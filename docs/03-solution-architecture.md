# Solution architecture

## Decision

Use one isolated batch application, persistent SQLite state and a restricted evidence directory on an approved existing host. Proposed implementation: supported patched Node LTS, TypeScript CLI, permitted direct requests, Playwright only when needed, PDF text extraction and limited local OCR. Host capacity, dependency versions and source access remain to be verified.

No always-on public server, distributed queue, managed database, CRM, mailbox API, Drive API, custom payment app or runtime LLM is required. Operator-assisted review and manual secure folder upload are part of the pilot, not hidden automation claims.

## Components

| Component | Responsibility | Durable output |
|---|---|---|
| Policy/source registry | Approved fields, gates, allowed hosts and mappings | Versioned policy and per-county evidence |
| Collector | Complete permitted windows, all pages, bounded retries | Recordings, coverage and queued jobs |
| Extractor | Text first, narrow OCR, exact field evidence | Field candidates and hold reasons |
| Review | Approve, correct, reject or hold | Reviewer, timestamp, reason and evidence |
| Identity/status | Notice/prospect linkage and scoped events | Audited lineage and exclusions |
| Qualification | Approved hard gates, suppression and novelty | Eligible reviewed prospect IDs |
| Export | Deterministic CSV and aggregate manifest | Immutable batch and hash |
| Delivery ledger | Approval, upload verification and acknowledgement | Separate operational states |
| Shared log | Acceptance, activity and actual receipts | Restricted reconciliation evidence |
| Operations | Locks, alerts, backup and recovery | Run history and restore evidence |

## State and replay

Recording uniqueness is county plus instrument number. Keep recording, notice, liability, taxpayer/prospect, review, status event, batch, delivery and receipt identities distinct. Never use taxpayer IDs as deduplication keys.

Persist discovered results and follow-up jobs before advancing a window checkpoint. A blocked, clipped or schema-invalid response cannot mark a window complete. A single-writer application lock and durable leased work prevent overlapping jobs; reclaim expired work after a crash. Bound transient retries; stop on permission/payment/schema changes and alert rather than looping.

A rerun reuses identities and does not create duplicate records, deliveries or receipt entries. Schema migrations and rollback compatibility are explicitly tested before release. Do not put SQLite on an unverified shared network filesystem.

## Review and export

Hold missing/conflicting amounts, ambiguous identities, material unmatched status events and unapproved contact fields. Every included pilot row has a reviewer and restricted evidence. Simple date/ID ordering replaces elaborate scoring.

Apply suppressions and prior-delivery checks at selection and immediately before transfer. An intervening suppression requires a revised immutable batch and approval. Export fixed headers, exact amounts, stable lead IDs and public record links without session tokens.

## Delivery states

Use draft → validated → approved → upload_pending → uploaded_verified → acknowledged; rejected, cancelled and upload_unknown are explicit alternatives. Approval is not upload, upload is not client acceptance and acceptance is not fee entitlement.

Record approved folder identity and authorized members, local hash, remote object/version, verified content/hash where supported, operator and timestamps. On timeout, inspect the destination before retrying. Do not promise exactly-once remote delivery. Corrected batches have revision IDs; do not overwrite the audit trail.

## Schedule and isolation

Delivery weekday, cutoff, timezone, holiday policy and source overlap interval remain unset pending approval. Store run timestamps in UTC while preserving source date semantics. The application enumerates missed windows; timer catch-up alone is insufficient.

Proposed paths: `/opt/york-tax-lien-pilot/` for releases, `/etc/york-tax-lien-pilot/` for restricted configuration and `/var/lib/york-tax-lien-pilot/` for persistent state. Dedicated non-root identity, least privilege, independent state and credentials. No modification to the earlier deployment or automatic enablement of timers.

## Deferred work

General OCR, extra automated counties after freeze, APIs, CRM, campaign infrastructure, paid enrichment, custom portal, conversion scoring and geographic expansion. Four-county scope remains a business requirement; deferred automation requires accepted manual coverage or an explicit scope change, not omission.
