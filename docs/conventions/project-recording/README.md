# Project recording

**How a project records its decisions, state, plans, history and
lessons: what each record is, why it exists, where it
lives, and how to write it.**

## What it is for

So that what a project decided, where it stands, what it tried and
what it learned can be read by someone who was not there — a
newcomer, future-you, or the deliverer, which reads a run through
its records and nothing else (`docs/conventions/exchange/` §6.1).
Adopted with the container (CBC ADR-0038, 1d for the README's
moment); no failure of the deliverer's is recorded before it. Lived
since: three runs kept their records under these stubs, and every
reading of run 3 has been a reading of its decisions log, its
backlog and its devlog — the need proved by being the only channel
there is.

## What this is made usable as

- **The record stubs, shipped**, in `delivery/container/`:
  `README.md`, `PLAN.md`, `TODO.md`, `CHANGELOG.md`,
  `ARCHITECTURE.md`, `docs/adr/0001-record-architecture-decisions.md`
  and `devlog/devlog.md`. Each carries its own rules as comments,
  met when the file is opened; each is the run's own from birth.
- **The records table in the entry file,
  `delivery/container/.claude/CLAUDE.md`** — this convention's one
  stake in a file `docs/conventions/agent-arrangement/` owns (§13):
  the rule that cannot live inside a record, when to open it.
- **`delivery/fills/cbc-run-pure-playbook.md` — the playbook's
  steps, filled into a run's `PLAN.md` at birth** (§9).
- **The deliverer's own records**, derived from this page as the
  stubs are, and never copied from them (CBC ADR-0042).

This page explains the records; the stubs state the rules. Nothing
here is loaded into an agent. What derives from this page is that
list. A change here walks it; a change forced in one of them is
checked back against this page.

## The seats

The same records in both seats, each derived from this page — the
run's through the stubs, the deliverer's directly — with four
differences of rule or ownership — so a section each
(`docs/conventions/conventions/` §3.4).

### The run's seat

A run keeps every record the stubs name, from birth. Its `PLAN.md`
steps arrive whole from a playbook it does not hold, filled in at
birth. Its retrospective runs at the project's end, and its
lessons reach the playbook when the deliverer reads the run. Its
`CHANGELOG.md` logs releases.

### The deliverer's seat

The deliverer keeps the same records, derived from this page rather
than from the stubs (CBC ADR-0042), and differs in four things. It
has no project end, so lessons fold back at each step's gate close
rather than at a retrospective, as its first devlog entry agreed on
2026-08-27. It owns the playbook,
`delivery/fills/cbc-run-pure-playbook.md`, where a run holds only
the steps filled into its plan (§9). Its `CHANGELOG.md` versions the
concept, not a release (CBC ADR-0003).

And its `PLAN.md` holds milestones only: things that become true
once and have a gate, like a birth or a release. Recurring work —
reading runs, delivering, keeping the conventions — is not a step;
TODO's Now holds it. A run's step names the skill that holds it, and
its gate is derived from that skill when the step opens; the
deliverer's milestones come from the situation, no skill holds them,
and their gates are written when they are named. A reached milestone
leaves the plan, and the devlog entry that closes it names the step.
A run keeps its finished steps whole, because they are the evidence
its playbook is folded from; no playbook is folded from the
deliverer's own plan, so its finished steps are only history, which
is the devlog's. For the same reasons its plan has no Retrospective,
whose two jobs — folding lessons back and re-reading the entry file
— close each milestone's gate instead; no "Discovered along the
way", since TODO takes a finding at once; and no decision index,
since `docs/adr/` lists itself (§3.3's index is the run's).

*Found 2026-09-29: from 2026-09-20, with Step 10 in progress, 203
commits, two of them touching `PLAN.md`; one step written after
its work was done; the decision index stale twice. The work had been led by TODO and the devlog's Resume all
along (CBC ADR-0041).*

## 1. The model at a glance

The **Plan** is the spine. Every other record either feeds it, hangs off one
of its steps, or is produced when a step closes. The **Playbook** sits outside
any single project: it hands the Plan its step sequence at birth and
absorbs its lessons at the end.

```
                    PLAYBOOK  (reusable, lives across projects)
                       │  steps at birth         ▲  fold lessons back
                       ▼                         │
   ┌────────────────  PLAN.md  (the spine) ──────┴─────────────┐
   │  Step 1 [x] ── Step 2 [~] ── Step 3 [ ] ── ... ── Retro   │
   └───┬──────────────┬────────────────┬────────────────┬──────┘
       │              │                │                │
   forced a       daily work      found new        step shipped
   decision       inside step     non-blocking     something
       │              │           work │               │
       ▼              ▼                ▼               ▼
     ADR           DEVLOG           TODO          CHANGELOG
  (why we        (what we        (what's not     (what changed,
   chose X)       tried, what     done yet)       for users)
                  failed)
       │
       └──► summarized into ARCHITECTURE.md (current state of the system)

   README.md = the front door: what this is, how to run it, where the
               other records are.
```

Reading order for a newcomer: README → ARCHITECTURE → PLAN → (ADRs as
needed). The devlog and TODO are working documents; nobody is expected to
read them cover to cover.

**Repository layout:**

```
repo/
├── README.md
├── .claude/
│   └── CLAUDE.md             (the entry file: agent-arrangement §2)
├── PLAN.md
├── CHANGELOG.md
├── TODO.md
├── ARCHITECTURE.md
├── docs/
│   ├── adr/
│   │   ├── 0001-record-architecture-decisions.md
│   │   └── 0002-....md
│   └── rfc/                  (only if the team uses design docs)
└── devlog/
    └── 2026-08.md            (one file per month, or devlog.md if small)
```

The playbook is absent on purpose: it lives in the repo that owns the
project type, never in a project born from it (§9).

Everything is Markdown, in the repo, versioned with git. That is itself a
rule of the convention: records live next to the code they describe, so
they branch, review, and roll back together with it.

## 2. PLAN.md — the spine

### 2.1 What

The gated step plan: the full journey sketched coarsely, the next
1–2 steps detailed finely (rolling wave), each step with exit
criteria (gates) and a live status.

### 2.2 Why

It answers "where are we, what's next, and what does *done* mean" at
any moment — the three questions that otherwise live only in
someone's head. Gates prevent steps from being declared finished by
fatigue. The completed plan is also the raw material for the
retrospective and the playbook.

### 2.3 Where

Repo root, `PLAN.md`. One per project.

### 2.4 How

- Statuses: `[ ]` planned, `[~]` in progress, `[x]` done (+date), `[!]`
  blocked (+what unblocks it), `[-]` skipped (+why).
- A gate is a checklist of verifiable facts, not intentions: "tests pass on
  a clean clone," not "code is good."
- When a step closes, add a one-line note of what actually happened,
  especially if it diverged from the estimate — this is retro fuel.
- Steps link outward: "Decisions: ADR-nnnn," "see devlog 2026-08-14."
- Ends with a "Discovered along the way" holding pen and a Retrospective
  section (see Playbook, §9).

### 2.5 When

Created at project start; its steps arrive whole from a playbook at
birth and are confirmed at Framing — the middles written fresh there
when the project was born without one (§9); touched every working
session — updating it *is* part of the work, not paperwork after it.

### 2.6 Anti-patterns

Steps without gates (it's just a wish list); detailing step 9 before
step 2 is done; letting statuses go stale so the plan lies.

---

## 3. ADR — Architecture Decision Records

### 3.1 What

One short document per significant decision: the context that forced
it, options considered, the decision, and its consequences —
including the downsides knowingly accepted.

### 3.2 Why

Code shows *what* was built; ADRs preserve *why*. Six months later,
"why is this Postgres and not Mongo" has an answer, and — equally
important — "we already considered that and rejected it because…"
stops the same debate from recurring.

### 3.3 Where

`docs/adr/NNNN-short-title.md`, numbered sequentially, never
renumbered. Indexed with one line each in PLAN.md's Decision index.

### 3.4 How

The Nygard template:

```markdown
# 0004. Use PostgreSQL for primary storage
Date: 2026-08-15
Status: Accepted        <!-- Proposed | Accepted | Deprecated | Superseded by 0009 -->

## Context
What situation forces a decision. Facts and constraints, not opinions.

## Options considered
1. PostgreSQL — mature, relational fits our invariants; ops burden.
2. MongoDB — flexible schema; weak fit for our transactional needs.

## Decision
We will use PostgreSQL.

## Consequences
Good: transactions, constraints enforce invariants at the DB level.
Bad: schema migrations become a discipline we must maintain.
```

- **Immutable.** Changed your mind? Write a new ADR marked "Supersedes
  0004," set the old one's status to "Superseded by 00NN." History of why
  is the whole point.
- Threshold for "significant": would a future developer ask "why on earth
  is it done this way?" If yes, ADR. Choice of variable names: no. Choice
  of database, framework, sync-vs-async, build-vs-buy: yes.
- Keep it under a page. An ADR you won't write because it's heavy is worse
  than a terse one.

### 3.5 A number is local to one repo

A bare `ADR-nnnn` names the decision in the repo where it is read. A
reference to another repo's decision carries that repo's tag before
the number — `CBC ADR-0012`, as a run cites the deliverer's — a
short upper-case name each repo declares once in its README's
decisions row (§7). A document written to be read in another repo
carries the tag on every citation (CBC ADR-0020).

### 3.6 When

At the moment the decision is made — typically when a gate in the
plan forces it. Writing it *before* deciding (status: Proposed) is
even better; the writing often changes the decision.

### 3.7 Anti-patterns

Editing old ADRs; ADRs so long nobody writes them; recording the
decision but not the rejected options (the rejections are half the
value).

---

## 4. Devlog — the engineering journal

### 4.1 What

Dated, informal entries: what was worked on, what was tried, what
failed and why, open questions, hunches. The lab notebook of the
project.

### 4.2 Why

Three payoffs: (1) dead ends are recorded, so they aren't
re-explored — "tried caching at the repo layer, caused stale reads"
saves the next attempt; (2) resuming after a break takes minutes
instead of an hour of re-reading code; (3) it is the raw material
that gets distilled upward — a devlog struggle becomes an ADR's
context, a retro lesson, a playbook warning.

### 4.3 Where

`devlog/2026-08.md` (file per month) or a single `devlog.md` for
small projects. Newest entries on top.

### 4.4 How

```markdown
## 2026-08-21  (Step 2: data model)
- Migrations up/down now clean. Down-migration for soft deletes was the
  hard part; note in ADR-0004 consequences.
- DEAD END: tried enforcing the "one active order per user" invariant in
  application code — race condition under two concurrent requests.
  Moving it to a partial unique index instead.
- Open: do we need audit history on orders now or can it wait to Step 5?
- Resume: finish CRUD tests, close Step 2 gate.
```

- Written for future-you, not an audience: fragments fine, spelling
  irrelevant, honesty mandatory. "I don't understand why this works" is a
  legitimate and valuable entry.
- Tag entries with the current plan step; mark dead ends loudly
  (`DEAD END:`) so they're greppable.
- End sessions with a "Resume:" line — the cheapest save-point that
  exists. It marks a place in the work, not a time: sessions resume
  after walks, days or weeks.

### 4.5 When

Every working session, 2–5 minutes, ideally as you go or at session
end. Never retroactively "cleaned up."

### 4.6 Anti-patterns

Polishing it (kills the habit); recording only successes (the
failures are the valuable part); letting it replace ADRs (decisions
must still be promoted to their durable form).

---

## 5. TODO / backlog

### 5.1 What

Everything known but not done: upcoming work not yet in a plan step,
bugs, ideas, and consciously deferred problems.

### 5.2 Why

An open loop held in the head costs attention; written down and
triaged, it costs nothing until its time comes. It also makes
deferral *explicit* — "we know about this and chose not yet" is a
decision, and this is where it's recorded.

### 5.3 Where

`TODO.md` in the repo root for small/solo projects; an issue tracker
(GitHub Issues, Linear, Jira) when there's a team — same structure,
different tool. Inline `TODO:`/`FIXME:` code comments are allowed
only with an issue/TODO reference attached, otherwise they rot.

### 5.4 How

```markdown
# TODO

## Now (this plan step)
- [ ] Add CRUD tests for the Order entity (08-18, the plan).
      Context: Step 2's gate names them; none exist yet.
      Trigger: Step 2's close.

## Next (upcoming steps — assign to a step when triaged)
- [ ] Rate-limit the public endpoints (08-19, load test).
      Context: one client held the pool for 40 s at 200 rps.
      Trigger: Step 3 opens.
      See: devlog 08-19.

## Later / someday
- [ ] Consider an admin dashboard (08-20, the owner).
      Context: no committed step wants it; support reads the DB.
      Ideas: a read-only view over the orders table first.
      Trigger: a second support person.

## Known issues (deferred deliberately)
- Slow query on /orders list past 10k rows. Accepted for now: real data
  won't hit that before Step 6. Revisit at Step 6 gate.
```

- Three-horizon structure (now / next / later) plus known-issues. "Now"
  should mirror the current plan step's remaining work.
- Each "Discovered along the way" item in PLAN.md gets triaged here:
  assigned to a step, parked in later, or deleted.
- Prune ruthlessly. A 200-item "later" list is a graveyard, not a plan;
  deleting an idea you'd re-derive anyway if it mattered costs nothing.
- Open work only. A closed item goes: what closed is the devlog's,
  the ADRs' and git's to tell, and a closed entry kept here is a
  second copy of it.
- One shape per item: what to do or decide, with the date and who
  raised it; a **Context** of at most eight lines, saying why it
  holds today; **Ideas**, optional; a **Trigger**, the moment it is
  due; and **See**, the devlog entry, ADR or commit that tells its
  story. The context is there so triage reads an item without
  opening its pointer; the story is not, because the devlog already
  holds it.
- Ideas are how the item might be handled, noted when they come, a
  line each and none weighed. Weighing is the work's: when the item
  is due, each idea is taken, extended or declined, and the verdict
  is recorded with the work. An idea parked here is not lost to the
  session that had it, and not mistaken for a decision.
- The story is written where it happens. When something is noticed,
  that session's devlog entry says so and the item points at it.
  An item that is its story's only home keeps the story and has no
  See.
- An item that changes is rewritten true for today. A dated update
  stacked on it is history, and history is the devlog's.

*Found 2026-09-29: the deliverer's TODO kept closed entries whole
and stacked dated updates on open ones — 2,120 lines, half of them
finished work, one item at 248. Run 3's, read the same day, stacks
its answers the same way, its longest items at 38 and 36 lines.
The deliverer's was pruned and reshaped to this form, and the cap
found on it: three lines cut meaning and lost a fact (CBC
ADR-0040).*

### 5.5 When

Item added the moment it's discovered (so it stops occupying your
head); triaged when closing a step (§11, rule 3: moments, not
schedules).

### 5.6 Anti-patterns

Using it as the plan (it has no gates or sequence); never deleting;
closed entries kept whole; dated updates stacked on an open item;
inline code TODOs with no tracked counterpart.

---

## 6. CHANGELOG.md

### 6.1 What

Human-written record of notable changes per released version,
addressed to *users* of the project (which may be your future self
or another team), not its developers.

### 6.2 Why

"What changed between 1.3 and 1.5, and will it break me?" must be
answerable without reading commit history. Commits are too granular
and developer-voiced; the changelog is the curated, user-voiced
digest.

### 6.3 Where

`CHANGELOG.md` in the repo root. Format: Keep a Changelog
(keepachangelog.com) with Semantic Versioning. What a version *is*
depends on the repo type — an application releases SemVer versions;
a concept or docs repo versions something else, and says what at
Framing. The discipline (curated, user-voiced, written per change)
carries unchanged.

### 6.4 How

```markdown
# Changelog

## [Unreleased]
### Added
- Order soft-deletion with 30-day recovery.

## [1.2.0] - 2026-08-20
### Added
- Login/logout with token expiry.
### Fixed
- Duplicate order creation under concurrent requests.
### Security
- Tokens no longer logged on auth failure.
```

- Categories: Added, Changed, Deprecated, Removed, Fixed, Security.
- The `[Unreleased]` section accumulates during work; releasing = renaming
  it to a version + date and opening a fresh Unreleased. Entries are
  written *when the change is made*, not reconstructed at release time.
- Breaking changes get called out explicitly and drive the major version.

### 6.5 When

A line whenever a user-visible change merges — natural moment is
when a plan step's gate closes.

### 6.6 Anti-patterns

Dumping git log into it; writing it from memory at release time;
developer-speak ("refactored OrderService") instead of user-speak
("order creation is ~3x faster").

---

## 7. README.md — the front door

### 7.1 What

What this project is, who it's for, how to run it, and where
everything else is.

### 7.2 Why

It's the entry point for every newcomer including future-you. Its
quality determines whether the rest of the record system gets found
at all.

### 7.3 Where

Repo root, mandatory.

### 7.4 How

Minimum sections, true for every project type: one-paragraph
purpose; a "Project records" section linking PLAN, ARCHITECTURE,
ADRs, CHANGELOG — the decisions row also declares the repo's tag,
the name its decisions are cited by from another repo (§3.5). A
project that runs adds: prerequisites; the *one command* to
build/run from a clean clone; how to run tests — each arriving at
the moment it becomes true (see When), not at birth. Keep it short
and current — a wrong README is worse than a sparse one, so anything
that changes often (detailed status) belongs in PLAN.md and is only
*linked* from here.

### 7.5 When

Stubbed at project start; thereafter, when something became true
that the outside should see — projection follows truth, so the
README never claims what is not yet true (CBC ADR-0038, 1d). The
mechanism is a gate item where relevant: a step whose gate makes
something projectable true includes updating its projection, exactly
as record upkeep is already expressed in lived gates ("ARCHITECTURE
current"). Never a standing item on every gate — most steps make
nothing projectable true, and a usually-vacuous item trains
rubber-stamping. The Release gate includes "README verified on a
clean machine."

### 7.6 Anti-patterns

Duplicating live status into it; setup instructions that only work
on the author's machine.

README is the front door for people; the entry file is the one for
agents, `docs/conventions/agent-arrangement/` §2. Two audiences, two
files, no shared text.

---

## 8. ARCHITECTURE.md — the map of current state

### 8.1 What

A short prose description of the system as it *is now*: the main
components, their responsibilities, how they talk to each other,
where the important invariants live, and where in the codebase each
piece is found.

### 8.2 Why

ADRs are a history of individual choices; this is the synthesized
present. It's the difference between a stack of route decisions and
a map. Newcomers read it second, right after the README. (Convention
popularized by matklad's "ARCHITECTURE.md" essay.)

### 8.3 Where

`ARCHITECTURE.md` in the repo root (or `docs/`).

### 8.4 How

One or two pages: a component diagram (ASCII is fine), a paragraph
per component ("the `orders` module owns all order state
transitions; nothing else writes to the orders table"), the system's
key invariants, and a "where to find things" codemap. Link ADRs for
the *why* behind each shape. Update it when structure changes —
practical trigger: whenever a step gate closes and the diagram it
implies no longer matches reality.

### 8.5 Anti-patterns

Describing the aspirational design instead of the real one; so much
detail it goes stale in a week — it maps the forest, the code is the
trees.

---

## 9. Playbook — the cross-project script

### 9.1 What

The reusable, versioned template distilled from completed plans of
the same project type: the full step sequence, gates, and
accumulated "warnings from past runs."

### 9.2 Why

It converts one project's experience into the next project's head
start. The first plan of a familiar project type writes itself, and
past mistakes are pre-loaded as warnings at exactly the step where
they bit.

### 9.3 Where

In the repo that owns the type — the one a project's "Steps from"
line names — and never in the project born from it, which holds only
the copy in its plan. Here,
`delivery/fills/cbc-run-pure-playbook.md`. Versioned (v1, v2, …)
with a note of which project last updated it.

### 9.4 How

The full sequence, first step to last. The plan's stub prescribes no
step; a playbook prescribes them all. Each step keeps the plan's
form — a goal, a gate of verifiable facts, the records expected —
plus its own "Warnings from past runs"; its Release step carries the
type's own release facts. The lifecycle:

1. **Birth:** whoever births the project copies the chosen playbook
   whole into PLAN.md; the plan's "Steps from" line records which
   and at what version. Born without one, the stub's placeholders
   are filled in place.
2. **Framing:** confirm the steps against the framed problem — fill
   specifics, delete what this project has no use for, add what it
   needs, renumber; author the steps if the project was born
   without one.
3. **Project end:** run the retrospective in PLAN.md — estimate vs
   reality per step, wrong ordering, dead ends, missing steps, useless
   gates.
4. **Fold back:** each surviving lesson becomes a changed gate, a new
   step, or a warning line in the playbook where it lives — the plan's
   "Steps from" line names it; bump its version there. Framing
   and Release lessons fold into the playbook's own copies of those
   steps — they have a home now.

### 9.5 When

Created after the *second* project of a type (the first time you
notice "I've done this before"); updated at every retro thereafter.

### 9.6 Anti-patterns

Writing a playbook from theory before doing the project type even
once; never folding retros back (a playbook that stops learning is
just bureaucracy); gates so heavy people route around the playbook.

---

## 10. Supporting records (use when scale demands)

### 10.1 Design docs / RFCs

For decisions too large for an ADR — a multi-page proposal written
*before* building, circulated for comment, kept in `docs/rfc/`. The
ADR that follows records the outcome; the RFC records the full
exploration. Solo projects rarely need them; teams making
cross-cutting changes do.

### 10.2 Commit messages

The finest-grained decision trail —
`docs/conventions/commit-messages/` §1.

### 10.3 PR descriptions

Where a change's reasoning and its review discussion live. Link the
plan step and any ADR; the review thread often contains the "options
considered" that should be promoted into the ADR.

### 10.4 Runbooks

Operational procedures for a *running* system ("how to restore the
DB from backup," "release checklist"). Same checklist spirit as
playbooks, but for operating, not building. `docs/runbooks/`.

---

## 11. How information flows between records

Records form a distillation pipeline — raw experience at the bottom,
durable knowledge at the top:

```
devlog (raw, daily)
  → ADR          when a struggle crystallizes into a decision
  → TODO         when it surfaces future work
  → PLAN notes   when it explains why a step diverged
       → CHANGELOG      when the step ships something user-visible
       → ARCHITECTURE   when the step changed the system's shape
       → RETROSPECTIVE  when the project ends
            → PLAYBOOK  lessons made reusable
                 → next project's PLAN
```

The rules that make the pipeline work:

1. **Write once, at the source.** Each fact has one home; other records
   *link* to it, never copy it. Duplicated facts diverge, and diverged
   records stop being trusted.
2. **Promote, don't rely on memory.** A dead end noted in the devlog is
   safe; one merely remembered will be repeated. Same for decisions
   (→ADR) and lessons (→playbook).
3. **Update at natural moments, not on a schedule.** Bound to events,
   recording never becomes a separate chore to skip. *Which* moment
   belongs to which record is stated once, in the entry file's records
   table (§13): that is where an agent meets it, and a second list here
   would be a copy that drifts.
4. **Cheap at the bottom, durable at the top.** The devlog may be messy;
   ADRs and the playbook must be clean. Effort belongs where the record
   will be re-read.

## 12. Minimum viable set

Not every project needs all of it. Scale by stakes:

- **Throwaway / experiment:** devlog only (even that pays off).
- **Solo, real project:** README, PLAN, TODO, devlog, ADRs when a real
  decision happens.
- **Anything with users or teammates:** add CHANGELOG and ARCHITECTURE.
- **Second project of the same type:** add the playbook.

The test for adding any record is always the same: *will someone —
probably future-you — need this answer and be unable to reconstruct it?*
If yes, it gets written down, once, in its designated home.

---

## 13. The records table in the entry file

*Numbered by creation, not reading order: §11, §12 and §13 are
cited by number from other conventions, and renumbering would break
them for a cosmetic gain.*

The entry file — the one file loaded before any task, what it may
hold, how it stays small — is
`docs/conventions/agent-arrangement/` §2. This convention keeps one
stake in it: the records table, the only ambient part of
project-recording (*Why it arrives this way*).

**Every row of the records table names three things: the moment, what
the record holds, and its path** — and adding a record means adding
its row. This is a requirement, not a convenience.

The moment is the half that is new and the half that is load-bearing.
The table is then readable in both directions: *I just did X, where
does it go?* reads down the first column, *where is Y recorded?* reads
down the second. Both are real questions and a table answering only
one of them is half a table. A rule written only inside the record it
governs teaches the format but cannot teach the timing: "write a
devlog entry at session end" sits in `devlog.md`, and opening
`devlog.md` at session end is the thing you needed telling. A
moment is not a restatement — it says when to go, and
contains nothing about what to write.

**Anti-pattern.** Local status in the entry file — where the work
stands, what is next. It belongs in PLAN.md; the table's row for
PLAN.md is where the entry file says so.

## Why it arrives this way

A rule for filling in `PLAN.md` sits inside `PLAN.md`, so acting on
the record is what puts the rule in front of you; there is no
trigger to fire and nothing to remember. Timing is the
one exception: a rule saying when to open a record cannot live
inside it, so the entry file's records table carries a moment per
row (§13). A skill would not do: it fires when the agent
recognises the moment, and failing to recognise the moment is the
failure being fixed. Restating a record's rules in the entry file
"so they are always available" is the failure
`docs/conventions/agent-arrangement/` measured.

## What this does not cover

- **The entry file as a whole: what it may hold, and how it stays
  small** — `docs/conventions/agent-arrangement/` §2.
- **How a commit is written, and why its body is a micro-ADR** —
  `docs/conventions/commit-messages/`.
- **How work larger than one commit is sequenced** —
  `docs/conventions/commit-plan/`.
- **Why the records are never re-delivered to a run** —
  `docs/conventions/exchange/` §2.4.
- **What the deliverer's CHANGELOG versions** — the concept, CBC
  ADR-0003 and `docs/master.md` §1.1.

## Where to look

- The stubs: `delivery/container/`.
- The entry file and its records table:
  `docs/conventions/agent-arrangement/`.
- Commit messages, the finest-grained record:
  `docs/conventions/commit-messages/`.
