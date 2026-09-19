# 0029. Three groups, three directories

Date: 2026-09-18
Status: Accepted

## Context

This repo ships one pile. A run copies all of it at birth, Spring and
PostgreSQL included, and nothing written down says which parts a
project on another stack should leave out. PLAN Step 9 asks for the
line to be drawn: the work kit, the concept and what derives from it,
and the executions shaped by one stack.

The line has in fact been drawn three times already, and never named.
ADR-0005 gave the two stack-free skills the phrasing *derives from*
concept v1 and the three practice-born ones *checked against* — the
same split, arrived at from the pinning question. ADR-0021 held
`spring-slice-reference.md` out of the bundle so cbc-slice would stay
stack-free — the same split again, enforced by hand for one file.
ADR-0008 put the templates inside their skills, which is where the
stack now sits. Three decisions circling one boundary, each
re-arguing it from scratch, because it has no name to be cited by.

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

2. **cbc-framing and cbc-slice carry no stack at all** — nine files,
   checked line by line. That is the finding the groups are drawn on,
   and it is exactly ADR-0005's *derives from* set.

3. **The other three mix**, by content: every `SKILL.md` is
   stack-free or nearly, and the 13 hard-stack files — unusable
   without Spring, PostgreSQL or podman — are all `references/` and
   `templates/` in infra-establish and cbc-bootstrap. Six more files
   only *name* a lived default: podman-and-compose in a sentence the
   reader is invited to re-decide.

4. **The gate's arithmetic is wrong twice.** Ten templates in three
   skills, not six in one, and `cbc-framing/templates/registry.md` is
   method.

## Options considered

**A. A fourth group for the container ground.** Finding 3's six
soft files look like a third thing — podman and compose without
Spring or PostgreSQL. Rejected on reading them: they are method files
naming a default, and infra-establish's SKILL already points at its
Postgres references *conditionally*. A fourth group would move method
files into a stack group for the crime of naming their lived default.
The middle is a property of a file, not a set of files.

**B. Split each mixed skill into two skills** —
`infra-establish` and `infra-establish-spring`. Rejected: the reader
of the method half has no route to the walkthrough that makes it
concrete, which is the failure ADR-0028 named about `playbooks/`.

**C. Quarantine the stack inside each skill**, in a `stack/`
subdirectory, with the copy rule *everything except every `stack/`*.
**Built, at 01a4729, and then rejected** — recorded at length because
it was live for an hour and its argument was good.

It was argued on *a skill is one directory an agent loads*, so
splitting one breaks the unit. That is true of the **destination** —
a run's `.claude/skills/infra-establish/` — and false of this repo.
ADR-0004 and ADR-0006 say executions here are *content*, never
installed in our own `.claude/`; nothing loads a skill from
`delivery/`. The argument protected a property the source layout does
not have.

Two further things decided it once that fell. The gate's own rule is
*each group is copied whole or not at all*, and a quarantine makes a
skill **half**-copied, which is what the rule is against. And the
precedent runs the other way: ADR-0021 kept cbc-slice whole and
stack-free by putting its Spring reference **outside** the bundle
entirely, not in a sub-directory of it.

**D. Three groups, three directories, whole skills.** Chosen.

## Decision

1. **`starter/` becomes `delivery/`.** The name came from "starter
   kit" and says *birth*, but the directory also holds
   `installs/bundle-update.md`, which serves a run born months
   earlier, and ADR-0024 widened it to carry the container too. The
   codemap has called it "the delivery layout" since then while the
   directory said otherwise. "Starter kit" remains the historical
   name for what was taken from the handbook, so the provenance
   sentences still read true. (ADR-0010 named the directory; this
   supersedes that half of it and nothing else.)

2. **Three groups, and each is a directory under `delivery/`.**

   - **`container/`** (was `kit/`) — what a run is born into. "Kit"
     named where it came from; this names what it is.
   - **`method/`** — cbc-framing and cbc-slice, the two that derive
     from concept v1.
   - **`spring-postgres/`** — infra-establish, infra-serve and
     cbc-bootstrap, whole.

   Named for the stack it assumes, as the gate requires, and not
   "practice" or "app": a stranger matches the name against their own
   project, not against our tiers, and the day a second one is
   harvested `spring-postgres/` and `go-mysql/` read correctly side
   by side where `app/` would not.

3. **A skill belongs to exactly one group and travels whole.** No
   skill is split, and no group is partially copied. A project on
   another stack takes `container/` and `method/` and leaves
   `spring-postgres/`: two directories of three, decided by reading
   their names.

4. **What that costs is stated rather than softened.** Such a project
   gets **nothing** for ground or bootstrap — no infra-establish, no
   cbc-bootstrap, not even their stack-free stages, which finding 3
   says is most of those files. The judgment is that all three are
   practice-born (ADR-0005): harvested from lived Spring and
   PostgreSQL runs, never derived from the concept, and carrying
   their lived shape in their bones rather than only in their
   examples. Another stack's versions are that stack's to harvest,
   and would land as a fourth group beside this one — which is the
   garden rule's shape, applied to a group instead of a repo. If the
   judgment is wrong it is wrong visibly: PLAN Step 10's first birth
   is where it shows.

5. **Anything *about* a group sits beside it and never inside one.**
   `fills/`, `installs/` and `delivery/README.md` are about delivery,
   so they sit beside the three groups. `docs/conventions/` is about
   the container and stays out of `delivery/` entirely. The rule was
   asserted in prose before this decision; now the tree holds it.

6. **`format-comparison` is container group, and is held back for
   maturity rather than membership.** An earlier draft excluded it as
   a method *about* the work rather than part of it. That test is
   wrong and is recorded because it was convincing: `commit-messages`
   is about how you write a commit, `artifact-kinds` about how you
   name a document, `change-plans` about how you plan work, and all
   four kit skills ship. So the group answers nothing here, and
   ADR-0028 decision 5's own reason stands — two uses by one author
   in one week is thin, and its trigger, the first run meeting a
   format question of its own, has not fired.

   `container/.claude/skills/` therefore still means one thing, and
   the *kind* says so rather than the group: it holds pinned
   convention copies, and ADR-0028 decision 4 already found this one
   is a playbook.

7. **The three `java-spring/*.part` files belong to spring-postgres,
   and stay where they are for now.** They are stack files inside the
   container's manuals, which decision 5 forbids directly — so the
   group answer is not in doubt. The destination is: the only home is
   `spring-postgres/cbc-bootstrap/templates/`, and nothing points at
   them there either. Three runs have re-derived by hand what they
   already hold, because cbc-bootstrap's walkthrough has a run grow
   its `.gitignore` from what the Spring skeleton produces. Moving
   them unwired would ship three unread files to every Spring run,
   a worse breach than the one it fixes. So: an exception recorded
   against a named rule, and the move travels with the wiring. Both
   stay in TODO with this ADR as the reason.

8. **ADR-0005's pin phrasings are this boundary, and are left
   alone.** *Derives from* and *checked against* answer a different
   question — what a pin claims — and fall on the same line. Recorded
   so the coincidence is not mistaken for redundancy and one of them
   deleted.

## Consequences

Good: a project on another stack is born by reading three directory
names. No glob, no rule to remember, no ADR to consult. The boundary
three ADRs re-argued has a name to be cited by, and the
about-a-group-sits-beside-it rule is now a fact about the tree rather
than a sentence in a record.

Bad: the rename reaches every manual — `pure-seed.md`,
`bundle-update.md`, the delivery README — and every path in them. It
is mechanical, and it is the kind of change that leaves one stale
pointer somewhere nobody looks. And a `spring-postgres/` group that
only ever has one sibling will read as over-built until the second
one arrives.

Worse, and worth naming: three of five skills now ship to nobody
outside this stack. Decision 4 takes that knowingly, but it means the
pipeline this repo describes — framing → establish → bootstrap →
slice — is only whole for Spring and PostgreSQL. Everyone else gets
its two ends. That is the honest state of what we have harvested, and
writing it down is better than a group boundary that hides it behind
a half-copied skill.

Also: the quarantine at 01a4729 stands in history as built and found
wrong within the same change set. It was wrong for a reason worth
having on file — an argument about the destination applied to the
source — and the next shape question about `delivery/` should read it
before repeating it.
