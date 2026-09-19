# Change-plan: decide-first, and the comparison skills

**Revised 2026-09-19 at step 3's boundary.** Step 3 was planned as
a rename and a widening; it landed as a split, because the method
turned out to have a general spine and one specialisation rather
than a scope that could widen. Two commits are added: this
revision, and a correction to ADR-0030 decision 6, which describes
the rename that did not happen.

Ordered so that nothing expensive is built on an unvalidated
decision — which is the thing this set exists to write down. The
step most likely to be wrong is step 6, and everything before it is
cheap or independent of it.

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

**3. `chore(agent): format-comparison splits into visual and option`**
Planned as a rename plus a widening; landed as a split. Widening the
one file would have left it saying *render them where they will be
read*, which is literal for a picture and a metaphor for a plan —
and the act is where the discipline lives. So `visual-comparison`
keeps every word of the old file and its subject is how a structure
is shown; `option-comparison` is written fresh with general verbs.
Two rules arrived with it, both the user's: a findings list is
things to check rather than rules to obey, each entry naming its
case; and a visual comparison's candidate set must hold a
non-picture, or a picture wins by construction.

**4. `docs(agent): revise change-plan — the skill split in two`**
This revision, per the convention's §5.

**5. `docs(adr): 0030 decision 6 described a rename, not a split`**
The ADR is Proposed, which is what makes this cheap; it is corrected
here rather than at the close, because a Proposed record may be
unsettled but should not be inaccurate. Decision 8's
one-directional reference survives unchanged and now has two
skills to hold between.

**6. `feat(agent): decide-first`**
**The step most likely to be wrong.** Its own objection is in the
ADR: the routing step has one destination filled in, so the skill
may be a wrapper with two empty slots — and step 3 has just given it
a second destination, which weakens that objection without
answering it. Building it is the only way to find out and costs one
file. If it is a wrapper, the set stops here and the ADR is revised
— steps 8 to 10 survive either way, because "change-plan" reads as
*plan the change* whatever else is true.

**7. `docs(agent): register decide-first`**
`.claude/decisions.md`. Its own commit because HANDBOOK ADR-0019
keeps the agent's files out of project commits, and because step
4's outcome may change what this entry says.

**8. `docs(conventions): change-plans becomes commit-plan`**
The manual, the shipped skill under
`delivery/container/.claude/skills/`, the delivery's references,
and this file's name. The project half.

**9. `chore(agent): our copy and the registry follow the rename`**
`.claude/skills/` and the registry entry. Separate from step 6 for
the same reason step 5 is separate.

**10. `docs(delivery): bundle-update learns the renamed convention`**
The gap the rename exposed: the procedure copies conventions by
name, so a rename installs the new directory and leaves the old one
in the run forever. It will recur whatever we decide here.

**11. `docs(adr): accept 0030, and the records catch up`**
The final records commit. ADR-0030 flips to Accepted here and
nowhere earlier; TODO's change-plans watch is retargeted or closed;
devlog takes the session; the temp draft is deleted, having served.

**12. `docs(agent): close the plan`**
Deletes this file, under its new name. The body records what
diverged.

## Decisions taken inside this plan

- **Ordered by what rests on it, not strictly by risk.** Step 3 was
  less likely to be wrong than step 6 but came first, because
  `decide-first` names those skills and naming them twice is churn
  for nothing. That held: step 3 changed what they are called and
  how many there are, and a `decide-first` written first would have
  named a skill that no longer exists. The principle being kept is the narrower one:
  nothing *expensive* is built before the step that could overturn
  it. Steps 3 and 5–8 are cheap or independent.

- **The renames do not depend on the skill.** If step 6 finds a
  wrapper, steps 8 to 10 still stand. "change-plan" reads as *plan
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
