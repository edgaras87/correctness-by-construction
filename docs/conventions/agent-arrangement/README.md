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
in the Entry File of the handbook, the repo this convention came
from, now history (ADR-0038). It is reported here, since this repo
cannot re-check it. Restating convention rules "so they are always in
context" grew the Entry File to 98 lines, split across two files,
with three disagreeing copies of one rule. Adopted with the
Container Group (ADR-0038, 1c). Lived since: every CBC Run was born
with the arrangement. CBC Run 3 moved its Entry File under `.claude/`.
It was a pure rename, content untouched, and the tool read it at the
new address from the next session. That is why the Container Group
now ships it there.

## What this is made usable as

- **`delivery/container/.claude/CLAUDE.md` — the Entry File,
  shipped**, a body composed by the Concept Deliverer and not a Record Stub;
  loaded at the start of every session, the CBC Run's own from birth.
- **`delivery/container/.claude/decisions.md` — the Decisions Log's
  Record Stub, shipped**, opened when the arrangement changes; the CBC Run's
  own from birth.
- **The Concept Deliverer's own `CLAUDE.md` and `.claude/decisions.md`.**

Every rule here is a comment in the file it governs, met when
the file is opened to edit it; nothing here is loaded into an
agent. What derives from this page is that list. A change here
runs the Change Walk on it; a change forced in one of them is checked back against
this page.

## The seats

Two derivations of this page, neither copied from the other: nearly
the same files, and different by design in their job — so a
section each (`docs/conventions/conventions/` §2.4, *The seats*).

### The CBC Run's seat

A builder's. Shipped in `delivery/container/`: the Concept Deliverer writes it and the
CBC Run receives it. Its Entry File says two things. `docs/concept/`
and the Agent Skills, Agent Rules, Output Shapes and Approaches on
Trial under `.claude/` are delivered copies, pinned. Until the CBC
Framing Exports exist, the only method work is running the
cbc-framing Agent Skill jointly with the reviewer. It holds:

- five convention Agent Skills, the retrospective Agent Skill and the
  apply-retrospective Agent Skill among them;
- one Approach on Trial, `approach-drafting`;
- four Agent Rules: `shapes-lifecycle.md`; `delivered-copies.md`, the
  Exchange Convention's half for this side; and `writing.md` and
  `one-home.md`, loaded in every session.

The work
it arranges is building a real system, keeping its records and
taking deliveries; it changes the arrangement through its own
Decisions Log.

### The Concept Deliverer's seat

A maintainer's. The maintainer of the concept, the delivery and the records that
hold both: it keeps the concept's statement true, derives the
method from it, holds the Master Copy of every file a CBC Run receives,
delivers to CBC Runs, and reads them back to learn what to change. It
is not a builder; there is nothing to build. Its Entry File sits at
the repo root, the address the arrangement is described from: *"A
Concept Repo… Documents only — no code, no CBC Runs."* It holds:

- the convention Agent Skills `commit-messages`, `commit-plan` and
  `visual-comparison`, not the retrospective manual's Agent Skills,
  whose Convention Seat here is on trial;
- the Exchange Convention's Agent Skills, `exchange-read` and
  `exchange-deliver`;
- the Agent Rules every session loads: `writing.md`, `one-home.md`
  and `foundation-check.md`, the Foundation Check;
- the Agent Rules loaded by path: `exchange-reading.md`, the form of a
  CBC Run Reading; `working-a-reading.md`, how a CBC Run Reading's list
  is worked; and `convention-manual.md`, the form of a manual;
- its Approaches on Trial (§3.8, *`.claude/approaches-on-trial/`*).

Its Decisions Log holds arrangement decisions only, and no birth
entry's list of conventions: it receives no conventions. No one reads
it but itself, so an entry that follows from an ADR is a line
pointing at it (ADR-0042). A CBC Run's Decisions Log keeps that list,
and its entries run longer because the exchange-read Agent Skill
reads them.

### What the difference is

What differs is the job, and the two hold different things because
of it (ADR-0036). Three things are the same:

- each Convention Seat's Agent Skills and Agent Rules are derived
  from their manuals and written for their Convention Seat, never
  copied across (ADR-0042, ADR-0069);
- the records table has the same shape;
- the agent and project split is the same rule.

The difference in what they hold: the CBC Run holds the receiver's
Agent Rule, `delivered-copies.md`. It says how to take a newer copy
without losing its own edits, and what it may do to one meanwhile.
The Concept Deliverer holds its Agent Skills, and the form of the CBC
Run Reading they produce.
Neither holds the other's half, because neither could run it. The
two Agent Rules both Convention Seats load in every session differ by the job too,
and each
manual names how in its list of what derives from it:
`docs/conventions/writing/` and
`docs/conventions/facts-in-sync/`.

*Its story: devlog 2026-09-26; devlog 2026-10-29, the lessons' own stories: project-recording and agent-arrangement.*

## 1. What the arrangement is

The arrangement is a closed list of agent-side paths a copy of the
project can drop. The theory this leans on is `docs/models/agent.md`:
the Ambient Channel (`docs/models/agent.md` §4.1, *Ambient Channel*), the choosing table
(`docs/models/agent.md` §8, *Choosing a channel*), the claims (`docs/models/agent.md`
§12, *Claims*). The Agent Model describes; this page explains against it. Its Tool Binding is what Claude Code gives each channel
(§5, *The Claude Code Tool Binding*).

### 1.1 A closed list of paths

The arrangement's paths are a closed list (ADR-0038, 1c):

- **`CLAUDE.md`** — the Entry File (§2, *The Entry File*). The name is the tool's;
  what goes in it is this convention's.
- **`.claude/`** — the Agent Skills directory, the Agent Rules directory, the
  Output Shapes directory, the Approaches on Trial, the Decisions Log, and
  the tool's settings, tracked and machine-local (§3, *`.claude/`*).

### 1.2 Detachability

A file is agent-side when removing it
breaks nothing about the project (ADR-0038, 1c). How a commit that
touches these paths is made is the commit-messages manual's
(`docs/conventions/commit-messages/` §2.3, *The `agent` scope*). `COMMIT-PLAN.md`
is the commit-plan manual's file, not this
convention's.

### 1.3 Not records

The arrangement holds no project truth: nothing
here says what the project is deciding, planning or shipping. It
says how an agent is to work in it. Where a project fact sits in an
arrangement file, the convention that owns the fact states it, and
this one holds the file it sits in: the records table in the Entry File, and a CBC
Run's Decisions Log's birth entry.

## 2. The Entry File

### 2.1 What the Entry File is

One file, loaded into an agent's context at the start of every
session before it is given any task. It holds what every session
needs: what the project is, where the records are, and the little
that has to be present on every task because no moment would
deliver it. It is not a map of the code. An overview of a repository
did not help agents find the right file (Gloaguen et al., arXiv
2602.11988, 2026, measured), and the tool's documentation leaves
file-by-file descriptions out. Which conventions
apply is not in it: in a CBC Run, the birth entry in
`.claude/decisions.md` is that list (§3.4, *`.claude/decisions.md`*); at the Concept Deliverer, it is
the `foundation` each of its Agent Skills and Agent Rules names. Each
convention reaches the agent through its own channel.

### 2.2 Why an Entry File

The Entry File is the one piece of text present before anything is
looked up. The records teach their own use, and so does every Record
Stub in the arrangement: each carries its rules in embedded comments,
met at the moment the file is opened. That only works if the agent
knows the files exist. The Entry File earns that by holding only
what every session needs, never a convention's rules.

### 2.3 Where the Entry File lives

Repo root, or under `.claude/` — Claude Code reads `CLAUDE.md` at
either address as one file (§5.1, *Channels to mechanisms*). The
Container Group ships it under `.claude/`, so that every agent-side path
sits in one directory; a project that wants it at the root moves it.
The Concept Deliverer's sits at the root.

### 2.4 How the Entry File is written

The file is paid for on every task, so the boundary is a test
applied to every line, not a list of sections. Three tests, the same
three the Entry File's guard comment states:

- **True of this project and nowhere else.** A line that would be
  true in another project is a convention, and lives there — once. If
  the rule sits in an Agent Skill or a Record Stub, it is not repeated here. If
  the convention's moment is every task, its Agent Rule loads with no
  `paths:` (§3.9, *An Agent Rule always loaded*): the convention's channel, not a line here.
  **It points; it never restates**: a summary is lossy on arrival,
  and then two files disagree while both look current
  (`docs/models/agent.md` §12.7, *Claims on summaries*, claim M1).
- **No moment.** A line with a moment goes where the moment is:
  - the record's Record Stub;
  - README;
  - an Agent Skill;
  - for a rule true only under one directory, an Agent Rule with a
    `paths:` list (§3.2, *`.claude/rules/`*).

  It is read there, at the moment it is about, instead of on every
  task it is not.
- **Nothing else would deliver it.** What stays is what no channel fires
  for: what the project is, where its records are, a stance, a fact
  whose failure is not noticing it. A
  rule that acts somewhere lives there; the Entry File says where.

What passes, in practice, is five kinds of content:

1. what the project is;
2. the records table;
3. build and test commands, where the project has them;
4. how to work here;
5. local rules that have no moment.

That is a description of what the tests leave, not a rule of its
own. A line that passes belongs whatever heading it sits under, and no
heading saves one that fails. The first two are present at birth. The
other three arrive when they become true, and take their headings
from the names below, *How to work here* and *Local rules*, so two
born repos spell them the same way.

*The records table* is the slot this convention provides and
`docs/conventions/project-recording/` fills: its rows, and the
requirement that every row names a moment, belong to that
convention (`docs/conventions/project-recording/` §13, *The records table*).

*How to work here* is the stance a project expects where it is not
the obvious one — "decide before building", "prefer exploring over
shipping". It is the one thing that is genuinely per-project and has
no other home: a convention cannot hold it, because a convention is
what is true across projects. It is also the easiest slot in which to
start restating the rules, so it takes stance and not rules.

*Local rules* pass one test before they enter: **a rule earns a
place in the Ambient Channel only when its failure is not noticing the
moment**. A test prerequisite, a migration rule or a service that
must be running fails this test: each has a moment, and goes where the moment is, as
the second test says. Most
facts that feel local have a moment, which is why this slot stays
short.

### 2.5 When the Entry File changes

Written at project start — a CBC Run's from the Container Group's, the
Concept Deliverer's from this page (ADR-0042). Revisited when a record
moves, a convention is adopted, or the build command changes, and at the re-reading its size asks for (§2.6, *The Entry File's size*), not otherwise.

### 2.6 The Entry File's size

The Entry File goes through the Ambient Channel (`docs/models/agent.md` §4.1, *Ambient Channel*).
It is paid on every task, including the tasks it is irrelevant to. Each
line added lowers compliance with every other
(`docs/models/agent.md` §12.1, *Claims on the Ambient Channel*, claim A2,
assumed). So its size is a running concern, not a one-time one.

The cost is what the tool delivers, not the file. HTML comments are
dropped on load (§5.3, *Memory files' comments*). So the guard comment,
the Entry File's comment that holds the three tests, and the records
comment cost nothing per task, and are read when the file is
opened to edit it, the moment they govern. If what remains is longer
than a screen, something in it belongs in a convention, a record or
an Agent Skill; shrinking it is maintenance, not tidying. The tool's
documentation sets a looser bound, under 200 lines; a screen is
ours.

Noticing that has no moment of its own, so a CBC Run re-reads the
file at its retrospective. The retrospective Agent Skill's close asks
it, and every line passes the three tests again or leaves. A CBC
Run's Decisions Log makes the same move for its entries.
The Concept Deliverer has no project end, and re-reads it at each Plan Step's close
instead, as a closing item of its Plan Step Gate (ADR-0057).

## 3. `.claude/`

### 3.1 `.claude/skills/`

Where a convention's Agent Skills live, one directory per Agent Skill: in a
CBC Run, a delivered copy, verbatim (the update is
`docs/conventions/exchange/`'s); at the Concept Deliverer, its own
derivation from the manual (ADR-0042). This convention owns the
place. A project may add an Agent Skill of its own, for a moment-bound
local rule the Entry File must not hold (§2, *The Entry File*). Work no Agent Skill covers
starts from an Approach on Trial (§3.8, *`.claude/approaches-on-trial/`*), and an Agent Skill is written only
when an evaluation places one (`docs/models/idea-to-output.md` §4.2,
*The upward direction*). How that is done is
`.claude/approaches-on-trial/approach-drafting.md`'s and its
evaluation's.
*Its story: ADR-0056; ADR-0058.*

### 3.2 `.claude/rules/`

Instruction files read like the Entry File, with one extra: a `paths:`
list at the top. When a file loads, and its limits, are this page's
(§5.6, *Rules files*). The
home for a rule true only in one part of the tree, which an Agent Skill would
carry only if the agent noticed the moment. Without the list, the file
is the Entry File by another name and fails the Entry File's tests the same way
(§2.4, *How the Entry File is written*), with one exception (§3.9, *An Agent Rule always loaded*).

### 3.3 `.claude/shapes/`

Where a project keeps its Output Shapes. What an Output Shape is, and why this is
a directory nothing loads, are `docs/conventions/shapes/`'s; this
convention places the directory and states nothing else about it.
A project with no Output Shape has none: it arrives with a group that
ships Output Shapes, or when the project writes its first.

### 3.4 `.claude/decisions.md`

The arrangement's Decisions Log: append-only and dated, each entry in
three parts: what changed, why, what was rejected. The standing rule
is a comment in the file it governs. The Decisions Log keeps the why
and the rejected options. Neither repeats the other. A CBC Run's also
holds what it was delivered: its birth entry lists the conventions
it holds, and each delivery entry the Delivery Pin and the Read-Through Commit
(`docs/conventions/exchange/` §2.2, *The CBC Run*). The Concept Deliverer's holds neither,
since it receives no delivery (ADR-0042). Its rules sit in its
header comment.

*Its story: devlog 2026-10-17, later; devlog 2026-10-29, the lessons' own stories: project-recording and agent-arrangement.*

### 3.5 `.claude/settings.json`

The tool's settings that are the project's: tracked, and the one
place the arrangement holds an Enforcement Gate as repo state. Not born with the
project: a project adds it when it has a rule that must not depend
on text — a permission rule that halts a command at a prompt the
human answers — or an exclude to declare. The commit stop is not
such a rule (`docs/conventions/commit-messages/` §2.4, *Commit on the word*). JSON carries no
comment, so the why lives in the Decisions Log, never in the file;
later inserts are merges, not text edits.

### 3.6 `.claude/settings.local.json`

The tool's machine-local state, never project truth; the Hygiene
Base ignores it (`docs/conventions/repo-hygiene/`).

### 3.7 `CLAUDE.local.md`

Not under `.claude/`, but the arrangement's neighbour: the operator's
standing instructions, loaded beside the Entry File and read the same
way (`docs/models/agent.md` §4.1, *Ambient Channel*, ownership). One person, one
checkout. The Hygiene Base ignores it. Its words never enter a record:
a record that quotes it has let one operator's preference into the
project's truth. The Container Group ships none, and a CBC Run's
stays ignored. The Concept Deliverer tracks its own: it has one operator,
and a setting kept out of git is one no reader of the repo can see
(ADR-0062). Outside practice ignores the file, as the tool's
documentation advises.

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


### 3.8 `.claude/approaches-on-trial/`

Where a project keeps its Approaches on Trial: one file per kind of
work, not yet proven. Nothing loads the directory. A Plan Step's opening
item sends the agent to it (the Plan Step Form). What an Approach on Trial
is lives above (`docs/models/idea-to-output.md` §2, *The kinds*);
how one is drafted and how one is evaluated are
`.claude/approaches-on-trial/approach-drafting.md`'s and
`.claude/approaches-on-trial/approach-evaluation.md`'s. This
convention places the directory and states nothing else about it.
In a CBC Run, an Approach on Trial the Concept Deliverer ships is a pinned copy
(`docs/conventions/exchange/` §3.2, *What goes*), and one the CBC Run drafts is its
own. *Its story: ADR-0058.*

### 3.9 An Agent Rule always loaded

A convention whose moment is every task ships its Agent Rule with no
`paths:`, so it loads in every session. Its moment is every answer
and every record written, and no path, Agent Skill or Record Stub fires at all
of them. Such an Agent Rule fails the Entry File's first test (§2.4, *How the Entry File is written*), since it is true in
any project. It passes as the convention's own channel: derived
from its manual, and naming the manual in `foundation`. That keeps it from restating the rules, which the anti-patterns warn of
(§4, *Arrangement anti-patterns*): one file per convention, never a
restatement. It is paid for in every session (§2.6, *The Entry File's size*), so two
qualify in a CBC Run and three here. *Its story: ADR-0053.*

## 4. Arrangement anti-patterns

- **Putting rules in the *How to work here* slot** — a rule that is true
  in another project is a convention written as a stance.
- **A local rule with a moment** — "run Docker before the tests" —
  paid for on every session and read at none of the moments it is
  about.
- **Shipping the *How to work here* and *Local rules* slots as empty
  sections** — a header waiting for content is cost with no guard in
  it; the shipped Entry File carries the test, and the header arrives with the first line that
  passes it.
- **Restating a convention's rules "so they are always in context"** —
  it grows once per convention and drifts from its manual.
- **A second Entry File kept beside the first for another tool**,
  unless that tool is actually in use.
- **Project truth in the arrangement** — local status, a decision
  about the system, a Plan Step. They belong in `PLAN.md`, `docs/adr/`,
  the records; the arrangement is what a portfolio copy drops.
- **Growth by accretion** — every line added dilutes every other line,
  so removing one is maintenance, not tidying.
- **Keeping a repeated rule in the operator's file** — a rule the
  human keeps saying is the Agent Model's Told Channel diagnostic
  (`docs/models/agent.md` §8, *Choosing a channel*): a convention
  is missing, or its channel is not firing. `CLAUDE.local.md` makes
  the saying persistent and the diagnosis invisible.

## 5. The Claude Code Tool Binding

The Agent Model names the channels and the Enforcement Gate
(`docs/models/agent.md` §4, *The channels*, §7, *The Enforcement Gate*); a Tool Binding names the mechanisms one
tool gives each (`docs/models/agent.md` §10, *The Tool Bindings*). This is Claude Code's,
the tool both Convention Seats use. It changes with the tool's releases, so
each fact says which release it was checked against, and a change
is made here alone. A second tool's Tool Binding would be written beside
this one, and writing it is the test for tool-shaped assumptions
hiding in the Agent Model. None has been needed.

### 5.1 Channels to mechanisms

Sketch, Claude Code — checked against 2.1.310 on 2026-10-24, by its
documentation, by what could be observed here, and by bug reports
(first checked against 2.1.284 on 2026-09-29):

| Channel (the Agent Model's Layer 1) | Claude Code mechanism |
|---|---|
| Ambient Channel | memory files — `CLAUDE.md` (root or under `.claude/`), `~/.claude/CLAUDE.md`, `@` imports; `AGENTS.md`, read when no `CLAUDE.md` is found; `.claude/rules/*.md` without a `paths:` list; `CLAUDE.local.md`, the operator's; the first 200 lines of auto memory's `MEMORY.md`; an Agent Skill's `name` and `description` |
| Pulled Channel | `Read`, `Grep`, `Glob`; an Agent Skill's body, once the agent invokes it |
| Pushed Channel | context-injecting hooks, slash commands, subagents; `.claude/rules/*.md` with a `paths:` list, and a `CLAUDE.md` in a subdirectory — loaded when the agent reads, writes or edits a matching file, or reads one from the shell with a command such as `cat`; not on a script's edit (§5.6, *Rules files*) |
| Told Channel | the prompt |
| Observed Channel | tool results |
| Installed Channel | files in the repo; the Container Group that puts them there at birth |
| Enforcement Gate | blocking hooks (`PreToolUse`), CI; permission rules in `settings.json` — `ask` stops at a prompt, `deny` refuses |

### 5.2 Hooks

Hooks appear twice: some inject context, the Pushed Channel; others
block, an Enforcement Gate. One mechanism, two roles: a Tool Binding
has to say which.

### 5.3 Memory files' comments

Memory files arrive without their HTML comments. The loader drops every
block-level `<!-- … -->` comment before the text enters context. One
inside a code block is kept. So a comment in an Entry File never goes
through the Ambient Channel. It reaches the agent only when the file
is opened with a tool, which for the Entry File is edit time.
Observed on 2.1.260 through 2.1.263, documented since, and observed
again on 2.1.284: this repo's `CLAUDE.md` holds two comment blocks,
and the text a session loads holds neither. The same loader honours
`claudeMdExcludes` in `settings.json`. It matches globs against the
absolute path. That is how a template Entry File kept inside a repo
stays out of its sessions.

### 5.4 Permission rules

A permission rule is an Enforcement Gate only in a mode that honours it. `deny`
refuses in every mode. `ask` still prompts in auto mode and in the
mode that bypasses permissions; the mode that never asks turns it
into a refusal. What no rule matches, auto mode has a classifier
decide in the background. The Enforcement Gate is the tool's, not the repo's.

A rule reaches only what the tool can name. A `Read` deny covers the
file tools and the shell commands the tool knows as file commands,
such as `cat`, `head` and `sed`. It does not cover `grep -r` across a
tree, or a script that opens files itself; the documentation sends
that to the sandbox.

### 5.5 Agent Skills

Agent Skills appear twice as well, and neither time in the Pushed
Channel. Claude Code loads an Agent Skill's `name` and `description`
at session start, and its body only when the agent invokes it: a
trigger in the Ambient Channel over a body in the Pulled Channel. The
agent still decides, and the Pushed Channel promises it does not
(`docs/models/agent.md` §4.3, *Pushed Channel*). An Agent Skill is
still the closest this tool gets to the Pushed Channel for a rule
about an action; a hook closes the remainder.

The tool ignores a frontmatter field it does not know, without an
error, in an Agent Skill as in an Agent Rule. Our Foundation Lines are
for a reader of the file, never for the tool. An Agent Skill may also
carry a `paths:` list; what it does to an Agent Skill this repo has
not checked.

### 5.6 Rules files

Without a `paths:` list, the file is read every session, through
the Ambient Channel, no different from `CLAUDE.md`. With it, the file
loads when the agent reads, writes or edits a file under one of
those paths, or reads one from the shell with a command such as
`cat` or `head`. The tool decides that, not the agent. That is the
Pushed Channel with no hook to write. A `CLAUDE.md` in a subdirectory loads the
same way.

Three limits:

- **It arrives after the first draft.** A new file's content is
  written in the call that loads the rule, so a record written from
  scratch gets the rule no earlier than a comment in a template would
  have given it.
- **A script's edit loads nothing,** and nor does listing the
  directory.
- **Its condition is a place, never an action** — "when work is under
  `generated/`", not "when committing" — so it does not replace an
  Agent Skill. An Agent Skill is the agent's judgment about an action; a rules
  file is the tool's check on a touched file.

What is documented and what is seen have differed. On 2.1.284 this
repo saw the Read tool alone load a rule; on 2.1.310 a `sed` read
loaded one, as the documentation now says. Bug reports, checked
2026-10-24, show `paths:` failing silently in some formats and surfaces
(Claude Code issues #17204, #33581, #87217). An Agent Rule that must arrive
does not rest on a path alone (`docs/models/agent.md` §7, *The Enforcement Gate*).

### 5.7 Compaction and subagents

- **Compaction** restores the root `CLAUDE.md`, the Agent Rules without
  `paths:` and auto memory from disk. An Agent Rule with `paths:` and a subdirectory's
  `CLAUDE.md` come back only when a matching file is touched again.
  An invoked Agent Skill's body comes back cut to 5,000 tokens.
- **A subagent** loads the `CLAUDE.md` files, the Agent Rules and
  `CLAUDE.local.md`, but not auto memory, and no Agent Skill body unless
  its definition names the Agent Skill. The built-in Explore and Plan
  agents skip `CLAUDE.md`. A fork inherits the whole conversation.

So what a delegated task must know goes in its prompt, the Told Channel
(`docs/models/agent.md` §4.4, *Told Channel*). An Explore or Plan agent gets none of
the Agent Rules loaded every session, only those whose `paths:` match the files it
touches.

## Why it arrives this way

Every rule here governs a file the Container Group ships and is a
comment in it. The Entry File's comments carry the rule that it
points and never restates, the guard comment and the size rule. The
Decisions Log's carry its own.
Acting on the file is the trigger (`docs/models/agent.md` §4.6, *Installed Channel*).

Not an Agent Skill, because the failure guarded against is a noticing
failure. Told "remember X", an agent writes X into the Entry File.
An Agent Skill would fire only if the agent recognised the moment,
and here it does not.
Not paid at the Ambient Channel's cost either: the comments are dropped on load
(§5.3, *Memory files' comments*), so they are read when the file is opened to edit it
and cost nothing on any other task. A long guard is free; a long
records table is not.

A rule for an arrangement file goes in that file's Record Stub comment,
not here and not in the Entry File's prose. A project meets this
convention only as its files at birth, which are its own from then
on (`docs/conventions/exchange/` §2.4, *The records' exception*).

## What this does not cover

- **The commit that touches these paths, and its scope** —
  `docs/conventions/commit-messages/`.
- **The records the Entry File's table lists, and when each is
  touched** — `docs/conventions/project-recording/` §13, *The records table*.
- **What an Output Shape is, and how one lives** —
  `docs/conventions/shapes/`.
- **How a copy under `.claude/` is updated, and what a CBC Run may do
  to it** — `docs/conventions/exchange/`.
- **What the Hygiene Base ignores** —
  `docs/conventions/repo-hygiene/`.

## Where to look

- The Entry File and the Decisions Log's Record Stub:
  `delivery/container/.claude/CLAUDE.md` and
  `delivery/container/.claude/decisions.md`.
- The Agent Model it explains against: `docs/models/agent.md`.
