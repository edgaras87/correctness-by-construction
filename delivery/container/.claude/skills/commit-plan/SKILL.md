---
name: commit-plan
description: How work larger than one commit is sequenced into commits, reviewed at each boundary, and closed. Use before starting a Commit Set that needs more than one commit.
---

<!-- One of the Backend Kit's files: the Instruction Text of its Adapted Case for commit sets, an Agent Skill. Why it is as it is: its Adapted Understanding Text, kept in the Maintainer Repo. -->

# Commit Plan

A Commit Set is a body of work that needs more than one commit.
Its commits are planned before it starts, in its Commit Plan,
reviewed as they land, and closed.

**It plans the commits, not the change.** What is being changed is
settled before the Commit Plan is opened — in discussion, or in a record.
When it turns out not to have been, the Commit Plan is revised
(§5, *Divergence*) and the
Commit Set's ADR is still Proposed.

## 1. When a Commit Plan is needed

Why it is so: (commit sets, kept in the Maintainer Repo, §2, *What a Commit Set is*; records, kept in the Maintainer Repo, §4, *The plan*).

Write one when the work is worth splitting into more than one
commit. A single-commit change gets none: the Commit Plan costs two extra
commits, and pays for itself only across a sequence. Reach for one
especially when the split could turn out wrong halfway through, or
when someone other than the author reviews as it lands.

A Plan Step needs no Commit Plan when each of its stages is one commit or a few: the stages already list the commits. Open a Commit Plan only for a stage that takes many commits.

## 2. The Commit Plan

Why it is so: (commit sets, kept in the Maintainer Repo, §3, *The Commit Plan*).

One file, `COMMIT-PLAN.md`, at the repo root, one at a time:

```markdown
# Commit Plan: <what this Commit Set does>

## Summary — the state after all commits
<Prose. The end state, not the commits. What the repo looks like once
this is done, and what it gives us that it did not have before.>

## Commits

**1. `<type>(<scope>): <subject>`**
<What this commit does, or what it gives us, or both — whatever tells
the reader why this commit exists as its own commit.>

**2. `<type>(<scope>): <subject>`**
<…>

## Decisions taken inside this Commit Plan
<Judgment calls made while planning that a reviewer should see and
could reasonably object to. Optional, but usually the most useful
section.>
```

- Commit subjects follow the commit-messages Agent Skill. They are
  counted against its limit when the Commit Plan is written, not when each
  commit lands. A subject planned too long lands too long, or is
  rewritten at its boundary with nothing in the Commit Plan saying why. A
  subject the Commit Plan left provisional is written at its commit, and
  counted there by script before it lands. The note under each
  commit says why it is a commit of its own; the commit body is
  written at commit time.
- **The list may change past a point.** Commits near at hand are
  firm. Commits that a result not yet seen must shape are
  provisional and marked so; a provisional commit names its intent
  and defers its wording and exact split.
- **No status in the file.** No checkboxes. The commits that exist
  are the Commit Plan done so far.
- **A commit inserted later takes a letter,** `8b` after `8`, so the
  numbers already cited stay true.
- **A planned commit may repeat over a series,** when the same change
  reaches many records: "one commit per record, in this order". It
  names the order, and, if it may run again, the rule that stops it
  ("a second pass only over the records the first one changed").

## 3. How the commits are split

Why it is so: (commit sets, kept in the Maintainer Repo, §4, *How the commits are split*).

- **By change, not by file.** One commit is one coherent thing
  the repo needs, whatever files that touches; one file may appear
  in as many commits as it has distinct changes.
- **The test is revert:** undo one commit, and the repo lands in a
  coherent state. A module and the ARCHITECTURE paragraph mapping
  it are one commit; adding a Commit Plan, revising it and deleting it are
  three.
- **Order follows where the decision lives.** A decision settled in
  conversation runs decision-first: record it, then implement it. A
  decision only seeable in the material runs material-first: touch
  the material, let the shape emerge, write the durable record from
  what held. One Commit Plan may mix both, per decision. Two constraints
  either way: no commit references what does not yet exist, and
  durable records are caught up before the close.
- **Plan the records commits.** Walk the Entry File's records
  table: every record whose moment this Commit Set will create gets a
  commit, at the boundary where its truth exists. A Commit Set that closes
  a `PLAN.md` Plan Step Gate item names the commit that closes it. A change to
  the agent's own files is a commit of its own: an Agent Skill or Agent Rule corrected or added, and
  its Decisions Log entry. It is never
  folded into a records commit, since the two are kept apart
  (`.claude/skills/commit-messages/SKILL.md`, *The agent's own files*). A records commit planned to carry one has to be split
  when it opens.

## 4. The lifecycle

Why it is so: (commit sets, kept in the Maintainer Repo, §3, *The Commit Plan*; §6, *The close*).

| When | Commit | Contents |
|---|---|---|
| Open | `docs: add commit plan for <X>` | the approved Commit Plan |
| Work | the planned commits | as planned; stop at each boundary |
| Small commits | tries, fixes, a way abandoned | inside a planned commit, on the reviewer's grant; folded into it at its boundary (§6.2, *Small commits*) |
| Diverge | `docs: revise commit plan — <what changed>` | only when reality diverged; body says why |
| Close | `docs: close commit plan for <X>` | deletes the file; **body records what diverged** |

- Commit the Commit Plan after it is agreed and before any of the work.
- The close commit's body is the Commit Set's retrospective: what diverged
  and why. If nothing diverged, say so. An abandoned Commit Set closes the
  same way, with the reason.
- **An ADR inside the Commit Set opens as Proposed** and flips to Accepted
  in the Commit Set's final records commit, never in the close commit. An
  ADR committed Accepted early claims that no later boundary can
  contradict it. An abandoned Commit Set leaves its ADRs Proposed.
- **Before the close, sweep for every name the Commit Set moved.** When a
  commit renamed, renumbered, retitled or moved anything, grep Living Text
  for each old identifier, path, number and title: all of
  them, not the one being described. A
  renumbering moves every number, so the search is the whole span;
  the cheapest form is every old value at once. Grep the text
  unwrapped, its lines joined and its spaces squeezed
  (`tr '\n' ' ' | tr -s ' '`), since a name the file breaks across
  two lines is invisible to a line-by-line grep. What is history
  stays; what points at the old name from Living Text is the defect.
- **Before the close, look back at the landed commits as a whole.**
  Where a better grouping shows (two that are one change, or one
  that is two), propose it to the reviewer, regroup on the word, and
  revise the Commit Plan to match what landed. The look sees the planned
  commits, never the pile of small ones.

## 5. Divergence

When a commit needs something other than what was planned:

1. Stop before committing it.
2. Re-evaluate the remaining commits.
3. Revise `COMMIT-PLAN.md` and commit the revision on its own, with
   a body saying what forced it.
4. Continue.

Refining a provisional commit follows the same four steps, and is
planned refinement, not divergence; the close body distinguishes the two.

## 6. Review protocol

### 6.1 The stop at each boundary

Work stops at every commit boundary: stage, show the diff, commit
only on the reviewer's word. The rule is the commit-messages Agent Skill's, and binds
at every commit, not only inside a Commit Set (`.claude/skills/commit-messages/SKILL.md`, *Rules*).

### 6.2 Small commits

Where the reviewer has granted them, a planned commit may be built as several small
commits: a try, a fix, a way abandoned. Before its boundary, they
are squashed into the one commit the Commit Plan names, and the reviewer
reviews that. The small commits are kept on a local
`<branch>-detail` branch, so nothing tried is lost. Where the
reviewer lets small commits land as they go, they are grouped by
kind at the look back instead, and the `-detail` branch keeps them
the same way (commit sets, kept in the Maintainer Repo, §5, *At each boundary*). Each small commit follows the commit-messages Agent Skill too: subject
and body are counted when it is written, not at the regroup. Without
the grant, every commit is a boundary.

### 6.3 A second way

Why it is so: (commit sets, kept in the Maintainer Repo, §5, *At each boundary*).

At a boundary, when another way looks worth trying, name it beside the diff. Try it only on the reviewer's word, on a branch of its own, and compare the two before one is kept. Look for it while the choice is still open, not after the work.

## 7. A Commit Plan's anti-patterns

- **Commits grouped by file type.** Tidy-looking, reverts incoherently.
- **Checkboxes in the Commit Plan.** Status belongs to git history.
- **The Commit Plan written after the work.** A summary, not an agreement;
  nothing was reviewable and divergence is unrecorded. A provisional
  commit refined at its boundary is not this.
- **An ADR committed Accepted whose shape a later boundary decides.**
- **A Commit Plan for a single commit.**
- **The file kept after the close.** History keeps it.
- **Silent divergence.** Doing something other than the Commit Plan and
  fixing the Commit Plan afterwards, or not at all.

---

## Decisions

- ADR-0038, 1b — a separate convention; the Commit Plan is temporary,
  not a record
- ADR-0038, 1d — §3: a Commit Set that closes a Plan Step Gate item
  names the commit
- ADR-0038, 1e — §3: order follows where the decision lives;
  §2: provisional commits; §4: ADRs open Proposed
- ADR-0038, 1f — §6: the stop at every boundary is
  the commit-messages Agent Skill's
- ADR-0049, 1 — a Commit Plan counts commits; "step" is
  `PLAN.md`'s
- ADR-0049, 3 — §4: the sweep greps the text unwrapped
- ADR-0050, 1–3 — §6: small commits on the reviewer's grant, each
  counted when written; §4: a look back before the close
- ADR-0050, 4–5 — §2: an inserted commit takes a letter; a
  planned commit may repeat over a series
