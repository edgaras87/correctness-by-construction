# Commit plan: tagged retelling

A design change inside the refinement
(`.claude/approaches-on-trial/refinement.md` §2.7), from TODO's Now:
round 1's DECISION-3 and its findings on retellings rest on it.

## Summary — the state after all commits

One home per fact gains a general rule: a fact may be retold
beside its pointer where the reader acts on it in place, if it
carries a tag, a label grep finds, defined at the fact's home. When
the fact changes at its home, every tagged retelling is found and
re-read with the paragraph around it, and a host that is itself a
source walks on. Elsewhere: point, don't retell.

Each case applies it with its own tag and its own moment. Ours is
applied now: a manual's path and section, re-read by the walk at
every commit. A run's case, its invariants, kills and slices
tagged by id, is designed with the convention round 2 makes, so
the container's rule changes once, then.

The rule changes where its pieces live today. Project-recording
§11 leads with the general rule. Conventions §3.2 and §3.5 are our
case's tag and re-read; §3.1 and the manual form gain the
exception. Round 2's Layout finding names the convention of its
own that will hold the general idea, with a rule for each case.

## Commits

**1. `docs(agent): add commit plan for tagged retelling`**
This file.

**2. `docs(adr): ADR-0059 tagged retelling, proposed`**
The choice and the ways rejected: the rule kept as it is; retelling
allowed everywhere; a third home made now; the whole subject moved
into one of the two manuals; the run's rule widened now, before its
case is designed.
Decision-first: settled in conversation, from a sample the
reviewer judged.

**3. `docs: a retelling may stand, tagged to its source`**
Project-recording §11, rule 1, in general terms: the follower
bullet widens from "cannot be avoided" to "the reader acts on it in
place"; the tag is a label grep finds, defined at the fact's home;
changing a fact at its home re-reads each tagged retelling. Its
seats say each case has its own tag and moment: ours is
conventions §3.2 and §3.5; a run's comes with round 2's
convention. Foundation check: the container's `one-home.md` stays,
by that seat line.

**4. `chore(agent): our one-home allows tagged retelling`**
`.claude/rules/one-home.md` rules 2 and 5 follow §11. Agent side of
commit 3.

**5. `docs: conventions tag and recheck a retelling`**
§3.1's "stated twice" gains the exception; §3.2 says a retelling's
pointer always names its section; §3.5 step 3's walk re-reads each
tagged retelling of the changed section, with its paragraph, and a
host that is a source walks on.

**6. `chore(agent): manual form and check follow`**
`.claude/rules/convention-manual.md` item 5 gains the exception.
*Provisional:* `.claude/rules/foundation-check.md` points at §3.5
step 3 and may need nothing; read at the boundary.

**7. `docs(temp): round 2's Layout finding names a home`**
The refinement's file: the Layout note on staying in step names a
convention of its own as the candidate fix: the general idea in
its manual, and a rule for each case, ours (manuals, path and
section, the commit's walk), a run's (invariants, kills, slices,
tagged by id), and records linking records. DECISION-3 notes what
this settled for it.

**8. `docs: ADR-0059 accepted; TODO's item closes`**
The final records commit: the ADR flips, and TODO's tagged-retelling
item goes. The devlog names it at the session's end.

**9. `docs(agent): close commit plan for retelling`**

## Decisions taken inside this plan

- **Ours now, a run's in round 2.** The rule is general, and a run
  can re-read when it changes a fact. But its case, which ids are
  tags and when they are re-read, is designed once, with round 2's
  convention, so a shipped rule changes once. No run is born
  before then.
- **The content changes in today's homes.** Moving the subject to
  one home is round 2's Layout work, on text round 1 has made true.
- **No devlog commit inside the plan.** Today's entry was written
  mid-session; this goes in the session's closing entry.
- **DECISION-3 is not ended here.** It is narrowed: a retelling's
  pointer must carry path and section. Whether every plain pointer
  must is still its question.
