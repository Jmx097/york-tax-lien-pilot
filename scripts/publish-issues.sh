#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO="Jmx097/york-tax-lien-pilot"
MODE="${1:---dry-run}"
if [[ $# -gt 1 || ( "$MODE" != "--dry-run" && "$MODE" != "--publish" ) ]]; then
  echo "Usage: bash scripts/publish-issues.sh [--dry-run|--publish]" >&2
  exit 2
fi
if [[ "$MODE" == "--dry-run" ]]; then
  echo "PREVIEW ONLY: no GitHub writes. Target: $REPO"
  for file in "$ROOT"/planning/issues/p[0-9][0-9]-*.md; do
    title="$(head -n 1 "$file")"
    printf '%s\n' "${title#\# }"
  done
  exit 0
fi
command -v gh >/dev/null || { echo "Install GitHub CLI and authenticate locally." >&2; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "No authenticated CLI session; nothing published." >&2; exit 1; }
echo "Review public-data safety before creating issue text in $REPO."
read -r -p "Type the full repository name to confirm: " confirmation
[[ "$confirmation" == "$REPO" ]] || { echo "Cancelled; nothing published."; exit 1; }
EXISTING="$(gh issue list --repo "$REPO" --state all --limit 1000 --json title --jq '.[].title')"
for file in "$ROOT"/planning/issues/p[0-9][0-9]-*.md; do
  title="$(head -n 1 "$file")"
  title="${title#\# }"
  if grep -Fxq -- "$title" <<< "$EXISTING"; then
    echo "Skip existing exact title: $title"
  else
    gh issue create --repo "$REPO" --title "$title" --body-file "$file"
  fi
done
