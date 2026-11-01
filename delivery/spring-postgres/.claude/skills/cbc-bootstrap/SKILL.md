---
name: cbc-bootstrap
description: Run the CBC Bootstrap of a framed project on an established Runtime Ground. Decide the stack and what the CBC Bootstrap builds, as capabilities and constraints. Write the CBC Bootstrap Requirements. Build an empty but running skeleton wired to the real services, and prove the Adversity Harness creates one named adversity end to end. Use whenever the user asks to bootstrap the system, stand up the skeleton, "bring the system to life", or continue a project that has a completed framing and a running Runtime Ground but no application code yet, even if they just say "let's start building". It requires a completed CBC Framing AND an established, verified Runtime Ground. Stage 0 checks both, and refuses to go on if either is missing. Do NOT use for framing (the cbc-framing Agent Skill), for implementing Invariant Slices (the cbc-slice Agent Skill), or for setting up databases or infrastructure: that is Infrastructure Establishment, done before this.
foundation: practice, checked against concept v1
---

# cbc-bootstrap — bring a framed system to life

One run, one exit, the CBC Bootstrap's end:

- the stack settled;
- an empty but running skeleton, wired to the real Runtime Ground
  already established;
- the Adversity Harness proven able to **create** one named adversity
  end to end.

After this, the cbc-slice Agent Skill has somewhere to land.

## The boundary you must keep — WHAT before HOW

Stages 1 and 2 name no mechanism. Stage 4 decides the code. Between
them is a **hard boundary between Agent Skill Stages**:

- Stages 1 and 2 decide only the *what*: capabilities, constraints,
  Build Coordinates, the evidence owed. **No dependency, no class, no
  file layout is named there.**
- Stage 4 is where implementation judgment lives: the dependencies
  and when they enter, the shape of the code, the commit split, under
  the stack conventions in `references/`.
- Never let a mechanism chosen early pass for a requirement. While
  implementing, you may find a missing *what*: a capability or
  constraint the work turns out to need. Then **stop and return to
  Stage 1, as a logged decision taken again.** Never absorb it
  silently.

This rule was written from a practice with two roles: one decided
**what** was built and under which constraints, another **how** it
was realized in code. Run as one agent, the boundary between the
Agent Skill Stages keeps the two apart.

Every decision is written down with its why **before** the code that
applies it exists. The CBC Bootstrap Requirements (Stage 2) are the
contract. On any conflict between them and the walkthrough reference,
**the CBC Bootstrap Requirements win**, and the conflict is reported.

## Stage 0 — System Readiness (refuse if not ready)

Check, in the repo as it stands:

1. **The CBC Framing Exports committed:** the CBC Framing Intent, the
   System Definition, the Invariant Slice Registry. Missing: stop.
   That is the cbc-framing Agent Skill's work.
2. **The Runtime Ground established, running and verified:** the
   Infrastructure Contract and the Operator Manual exist
   (`.claude/skills/infra-establish/SKILL.md`, *Records and outputs*),
   and the Runtime Ground's stand-up check is recorded. Missing: stop.
   That is Infrastructure Establishment, done before this Agent Skill.
3. **No skeleton yet:** if application code already exists, this
   Agent Skill does not apply. Go to the cbc-slice Agent Skill.

Then **check the Runtime Ground live,** by the Operator Manual,
before any wiring. The records say it was verified. The wiring needs
it up now.

Record what stood, what was checked, and what was noticed. Only a
missing member stops; a note goes in the record.

## Stage 1 — decide (no mechanism; the reviewer confirms)

Reason out each of these and present it for confirmation, with its
why:

- **The stack evaluation.** The deciding inputs are **fluency and
  audience**: which stack the builder or team is proven on, and what
  the intended reader of this codebase reads fluently. The
  correctness work should be the visible substance, not a new stack.
  Record the decision **in an ADR before any code exists.** It
  includes:
  - the migration tool stays outside the app;
  - the app knows one identity, the `runtime` role;
  - the migrations directory is confirmed.
- **The CBC Bootstrap Adversity Class.** Read it from CBC Framing's
  own words: the Falsifiable Promise's named Adversity Class, and the
  first Invariant Slice's shape, such as contention or duplicate
  delivery. The Adversity Harness proves its *machinery* on that one
  Adversity Class alone. Every other Adversity Class is created at
  its own Invariant Slice.

  Read, too, **from how many instances** the adversity comes. The
  System Definition's Runtime Ground says whether the system runs as
  more than one instance. If it does, a pass in a single process
  proves a shape nobody runs: the proof must cross the process
  boundary (the stack walkthrough's step 5). Decide it here, by name,
  with its why.

  Decide, too, **the form the Adversity Harness starts the system in:
  the form it ships.** A plain process ships, so the evidence starts
  plain processes from the build's output, with the environment a
  real instance gets and no test code inside. An image ships, so it
  starts the image. Never the form that is cheapest to start: that
  proves a system nobody runs.
- **The Build Coordinates:** group (the owner's namespace: ask, never
  invent), artifact (the project's name), base package (hyphens
  dropped), packaging, language version.
- **The capabilities, few, typically four:**
  1. an HTTP surface: the adversity arrives through the real door;
  2. operational health: every evidence run needs a cheap check that
     the system is up;
  3. connectivity to the Runtime Ground **as the `runtime` role**:
     the Falsifiable Promise is a property of persisted state;
  4. the Adversity Harness proving the CBC Bootstrap Adversity Class
     end to end, with migrations run on the Adversity Harness's side
     from the one migrations directory, integration tests under the
     one standard test command, and the migration path proven by the
     Migration Path Test.
- **The constraints,** cited against the Infrastructure Contract:
  1. one identity: no `migrator` credentials in any profile;
  2. nothing in the app controls the schema: migration tooling is in
     test scope only;
  3. one migrations directory, empty at the CBC Bootstrap, and saying
     so;
  4. the standing one, **nothing enters ahead of need:** no ORM or
     object mapping while nothing persists domain state yet; plain
     SQL access.
- **The CBC Bootstrap Exclusions, each with its why:**
  1. no business behavior: the CBC Bootstrap Probe is scaffolding,
     marked to die at the first Invariant Slice;
  2. no persistence schema: no table before its invariant;
  3. no other Adversity Classes;
  4. no auth, unless an Invariant Slice needs identity at the door;
  5. no delivery machinery beyond running and testing locally;
  6. **no fail-fast on a missing secret.** The trap is in
     `.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`,
     step 3. At the CBC Bootstrap the only operator is the reviewer.
     The Adversity Harness accepts an instance only on health with
     the store UP. The release Plan Step Gate's clean-machine test is
     where a forgotten export becomes a real need, and it is decided
     there, unless this CBC Run decides otherwise by name.

**Gate: the reviewer confirms the decisions before Stage 2.**

## Stage 2 — write the CBC Bootstrap Requirements

Write `bootstrap-requirements.md` in the project's language, at the
path the project's records choose. It goes beside the builder's
other manuals. Both CBC Runs that ran this Agent Skill put it at
`docs/construction/`.

- §1 the Build Coordinates
- §2 the capabilities, each with its why
- §3 the constraints, each **by reference** to the ADR or contract
  that decided it. The why is stated here only where no record holds
  it.
- §4 the Runtime Ground's facts **by reference:** cite the Operator
  Manual and the Infrastructure Contract, never restate them. Carry
  only what the code needs in hand: the identity the application
  connects as, and the endpoint facts. **State environment facts in
  no tool's notation:** "env var X, default Y", never in any tool's
  placeholder syntax. The trap is in
  `.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`,
  step 3.
- §5 the evidence owed at the end:
  - the CBC Bootstrap Step Plan as executed, with its deviations;
  - the run proof: the app up, health UP with the database component
    UP, the one standard test command green;
  - the commits standing.
- §6 the CBC Bootstrap Exclusions, with their whys.

**It names no dependency, no class, no file layout.** That gap is
deliberate, and Stage 4 closes it. Commit it before implementing.

## Stage 3 — the CBC Bootstrap Step Plan (the reviewer confirms)

Produce an ordered CBC Bootstrap Step Plan. Each step is one logical
change, with its own verification and its own commit, naming what it
gives. The shape CBC Runs have used is five steps (see the stack
walkthrough in `references/`):

1. the stack decision recorded;
2. the skeleton standing in the live repo;
3. the runtime datasource wired to the real Runtime Ground;
4. the Adversity Harness standing, the migration on its side proven;
5. the Adversity Harness proven able to create the adversity.

The **order is load-bearing; the commit split is judgment.** Nothing
outside the CBC Bootstrap Requirements enters the plan. **Gate: the
reviewer confirms.**

## Stage 4 — execute, step by step

For each step: make the change, **verify it**, commit. A step whose
verification fails is not committed; it is reported. Implementation
decisions are yours here, under the stack conventions:

- Read `.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`
  for the outcomes and the traps CBC Runs met: Boot 4 renames, test
  companions, setting up the container runtime, the Migration Path
  Test, the shape of the CBC Bootstrap Probe.
- Write the build file by
  `.claude/skills/cbc-bootstrap/references/spring-pom-convention.md`.
  Every dependency enters at the step that needs it, with that reason
  as a comment, grouped by capability.
- The repo already exists: **extract into it, never overwrite.** Each
  hygiene file, `.gitignore`, `.gitattributes` and `.editorconfig`,
  takes its Stack Overlay below the marked line it carries. The README
  is kept.
- Widen the build's test includes, so integration tests run under the
  one standard test command: no second command, no test that quietly
  never runs.

**When something does not fit, report it, never absorb it:**
- silent on a *what*: back to Stage 1, a logged decision taken again;
- a missing service or constraint in the wiring: Infrastructure
  Establishment's work, reported, not patched here;
- something larger than the CBC Bootstrap: reported, not solved here;
- the CBC Bootstrap Requirements wrong against the repo's reality:
  reported with what was found.

## Stage 5 — certify and close

Certify **against the delivered state, never a report alone.** Check,
member by member:

- **§5 evidence:**
  - the CBC Bootstrap Step Plan as executed, its deviations honest;
  - the run proof: the Java version announced; health UP with the
    database component UP against the running Runtime Ground; the
    standard test command green end to end, checked by structure:
    the integration tests actually run under it;
  - the commits standing.
- **§1:** the Build Coordinates exact.
- **§2:** all capabilities present **and bounded.** The CBC Bootstrap
  Probe carries no business meaning, and is documented to die at the
  first Invariant Slice.
- **§3:** all constraints visible in the delivered files:
  - the `runtime` role alone in config;
  - the password from the environment;
  - deliberate absences commented;
  - nothing on the runtime path that controls structure;
  - the migrations directory empty, and saying so;
  - nothing ahead of need.
- **§6:** the CBC Bootstrap Exclusions respected.

Then write the exit records in the project's own docs: the milestone
certified, the run and test commands, the Operator Manual linked, an
honest "no business behavior yet", and the CBC Bootstrap Probe's
death scheduled at the first Invariant Slice.

**Once certified, the CBC Bootstrap Requirements are history,** like
a closed ADR. They are never updated, and carry no banner of what
changed since. What an Invariant Slice may rely on from now on is
`ARCHITECTURE.md`'s. So the close writes its components as they
stand: the store, the application, the Adversity Harness. Each
carries what an Invariant Slice may rely on, and the ADR that shaped
it. The Adversity Harness's component says the form it starts the
system in, and why that is the form that ships. The project's records
table sends "what may an Invariant Slice rely on" there.

The certified facts also go into the README:

- the **Run** and **Test** sections;
- the stack's line, joining the Prerequisites section that
  Infrastructure Establishment opened.

They are merged and filled from
`.claude/skills/cbc-bootstrap/templates/readme-run-test.md`. Run ends
in a check that the system answers. Test is the one standard test
command, checked by structure at certification. The container's
README has no Run or Test section. They arrive now, because the
Adversity Harness is real.

**Exit test:** the skeleton runs on the real Runtime Ground as the
`runtime` role alone, and the Adversity Harness demonstrably creates
the CBC Bootstrap Adversity Class through the real door. Then hand
over: growth belongs to the cbc-slice Agent Skill.

---

## Decisions

- ADR-0008 — `references/app-structure.md`,
  `references/spring-boot-walkthrough.md` and
  `references/spring-harness-reference.md`: a reference is read and
  imitated, an Agent Skill Template copied and filled
- ADR-0013 — Stage 5: the README's Run and Test sections arrive when
  the CBC Bootstrap makes them true
