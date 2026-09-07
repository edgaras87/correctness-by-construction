# Handoff from correctness-by-construction — 2026-09-08

<!-- Staging copy, tracked in temp/ while it is shaped; deleted
     once the handbook's reply is absorbed. Substance is on record
     in this repo's TODO (gates-experiment item, the 2026-09-07/08
     notes), .claude/decisions.md (2026-09-07 entry), and the
     devlog. -->

From the concepts tier (correctness-by-construction). Context
first: run 3 of the pure seed closed Step 0 and waits on its
briefing; before the briefing it receives four pieces of working
arrangement on trial, evaluated at its retrospective for folding
back to the kit stub or the bundle. This repo already took one of
them for itself. Four asks, one FYI. What we need back is at the
end. Nothing here blocks us.

## 1. Ask: the agent model, three observations

All three read against models/agent.md §4, §7, §8 as pinned here
(@ 4fe8083). The model already holds the vocabulary; what follows
is the model applied to a rule that kept failing.

**The reviewer's pace was a §8 diagnostic, and the model's own
table names the fix.** "Stage, show the diff, commit only on the
reviewer's word" lived in change-plans §6 — a pulled channel that
fires only for multi-commit work. Single commits never opened it,
so the human said the rule again every session: §8's last row,
"stated by a human repeatedly — a convention is missing, or its
channel is not firing." By the table, a rule bound to a specific
action is pushed (the commit-messages skill fires at commit time
and carries no stop today), and a rule that must never be violated
adds a gate. We propose both: one sentence in commit-messages at
the moment of committing, and the gate below.

**§7 has a gate with no machinery.** The harness's permission
rules are a gate the kit can ship as repo state:
`{ "permissions": { "ask": ["Bash(git commit *)"] } }` in a
tracked .claude/settings.json stops every commit at a prompt the
human answers — no hook, no CI, nothing to maintain. §7 lists
hooks, CI, and human review; this is the cheapest of the kind and
worth naming.

**Told has a persistent form, and the model does not say whose
the text is.** CLAUDE.local.md is ambient in delivery — loaded at
session start beside the project's entry file — but told in
ownership: one person, one checkout, ignored by git by the
harness's own convention. It is where the human's standing
instructions go without becoming project text or a convention.
§4 classifies channels by when they fire; an ownership note
(project's text vs the operator's) would let the model say why
such a file is ignored and why its words never enter records.

## 2. Ask: the handbook's own CLAUDE.md under .claude/

The harness reads `./CLAUDE.md` and `./.claude/CLAUDE.md` as two
addresses of one scope. We moved ours on 2026-09-07 (ebd1416): a
pure rename, one codemap row, one decisions entry. The pinned
commit-messages split needed no edit — its "`.claude/`" term
already covers the moved file — and every other mention names the
file, not its path. Every agent-side file now sits in one
directory, and the agent/project split reads as "under .claude/ or
not." We ask the handbook to take the same shape for itself.

## 3. Ask: the kit stub at .claude/CLAUDE.md

Same move for starter/kit: CLAUDE.md becomes .claude/CLAUDE.md,
content unchanged, and the install block's paths follow. Our
pure-seed install delivers the entry file to wherever the stub
lives, so it follows the stub's address at the next pin. Run 3
trials this exact move before its briefing; its Step 1 reading
will show whether the harness read the file there and whether the
rename stayed pure.

## 4. Ask: two starting templates in the stub

- **.claude/settings.json**, tracked, holding the one ask rule
  from §1. JSON carries no comments, so its why lives in the kit's
  decisions.md entry and the install block; reusable inserts later
  are jq merges, not text edits.
- **CLAUDE.local.md**, shipped as a committed shape beside the
  real thing — the kit's gitignore already uses that pattern for
  .env.example — with a gitignore line for CLAUDE.local.md itself
  and an install step that copies the shape into place, untracked.
  Its starting content is the reviewer's pace: staged and shown
  first, commit on the word, one decision at a time, no push.

Both are on trial in run 3 from its Step 1, alongside the branch
rule (each step on its own branch, fast-forward merged after its
gate closes) and the move in §3.

## FYI: where the evidence lands

Run 3's pre-briefing session installs all four pieces in two or
three agent-split commits, recorded as decisions entries and one
TODO Later item. The first reading is at its Step 1 boundary; the
fold-back decision is its retrospective. A reply can wait for the
Step 1 reading or not — §1 and §2 are the handbook's own and need
no run evidence; §3 and §4 gain from it.

## What we need back

- On §1: whether the model gains the two notes (harness permission
  as a gate; ownership of ambient text) and the commit-messages
  sentence — or where you'd put the pace instead.
- On §2–§4: yes, no, or wait for run 3's Step 1 reading. If yes on
  §3 or §4, the new kit pin, so pure-seed and the fills follow it.
