# 0029. Three groups, and the stack quarantines

Date: 2026-09-19
Status: Proposed

## Context

This repo ships one pile. A run copies all of it at birth, Spring
and PostgreSQL included, and nothing written down says which parts
a project on another stack should leave out. PLAN Step 9 asks for
the line to be drawn: the work kit, the concept and what derives
from it, and the executions shaped by one stack.

The line has in fact been drawn three times already, and never
named. ADR-0005 gave the two stack-free skills the phrasing
*derives from* concept v1 and the three stack-shaped ones *checked
against* — the same split, arrived at from the pinning question.
ADR-0021 held `spring-slice-reference.md` out of the bundle so
cbc-slice would stay stack-free — the same split again, enforced by
hand for one file. ADR-0008 put the templates inside their skills,
which is where the stack now sits. Three decisions circling one
boundary, each re-arguing it from scratch, because it has no name
to be cited by.

The sort (`temp/groups-sort.md`, commit 729368d) measured the
material before this was written, and corrected the premises it was
about to be written on.

## What the sort found

1. **A grep is not a measurement here.** `compose`, `bootstrap` and
   `boot` are method vocabulary in this bundle as much as stack
   vocabulary — "compose the requirements document", the pipeline's
   third stage. cbc-framing scored 5 hits and cbc-slice 5; all ten
   are false on reading. Recorded because the counts looked like
   evidence.

2. **The boundary runs inside three skills, not between five.**
   Every `SKILL.md` in the bundle is stack-free or nearly. The 13
   hard-stack files — unusable without Spring, PostgreSQL or
   podman — are all `references/` and `templates/`, in
   infra-establish and cbc-bootstrap.

3. **Six files refused to sort**, and four of the six are method
   files that merely *name a lived default*: infra-establish's
   SKILL and walk naming podman-and-compose, cbc-bootstrap's SKILL
   pointing at its Spring references in three lines, app-structure
   spending one line of ninety-one on Spring Modulith,
   infra-serve's single hedged `podman compose ps`.

4. **The gate's arithmetic is wrong twice.** Ten templates in three
   skills, not six in one, and `cbc-framing/templates/registry.md`
   is method.

## Options considered

**A. Three groups, skills whole.** A skill belongs to one group
entire, so infra-establish, infra-serve and cbc-bootstrap are all
stack. Rejected: a non-Spring project then loses the *method* of
establishing a ground and bootstrapping a system — how to evaluate
services against the registry's adversity needs, how to decide a
stack at capability grain, how to shape packages. That method is
most of those three skills by line count and all of their value to
a project that will not use our templates. It is the content the
group split exists to save.

**B. Four groups — the container ground gets its own.** Finding 3
looks like a third thing: six files assuming podman-and-compose
without assuming Spring or PostgreSQL. Rejected on reading them:
four of the six are method files naming a default they invite the
reader to re-decide, and infra-establish's SKILL points at its
Postgres references *conditionally* already. A fourth group would
move four method files into a stack group for the crime of naming
their lived default. The middle is a property of a file, not a set
of files.

**C. Split each mixed skill into two directories.** `infra-establish`
and `infra-establish-spring`. Rejected: a skill is the unit an agent
loads, and the split breaks the channel — the reader of the method
half has no route to the walkthrough that makes it concrete, which
is the failure ADR-0028 named about `playbooks/`.

**D. Quarantine, chosen.** The skill stays one directory; its
stack material gathers in one named subdirectory of it. The group
is then copyable whole by a rule a person can follow without
reading this file.

## Decision

1. **Three groups, named.** **The container** — what a run is born
   into (`starter/kit/`, with `docs/conventions/` beside it).
   **The method** — the concept and the executions derived from it
   (`concept/`, and the five skills' own instruction). **spring-postgres**
   — everything unusable without Spring Boot, Maven, PostgreSQL or
   podman. The third is named for the stack it assumes, as the gate
   requires; it is not "practice" or "the stack-shaped tier",
   because those name its relation to us rather than its contents,
   and its contents are what a stranger needs to match against
   their own project.

2. **The container ground is not a fourth group.** A method file
   may name a lived default, and naming one does not move the file.
   Written as a rule because it is the judgment most likely to be
   re-litigated: the test is whether the file is *unusable*
   without the named thing, not whether it mentions it.

3. **Stack material quarantines in a `stack/` subdirectory of its
   own skill.** Every hard-stack file moves under
   `<skill>/stack/`, and the copy rule becomes one sentence:
   *a project on another stack copies everything except every
   `stack/` directory*. Greppable, followable by someone who has
   read no ADRs, and it keeps each skill whole as a directory an
   agent loads. `cbc-framing/templates/registry.md` stays where it
   is — it is method.

4. **A group is copied whole or not at all, and anything *about* a
   group sits beside it.** The two rules the gate asks for, and
   they settle two things that have been open:

   - **`format-comparison` is container group, and is held back for
     maturity rather than membership.** The first draft of this ADR
     excluded it as a method *about* the work rather than part of
     it. That test is wrong and is recorded because it was
     convincing: `commit-messages` is about how you write a commit,
     `artifact-kinds` is about how you name a document,
     `change-plans` is about how you plan work, and all four kit
     skills ship. A group is what a file *is about*, not how many
     removes it stands from the code. So the group answers nothing
     here, and ADR-0028 decision 5's real reason is the one that
     stands: two uses by one author in one week is thin evidence
     for a rule, and the trigger named there — the first run that
     meets a format question of its own, seen through the harvest
     loop — has not fired. Held, with a condition that can be
     observed to change, rather than excluded by a boundary.
   - **`starter/kit/.claude/skills/` means one thing again, and the
     kind says so, not the group.** The directory holds pinned
     *convention* copies; ADR-0028 decision 4 already found
     `format-comparison` is not a convention, its kind being
     playbook, so it is ineligible on the kind whatever the group
     says. The "carried by absence" worry ADR-0028 closed on is
     answered by that rule rather than by a boundary that, per the
     bullet above, does not fall where the worry sits.

5. **The three `java-spring/*.part` files belong to
   spring-postgres**, and move out of
   `docs/conventions/repo-hygiene/templates/`. They are stack files
   living inside the container's manuals, which decision 4's
   beside-it rule forbids directly. Wiring cbc-bootstrap to point
   at them — three runs have re-derived by hand what they already
   hold — is the work this decision authorizes and not part of this
   set; it stays in TODO.

6. **ADR-0005's pin phrasings are this boundary, and are left
   alone.** *Derives from* and *checked against* answer a different
   question — what a pin claims — and they happen to fall on the
   same line. Recorded so the coincidence is not mistaken for
   redundancy and one of them deleted.

## Consequences

Good: a non-Spring CbC project is born by a rule instead of by
judgment, and the rule is one sentence. The boundary that three
ADRs re-argued has a name to be cited by. And one parked question
was answered twice here — wrongly by the boundary, then rightly by
its own reason — which is the most useful thing a boundary can do:
show where it does not reach.

Bad: `stack/` is a fourth directory kind inside a skill, after
`references/` and `templates/`, and the distinction between a
reference that is stack and one that is not has to be got right
each time a file arrives. The test in decision 2 is the only guard,
and it is a judgment call wearing a rule's clothes.

Also: the pipeline's three middle skills now ship with a hole in
them for a project that quarantines the stack — the method without
its lived walkthrough. That is the trade decision 1 took over
option A deliberately, and the first non-Spring run is where it
will be seen to have been right or wrong.
