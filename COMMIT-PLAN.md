# Commit plan: the text-division item closes

## Summary — the state after all commits

This repo's text is divided by kind, and the kinds are a model of
their own, `docs/models/idea-to-output.md`.

- ADR-0063 records the decisions taken in the talk of 2026-10-23
  and 2026-10-24 (`TODO-CONVERSATION-MEMORY.md` §1, last whole at
  this plan's opening commit).
- The idea-to-output model states the kinds, model, description,
  approach, output and shape; their links; and both directions.
- A model binds what stands on it: "binds nothing" leaves both
  models' headers.
- **One root, tags for parts.** A file names one `foundation`, what
  the whole of it was written from: in frontmatter, or in a
  record's header comment. Every line that uses a particular part
  of any document, its root included, carries a tag to that part.
  A manual's root may be a model.
- The agent's chain, rechecked (question 6), is fixed where it
  failed: agent-arrangement names its model as its root; the agent
  model's §1 points at tiers; each manual's *Why it arrives this
  way* tags the part of the agent model it reasons from.
- Both entry files keep one `foundation`, agent-arrangement; the
  records table's comment tags project-recording §13.
- The held questions are TODO items; the text-division item, the
  records-table item and the item's conversation-memory section go.

## Commits

**0. `docs(agent): add commit plan for text division`**
Opens the set.

**1. `docs: ADR-0063 text is divided by kind`**
The ADR, Proposed. Every later commit stands on it.

**2. `docs: the idea-to-output model`**
The model, new in `docs/models/`. Nothing stands on it yet, so it
lands alone.

**3. `docs: one foundation per file, tags for parts`**
Conventions §2: a model is a value of `foundation`. §3.5 step 2:
one `foundation` per file, the root; a line using a part of any
document carries a tag. §3.3: a manual's *Why it arrives this way*
tags the part of the agent model it reasons from.
`ARCHITECTURE.md`'s *The words*: foundation names a manual too, and
is one per file. One rule and its retellings.

**4. `chore(agent): the manual's form and the check`**
`.claude/rules/convention-manual.md`: a manual may open with
frontmatter naming its model; its item 7 asks the channel section
to tag the agent model where it reasons from it.
`.claude/rules/foundation-check.md` step 1: a model is a
description, and a record carries one `foundation:` line. The
agent's own files, next after commit 3.

**5. `docs: channel sections tag the agent model`**
Each of the 11 manuals' *Why it arrives this way* gains a tag where
its reasoning rests on the model: the channel it picks (§4), the
choice (§8), or a claim (§12). A tag to agent-arrangement §3.2
already reaches the model through that host, and stays. One change
over 11 files, so one commit.

**6. `chore(agent): the records table tags its rules`**
Our `CLAUDE.md`: the records table's comment drops its
`foundation:` line for a tag to project-recording §13. The guard's
line, agent-arrangement, stays the file's one root.

**7. `fix(delivery): the records table tags its rules`**
The same in the container's entry file. A delivery file apart from
our own, by precedent (`e0e426b`, `d19e37e`).

**8. `docs: models bind what stands on them`**
"Binds nothing" leaves the headers of `docs/models/agent.md` and
`docs/models/tiers.md`. agent-arrangement gains
`foundation: the agent model`. One decision: the first manual to
stand on a model, and the models that now bind it.

**9. `docs: the agent model's §1 points at tiers`**
§1 keeps whose case the model is tuned for, and points at
`docs/models/tiers.md` §2.3 for how the repos relate. Its own
commit: a retelling removed, not a decision.

**10. `docs: the text-division item closes`**
The final records commit. ADR-0063 Accepted. TODO: the item goes,
and so does the records-table item (`df1540b`), answered by
commits 6 and 7; three held questions become items (ship the
model?, a model to approach link, a model for one convention); the
fold item's trigger line is rewritten true for today, not stacked
with a date. TODO is grepped for items waiting on the text-division
item: "Choose whether a manual is called a concept", whose trigger
names an item that does not exist and meant this one, and "Decide
whether a session's end has a home of its own". Each one's trigger
is rewritten true for today. `TODO-CONVERSATION-MEMORY.md` §1 goes,
the file stays.

**11. `docs(agent): close commit plan for text division`**
Deletes this file; the body says what diverged.

## Decisions taken inside this plan

- **Round 2 keeps its part.** Moving conventions §1 to the model,
  staying in step as a convention, the hand-off chain's rename,
  *The words*' "model" entry and the requires grep in the walk are
  round 2's, as decided. So is the tag's exact form, how a run's
  ids serve as tags, and the walk's grep for each.
- **Only the agent model gets a manual standing on it.** No manual
  is named as standing on tiers; that is not decided.
- **One root, tags for parts.** A second `foundation` in one file
  is a tag. The root tells the foundation check which document to
  open; a tag tells the walk which line to re-read. This replaces
  the earlier rule of a comment for each part's `foundation`.
- **The channel link is a tag in each manual.** A manual as a whole
  stands on its own convention; only its channel section reasons
  from the agent model. A pointer in the form alone would leave the
  walk unable to find the 11 sections when the model changes.
- **The devlog** is written at the session's end: the item's story,
  the commit where §1 is last whole, two delegation lines and the
  missing-context finding.
