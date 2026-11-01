# The whole system in plain words

*One page. No jargon: each Name is given once, beside its plain
words. A summary of the concept, `docs/concept/`, and of the two
workflows, `.claude/skills/cbc-framing/references/cbc-framing-workflow.md`
and `.claude/skills/cbc-slice/references/cbc-slice-workflow.md`. If
this page and they ever disagree, one of them is wrong: find out
which.*

**What this is, in one sentence:** a way of designing a backend that
starts from what must never happen.

It derives the backend from one Falsifiable Promise. It asks *"what
must never happen?"* before *"what should it do?"* It answers each
System Never-Event with a Structural Wall, proven by a test that
creates the attack.

## The one idea

Ask **"what must never happen?"** first. Money counted twice. An
order created twice. A stale answer shown as fresh. Most software is
designed the other way round, by asking "what should it do?" and
listing features.

Then build the smallest system that makes those disasters
*impossible by structure*: not caught by tests, not fixed after
alerts. Features come last, as the minimum needed to keep the
promises real. Every extra feature is a new way to break your own
System Guarantees. So staying small is discipline, not taste.

## The Layered System: five nested layers

- **LAYER-1-ENVIRONMENT — The world.** Everything outside your
  control: users, networks, other systems, your own process crashing.
  It is hostile: things vanish, duplicate, and lie.
- **LAYER-2-SYSTEM — Your system.** One Falsifiable Promise: which
  facts you are the authority on, and what you commit to about them.
  A real promise can be broken: you can describe the exact scenario
  where it fails. Also the boundary: everything crossing from outside
  is checked right at the door.
- **LAYER-3-AREAS — The parts inside,** the Responsibility Areas.
  They are split by one rule: every fact has exactly one owner. Often
  the answer is "one part", and that is fine.
- **LAYER-4-PROBLEMS — The small problems.** Inside each part: what
  must hold true, and what attacks it. They are small on purpose: the
  layers above made them small.
- **LAYER-5-INTERACTION — Between the parts.** Correctness no single
  part can own. Most real incidents happen here. It is empty if there
  is only one part.

## The order of work (not the same as the layers' order)

0. **Choose the Falsifiable Promise** (the CBC Framing Intent). One
   sentence, worth proving, for a named audience.
1. **What must be ours?** (LAYER-2-SYSTEM). For each candidate: "if
   someone else owned this, could they break our promise?" Yes: ours,
   a System Possession. No: refused, in writing.
2. **List the enemies** (LAYER-1-ENVIRONMENT). Follow one request
   through its whole life. Everything beyond your control is an
   actor. For each: can it vanish, duplicate, or lie? Write Enemy
   Facts you can attack with ("responses get lost"), not vague worries
   ("networks are unreliable"). Stop when two fresh attacks on the
   list find nothing new.
3. **Run the Enemy Collisions** (LAYER-4-PROBLEMS). Each Enemy Fact ×
   each thing you own: what dies? Name the Enemy Collision Kill, never
   the cure. Mechanisms come later.
4. **Sort into owners** (LAYER-3-AREAS), only if the Enemy Collisions
   actually force separate owners. One owner is a confirmed answer,
   not a gap.
5. **Check between owners** (LAYER-5-INTERACTION), only if Stage 4
   made more than one.
6. **Cut into Invariant Slices.** An Invariant Slice is one invariant
   made real: proven to survive its specific attack, end to end.

*(Numbered 0 to 6 to match the detailed workflows, Stage for Stage.)*

## Working one Invariant Slice

- **Specify:** write what must hold and what attacks it. No solutions
  yet.
- **Plan:** pick the mechanism, and say why it beats *that* attack.
- **Build:** the mechanism, plus a test that *creates* the attack
  (hammer it concurrently, inject duplicates, kill it mid-write) and
  shows the invariant surviving.
- **Document:** the Falsifiable Promise, the guarantees, the proof,
  readable later.

The test that creates the attack is the deliverable most projects
skip.

## Enforcement: who guards each guarantee

Every System Guarantee gets exactly one Structural Wall, the
strongest available:

the store's refusal (a constraint, a right withheld) → type system →
single checked entry path → runtime check → code review → hope.

"All the code being careful" is not a Structural Wall. It is the
absence of one.

## How it fails (watch for these)

- **System Guarantee Erosion:** new features ship without re-checking
  the System Guarantees.
- **Escape Hatch:** an admin script goes around the one enforced
  path, and the System Guarantee quietly becomes fiction.
- **Testing Theater:** System Guarantees drift out of structure and
  back into test suites.
- **Theory Swamp:** theory before the layers have shrunk the problem.

## When NOT to use this

Throwaway code, experiments, low-stakes tools: iterate-and-fix is
cheaper there, and not wrong. This method pays off when breaking the
promise is expensive or cannot be undone (money, safety, trust), or
when the system will live long.
