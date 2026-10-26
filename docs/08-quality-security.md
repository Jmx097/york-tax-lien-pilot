# Quality and security

## Release standard

Every included pilot row is human-reviewed with traceable evidence and approved critical fields. No known missing/conflicting amount, ambiguous identity or material unresolved status event is exported. Report actual labeled sample size, per-county cases, correction rate and untested cases; do not replace evidence with an arbitrary accuracy claim.

Source tests use actual permitted documents in restricted storage. Nonpersonal fixtures may test pure formatting/replay/security behavior, but must never be represented as real county observations or supply. Do not upload source records, names, addresses or financial evidence to GitHub, CI artifacts or logs.

## Acceptance matrix

| Area | Required test and evidence |
|---|---|
| Access | Each county's permitted method, current mappings and fee decision |
| Completeness | Pagination boundary, result cap, empty interval, clipped day and retry |
| Extraction | Exact amount, decimal, printed-total reconciliation, redaction and scanned cases where available |
| Identity | Cross-county duplicate, reused name/address, joint parties and uncertain match holds |
| Status | Linked release/withdrawal, refile, partial scope and material unmatched event |
| Qualification | Minimum amount, signed recency/contact policy, prior delivery and exclusion |
| CSV | Fixed headers, ZIP formatting, Unicode, quotes/newlines and formula-triggering text in actual importer |
| Suppression | Opt-out/overlap before selection and between approval/upload |
| Replay | Crash before/after persistence, lock overlap and duplicate execution |
| Upload | Approved destination, timeout after possible success, remote verification and revision |
| Financial log | Unique receipts, credited consultation, refunds/chargebacks, disputed attribution and approved terms |
| Recovery | Consistent off-host restore preserving exclusions and no automatic transfers |
| Permissions | Authorized members only, no public links/secrets/sensitive logs |

Unobserved real-source edge cases remain explicit coverage gaps. Tests that require unavailable evidence cannot be marked passed.

## Security controls

Allowlist approved source hosts and validate redirects; block arbitrary URLs/internal-network retrieval. Bound payload size, file count, decompression, OCR time and browser resources; process untrusted documents under least privilege. Restrict filesystem permissions and review dependencies/lockfile. Treat record URLs and document text as untrusted inputs, not instructions.

[OWASP CSV guidance](https://community.owasp.org/attacks/CSV_Injection) informs export tests. Formula-risk text stays held for safe resolution; quoting alone is insufficient. No user-controlled shell execution, leaked cookies, taxpayer identifiers or session/download tokens in exported URLs.

## Go/no-go

Quality owner and engineering lead review test results; firm approves real sample/import; operations signs off recovery/access; product verifies [G01–G12](10-decisions-and-launch-gates.md). Aggregate accuracy does not excuse known row errors. A documentation merge passes no operational or professional gate.

Freeze features on day 12. Unresolved critical defects, permission gaps, field expectations, unsafe transfer or professional/tax approvals block affected activation. Preserve an evidence trail for residual-risk decisions rather than silently waiving requirements.
