---
foundation: the agent model
---

# Agent arrangement

**The agent side of a project: the files that make an agent work
here a particular way, and that a copy of the project can drop
while keeping the work.**

## What it is for

So that an agent works in a project the way the project needs, from
the first session, and the project can shed the arrangement and keep
its work. The failure it answers was measured before it was adopted,
in the handbook's entry file, and is reported here, since this repo
cannot re-check it: restating convention rules "so they are always
in context" grew the entry file to 98 lines, split across two files,
with three disagreeing copies of one rule. Adopted with the
container (ADR-0038, 1c). Lived since: every run was born with
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
section each (`docs/conventions/conventions/` §2.4, *The seats*).

### The run's seat — a builder's

Shipped in `delivery/container/`: the deliverer writes it and the
run receives it. Its entry file says that `docs/concept/` and the
skills, rules, shapes and approaches on trial under `.claude/` are
delivered copies, pinned, and that until the framing artifacts
exist the only method work is running `cbc-framing` jointly with
the human. It holds five convention skills, the retrospective's two
among them, one approach on trial, `approach-drafting`, and four
rules: `shapes-lifecycle.md`, `delivered-copies.md`, the
exchange's half for this side, and `writing.md` and `one-home.md`,
loaded in every session. The work
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
convention skills `commit-messages`, `commit-plan` and
`visual-comparison`, not the retrospective's, whose seat here is on
trial; the exchange's skills, `exchange-read` and
`exchange-deliver`; the rules every session loads, `writing.md`,
`one-home.md` and `foundation-check.md`, the check before a commit;
the rules loaded by path, `exchange-reading.md`, the form of a
reading, `working-a-reading.md`, how a reading's list is worked,
and `convention-manual.md`, the form of a manual; and its
approaches on trial (§3.8, *`approaches-on-trial/`*). Its
decisions log
holds arrangement decisions only, and no registry: it receives no
conventions, and no one reads it but itself, so an entry that
follows from an ADR is a line pointing at it (ADR-0042). A
run's log keeps its registry, and its entries run longer because
`exchange-read` reads them.

### What the difference is

Each seat's skills and rules are derived from their manuals and
written for their seat, never copied across (ADR-0042, ADR-0069);
the records
table has the same shape; the agent and project split is the same
rule. What differs is the job, and the two hold different things
because of it (ADR-0036): the run holds the receiver's rule,
`delivered-copies.md` — how to take a newer copy without losing its
own edits, and what it may do to one meanwhile; the deliverer holds
the deliverer's skills and the form of the reading they produce.
Neither holds the other's half, because neither could run it. The
two rules both seats load in every session differ by the job too,
and each
manual names how in its list of what derives from it:
`docs/conventions/writing/` and
`docs/conventions/facts-in-sync/`.

*Its story: devlog 2026-09-26; devlog 2026-10-29, the lessons' own stories: project-recording and agent-arrangement.*

## 1. What the arrangement is

The theory this leans on is `docs/models/agent.md`: the ambient
channel (`docs/models/agent.md` §4.1, *ambient*), the choosing table
(`docs/models/agent.md` §8, *Choosing a channel*), the claims (`docs/models/agent.md`
§12, *Claims*). The model describes; this page explains against it, and its binding is what Claude Code gives each channel
(§5, *The binding: Claude Code*).

### 1.1 A closed list of paths

The arrangement's paths are a closed list (ADR-0038, 1c):

- **`CLAUDE.md`** — the entry file (§2, *The entry file*). The name is the tool's;
  what goes in it is this convention's.
- **`.claude/`** — the skills directory, the rules directory, the
  shapes directory, the approaches on trial, the decisions log, and
  the tool's settings, tracked and machine-local (§3, *`.claude/`*).

### 1.2 Detachable, and kept so

A file is agent-side when removing it
breaks nothing about the project (ADR-0038, 1c). How a commit that
touches these paths is made is commit-messages'
(`docs/conventions/commit-messages/` §2.3, *The agent's files never share…*). `COMMIT-PLAN.md`
is `docs/conventions/commit-plan/`'s artifact, not this
convention's.

### 1.3 Not records

The arrangement holds no project truth: nothing
here says what the project is deciding, planning or shipping. It
says how an agent is to work in it. Where the two sides touch — the
records table in the entry file, a run's decisions log's promotion
queue — the touch is stated by the convention that owns the content,
and this one holds the container.

## 2. The entry file

### 2.1 What

One file, loaded into an agent's context at the start of every
session before it is given any task. It holds what every session
needs: what the project is, where the records are, and the little
that has to be present on every task because no moment would
deliver it. It is not a map of the code. An overview of a repository
did not help agents find the right file (Gloaguen et al., arXiv
2602.11988, 2026, measured), and the tool's documentation leaves
file-by-file descriptions out. Which conventions
apply is not in it: in a run, the birth entry in
`.claude/decisions.md` is that list (§3.4, *`decisions.md`*); at the deliverer, it is
the `foundation` each of its skills and rules names. Each
convention reaches the agent through its own channel.

### 2.2 Why

The records teach their own use, and so does every stub in the
arrangement — each carries its rules in embedded comments, met at
the moment the file is opened. That only works if the agent knows
the files exist. The entry file is the one piece of text present
before anything is looked up. It earns that by holding only what
every session needs, never a convention's rules.

### 2.3 Where

Repo root, or under `.claude/` — Claude Code reads `CLAUDE.md` at
either address as one file (§5.1, *The mapping*). The
container ships it under `.claude/`, so that every agent-side path
sits in one directory; a project that wants it at the root moves it.
The deliverer's sits at the root.

### 2.4 How

The file is paid for on every task, so the boundary is a test
applied to every line, not a list of sections. Three tests, the same
three the stub's guard comment states:

- **True of this project and nowhere else.** A line that would be
  true in another project is a convention, and lives there — once. If
  the rule rides in a skill or a stub, it is not repeated here. If
  the convention's moment is every task, its rule loads with no
  `paths:` (§3.9, *A rule loaded in every session*): the convention's channel, not a line here.
  **It points; it never restates**: a summary is lossy on arrival,
  and then two files disagree while both look current
  (`docs/models/agent.md` §12.7, *On summaries*, claim M1).
- **No moment.** A line with a moment goes where the moment is — the
  record's stub, README, a skill, or, for a rule true only under one
  directory, a rules file with a `paths:` list (§3.2, *`rules/`*) — and is read
  there, at the moment it is about, instead of on every task it is
  not.
- **Nothing else would deliver it.** What stays is what no channel fires
  for: what the project is, where its records are, a stance, a fact
  whose failure is not noticing it. A
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
convention (`docs/conventions/project-recording/` §13, *The records table*).

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
`.claude/skills/`, a rules file under `.claude/rules/` (§3.2, *`rules/`*). Most
facts that feel local have a moment, which is why this slot stays
short.

### 2.5 When

Written at project start — a run's from the container's, the
deliverer's from this page (ADR-0042). Revisited when a record
moves, a convention is adopted, or the build command changes, and at the re-reading its size asks for (§2.6, *Size*), not otherwise.

### 2.6 Size

The entry file is the ambient channel (`docs/models/agent.md` §4.1, *ambient*):
paid on every task, including the tasks it is irrelevant to, and each
line added lowers compliance with every other
(`docs/models/agent.md` §12.1, *On ambient*, claim A2,
assumed). So its size is a running concern, not a one-time one. The
cost is what the harness delivers, not the file: HTML comments are
dropped on load (§5.3, *Memory files and their…*), so the guard and the
records comment cost nothing per task and are read when the file is
opened to edit it — the moment they govern. If what remains is longer
than a screen, something in it belongs in a convention, a record or a
skill; shrinking it is maintenance, not tidying. The tool's
documentation sets a looser bound, under 200 lines; a screen is
ours. Noticing that has no
moment of its own, so a run re-reads the file at its retrospective:
the skill's close asks it, and every line passes the three tests again
or leaves — the same move a run's decisions log makes for its entries.
The deliverer has no project end, and re-reads it at each step's close
instead, as a closing item of its gate (ADR-0057).

## 3. `.claude/`

### 3.1 `skills/`

Where a convention's skills live, one directory per skill: in a
run, a delivered copy, verbatim (the update is
`docs/conventions/exchange/`'s); at the deliverer, its own
derivation from the manual (ADR-0042). This convention owns the
place. A project may add a skill of its own, for a moment-bound
local rule the entry file must not hold (§2, *The entry file*). Work no skill covers
starts from an approach on trial (§3.8, *`approaches-on-trial/`*), and a skill is written only
when an evaluation places one (`docs/models/idea-to-output.md` §4.2,
*Up, work to an idea*). How that is done is
`.claude/approaches-on-trial/approach-drafting.md`'s and its
evaluation's.
*Its story: ADR-0056; ADR-0058.*

### 3.2 `rules/`

Instruction files read like the entry file, with one extra: a `paths:`
list at the top. When a file loads, and its limits, are this page's
(§5.6, *Rules files*). The
home for a rule true only in one part of the tree, which a skill would
carry only if the agent noticed the moment. Without the list, the file
is the entry file by another name and fails the entry file's tests the same way
(§2.4, *How*), with one exception (§3.9, *A rule loaded in every session*).

### 3.3 `shapes/`

Where a project keeps its shapes. What a shape is, and why this is
a directory nothing loads, are `docs/conventions/shapes/`'s; this
convention places the directory and states nothing else about it.
A project with no shape has none: it arrives with a group that
ships shapes, or when the project writes its first.

### 3.4 `decisions.md`

The arrangement's decision log: append-only and dated, each entry in
three parts — what changed, why, what was rejected. The standing rule
rides as a comment in the artifact it governs; the log keeps the why
and the rejected options; neither repeats the other. A run's also
holds what it was delivered: its birth entry lists the conventions
it holds, and each delivery entry the pin and the read-through
(`docs/conventions/exchange/` §2.2, *The run*). The deliverer's holds neither,
since it receives no delivery (ADR-0042). Its rules ride in its
own stub.

*Its story: devlog 2026-10-17, later; devlog 2026-10-29, the lessons' own stories: project-recording and agent-arrangement.*

### 3.5 `settings.json`

The tool's settings that are the project's: tracked, and the one
place the arrangement holds a gate as repo state. Not born with the
project: a project adds it when it has a rule that must not depend
on text — a permission rule that halts a command at a prompt the
human answers — or an exclude to declare. The commit stop is not
such a rule (`docs/conventions/commit-messages/` §2.4, *Commit on the word*). JSON carries no
comment, so the why lives in the decisions log, never in the file;
later inserts are merges, not text edits.

### 3.6 `settings.local.json`

The tool's machine-local state, never project truth; the hygiene
base ignores it (`docs/conventions/repo-hygiene/`).

### 3.7 `CLAUDE.local.md`

Not under `.claude/`, but the arrangement's neighbour: the operator's
standing instructions, loaded beside the entry file and read the same
way (`docs/models/agent.md` §4.1, *ambient*, ownership). One person, one
checkout; the hygiene base ignores it, and its words never enter a
record — a record that quotes it has let one operator's preference
into the project's truth. The container ships none, and a run's
stays ignored. The deliverer tracks its own: it has one operator,
and a setting kept out of git is one no reader of the repo can see
(ADR-0062). Outside practice ignores the file, as the tool's
documentation advises. Ours differs only because this repo has one
operator.

It holds the operator's settings, never rules. A setting is a
choice one operator makes where the project leaves it open: how
often the agent stops for review, how far it decides alone, how a
session starts. One test sorts a line: would another operator of
the same project write it differently? Then it is a setting, and
stays here. Would every operator want it? Then it is a rule, and
goes where the project keeps its rules; the file only uses it. For
example, "small commits only where the reviewer grants them" is a
rule, and "on this branch, commit freely" is a setting. The
operator writes the file for each project and carries it there by
hand.

*Its story: devlog 2026-10-18; devlog 2026-10-29, the lessons' own stories: project-recording and agent-arrangement.*


### 3.8 `approaches-on-trial/`

Where a project keeps its approaches on trial: one file per kind of
work, not yet proven. Nothing loads the directory. A step's opening
item sends the agent to it (`PLAN.md`'s step form). What an approach
is lives above (`docs/models/idea-to-output.md` §2, *The kinds*);
how one is drafted and how one is evaluated are
`.claude/approaches-on-trial/approach-drafting.md`'s and
`.claude/approaches-on-trial/approach-evaluation.md`'s. This
convention places the directory and states nothing else about it.
In a run, an approach the deliverer ships is a pinned copy
(`docs/conventions/exchange/` §3.2, *What goes*), and one the run drafts is its
own. *Its story: ADR-0058.*

### 3.9 A rule loaded in every session

A convention whose moment is every task ships its rule with no
`paths:`, so it loads in every session. Its moment is every answer
and every record written, and no path, skill or stub fires at all
of them. Such a rule fails the entry file's first test (§2.4, *How*), since it is true in
any project. It passes as the convention's own channel: derived
from its manual, and naming the manual in `foundation`. That keeps it from being the rulebook the anti-patterns warn of
(§4, *Anti-patterns*): one file per convention, never a
restatement. It is paid for in every session (§2.6, *Size*), so few
qualify. *Its story: ADR-0053.*

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
  human keeps saying is the model's told diagnostic
  (`docs/models/agent.md` §8, *Choosing a channel*): a convention
  is missing, or its channel is not firing. `CLAUDE.local.md` makes
  the saying persistent and the diagnosis invisible.

## 5. The binding: Claude Code

The agent model names the channels and the gate
(`docs/models/agent.md` §4, *The channels*, §7, *The gate*); a binding names the mechanisms one
tool gives each (`docs/models/agent.md` §10, *Bindings (Layer 2)*). This is Claude Code's,
the tool both seats use. It changes with the tool's releases, so
each fact says which release it was checked against, and a change
is made here alone. A second tool's binding would be written beside
this one, and writing it is the test for tool-shaped assumptions
hiding in the model. None has been needed.

### 5.1 The mapping

Sketch, Claude Code — checked against 2.1.310 on 2026-10-24, by its
documentation, by what could be observed here, and by bug reports
(first checked against 2.1.284 on 2026-09-29):

| Layer 1 | Claude Code mechanism |
|---|---|
| ambient | memory files — `CLAUDE.md` (root or under `.claude/`), `~/.claude/CLAUDE.md`, `@` imports; `AGENTS.md`, read when no `CLAUDE.md` is found; `.claude/rules/*.md` without a `paths:` list; `CLAUDE.local.md`, the operator's; the first 200 lines of auto memory's `MEMORY.md`; a skill's `name` and `description` |
| pulled | `Read`, `Grep`, `Glob`; a skill's body, once the agent invokes it |
| pushed | context-injecting hooks, slash commands, subagents; `.claude/rules/*.md` with a `paths:` list, and a `CLAUDE.md` in a subdirectory — loaded when the agent reads, writes or edits a matching file, or reads one from the shell with a command such as `cat`; not on a script's edit (§5.6, *Rules files*) |
| told | the prompt |
| observed | tool results |
| installed | files in the repo; the container that puts them there at birth |
| gate | blocking hooks (`PreToolUse`), CI; permission rules in `settings.json` — `ask` stops at a prompt, `deny` refuses |

### 5.2 Hooks

Hooks appear twice: some inject context (pushed), others block (gate).
One mechanism, two roles — a binding has to say which.

### 5.3 Memory files and their comments

Memory files arrive without their HTML comments. The loader drops every
block-level `<!-- … -->` comment before the text enters context — one
inside a code block is kept — so a comment in an entry file is never
ambient: it reaches the agent only when the file is opened with a tool,
which for the entry file is edit time. Observed on 2.1.260 through
2.1.263, documented since, and observed again on 2.1.284: this repo's
`CLAUDE.md` holds two comment blocks, and the text a session loads
holds neither. The same loader honours `claudeMdExcludes` in
`settings.json`, globs against the absolute path, which is how a
template entry file kept inside a repo stays out of its sessions.

### 5.4 Permission rules

A permission rule is a gate only in a mode that honours it. `deny`
refuses in every mode. `ask` still prompts in auto mode and in the
mode that bypasses permissions; the mode that never asks turns it
into a refusal. What no rule matches, auto mode has a classifier
decide in the background. The gate is the tool's, not the repo's.

A rule reaches only what the tool can name. A `Read` deny covers the
file tools and the shell commands the tool knows as file commands,
such as `cat`, `head` and `sed`. It does not cover `grep -r` across a
tree, or a script that opens files itself; the documentation sends
that to the sandbox.

### 5.5 Skills

Skills appear twice as well, and neither time under pushed. Claude
Code loads a skill's `name` and `description` at session start and its
body only when the agent invokes it: an ambient trigger over a pulled
body. The agent still decides, and pushed promises it does not
(`docs/models/agent.md` §4.3, *pushed*). A skill is still the closest this tool
gets to pushed for a rule about an action; a hook closes the
remainder.

The tool ignores a frontmatter field it does not know, without an
error, in a skill as in a rule. Our `foundation` lines are for a
reader of the file, never for the tool. A skill may also
carry a `paths:` list; what it does to a skill this repo has not
checked.

### 5.6 Rules files

`.claude/rules/` holds instruction files like `CLAUDE.md`, with one
extra: a `paths:` list at the top. Without it, the file is read every
session — ambient, no different from `CLAUDE.md`. With it, the file
loads when the agent reads, writes or edits a file under one of
those paths, or reads one from the shell with a command such as
`cat` or `head`. The tool decides that, not the agent. That is pushed
with no hook to write. A `CLAUDE.md` in a subdirectory loads the
same way.

Three limits:

- **It arrives after the first draft.** A new file's content is
  written in the call that loads the rule, so a record written from
  scratch gets the rule no earlier than a comment in a template would
  have given it.
- **A script's edit loads nothing,** and nor does listing the
  directory.
- **Its condition is a place, never an action** — "when work is under
  `generated/`", not "when committing" — so it does not replace a
  skill. A skill is the agent's judgment about an action; a rules
  file is the tool's check on a touched file.

What is documented and what is seen have differed. On 2.1.284 this
repo saw the Read tool alone load a rule; on 2.1.310 a `sed` read
loaded one, as the documentation now says. Bug reports, checked
2026-10-24, show `paths:` failing silently in some formats and seats
(Claude Code issues #17204, #33581, #87217). A rule that must arrive
does not rest on a path alone (`docs/models/agent.md` §7, *The gate*).

### 5.7 What a session keeps, and what a helper gets

- **Compaction** restores the root `CLAUDE.md`, the rules without
  `paths:` and auto memory from disk. A path rule and a subdirectory's
  `CLAUDE.md` come back only when a matching file is touched again.
  An invoked skill's body comes back cut to 5,000 tokens.
- **A subagent** loads the `CLAUDE.md` files, the rules and
  `CLAUDE.local.md`, but not auto memory, and no skill body unless
  its definition names the skill. The built-in Explore and Plan
  agents skip `CLAUDE.md`. A fork inherits the whole conversation.

So what a delegated task must know goes in its prompt, which is told
(`docs/models/agent.md` §4.4, *told*). An Explore or Plan agent gets none of
the rules loaded every session, only the path rules of the files it
touches.

## Why it arrives this way

Every rule here governs a file the container ships and rides in it
as a comment: the entry file's comments carry points-never-restates,
the guard and the size rule; the decisions log's carry its own.
Acting on the file is the trigger (`docs/models/agent.md` §4.6, *installed*).

Not a skill, because the failure guarded against is a noticing
failure: told "remember X", an agent writes X into the entry file
where it stands, and a skill fires only on recognising the moment.
Not paid at ambient cost either: the comments are dropped on load
(§5.3, *Memory files and their…*), so they are read when the file is opened to edit it
and cost nothing on any other task. A long guard is free; a long
records table is not.

A rule for an arrangement file goes in that file's stub comment,
not here and not in the entry file's prose. A project meets this
convention only as its files at birth, which are its own from then
on (`docs/conventions/exchange/` §2.4, *The records are the one…*).

## What this does not cover

- **The commit that touches these paths, and its scope** —
  `docs/conventions/commit-messages/`.
- **The records the entry file's table lists, and when each is
  touched** — `docs/conventions/project-recording/` §13, *The records table*.
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
