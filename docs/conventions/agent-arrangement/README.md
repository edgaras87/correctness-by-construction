# Agent arrangement

**The agent side of a project: the files that make an agent work
here a particular way, and that a copy of the project can drop
while keeping the work. The line is detachability (CBC ADR-0038,
1c): a file is agent-side when removing it breaks nothing about the
project. This page says what sits on its far side and what each
file may hold.**

## What it is for

So that an agent works in a project the way the project needs, from
the first session, and the project can shed the arrangement and keep
its work. The failure it answers was measured before it was adopted,
in the handbook's entry file, and is reported here, since this repo
cannot re-check it: restating convention rules "so they are always
in context" grew the entry file to 98 lines, split across two files,
with three disagreeing copies of one rule. Adopted with the
container (CBC ADR-0038, 1c). Lived since: every run was born with
the arrangement; run 3 moved its entry file under `.claude/` and it
was a pure rename, content untouched, the tool reading it at the new
address from the next session — which is why the container now ships
it there.

## What this is made usable as

- **`delivery/container/.claude/CLAUDE.md` — the entry file,
  shipped**, a body composed by the deliverer and not a stub;
  loaded at the start of every session, the run's own from birth.
- **`delivery/container/.claude/decisions.md` — the decisions-log
  stub, shipped**, opened when the arrangement changes; the run's
  own from birth.
- **The deliverer's own `CLAUDE.md` and `.claude/decisions.md`.**

Every rule here rides as a comment in the file it governs, met when
the file is opened to edit it; nothing here is loaded into an
agent. What derives from this page is that list. A change here
walks it; a change forced in one of them is checked back against
this page.

## The seats

Two derivations of this page, neither copied from the other: nearly
the same files, and different by design in their job — so a
section each (`docs/conventions/conventions/` §3.4).

### The run's seat — a builder's

Shipped in `delivery/container/`: the deliverer writes it and the
run receives it. Its entry file says that `docs/concept/` and
everything under `.claude/` are delivered copies, pinned, and that
until the framing artifacts exist the only method work is running
`cbc-framing` jointly with the human. It holds the three
convention skills, and two rules: `shapes-lifecycle.md` and
`delivered-copies.md`, the exchange's half for this side. The work
it arranges is building a real system, keeping its records and
taking deliveries; it changes the arrangement through its own
decisions log.

### The deliverer's seat — a maintainer's

The maintainer of the concept, the delivery and the records that
hold both: it keeps the concept's statement true, derives the
method from it, holds the master of every file a run receives,
delivers to runs, and reads them back to learn what to change. It
is not a builder; there is nothing to build. Its entry file sits at
the repo root, the address the arrangement is described from: *"A
concept repo… Documents only — no code, no runs."* It holds the
same three convention skills; the exchange's two, `exchange-read`
and `exchange-deliver`; and three rules of its own,
`exchange-reading.md`, the shape of a reading,
`working-a-reading.md`, how a reading's list is worked, and
`convention-manual.md`, the shape of a manual. Its decisions log
holds arrangement decisions only, and no registry: it receives no
conventions, and no one reads it but itself, so an entry that
follows from an ADR is a line pointing at it (CBC ADR-0042). A
run's log keeps its registry, and its entries run longer because
`exchange-read` reads them.

### What the difference is

Three skills are identical files, each derived from its manual on
both sides rather than copied across (CBC ADR-0042); the records
table has the same shape; the agent and project split is the same
rule. What differs is the job, and since CBC ADR-0036 the two hold
different things because of it: the run holds the receiver's rule,
`delivered-copies.md` — how to take a newer copy without losing its
own edits, and what it may do to one meanwhile; the deliverer holds
the deliverer's skills and the shape of the reading they produce.
Neither holds the other's half, because neither could run it.

*Until 2026-09-26 the deliverer held the receiver's protocol,
`convention-lifecycle`, and had never once run it — its registry
pinned it to itself — while run 3 ran it at every take. Reading a
shared file and assuming a shared job is how a rule ends up held in
the repo that cannot apply it.*

## 1. What the arrangement is

The theory this leans on is `docs/models/agent.md`: the ambient
channel (§4.1), the choosing table (§8), the claims (§12). The model
describes; this page explains against it.

A closed list of paths (CBC ADR-0038, 1c):

- **`CLAUDE.md`** — the entry file, §2. The name is the tool's;
  what goes in it is this convention's.
- **`.claude/`** — the skills directory, the rules directory, the
  shapes directory, the decisions log, and the tool's settings,
  tracked and machine-local, §3.

**Detachable, and kept so.** A commit that touches these paths
touches nothing else, scoped `agent` — the rule is
`docs/conventions/commit-messages/` §2. `COMMIT-PLAN.md` rides the
same scope while it exists but is
`docs/conventions/commit-plan/`'s artifact, not this convention's.

**Not records.** The arrangement holds no project truth: nothing
here says what the project is deciding, planning or shipping. It
says how an agent is to work in it. Where the two sides touch — the
records table in the entry file, a run's decisions log's promotion
queue — the touch is stated by the convention that owns the content,
and this one holds the container.

## 2. The entry file

### 2.1 What

One file, loaded into an agent's context at the start of every
session before it is given any task. It is a map — what the project
is, where the records are — and the little that has to be present on
every task because no moment would deliver it. Which conventions
apply is not in it: in a run, the registry in `.claude/decisions.md`
is that list (§3.4); at the deliverer, it is the `foundation` each of
its skills and rules names. Each convention reaches the agent
through its own channel.

### 2.2 Why

The records teach their own use, and so does every stub in the
arrangement — each carries its rules in embedded comments, met at
the moment the file is opened. That only works if the agent knows
the files exist. The entry file is the one piece of text present
before anything is looked up, and it earns that by being a map, not
a rulebook.

### 2.3 Where

Repo root, or under `.claude/` — Claude Code reads `CLAUDE.md` at
either address as one file (model §10.1). The container ships it under
`.claude/`, so that every agent-side path sits in one directory; a
project that wants it at the root moves it, which one run showed to
be a pure rename — content untouched, the tool reading the file at
the new address from the next session. The deliverer's sits at the
root.

### 2.4 How

The file is paid for on every task, so the boundary is a test
applied to every line, not a list of sections. Three tests, the same
three the stub's guard comment states:

- **True of this project and nowhere else.** A line that would be
  true in another project is a convention, and lives there — once. If
  the rule rides in a skill or a stub, it is not repeated here.
  **It points; it never restates**: a summary is lossy on arrival,
  and then two files disagree while both look current (model claim
  M1).
- **No moment.** A line with a moment goes where the moment is — the
  record's stub, README, a skill, or, for a rule true only under one
  directory, a rules file with a `paths:` list (§3.2) — and is read
  there, at the moment it is about, instead of on every task it is
  not.
- **Nothing else would deliver it.** What stays is what no channel fires
  for: a map, a stance, a fact whose failure is not noticing it. A
  rule that acts somewhere lives there; the entry file says where.

What passes, in practice, is five kinds of content: what the project is
· the records table · build and test commands, where the project has
them · how to work here · local rules that have no
moment. That is a description of what the tests leave, not a fence — a
line that passes belongs whatever heading it sits under, and no heading
saves one that fails. The first two are present at birth; the other
three arrive when they become true, and take their
headings from the names below — *How to work here*, *Local rules* — so
two born repos spell them the same way.

*The records table* is the slot this convention provides and
`docs/conventions/project-recording/` fills: its rows, and the
requirement that every row names a moment, belong to that
convention (its §13).

*How to work here* is the stance a project expects where it is not
the obvious one — "decide before building", "prefer exploring over
shipping". It is the one thing that is genuinely per-project and has
no other home: a convention cannot hold it, because a convention is
what is true across projects. It is also the easiest slot in which to
start rebuilding the rulebook, so it takes stance and not rules.

*Local rules* pass one test before they enter: **a rule earns
ambient space only when its failure is not noticing the moment**. A
test prerequisite, a migration rule, a service that must be running
fails: each has a moment, and goes where the moment is — the
record's stub, README, a skill the project adds under
`.claude/skills/`, a rules file under `.claude/rules/` (§3.2). Most
facts that feel local have a moment, which is why this slot stays
short.

### 2.5 When

Written at project start — a run's from the container's, the
deliverer's from this page (CBC ADR-0042). Revisited when a record
moves, a convention is adopted, or the build command changes, and at
the re-reading §2.6 names — not otherwise.

### 2.6 Size

The entry file is the ambient channel (model §4.1): paid on every
task, including the tasks it is irrelevant to, and each line added
lowers compliance with every other (model claim A2, assumed). So its
size is a running concern, not a one-time one. The cost is what the
harness delivers, not the file: HTML comments are dropped on load
(model §10.3), so the guard and the records comment cost nothing per
task and are read when the file is opened to edit it — the moment
they govern. If what remains is longer than a screen, something in
it belongs in a convention, a record or a skill; shrinking it is
maintenance, not tidying. Noticing that has no moment of its own, so
a run re-reads the file at its project retrospective: the plan's
questionnaire asks it, and every line passes the three tests again
or leaves — the same move a run's decisions log makes for its
entries. The deliverer has no project end, and re-reads it at each
milestone's close instead, as a gate item (CBC ADR-0041).

## 3. `.claude/`

### 3.1 `skills/`

Where a convention's skill lives, one directory per convention: in a
run, a delivered copy, verbatim (the update is
`docs/conventions/exchange/`'s); at the deliverer, its own
derivation from the manual (CBC ADR-0042). This convention owns the
place. A project may add a skill of its own, for a moment-bound
local rule the entry file must not hold (§2) — permitted, and not
yet defined: what such a skill is, whether it registers, how it
survives the agent/project split are open until a project has
written one.

### 3.2 `rules/`

Instruction files read like the entry file, with one extra: a
`paths:` list at the top makes the file load only when the agent
reads a file under one of those paths with the Read tool — not when
it writes a new one there — the tool deciding, not the agent (model §10.6). The home for a rule true only in one part of the tree, which a
skill would carry only if the agent noticed the moment. Without the
list, the file is the entry file by another name and fails §2.4's
tests the same way. The container ships two — `shapes-lifecycle.md`,
whose convention is `docs/conventions/shapes/`, and
`delivered-copies.md`, whose convention is
`docs/conventions/exchange/` — and the deliverer holds its own.
*Empty at birth until 2026-09-23.*

### 3.3 `shapes/`

Where a project keeps an unexposed shape. What a shape is, why this
is a directory nothing loads, and who moves one between here and
`rules/` are `docs/conventions/shapes/`'s; this convention places
the directory and states nothing else about it. Not born with the
project: a project makes it when it writes its first shape.

### 3.4 `decisions.md`

The arrangement's decision log: append-only, dated, three lines per
entry — what changed, why, what was rejected. The standing rule
rides as a comment in the artifact it governs; the log keeps the why
and the rejected options; neither repeats the other. A run's doubles
as its convention registry (`docs/conventions/exchange/` §2); the
deliverer's does not, since it receives no conventions (CBC
ADR-0042). Its rules ride in its own stub.

### 3.5 `settings.json`

The tool's settings that are the project's: tracked, and the one
place the arrangement holds a gate as repo state. Not born with the
project: a project adds it when it has a rule that must not depend
on text — a permission rule that halts a command at a prompt the
human answers — or an exclude to declare. The commit stop is not
such a rule: `docs/conventions/commit-messages/` §2. JSON carries no
comment, so the why lives in the decisions log, never in the file;
later inserts are merges, not text edits.

### 3.6 `settings.local.json`

The tool's machine-local state, never project truth; the hygiene
base ignores it (`docs/conventions/repo-hygiene/`).

### 3.7 `CLAUDE.local.md`

Not under `.claude/`, but the arrangement's neighbour: the
operator's standing instructions, loaded beside the entry file and
read the same way (model §4.1, ownership). One person, one checkout;
the hygiene base ignores it, and its words never enter a record — a
record that quotes it has let one operator's preference into the
project's truth. The container ships none.

## 4. Anti-patterns

- **Putting rules in the working-style slot** — a rule that is true
  in another project is a convention wearing a stance's clothes.
- **A local rule with a moment** — "run Docker before the tests" —
  paid for on every session and read at none of the moments it is
  about.
- **Shipping the stance and local-rules slots as empty sections** — a
  header waiting for content is weight with no guard in it; the stub
  carries the test, and the header arrives with the first line that
  passes it.
- **Restating a convention's rules "so they are always in context"** —
  the rulebook pattern; it grows once per convention and drifts from
  the source.
- **A second entry file kept beside the first for another tool**,
  unless that tool is actually in use.
- **Project truth in the arrangement** — local status, a decision
  about the system, a plan step. They belong in PLAN.md, `docs/adr/`,
  the records; the arrangement is what a portfolio copy drops.
- **Growth by accretion** — every line added dilutes every other line,
  so removing one is maintenance, not tidying.
- **Parking a repeated rule in the operator's file** — a rule the
  human keeps saying is the model's told diagnostic (§8): a convention
  is missing, or its channel is not firing. `CLAUDE.local.md` makes
  the saying persistent and the diagnosis invisible.

## Why it arrives this way

Every rule here governs a file the container ships and rides in it
as a comment: the entry file's comments carry points-never-restates,
the guard and the size rule; the decisions log's carry its own.
Acting on the file is the trigger.

Not a skill, because the failure guarded against is a noticing
failure: told "remember X", an agent writes X into the entry file
where it stands, and a skill fires only on recognising the moment.
Not paid at ambient cost either: the comments are dropped on load
(§2.6), so they are read when the file is opened to edit it
and cost nothing on any other task. A long guard is free; a long
records table is not.

A rule for an arrangement file goes in that file's stub comment,
not here and not in the entry file's prose. A project meets this
convention only as its files at birth and as their changed comment
text at an update, through `docs/conventions/exchange/`.

## What this does not cover

- **The commit that touches these paths, and its scope** —
  `docs/conventions/commit-messages/`.
- **The records the entry file's table lists, and when each is
  touched** — `docs/conventions/project-recording/` §13.
- **What a shape is, and how one lives** —
  `docs/conventions/shapes/`.
- **How a copy under `.claude/` is updated, and what a run may do
  to it** — `docs/conventions/exchange/`.
- **What the hygiene base ignores** —
  `docs/conventions/repo-hygiene/`.

## Where to look

- The stubs: `delivery/container/.claude/CLAUDE.md` and
  `delivery/container/.claude/decisions.md`.
- The model it explains against: `docs/models/agent.md`.
