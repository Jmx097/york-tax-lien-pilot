# Three-week backlog

P01–P12 are stable work-package IDs, not assumed GitHub issue numbers. Live publication status is tracked in [GitHub issues](https://github.com/Jmx097/york-tax-lien-pilot/issues). All work remains planned and unassigned unless an actual issue says otherwise. Publishing these files passes no acceptance or launch gate.

| ID | Work package | Accountable role | Target |
|---|---|---|---|
| [P01](issues/p01-client-decisions.md) | Client acceptance and launch decisions | Product + firm | Days 1–2; gates before activation |
| [P02](issues/p02-source-validation.md) | Four-county permitted access and evidence | Source engineer | Days 1–2 initial; through day 7 |
| [P03](issues/p03-state-runner.md) | Isolated state and fail-closed runner | Technical lead + operations | Days 1–4 |
| [P04](issues/p04-first-vertical-slice.md) | First complete county-to-CSV path | Technical + source | Days 3–5 |
| [P05](issues/p05-review-identity-status.md) | Review, identity, and status safeguards | Technical + reviewer | Days 4–7 |
| [P06](issues/p06-four-county-coverage.md) | Accepted four-county coverage and supply | Source + reviewer | Days 6–10 |
| [P07](issues/p07-suppression.md) | Suppression and prior delivery | Technical + coordinator | Days 6–8 |
| [P08](issues/p08-folder-delivery.md) | Immutable restricted-folder delivery | Technical + operator | First target day 8 |
| [P09](issues/p09-shared-log.md) | Acceptance and collections log | Product + firm coordinator | Days 6–11 |
| [P10](issues/p10-operations-recovery.md) | Schedule, alerts, and recovery | Operations + technical | Days 8–10 |
| [P11](issues/p11-quality-acceptance.md) | Acceptance, security, and defects | Reviewer + technical + firm | Days 9–12 |
| [P12](issues/p12-repeat-handoff.md) | Repeat delivery and operator handoff | Product + operator + firm | Days 13–15 |

## Dependencies

P01, P02, and P03 run in parallel within approved access and data boundaries. P04 proves the complete path. P05 and P07 protect review, identity, and suppression. P06 extends only approved coverage. P08 delivers only after the applicable gates in [launch gates](../docs/10-decisions-and-launch-gates.md). P09 reconciles acceptance and actual receipts without payment APIs. P10 and P11 prove reliability and security. P12 closes handoff. Professional and tax review is an independent dependency, not a coding task presumed complete.

## Board proposal

Use Backlog, Ready, In progress, Review, Validation, Done, and an explicit Blocked state. Proposed milestones are Week 1 / prove path, Week 2 / deliver and harden, and Week 3 / repeat and handoff. These files do not create a project board, milestone, staff assignment, or due date.

## Publishing helper

`scripts/publish-issues.sh` defaults to `--dry-run`. An authenticated repository owner may explicitly run `bash scripts/publish-issues.sh --publish` after reviewing the public text. It confirms the exact repository and skips exact matching titles among the first 1,000 listed issues. It is not concurrency-safe unlimited-history deduplication. It creates no collaborators, milestones, board, deployments, or runtime activation. If live issues diverge from these files, update both deliberately instead of blindly republishing.
