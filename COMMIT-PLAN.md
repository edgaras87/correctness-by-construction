# Commit plan: the three skills become conventions

Ordered so the step that could overturn the rest is reachable in
three commits. That step is the first manual: if writing one
produces nothing a reader could not get from the skill itself, the
premise is wrong and the set stops.

## Summary — the state after all commits

`docs/conventions/` holds ten manuals, one per convention, and
`delivery/container/.claude/skills/` ships ten skills. The
distinction between borrowed and native is gone — ADR-0025 made
the manuals ours and today's corrections made them speak from this
seat, so there is one kind, uniformly held, and no exception to
explain. A run is born with ten conventions instead of four, and
`bundle-update.md` re-delivers ten.

## Commits

**1. `docs(agent): add commit plan for the three conventions`**
This file.

**2. `docs(adr): decide-first and the comparisons become conventions`**
ADR-0031, opening **Proposed**. Supersedes ADR-0028 decision 5,
which parked shipping, and ADR-0029 decision 6, which said the
container's skills directory holds conventions and a playbook is
ineligible. Both were argued from a borrowed/native split that
ADR-0025 had already dissolved and today's corrections finished
off. Records what the uniformity buys: no second kind in the
directory, no special case in the update loops, and a manual for
every rule a run holds.

**3. `docs(conventions): a manual for decide-first`**
**The step most likely to be wrong.** A manual is the *why* behind
a rule, for a maintainer. If this one only restates the skill, that
is evidence `decide-first` is not a convention — a method you copy
rather than a rule you owe an explanation for ignoring — and the
set stops here with ADR-0031 revised. Written first, and alone,
because it is the cheapest possible test of the premise.

**4. `docs(conventions): manuals for the two comparison conventions`**
The other two, once the shape is known to work.

**5. `docs(delivery): the three conventions ship`**
The skills into `delivery/container/.claude/skills/`, the table in
`docs/conventions/README.md` from seven rows to ten, the birth
entry's convention list, and a delta row in `delivery/README.md` —
our container now holds three files the handbook's kit never had.

**6. `docs(delivery): bundle-update re-delivers ten`**
Its two by-name loops name four. TODO already holds the better
answer — derive from the run's pin rather than a list — and this
set does not attempt it; the loops go to ten by name, and the item
stays with its reasoning intact.

**7. `chore(agent): the three are registered and pinned`**
Our copies are the originals, so they are identical to the
container by construction; what changes is that they gain registry
entries and a pin, like the other four.

**8. `docs(adr): accept 0031, and the records catch up`**
The final records commit. ADR-0031 flips here; ARCHITECTURE's
count of conventions and the codemap follow; devlog takes the
session.

**9. `docs(agent): close the plan`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **The first manual is the test, and it is written alone.** The
  premise of this set is that these three are conventions rather
  than playbooks. A manual that says nothing the skill does not is
  the cheapest evidence against it, and writing all three before
  looking would spend that evidence three times over.

- **`decide-first` is the one to test with**, not one of the
  comparisons. It has run zero times and is the thinnest-evidenced
  of the three; if any of them has a hollow manual it is this one.
  Testing with the strongest would prove the least.

- **The map is not in this set.** It describes how ten conventions
  relate and three of them do not exist yet, so writing it here
  means writing it twice. Next set, with `visual-comparison`
  settling its diagram — which is also the fourth use that skill's
  trigger has been waiting for.

- **The by-name loops are widened, not fixed.** Deriving from the
  run's pin is the right answer and is already filed; doing it here
  would put a second decision inside a set that has one.
