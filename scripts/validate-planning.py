#!/usr/bin/env python3
"""Static planning checks, not runtime or live-source tests."""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parent.parent
failures = []
for path in root.rglob('*.md'):
    if '.git' in path.parts:
        continue
    for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
        if target.startswith(('https://', 'http://', 'mailto:', '#')):
            continue
        if not (path.parent / target.split('#')[0]).exists():
            failures.append(f'Broken link: {path.relative_to(root)} -> {target}')
policy = json.loads((root / 'config/pilot-policy.example.json').read_text())
for field in ('collection_enabled', 'personal_data_transfer_enabled', 'paid_access_enabled', 'billing_enabled'):
    if policy[field] is not False:
        failures.append(f'Unsafe default: {field}')
if policy['minimum_notice_amount_cents'] != 1_000_000:
    failures.append('Minimum must be USD 10,000 in integer cents')
if policy['weekly_target_unique_taxpayers'] != 50 or policy['weekly_target_is_guarantee'] is not False:
    failures.append('Conditional target mismatch')
if set(policy['counties']) != {'dallas', 'collin', 'denton', 'bexar'}:
    failures.append('Four-county registry mismatch')
if any(c['enabled'] or c['access_decision'] != 'pending' for c in policy['counties'].values()):
    failures.append('Example county must remain disabled/pending')
for field in ('recency_days', 'required_contact_fields', 'delivery_weekday', 'delivery_timezone'):
    if policy[field] is not None:
        failures.append(f'Unapproved client default: {field}')
if len(list((root / 'planning/issues').glob('p[0-9][0-9]-*.md'))) != 12:
    failures.append('Expected twelve local issue drafts')
for path in (root / 'contracts').glob('*.columns.txt'):
    columns = path.read_text().splitlines()
    if not columns or len(columns) != len(set(columns)) or not all(re.fullmatch(r'[a-z][a-z0-9_]*', c) for c in columns):
        failures.append(f'Invalid headers: {path.name}')
if failures:
    raise SystemExit('\n'.join(failures))
print('PASS: internal links, disabled policy, four counties, amount/target, twelve issue drafts and headers.')
print('Not tested: runtime, live sources, security configuration, professional/tax clearance or deployment.')
