# Commit plan: the redesign hands over to the refinement

## Summary — the state after all commits

The redesign of the conventions has closed. Its two iterations
turned out to be refinement work: text brought up to rules that
already exist, under One home, Agreement and Writing. So the
refinement resumes at its rule check, and goes through the
conventions manual again, section by section, top to bottom.

Nothing the redesign found is lost. Its first fix, the manual's
top line (`ac796df`), counts as the rule check's. The agreed
rewrite of "What it is for" waits in the refinement's file, to be
applied first. Its design ideas wait in TODO, each with a trigger.
Its two lessons that held live in the refinement's manual.

## Commits

**1. `docs(temp): the redesign hands its work over`**
The refinement's file gains a note in its rule check: the top
line done at `ac796df`; the agreed "What it is for" rewrite, with
the two details for §3.3; the idea to split §3.3 into numbered
parts, for when the walk reaches it; and the walk itself, section
by section.

**2. `docs: TODO keeps the redesign's design ideas`**
TODO items for the targets the walk will not reach: a model apart
from a manual, and the names, concept or convention. Sub-ideas,
their picture and the links' upkeep are the walk's, and the note
says so. The regrouping item's trigger moves from the redesign to
the refinement's close. Their story goes in the devlog as each is
added.

**3. `docs: the rule check fixes in place, then judges`**
The refinement's manual, §2.3: before a fix adds anything, it
looks for the place that should already do the job; and each fix
to a manual is judged on maintenance, readability,
future-proofing and complexity before the next. The two lessons
the redesign's iterations showed.

**4. `docs: the redesign's manual and file go`**
`docs/conventions/conventions-redesign/` and its file leave: the
work it described was a refinement's. Its trial ends as dropped,
which the devlog in commit 5 records.

Then, on the reviewer's word and not a commit: main takes
`redesign-2026-10-19` by fast-forward.

**5. `docs: the redesign closes; the refinement resumes`**
On main, one commit, as the step form asks for a close: the
redesign's step leaves `PLAN.md`; the refinement's step is `[~]`
again, its Now line the rule check, the conventions manual
section by section; the devlog entry says why the redesign
closed and what it handed over.

**6. `docs(agent): close commit plan for the handover`**
On main. Then, on the reviewer's word and not a commit:
`refinement-2026-10-18` is fast-forwarded to main, and the work
goes on there.

## Decisions taken inside this plan

- **The redesign's manual is dropped, not kept.** Its stages were
  the refinement's rule check under another name; keeping both
  would give one way of working two homes. Rejected: keeping it on
  trial for a real design question later. If one comes, the TODO
  items hold the ideas, and first-time work starts again.
- **The "What it is for" rewrite waits in a note.** It was agreed
  under the redesign, but it is refinement work, so it lands under
  the refinement's step. A backup of the exact diff is kept
  outside the repo until then.
- **The top line at `ac796df` stays as it landed.** It is history;
  the note counts it toward the rule check.
- **Commit 5 is on main,** by the step form's close: the step is
  removed after main takes its branch.
- **The look back** over commits 1 to 4 runs before the
  fast-forward, as in the last plan.
