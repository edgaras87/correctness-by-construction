# Commit plan: stopping a step

## Summary — the state after all commits

A step can stop when another must come first. The step stays in
`PLAN.md`, marked `[!]` with the step that comes first, and its Now
line keeps the stage it stopped at. It resumes at that stage, and a
stage whose input the other step changed runs again.

The refinement of this repo is the first to stop. Its rule check
was two manuals of three in when the reviewer chose to redesign the
conventions first: rounds read against the conventions convention,
so the redesign comes before them. Main takes the refinement's
branch so far, by fast-forward. The redesign opens as a step on its
own branch, cut from main, above the stopped refinement.

Writing rule 8 lands in our own copy, and the writing manual's
check gets its result, so the stopped step's file says where each
of its three manuals stands. TODO asks how commits cited by hash
could still be regrouped.

## Commits

**1. `chore(agent): writing rule 8 in our own copy`**
Our `.claude/rules/writing.md` follows the manual and the shipped
rule (`8e86560`), with an example from this repo. An agent file,
so a commit of its own.

**2. `docs: a step can stop for another to come first`**
The description and every form derived from it, in one change:
project-recording §2, both seats; the playbook's step form for
runs; the container's `PLAN.md` stub legend; our `PLAN.md`'s step
form and legend. The stopped line names the step that comes first
and points at the devlog entry that says why; the why itself is
the devlog's. All project files, so the foundation check's walk
lands in this commit.

**3. `docs(temp): the writing manual's check, its result`**
The refinement's file records the writing row: rule 8 fixed, by
its commits. Then all three manuals have a result before the step
stops.

**4. `docs: TODO asks how cited commits can regroup`**
A TODO item, and its story in the devlog, written as it is added:
commits cited by hash cannot be regrouped without breaking the
citations, so the history keeps every small fix. A records change
of its own.

**5. `docs: the refinement stops for the redesign`**
The refinement's step in `PLAN.md` takes `[!]`, the step that
comes first, and the stage it stopped at. The devlog says why it
stopped. Under the form commit 2 wrote.

Then, before the fast-forward, the look back of `commit-plan` §4
runs over commits 1 to 5, and they are regrouped on the reviewer's
word if a better grouping shows. Then, on the reviewer's word and
not a commit: main takes `refinement-2026-10-18` by fast-forward,
and the redesign's branch is cut from main.

**6. `docs: the conventions' redesign opens as a step`** *(provisional)*
On the redesign's branch: its step goes into `PLAN.md` above the
stopped refinement, with its gate written before any work. Its
goal and gate are settled with the reviewer at this boundary; the
evidence it starts from is the six maintenance pains of
2026-10-19.

## Decisions taken inside this plan

- **A stopped step uses `[!]`,** the existing blocked mark, with
  "stopped: <the step> comes first" as what unblocks it. Rejected:
  a new mark, one more symbol for one more state that the old one
  already says.
- **Main takes a stopped step's branch so far.** The next step is
  then cut from main, as the step form asks, and holds the work it
  builds on. Rejected: cutting the redesign from the refinement's
  branch, which breaks "cut from main" and leaves main behind.
  Nothing is rebased.
- **Commit 2 is one commit** for the manual and its three derived
  forms: one change, and neither side is an agent file.
- **The look back runs before the fast-forward,** not at the
  plan's close: after it, the commits are on main, and main is
  never rewritten.
- **The refinement's commits before this plan are not regrouped.**
  Their hashes are cited in the refinement's file, the devlog,
  TODO and other commit bodies, and a regroup would break each
  citation. Each was also reviewed as it landed. How cited commits
  could regroup is commit 4's TODO item.
- **No skill changes.** No skill opens, stops or closes a step.
- **Commit 6 is provisional.** The redesign's goal and gate are
  the reviewer's to settle when it opens; this plan only places
  the commit.
