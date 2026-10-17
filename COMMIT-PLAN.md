# Commit plan: our plan holds the step being worked

## Summary — the state after all commits

This repo's `PLAN.md` holds the one piece of work being done now, as
a step in the run's form, and no milestones. A step is a reading, or
a TODO item big enough for a branch. Its gate is written when it
opens, and it leaves the plan at its close, the devlog naming it.
`## The step form` at the top of PLAN says how, with a Known already
list for a reading. Step 10 and Release are gone from PLAN: the
birth joins `exchange-birth` in TODO, our retrospective is a TODO
item due at the birth step's close, and Release waits in Later.
PLAN says no step is open until run 3's reading closes.

ADR-0057 records it, amending ADR-0041's decisions 1 and 2 and
ADR-0056's decision 6. The manuals' deliverer seats say steps, not
milestones; the reasons that rested on "no steps and no gates" are
rewritten; our `first-time-work` skill opens at a step's opening
item too. W13 of the reading of run 3 is done.

## Commits

D9 is settled in the reading's commit before this plan.

**1. `docs(agent): add commit plan for plan steps`**
The approved plan.

**2. `docs: ADR-0057 proposes steps in our plan`**
ADR-0057, Proposed: D9's seven decisions; the evidence, 3 of 364
commits since ADR-0041 touching PLAN, and the reading's gate living
outside it, which is ADR-0041's own reopen condition; the options
rejected at each decision.

**3. `docs: project-recording gives our plan steps`**
The deliverer seat: PLAN holds the step being worked, not
milestones; recurring work, a reading, is a step; the two
retrospective jobs close every step; the retrospective's trial at
the birth step's close, not Step 10's; the step form lives in our
PLAN. A dated lesson under the 2026-09-29 one. The body names the
foundation check's ending.

**4. `docs: our seats close a step, not a milestone`**
retrospective's deliverer seat: "its milestones closed", "At Step
10's close", "the next milestone". agent-arrangement §2.4's last
line: `CLAUDE.md` re-read at each step's close.

**5. `docs: shapes and manuals stay rules with steps`**
shapes' deliverer seat and conventions §3.3 said the deliverer has
no steps and no gate. Both now give the reasons that hold with
steps: a reading's form must hold while it is worked, and it is
deleted at the close; a manual is edited outside any step.

**6. `docs: first-time work opens at a step too`**
The first-time-work manual: our skill's line in *What this is made
usable as*, and "Our skill opens" in our seat, name the three
moments.

**7. `docs: our plan holds the step being worked`**
`PLAN.md`: the header comment rewritten; `## The step form`, ours,
with a reading's Known already; "No step open", with run 3's
reading named; Step 10 and Release gone.

**7b. `docs: a step takes the gates of its skills`**
Added on the reviewer's question: PLAN's form listed a reading's
close items, a second home for what its rule holds. project-
recording's seat: a step's gate takes the gates of what it uses, as
a run's does, and the rest is written when it opens. PLAN's Known
already says that, with no list; the reading's list and stages go.
ADR-0057's decision 3, still Proposed, says the list is the rule's.

**8. `docs: TODO takes Step 10 and Release`**
`exchange-birth` gains the birth, trigger run 5's birth; a new item,
our retrospective, trigger the birth step's close; Release to Later
with its four own items; the triggers that named Step 10 or
Release's gate rewritten.

**9. `chore(agent): our skills and rules open at a step`**
Our `first-time-work` description: the three moments.
`working-a-reading.md` gains *Gates*: a reading's five close items
as outcomes, and its stages for a step's Notes; step 9 keeps the
how and points at them. `exchange-read` step 4: "the shape" becomes
`.claude/rules/exchange-reading.md`. `CLAUDE.md`'s PLAN row: opening
a step, or closing its gate. `.claude/decisions.md`: one entry for
the arrangement, with the two reading rules kept apart on their
foundations, since the 2026-10-01 entry's reason, a shape is form
only, no longer holds.

**10. `docs: the front door and map name the step`**
README's Plan row; `ARCHITECTURE.md`'s codemap line for `PLAN.md`.

**11. `docs: records carry our plan's steps`**
ADR-0057 Accepted. ADR-0041's and ADR-0056's Status lines gain
"amended 2026-10-17 by ADR-0057", with an italic at each amended
decision, as ADR-0024 carries.

**12. `docs(agent): close commit plan for plan steps`**
Deletes this file; the body says what diverged.

After the close, the reading marks W13 done:
`docs(temp): the reading closes W13`.

## Decisions taken inside this plan

- **Manuals before what derives from them.** project-recording
  before PLAN and TODO; first-time-work's manual before our skill.
- **7b before 9.** PLAN's Known already points at what a step
  uses; the reading's gates then land in its rule, in the agent
  commit.
- **The old ADRs are amended at the records commit,** once
  ADR-0057 is Accepted, not while it is Proposed.
- **One agent commit.** Every agent file follows from the
  decisions above; none decides anything of its own.
- **Run 3's reading is left as it is,** by decision 3: no step is
  opened for it.
