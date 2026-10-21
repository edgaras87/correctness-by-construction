#!/usr/bin/env bash
# The reviewer's harness for the full-auto run. Runs at every Stop.
# Lets the agent stop only when Release's step in PLAN.md is closed,
# or when the reviewer has put a file named `stop` beside this
# script. Otherwise it refuses the stop and points at the records.
# Claude Code ends the turn anyway after repeated refusals with no
# tool call in between, so a truly stuck agent is not looped forever.
plan="${CLAUDE_PROJECT_DIR:-.}/PLAN.md"
halt="${CLAUDE_PROJECT_DIR:-.}/.claude/hooks/stop"
[ -f "$halt" ] && exit 0
if grep -Eq '^## Step [0-9N]+: Release[^[]*\[x\]' "$plan" 2>/dev/null; then
  exit 0
fi
cat <<'JSON'
{"decision": "block", "reason": "Release's gate is not closed, and this run has no stops. Read PLAN.md's open step, its Now line and its gate, and the devlog's Resume line, then continue from there. If a step is blocked, docs/run.md says what to do: log it blocked, close the step without it, and go on. Only a closed Release ends the run."}
JSON
