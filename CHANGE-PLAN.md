# Change-plan: decide-first, and two renames

Ordered so that nothing expensive is built on an unvalidated
decision — which is the thing this set exists to write down. The
step most likely to be wrong is step 4, and the two commits before
it are cheap and independent of it.

## Summary — the state after all commits

A skill, `decide-first`, sits before a commit plan and fires only
when a question would change the *shape* of a set rather than one
of its steps. `format-comparison` is `option-comparison`, widened
from questions of form to any question whose options can be built
cheaply enough to look at. The convention formerly called
`change-plans` is `commit-plan`, in this repo and in what we ship,
with `bundle-update.md` taught the case it lacked — a renamed
convention leaves its old directory in a run unless something
deletes it.

## Commits

**1. `docs(agent): add change-plan for decide-first and two renames`**
This file. Written under the convention it renames, and renamed by
step 6 with everything else.

**2. `docs(adr): the cascade wins; decide-first, and two renames`**
ADR-0030, opening **Proposed**. Carries the third run of the
comparison method: six requirements written before any candidate,
four candidates built, why three lost, and the finding that decided
it — the cascade surfaces a step the other three shapes do not
contain. Then the three decisions that follow. The temp draft
cannot be deleted before this exists (the method's §2 step 6).

**3. `chore(agent): format-comparison becomes option-comparison`**
The rename, and the widening that justifies it: the method's real
constraint was never *form*, it was whether the options can be
built cheaply enough to look at. Evidence is yesterday's `stack/`
quarantine — built, looked at, found wrong — which was a structure
question the skill's own §1 would have excluded. §1 widens and the
render stays the gate that keeps unbuildable options out.
**Before step 4, though less risky than it**, because `decide-first`
will name this skill and should name it once.

**4. `feat(agent): decide-first`**
**The step most likely to be wrong.** Its own objection is in the
ADR: the routing step has one destination filled in, so the skill
may be a wrapper around `option-comparison` with two empty slots.
Building it is the only way to find out and costs one file. If it
is a wrapper, the set stops here and the ADR is revised — steps 6
to 8 survive either way, because "change-plan" reads as *plan the
change* whatever else is true.

**5. `docs(agent): register decide-first`**
`.claude/decisions.md`. Its own commit because HANDBOOK ADR-0019
keeps the agent's files out of project commits, and because step
4's outcome may change what this entry says.

**6. `docs(conventions): change-plans becomes commit-plan`**
The manual, the shipped skill under
`delivery/container/.claude/skills/`, the delivery's references,
and this file's name. The project half.

**7. `chore(agent): our copy and the registry follow the rename`**
`.claude/skills/` and the registry entry. Separate from step 6 for
the same reason step 5 is separate.

**8. `docs(delivery): bundle-update learns the renamed convention`**
The gap the rename exposed: the procedure copies conventions by
name, so a rename installs the new directory and leaves the old one
in the run forever. It will recur whatever we decide here.

**9. `docs(adr): accept 0030, and the records catch up`**
The final records commit. ADR-0030 flips to Accepted here and
nowhere earlier; TODO's change-plans watch is retargeted or closed;
devlog takes the session; the temp draft is deleted, having served.

**10. `docs(agent): close the plan`**
Deletes this file, under its new name. The body records what
diverged.

## Decisions taken inside this plan

- **Ordered by what rests on it, not strictly by risk.** Step 3 is
  less likely to be wrong than step 4 but comes first, because
  `decide-first` names the renamed skill and naming it twice is
  churn for nothing. The principle being kept is the narrower one:
  nothing *expensive* is built before the step that could overturn
  it. Steps 3 and 5–8 are cheap or independent.

- **The renames do not depend on the skill.** If step 4 finds a
  wrapper, steps 6 to 8 still stand. "change-plan" reads as *plan
  the change*, which is what it must not mean, and that is true
  whether or not `decide-first` exists.

- **The widening is the thin part, and it is named as such.** Three
  uses, all on questions of form, plus one retrospective case. That
  is ADR-0028's own objection arriving again, so the ADR carries a
  trigger: if the widened skill never once settles a question that
  is not about form, the widening was wrong and the name goes back.

- **`option-comparison` gains no reference to `decide-first`.** Both
  of its uses arrived without one, and its trigger is
  source-agnostic. The reference is one-directional. Stated because
  the first draft of this shape described a pipeline, which would
  have coupled them.

- **The shipped half of a rename is the expensive half**, and it is
  why this is ten commits rather than four. Three runs hold
  `change-plans` at a pin with a registry entry naming it, and
  nothing in the delivery procedure has ever renamed a convention.
