# Kickoff for run 4, 2026-10-15

<!-- A draft on its way to a run: the first and only message the
     reviewer pastes into run 4's session (`~/IdeaProjects/
     cbc-pure-run-4`), after `claude --permission-mode auto` in
     that directory. Written here by the deliverer from run 3's
     hand-off (never-oversold, RUN-4.md at dac4dd1) and the pure
     seed's birth prompt, merged for a run with no reviewer at the
     gate. Deleted once the run has started and the devlog says so;
     git history keeps it. -->

```text
Build safe-reservation-2 from this seeded repo, on full auto: from the
first commit through Release, with no stops. I am not watching.
Nothing in a skill or a rule that asks for my sign-off waits for me:
the first entry in .claude/decisions.md delegates every one to you,
and docs/run.md says how each is taken.

The repo was seeded, not born whole. The branch birth-seed shows
it: the records, the entry files and the hygiene base from the
correctness-by-construction container; docs/concept/, the skills,
rules, shapes and check script from run 3 of this same problem;
the steps in PLAN; this run's own inputs; and the reviewer's stop
hook, an agent file, which with the reviewer's ignored local
settings keeps this run going until Release. Main holds the same
files untracked above the hygiene commit; the branch is a receipt,
never merged, never deleted. Step 0 is finishing the birth: read
the whole repository first, every file and every seed commit, then
commit it all on main under your own sequence and the commit split
the skills define, the record stubs filled, Step 0 closed on its
gate.

Read first: docs/run.md, then docs/settled.md, then
docs/system/framing/briefing.md, then docs/concept/00-cbc.md.

Settled decisions (docs/settled.md) say what the system is, and
are not reconsidered. Write them into the records in your own
words. How it is built is yours to derive: the facts that can
hurt, the kills, the slices, the ground, the door, the walls, the
code, the tests. The store and containers are this project's own,
named for it. Read nothing of run 3: not its records, its code or
its files. The settled list's source lines are for me.

A new question: classify it Small, Real or Conflict, and follow
docs/run.md. Try the options of a Real or Conflict question before
choosing. Log every decision in docs/decision-log.md.

When the work shows a skill, rule or shape wrong or missing
something, fix it as docs/run.md says, and log it.

Commits: one branch per step; small commits; agent files apart
from project files; regroup at the close, keep -detail, fast-forward
main, tag run4/step-<n>. Never push. Never delete a branch. Never
change anything outside this directory.

If you find yourself resumed, in a new or compacted session: read
PLAN's open step, its Now line and its gate, and the devlog's
Resume line, then continue from there with no stop. Do not re-read
the whole repository; the records are the memory.

Auto ends when Release's gate closes. Until then, a turn that ends
with work still open is a stop, and there are no stops.
```
