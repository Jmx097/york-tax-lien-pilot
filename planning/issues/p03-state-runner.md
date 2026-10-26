# [P03] Establish isolated state and a fail-closed runner

## Assignment

Owner role: technical lead and operations. Target: days 1–4. Dependency: approved build authority from P01. Source research proceeds in parallel.

## Tasks

- [ ] Inventory the host and isolate a non-root identity, credentials, release, configuration, and state paths, plus resource limits.
- [ ] Implement policy validation, database migrations, durable work, checkpoints, and one application lock.
- [ ] Persist results and follow-up jobs before marking a window complete. Reject clipped or schema-invalid success responses.
- [ ] Bound retries, classify access, schema, and payment errors, and reclaim expired jobs safely.
- [ ] Keep collection, transfer, paid access, and billing as separate approvals. Unresolved values fail closed.

## Acceptance

- [ ] Fresh state initializes. Invalid or unset policy cannot activate the affected operation.
- [ ] A crash and rerun skips no completed window and duplicates no persisted entity. Overlapping workers are excluded.
- [ ] No old credentials, personal records, databases, cookies, or deployment state are copied.

## Done and exclusions

Migration and replay evidence plus a second review are required. No public application, distributed queue, runtime model, or change to the previous deployment is included. Example JSON is not runtime enforcement; enforcement must be implemented and tested.
