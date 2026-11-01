# Infrastructure Establishment — Agent Skill Stage by Agent Skill Stage

Infrastructure Establishment, Stage 0 to Stage 7. It is generic throughout. The project's
concrete choices land in its own record and manuals, never here. Two
CBC Runs have done it. Deviations a different Runtime Ground forces
are legal when logged.

## Inputs, before Stage 0

The CBC Framing Exports, standing:

- the System Definition's environment facts: the Runtime Ground must
  honor them;
- the Invariant Slice Registry's Invariant Slices: their adversities
  are the deciding constraints. **Evidence needs drive
  infrastructure, not habit.**

The CBC Framing Intent is consulted at questions of scope and
tradeoff. If the CBC Framing Intent or the Invariant Slice Registry
is not settled, the step is not ready: stop (Stage 0 in `.claude/skills/infra-establish/SKILL.md`).
If only the System Definition's Runtime Ground facts are missing, the
System Definition is revised first: a CBC Framing Export Revision in
its LAYER-1-ENVIRONMENT, one commit. Then Stage 1 begins (Stage 0,
check 2).

## Stage 1 — Decide the Execution Environment, demands first, against the Stack Default

Derive what the Invariant Slices' adversities demand the evidence be
able to *do*: kill processes mid-write, race several instances,
break a commit boundary, survive restarts. Each project has its own
list. This derivation is the part of this Agent Skill Stage that
changes per project. It chooses the Execution Environment, and the
manuals record it.

**The demands choose the Execution Environment; the Runtime Ground
does not prove them.** The Runtime Ground proves the engine (below),
and, at Stage 5, what the store itself promises: each Infrastructure
Service Constraint seen refused. The evidence must be able to start
several instances on the Runtime Ground, kill one and freeze the
store. Each is proven where the Adversity Harness that does it is
built, in the form it does it:

- the CBC Bootstrap's Adversity Harness, for its first adversity;
- each Invariant Slice's System Readiness check, for the rest.

Proven here, it would be proven in a form the Adversity Harness may
never use.

Check the **Stack Default, podman local containers, compose-driven,**
against those demands and the System Definition's runtime facts.
Weigh alternatives **only when a demand or an environment fact
defeats the Stack Default,** and name what defeats it. Need governs:
the Stack Default is checked, never assumed. Log the decision with
its why.

Then stand the Execution Environment up, and **write the Operator
Manual's environment section from the setup as it is done, at the
time,** never reconstructed later. Standing the Stack Default up
records, at least, and checked by running them:

- the engine version (`podman version`);
- the compose provider actually answering the command
  (`podman compose version`). The canonical command is
  `podman compose`, whatever provider stands behind it;
- the host OS and arch; the cgroups version;
- rootless or not, with what that means in operation: ports,
  volumes, mount flags (`:Z` on SELinux hosts).

This checklist keeps every project's environment section comparable
in structure, while its facts stay each machine's own.

**No file of the Runtime Ground is created at this Agent Skill
Stage.** `compose.yaml` and the files like it are the outcomes of
Stages 2 to 5. Their content *is* the result of the service
evaluation and the Infrastructure Service Constraints. A file created
here would exist before the decisions that define it. The Execution
Environment's proof is at the engine's level: image pulled, container
run, end to end. The path at the file's level is covered by Stage 5's
opening sanity check (`podman compose config`). A throwaway compose
smoke test outside the repo is allowed when the operator wants the
earlier signal. It is never owed, and never committed.

## Stage 2 — Evaluate the Infrastructure Services, constrained by need

Invariant Slice by Invariant Slice: what capability does each
invariant's evidence actually require? The set of Infrastructure
Services is what survives that question. **Each Infrastructure
Service Exclusion is stated with its why:** a cache refused, a queue
refused, and for what reason. It is one ADR, or one Infrastructure Establishment Log entry. Anything joining
later re-enters this evaluation as a logged decision, an
Infrastructure Service Re-entry (the infra-serve Agent Skill).

## Stage 3 — Name each Infrastructure Service's constraints, the reference first

Infrastructure Service Constraints are requirements and limits put on
an Infrastructure Service. They govern the Runtime Ground, and are
stated as principles: for example, *the running application must not
control database structure*. They are deliberately **not**
invariants of the Invariant Slice Registry: they are not properties
of persisted state under adversity. **Each Infrastructure Service
Constraint names its enforcement mechanism.**

A reference may already be written for a decided Infrastructure
Service: for PostgreSQL,
`.claude/skills/infra-establish/references/postgres-role-split.md`,
in this Agent Skill's references. Then its set of Infrastructure Service Constraints is the
default, unless a project fact defeats it:

- check it against this project's facts;
- depart only when a project fact defeats it, and name what defeats
  it;
- the project's ADR or Infrastructure Establishment Log entry stays, since its own Infrastructure Service Constraints are its
  own facts, but it refers to the reference as how they are made
  real, and never derives them again.

An Infrastructure Service with no reference gets its Infrastructure Service Constraints
derived fresh.

## Stage 4 — Apply the reference, or record a new one

How an Infrastructure Service Constraint is made real can be the same across projects. Then
it is a reference, not a project fact: keep it generic, and keep the
project's concrete wiring in its manuals. When an Infrastructure Establishment derives a
new one that can be reused, for a new family of services, write it
up as a new reference beside
`.claude/skills/infra-establish/references/postgres-role-split.md`,
so no later project derives it again.

## Stage 5 — Stand the Infrastructure Services up, and verify both ways

The files of the Runtime Ground land as project files: declarations
(`compose.yaml`), setup scripts, tool configs. **Secrets are split
out** by the project's credential handling: `.env` git-ignored, and
`.env.example` committed. Decided identities stay literal; secrets
and what varies per machine are variables. The Infrastructure
Services come up on the Execution Environment.

Then **two verifications that complement each other, always both:**

- the Catalog Check: the Runtime Ground's real state queried against
  the reference's claims, the expected result written as a comment
  beside each query, so the reader needs no other doc open.
- the Behavioral Check: the Infrastructure Service Constraint
  *attempted*, and watched being **refused,** live. The rule shown,
  not assumed.

The Operator Manual grows its service sections from this work as
done.

For PostgreSQL, the whole of Stages 3 to 6 has a sequence end to end,
as CBC Runs did it:
`.claude/skills/infra-establish/references/postgres-setup-walkthrough.md`.
Consult it when PostgreSQL comes again. Never force its shape on a
different Infrastructure Service.

## Stage 6 — Write the Infrastructure Contract

The Infrastructure Contract is the builder's manual: a **living
document, one section per Infrastructure Service,** grown at every
later Infrastructure Service Re-entry. Each section says:

1. what Infrastructure Services exist;
2. how to reach them, inside and outside the Execution Environment's
   network;
3. **which identity to connect as, and which never to use;**
4. what the Infrastructure Service Constraints allow and refuse, the
   refusals written as contract terms;
5. how schema changes are made.

It is the home of the Runtime Ground's own words. The exit needs both
manuals standing: this one, and the Operator Manual.

## Stage 7 — Run the exit test

Against the Infrastructure Establishment as done:

1. Does the Runtime Ground run?
2. Is every Infrastructure Service tied to a stated need, and every
   Infrastructure Service Exclusion to a stated why?
3. Do both verifications pass, recorded from actual output?
4. Do both manuals stand, written from the work as done?
5. Could a reader stand the same Runtime Ground up on their own
   machine from the Operator Manual alone?

Any no: the Infrastructure Establishment is not done.

When the exit test passes, the CBC Run's README gains its
**Prerequisites** section. It holds the environment lines a
new machine needs before this Runtime Ground can stand. It is
derived from the Operator Manual, carries only what someone new to the repo needs
in hand, and links the manual for the rest. The Agent Skill Template is
`.claude/skills/infra-establish/templates/readme-prerequisites.md`,
in this Agent Skill. Merge it and fill it, and the section is the CBC
Run's own (`.claude/rules/delivered-copies.md`, rule 8, *An Agent Skill Template is…*).

The stack's own prerequisite line is **not** written here. Its fact
is created at the CBC Bootstrap, whose Agent Skill carries it. The
README this CBC Run was born with has no Prerequisites section. It arrives now,
because the exit test made it true.

If the project keeps public docs, derive the setup guide from the
Operator Manual now. It is never a second home.

## The Names defined here

The project's Infrastructure Contract is where it writes its own
words. These three are the stack's, listed in `docs/glossary/stack.md`:

- **Execution Environment** — the local runtime host for
  infrastructure.
- **Infrastructure Service** — a capability provided to the system.
- **Infrastructure Service Constraint** — a requirement or limit put
  on an Infrastructure Service.
