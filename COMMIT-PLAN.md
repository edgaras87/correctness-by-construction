# Commit plan: small steps

## Summary — the state after all commits

The commit-plan convention carries what run 3's Step 10 lived (its
RETRO.md, D19): a planned commit may be built as small commits, on
the reviewer's grant, kept on a `<branch>-detail` branch and folded
into the planned commit at its boundary; each small commit follows
commit-messages when written; before the close, the landed commits
are looked at as a whole and regrouped on the reviewer's word; a
commit inserted later takes a letter; and a planned commit may
repeat over a set, naming its order and its stop rule. ADR-0050
records it, with what was rejected. The manual, the shipped skill
and our own copy say it alike, and the two skill copies stay equal.
TODO's watch on provisional commits closes, its trigger fired.

## Commits

**1. `docs(agent): add commit plan for small steps`**
This plan, agreed.

**2. `docs(adr): 0050, small steps and a look back`**
The decision, opened Proposed: the five rules, the reviewer's grant
added to the first, and the options rejected (RETRO D19's three; and
the first rule as run 3 wrote it, which let small commits land
without a grant that commit-messages requires).

**3. `docs: small steps inside a planned commit`**
The manual and the shipped skill together: small steps on the
reviewer's grant, the `-detail` branch, each counted when written;
the look back before the close. The lifecycle table gains its row.
One change: the work inside a planned commit, and its review.

**4. `docs: a plan's list takes letters and repeats`**
The manual and the shipped skill: a commit inserted later takes a
letter; a planned commit may repeat over a set, with its order and
stop rule. A change to the plan file's form, apart from commit 3's
change to the work.

**5. `chore(agent): our commit-plan follows suit`**
`.claude/skills/commit-plan/SKILL.md` brought to the manual, equal
to the shipped copy again. The agent's files, a commit of their own.

**6. `docs: records carry the small steps`**
ADR-0050 Accepted; TODO's watch on provisional commits closes,
answered by commit 4.

**7. `docs(agent): close commit plan for small steps`**
Deletes this file; the body says what diverged.

## Decisions taken inside this plan

- **Commits 3 and 4 split the five rules by what they change**: how
  a planned commit is worked and reviewed, against how the plan's
  list is written. Reverting either leaves the other coherent.
- **No decisions-log entry.** Commit 5 brings our skill to its
  manual, which the log's header says is no decision; the ADR holds
  the why.
- **The devlog is not in this set.** It is written at the session's
  end, with the rest of the reading's work.
- **The reading's marks stay outside.** F5 is marked taken in
  `temp/` after the close, as every item has been.
- **The manual's lessons are run 3's, dated.** No set here has used
  small steps yet; the manual says so rather than claiming our own.
