# Change-plan: the groups are named (PLAN Step 9)

**Revised 2026-09-19 at step 6's boundary.** The first plan named the
groups in prose and drew the boundary *inside* two skills, in a
`stack/` quarantine. The user's reading of the gate was the literal
one and is right: the groups are directories, whole skills, named on
disk. What forced the revision is under *Decisions* below.

## Summary — the state after all commits

`delivery/` holds three named directories — `container/`, `method/`,
`spring-postgres/` — and the things *about* delivery sit beside them,
never inside one. A skill belongs to exactly one group and is copied
whole or not at all. A project on another stack takes two directories
of the three, and needs no rule, no glob and no ADR to know which. The
names say what they hold: `delivery` because the directory carries
updates as well as births, `container` because "kit" named where it
came from rather than what it is, `spring-postgres` because a stranger
matches it against their own project.

## Commits

**1. `docs(agent): add change-plan for the groups`**
This file.

**2. `docs(temp): the shipped files, sorted`**
The measurement before the naming. Still load-bearing after the
revision: it is what established that cbc-framing and cbc-slice carry
no stack at all, which is the line the groups are drawn on.

**3. `docs(adr): the groups are named`**
ADR-0029, Proposed.

**4. `docs(starter): the stack quarantines, and the pointers follow`**
The thirteen stack files under `<skill>/stack/`. Undone by step 9 —
the quarantine was the wrong answer, and the commit stays in history
as what was tried.

**5. `docs: the records read in the groups`**
ARCHITECTURE, `starter/README.md`, and ADR-0029 decision 5 corrected.

**6. `docs(agent): revise change-plan — the groups become directories`**
This revision.

**7. `docs(adr): rewrite 0029 — whole skills, three directories`**
Decision-first, per change-plans §3: this one was settled in
conversation, so it is recorded before it is implemented. ADR-0029
stays **Proposed**; three of its decisions are replaced and the
reasoning that lost is kept, including the quarantine and why it was
wrong.

**8. `docs(starter): starter becomes delivery, kit becomes container`**
The root and the container renamed, pointers and manuals following in
the same commit so nothing dangles mid-set.

**9. `docs(delivery): the bundle splits into method and spring-postgres`**
The five skills into their two groups, whole. This also undoes step
4's `stack/` directories — the files land in `spring-postgres/` at
their original paths, so the skills read as they did before the
quarantine.

**10. `docs(delivery): the manuals follow the groups`**
`pure-seed.md`, `bundle-update.md` and the delivery README: the birth
mapping, the copy rule, the update loops.

**11. `docs: the records read in the groups`**
ARCHITECTURE's overview, Executions component, invariant and codemap
rewritten for the shape that actually landed — step 5's text
described the quarantine.

**12. `docs(adr): accept 0029 and close Step 9`**
The set's final records commit. ADR-0029 flips to Accepted here and
nowhere earlier; PLAN's Step 9 gate closes with its two wrong premises
corrected rather than ticked; TODO's java-spring item is retargeted;
devlog takes the session.

**13. `docs(agent): close change-plan for the groups`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **Material first for the naming, decision first for the shape.**
  change-plans §3 allows one plan to mix both, per decision. The sort
  (step 2) had to precede the ADR because the misfits were invisible
  from conversation. The revision is the other way: the shape was
  settled in conversation, so step 7 records it before step 9 moves a
  file.

- **What forced the revision, kept because it was load-bearing.** The
  quarantine was argued on "a skill is one directory an agent loads."
  That is true of the *destination* — a run's `.claude/skills/` — and
  false here: ADR-0004 and ADR-0006 say executions in this repo are
  content, never installed in our own `.claude/`. Nothing loads a
  skill from `delivery/`. The argument protected a property the
  source layout does not have.

- **The gate's own rule decided it.** "Each group is copied whole or
  not at all" — and the quarantine made a skill half-copied, which is
  what the rule is against. ADR-0005 had already drawn this line
  between the same five skills, from the pinning question; ADR-0021
  kept cbc-slice whole by putting its stack reference *outside* the
  bundle rather than in a sub-directory of it. Two precedents for
  whole skills, none for splitting one.

- **The cost is taken knowingly, and it is not small.** A project on
  another stack gets `container/` and `method/` and nothing for ground
  or bootstrap — no infra-establish, no cbc-bootstrap, not even their
  stack-free stages. The judgment is that those three are
  practice-born (ADR-0005), harvested from lived Spring and PostgreSQL
  runs rather than derived from the concept, and that another stack's
  versions are its own to harvest and would land as a fourth group
  beside this one. If that is wrong, it is wrong visibly, and PLAN
  Step 10's first birth is where it shows.

- **Step 4 is not reverted as a commit.** Step 9 moves the files
  onward rather than `git revert`-ing, so the history reads as one
  forward line and the quarantine stays legible as a thing that was
  built and then found wrong.
