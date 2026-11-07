# [P03] Adapt isolated state and a fail-closed runner

## Assignment

Owner role: technical lead. Stage: 2, offline MVP, after the P02 source feasibility checkpoint. Dependencies: confirmed ownership and a sanitized handoff of in-progress work on the earlier engine's validation branch.

## Tasks

- [ ] Adapt the earlier engine's checkpoint, queue and retry foundations. Remove its default spreadsheet destination, alert recipient, schedulers and automated review workflow from the pilot path.
- [ ] Isolate a non-root identity, credentials, release, configuration and state paths, plus resource limits.
- [ ] Implement policy validation, database migrations, durable work, checkpoints, and one application lock.
- [ ] Persist results and follow-up jobs before marking a window complete. Reject clipped or schema-invalid success responses.
- [ ] Bound retries, classify access, schema, and payment errors, and reclaim expired jobs safely.
- [ ] Keep collection, transfer, paid access, and billing as separate approvals. Unresolved values fail closed.

## Acceptance

- [ ] Fresh state initializes. Invalid or unset policy cannot activate the affected operation.
- [ ] A crash and rerun skips no completed window and duplicates no persisted entity. Overlapping workers are excluded.
- [ ] No old credentials, personal records, databases, cookies, destinations or deployment state are copied, and external transfer is disabled by default.

## Done and exclusions

Migration and replay evidence plus a second review are required. No public application, distributed queue, runtime model, or change to the previous deployment is included. Example JSON is not runtime enforcement; enforcement must be implemented and tested.
