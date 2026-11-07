# Validation backlog

P01–P12 are stable work-package IDs, not assumed GitHub issue numbers. Live publication status is tracked in [GitHub issues](https://github.com/Jmx097/york-tax-lien-pilot/issues). All work remains planned and unassigned unless an actual issue says otherwise. Publishing these files passes no acceptance or launch gate.

| ID | Work package | Accountable role | Stage |
|---|---|---|---|
| [P02](issues/p02-source-validation.md) | NJ/CT permitted access and exact-amount evidence | Source engineer | 1. Source feasibility (first) |
| [P03](issues/p03-state-runner.md) | Adapted state and fail-closed runner | Technical lead | 2. Offline MVP |
| [P05](issues/p05-review-identity-status.md) | Review, identity and status safeguards | Technical + reviewer | 2. Offline MVP |
| [P07](issues/p07-suppression.md) | Suppression and prior delivery | Technical lead | 2. Offline MVP |
| [P04](issues/p04-first-vertical-slice.md) | First permitted source-to-local-review slice | Technical + source | 2–3. MVP to permitted integration |
| [P10](issues/p10-operations-recovery.md) | Restart, replay and recovery | Technical + operations | 3. Permitted integration |
| [P06](issues/p06-nj-ct-coverage.md) | NJ/CT coverage and supply evidence | Source + reviewer | 3–4. Integration to QA |
| [P11](issues/p11-quality-acceptance.md) | Independent QA and founder workload | Reviewer + technical | 4. QA and workload |
| [P01](issues/p01-client-decisions.md) | Owner and client decisions | Product + firm | 5. Decision, then before activation |
| [P12](issues/p12-repeat-handoff.md) | Recommendation, then repeat delivery and handoff | Product + operator + firm | 5. Decision, then handoff |
| [P08](issues/p08-folder-delivery.md) | Immutable restricted-folder delivery | Technical + operator | After a GO or NARROW SCOPE decision |
| [P09](issues/p09-shared-log.md) | Acceptance and collections log | Product + firm contact | After a GO or NARROW SCOPE decision |

## Dependencies

P02 comes first: no other build work proceeds until the permitted exact-amount path is assessed for CT statewide and Bergen. P03, P05 and P07 adapt the existing engine offline. P04 proves one real permitted slice. P10 proves restart and replay. P06 measures actual eligible supply per state. P11 independently compares fields and measures founder effort. P01 and P12 turn the evidence into a recommendation. P08 and P09 start only after a GO or NARROW SCOPE decision and the applicable [launch gates](../docs/10-decisions-and-launch-gates.md). Professional and tax review is an independent dependency, not a coding task presumed complete.

## Ownership

Work runs as a single-worker chain. Before editing in-progress work on the earlier engine's validation branch, confirm ownership and obtain a sanitized code handoff; never run two writers in the same checkout.

## Publishing helper

`scripts/publish-issues.sh` defaults to `--dry-run`. An authenticated repository owner may explicitly run `bash scripts/publish-issues.sh --publish` after reviewing the public text. It confirms the exact repository and skips exact matching titles among the first 1,000 listed issues. It is not concurrency-safe unlimited-history deduplication. It creates no collaborators, milestones, board, deployments or runtime activation. If live issues diverge from these files, update both deliberately instead of blindly republishing.
