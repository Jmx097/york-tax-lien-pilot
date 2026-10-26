# [P10] Schedule operations and demonstrate recovery

## Assignment

Owner role: operations and technical lead. Target: days 8–10. Dependencies: the P03 runner, P08 delivery state, and approved host, source, and schedule policy.

## Tasks

- [ ] Implement schedules that are disabled by default, plus a lock, missed-window enumeration, and coverage watermarks.
- [ ] Alert on errors, stale state, false zero, budget stop, and review backlog without including sensitive text.
- [ ] Create a consistent encrypted off-host backup with approved key access and retention.
- [ ] Restore into an isolated environment with transfer and spend disabled. Rehearse a code and database-compatible rollback.

## Acceptance

- [ ] Blocked access or capped pagination cannot become a successful zero.
- [ ] Restore preserves suppression, prior delivery, and checkpoints without replaying old transfers.
- [ ] An operator can safely stop, resume, and recover independently of the previous deployment.

## Done and exclusions

A second reviewer witnesses the restore. Document actual objectives, capacity, and escalation. Do not invent an uptime or recovery service level, blindly copy an active database, use a default public link, or activate production automatically.
