# Agent arrangement

The agent side of a project: the files that make an agent work here
a particular way, and that a copy of the project can drop while
keeping the work. ADR-0019 drew the line; this page says what sits
on its far side and what each file may hold (ADR-0033).

**What ships:** two stubs in the starter kit, linked from
[`stubs/`](stubs/) beside this page — the entry file `CLAUDE.md`
and the decisions log `.claude/decisions.md`. Every rule here rides
as a comment in the file it governs, met when the file is opened to
edit it. This page explains the arrangement; the stubs state the
rules. Nothing here is loaded into an agent.

The theory this leans on is [`models/agent.md`](../../models/agent.md):
the ambient channel (§4), the choosing table (§8), the claims (§12).
The model describes; this page explains against it.

---

## 1. What the arrangement is

A closed list of paths (ADR-0019):

- **`CLAUDE.md`** — the entry file, §2. The name is the tool's
  (ADR-0014); the shape is this convention's.
- **`.claude/`** — the skills directory, the decisions log, and the
  tool's settings, tracked and machine-local, §3.

**Detachable, and kept so.** A commit that touches these paths
touches nothing else, scoped `agent` — the rule is commit-messages',
stated there. `CHANGE-PLAN.md` rides the same scope while it exists
but is change-plans' artifact, not this convention's.

**Not records.** The arrangement holds no project truth: nothing here
says what the project is deciding, planning or shipping. It says how
an agent is to work in it. Where the two sides touch — the records
table in the entry file, the decisions log's promotion queue — the
touch is stated by the convention that owns the content, and this one
holds the container.

## 2. The entry file

**What.** One file at the repo root, loaded into an agent's context
at the start of every session before it is given any task. It is a
map — what the project is, where the records are — and the little
that has to be present on every task because no moment would deliver
it. Which conventions apply is not in it: the registry in
`.claude/decisions.md` is that list (§3, ADR-0034), and each
convention reaches the agent through its own channel.

**Why.** The records teach their own use, and so does every stub in the
arrangement — each carries its rules in embedded comments, met at the
moment the file is opened (ADR-0004). That only works if the
agent knows the files exist. The entry file is the one piece of text
present before anything is looked up, and it earns that by being a map,
not a rulebook.

**Where.** Repo root, or under `.claude/` — Claude Code reads
`CLAUDE.md` at either address as one file (model §10), and a project may
take the second so that every agent-side path sits in one directory.
Whatever the tool looks for otherwise (ADR-0014). The starter
kit ships it at the root; a bundle that wants the other address
renames it at birth (ADR-0035, decision 5).

**How.** The file is paid for on every task, so the boundary is a
test applied to every line, not a list of sections. Three tests, the
same three the stub's guard comment states:

- **True of this project and nowhere else.** A line that would be
  true in another project is a convention, and lives there — once. If
  the rule rides in a skill or a stub, it is not repeated here.
  **It points; it never restates**: a summary is lossy on arrival,
  and then two files disagree while both look current (model claim
  M1; ADR-0014 records the measured case).
- **No moment.** A line with a moment goes where the moment is — the
  record's stub, README, a skill, or, for a rule true only under one
  directory, a rules file with a `paths:` list (§3) — and is read
  there, at the moment it is about, instead of on every task it is
  not.
- **Nothing else would deliver it.** What stays is what no channel fires
  for: a map, a stance, a fact whose failure is not noticing it
  (ADR-0018). A rule that acts somewhere lives there; the entry
  file says where.

What passes, in practice, is five kinds of content: what the project is
· the records table · build and test commands, where the project has
them (ADR-0026) · how to work here · local rules that have no
moment. That is a description of what the tests leave, not a fence — a
line that passes belongs whatever heading it sits under, and no heading
saves one that fails. The first two are present at birth; the other
three arrive when they become true (ADR-0032), and take their
headings from the names below — *How to work here*, *Local rules* — so
two born repos spell them the same way.

*The records table* is the slot this convention provides and
project-recording fills: its rows, and the requirement that every row
names a moment, belong to that convention (its §13, ADR-0018).

*How to work here* is the stance a project expects where it is not
the obvious one — "decide before building", "prefer exploring over
shipping". It is the one thing that is genuinely per-project and has
no other home: a convention cannot hold it, because a convention is
what is true across projects. It is also the easiest slot in which to
start rebuilding the rulebook, so it takes stance and not rules.

*Local rules* pass one test before they enter: **a rule earns ambient
space only when its failure is not noticing the moment**
(ADR-0018). A test prerequisite, a migration rule, a service
that must be running fails: each has a moment, and goes where the moment
is — the record's stub, README, a skill the project adds under
`.claude/skills/`, a rules file under `.claude/rules/` (§3). Most facts
that feel local have a moment, which is why this slot stays short.

**When.** Written at project start, from the starter stub. Revisited
when a record moves, a convention is adopted, or the build command
changes — not otherwise.

**Size.** The entry file is the ambient channel (model §4): paid on
every task, including the tasks it is irrelevant to, and each line added
lowers compliance with every other (model claim A2, assumed). So its
size is a running concern, not a one-time one. The cost is what the
harness delivers, not the file: HTML comments are dropped on load (model
§10, ADR-0036), so the guard and the records comment cost
nothing per task and are read when the file is opened to edit it — the
moment they govern. If what remains is longer than a screen, something
in it belongs in a convention, a record or a skill; shrinking it is
maintenance, not tidying. Noticing that has no moment of its own, so the
one moment that re-reads the file is the project retrospective: the
plan's questionnaire asks it, and every line passes the three tests
again or leaves — the same move the decisions log makes for its entries
(ADR-0020).

## 3. `.claude/`

**`skills/`** — where a convention delivered as a skill lands, one
directory per convention, the copy verbatim (convention-lifecycle §3
owns the update; this convention owns the place). A project may add
a skill of its own, for a moment-bound local rule the entry file
must not hold (§2) — permitted, and its
shape is not yet stated: what such a skill is, whether it registers,
how it survives the ADR-0019 split are open until a project has
written one.

**`rules/`** — instruction files read like the entry file, with one
extra: a `paths:` list at the top makes the file load only when the
agent reads a file under one of those paths with the Read tool — not
when it writes a new one there — the tool deciding, not the agent
(model §10). The home for a rule true only in one part
of the tree, which a skill would carry only if the agent noticed the
moment.
Without the list, the file is the entry file by another name and
fails §2's tests the same way. Empty at birth; the kit ships none.

**`decisions.md`** — the arrangement's decision log (ADR-0020):
append-only, dated, three lines per entry — what changed, why, what
was rejected. The standing rule rides as a comment in the artifact it
governs; the log keeps the why and the rejected options; neither
repeats the other. It doubles as the project's convention registry
(convention-lifecycle §2). Its rules ride in its own stub.

**`settings.json`** — the tool's settings that are the project's:
tracked, and the one place the arrangement holds a gate as repo state.
Not born with the project: a project adds it when it has a rule that
must not depend on text — a permission rule that halts a command at a
prompt the human answers — or an exclude to declare (ADR-0035,
ADR-0036). JSON carries no comment, so the why lives in the
decisions log, never in the file; later inserts are merges, not text
edits.

**`settings.local.json`** — the tool's machine-local state, never
project truth; the repo-hygiene base ignores it.

**`CLAUDE.local.md`** — not under `.claude/`, but the arrangement's
neighbour: the operator's standing instructions, loaded beside the
entry file and read the same way (model §4, ownership). One person,
one checkout; the repo-hygiene base ignores it, and its words never
enter a record — a record that quotes it has let one operator's
preference into the project's truth. The kit ships no shape for it.

## 4. Anti-patterns

- **Putting rules in the working-style slot** — a rule that is true
  in another project is a convention wearing a stance's clothes.
- **A local rule with a moment** — "run Docker before the tests" —
  paid for on every session and read at none of the moments it is
  about.
- **Shipping the stance and local-rules slots as empty sections** — a
  header waiting for content is weight with no guard in it; the stub
  carries the test, and the header arrives with the first line that
  passes it (ADR-0032).
- **Restating a convention's rules "so they are always in context"** —
  the rulebook shape; it grows once per convention and drifts from
  the source.
- **A second entry file kept beside the first for another tool**,
  unless that tool is actually in use (ADR-0014).
- **Project truth in the arrangement** — local status, a decision
  about the system, a plan step. They belong in PLAN.md, `docs/adr/`,
  the records; the arrangement is what a portfolio copy drops.
- **Growth by accretion** — every line added dilutes every other line,
  so removing one is maintenance, not tidying.
- **Parking a repeated rule in the operator's file** — a rule the
  human keeps saying is the model's told diagnostic (§8): a convention
  is missing, or its channel is not firing. `CLAUDE.local.md` makes
  the saying persistent and the diagnosis invisible.

---

## Why it is delivered as stubs

Every rule here governs a file the kit ships and rides in it as a
comment: the entry file's comments carry points-never-restates, the
guard and the size rule; the decisions log's carry ADR-0020's.
Acting on the file is the trigger (ADR-0004).

Not a skill, because the failure guarded against is a noticing
failure: told "remember X", an agent writes X into the entry file
where it stands, and a skill fires only on recognising the moment
(ADR-0018, ADR-0015). Not paid at ambient cost either: the harness
drops HTML comments from the entry file on load, so the comments
are read when the file is opened to edit it and cost nothing on any
other task (ADR-0036). That is why §2's size rule counts the lines
the harness delivers; a long guard is free, a long records table is
not.

A rule for an arrangement file goes in that file's stub comment,
not here and not in the entry file's prose. A project meets this
convention only as its stubs at birth and as their changed comment
text at an update, through the kit's protocol.

## Where to look

- The stubs: [`stubs/`](stubs/), links into `starter/kit/`.
- The records table the entry file carries:
  [`../project-recording/`](../project-recording/), its §13.
- The `agent` scope: [`../commit-messages/`](../commit-messages/).
- How a project receives and updates its arrangement:
  [`../convention-lifecycle/`](../convention-lifecycle/).
