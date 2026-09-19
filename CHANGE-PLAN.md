# Change-plan: the groups are named (PLAN Step 9)

## Summary — the state after all commits

What this repo ships is named as the three things it is, in an ADR
that states each group's boundary and its pin: the container a run
is born into, the concept and the executions derived from it, and
the executions shaped by one stack. The naming is made true — in
the layout where it moves files, in `ARCHITECTURE.md` and
`starter/README.md` where it changes what the records say, and in
the three questions parked on this step. After it, a CbC project
that is not Spring and Postgres can be born from two groups
instead of refusing the third by hand, and "copy this, not that"
is a line someone can follow without reading twenty-nine ADRs.

## Commits

**1. `docs(agent): add change-plan for the groups`**
This file.

**2. `docs(temp): the shipped files, sorted`**
The measurement before the naming: every file under `starter/`,
plus the two held baselines, assigned to a candidate group — and
the ones that refuse to sort listed as refusals rather than
forced. ADR-0024's take was measured before it was made and came
in smaller than the measurement; the same move turns "three
groups" from a sentence in a gate into a boundary that either
holds or does not. It also settles the gate's own arithmetic: the
gate says "six templates all in one group" and the disk says
`infra-establish/templates/` holds six while `cbc-bootstrap/` holds
three more and `cbc-framing/` holds one that is not stack-shaped
at all. Whether that is one group or two is the first thing the
sort will say.

**3. `docs(adr): the groups are named`**
ADR-0029, opening **Proposed** (change-plans §4). Names the three
groups, their boundaries and their pins, weighing the four pieces
of evidence the gate lists — ADR-0005's derives-from/checked-against
split, ADR-0021 holding the Spring reference out of the bundle,
the templates the sort has just counted, and
`starter/kit/.claude/skills/` meaning exactly one thing until
ADR-0028 put a native skill in it. Names the stack-shaped group
for the stack it assumes, not the tier it serves. States the
copied-whole-or-not-at-all rule and the about-a-group-beside-it
rule, which is what decides where `docs/conventions/` and
`starter/README.md` sit.

**4. *(provisional)* the layout follows the naming**
Intent: whatever step 3 makes untrue of the directories. If the
groups turn out to be a lens over the layout we have, nothing
moves and this step does not exist; if a group is a directory,
this is the move, as one step, so that a revert lands somewhere
coherent. Wording and split deferred to step 3's boundary — the
first place the answer is visible, and not guessable from here.

**5. `docs: the records read in the groups`**
`ARCHITECTURE.md`'s components, invariants and codemap, and
`starter/README.md`, in the groups' terms. The Executions
component currently describes five skills as one thing; if step 3
says they are two, this is where that stops being wrong.

**6. `docs(adr): accept 0029 and close Step 9`**
The set's final records commit, on the pattern of `92fd3b5`.
ADR-0029 flips to Accepted here and nowhere earlier; PLAN's Step 9
gate closes and its three items are ticked or corrected in place;
TODO's parked items are closed or retargeted — the repo-hygiene
template parts, which name this step as their trigger, and the
`format-comparison` shipping question ADR-0028 sent here; devlog
takes the session.

**7. `docs(agent): close change-plan for the groups`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **Material first, for the naming.** change-plans §3 says order
  follows where the decision lives. "What are the groups" is
  visible in the material and not in conversation — the misfits
  are the whole question, and three sessions of argument would not
  produce the list that one sort produces in twenty minutes. So
  the measurement precedes the ADR, and the ADR is written from
  what the sort found.

- **One ADR, five questions.** The gate's three items and the two
  questions handed here (does `format-comparison` ship;
  what `starter/kit/.claude/skills/` means now that it holds two
  kinds) are one decision, not five: each of the two is a *test*
  of the boundary rather than a separate call, and a boundary that
  cannot answer them is the wrong boundary. If the sort shows
  otherwise, that is a divergence and gets its own revision commit.

- **The gate is expected to be corrected, not only ticked.** Step
  8's close did this twice and said so. Its "six templates"
  arithmetic is already suspect and step 2 will settle it; a gate
  that closes by rewording itself says which items it reworded.

- **No step for the third parked question's fix.** The
  repo-hygiene template parts (`gitignore.part` and the two beside
  it) are *decided* here — which group they ride — but moving or
  wiring them is the work that decision authorizes, not this set.
  Deciding and doing in one set is how a set's scope escapes it.
