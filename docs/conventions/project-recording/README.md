# Project recording

**How a project records its decisions, state, plans, history and
lessons: what each record is, why it exists, where it
lives, and how to write it.**

## What it is for

So that what a project decided, where it stands, what it tried and
what it learned can be read by someone who was not there: a
newcomer, future-you, or the Concept Deliverer, which reads a CBC Run through
its records and nothing else (`docs/conventions/exchange/` §6.1, *Reading a CBC Run*).
Adopted with the Container Group from the handbook, the repo this
arrangement came from, now history (ADR-0038; its decision 1d sets
when the README changes). No failure of the Concept Deliverer's is recorded before it. Lived
since: by 2026-10-20, four CBC Runs had kept their records under these Record Stubs. Every
CBC Run Reading of CBC Run 3 has been a reading of its Decisions Log, its
backlog and its devlog. The records proved the need by being the only
channel there is.

## What this is made usable as

- **The Record Stubs, shipped**: `delivery/container/README.md`,
  `delivery/container/PLAN.md`, `delivery/container/TODO.md`,
  `delivery/container/CHANGELOG.md`,
  `delivery/container/ARCHITECTURE.md`,
  `delivery/container/docs/adr/0001-record-architecture-decisions.md`
  and `delivery/container/devlog/devlog.md`. Each carries its own
  rules as comments, met when the file is opened; each is the CBC Run's
  own from birth.
- **The records table in the Entry File,
  `delivery/container/.claude/CLAUDE.md`, and ours, in `CLAUDE.md`**
  — the one part of the Entry File this convention owns (§13, *The records table*).
  The file is the agent-arrangement manual's. The table holds the one
  rule a record cannot hold: when to open it.
- **`delivery/fills/cbc-run-pure-playbook.md` — the playbook's
  Plan Steps, put into a CBC Run's `PLAN.md` at birth by a Delivery
  Fill** (§9, *The playbook*).
- **The Concept Deliverer's own records**: `README.md`, `PLAN.md`,
  `TODO.md`, `CHANGELOG.md`, `ARCHITECTURE.md`, `docs/adr/` and
  `devlog/`, derived from this page as the Record Stubs are, and never
  copied from them (ADR-0042); and `TODO-CONVERSATION-MEMORY.md`,
  on trial, which has no Record Stub (§14, *Conversation Memory*, ADR-0060).

This page explains the records; the Record Stubs state the rules. What
derives from this page is that
list. A change here runs the Change Walk on it; a change forced in one of them is
checked back against this page.

## The seats

Both Convention Seats keep the same records, each derived from this
page: the CBC Run's through the Record Stubs, the Concept Deliverer's
directly. They differ in seven things of rule or ownership, so each
has a section (`docs/conventions/conventions/` §2.4, *The seats*).

### The CBC Run's seat

A CBC Run keeps every record the Record Stubs name, from birth. Its `PLAN.md`'s
Plan Steps arrive whole from a playbook it does not hold, filled in at
birth. Its retrospective runs before its Release Plan Step
(`docs/conventions/retrospective/`), and its lessons reach the
playbook when the Concept Deliverer reads the CBC Run. Its
`CHANGELOG.md` logs releases.

### The Concept Deliverer's seat

The Concept Deliverer keeps the same records, derived from this page rather
than from the Record Stubs (ADR-0042). It differs in seven things:

1. **No project end.** Lessons are written back at each Plan Step's
   close, rather than at a retrospective. Whether a retrospective serves it too is on trial, at the moment
   TODO's item "Run this repo's retrospective, on trial" names
   (`docs/conventions/retrospective/`, *The seats*).
2. **The playbook.** It owns
   `delivery/fills/cbc-run-pure-playbook.md`, where a CBC Run holds
   only the Plan Steps filled into its plan (§9, *The playbook*).
3. **`CHANGELOG.md`.** It versions the concept, not a release
   (ADR-0003).
4. **`PLAN.md`.** It holds one Plan Step being worked: the piece of
   work being done now, and beside it any Plan Step stopped for it.
   What makes work a Plan Step, and the Plan Step Form, are under
   `## The Plan Step Form` at the top of the Concept Deliverer's own
   `PLAN.md` (ADR-0057). The form is the CBC Run's, adapted to this
   Convention Seat. A CBC Run keeps its finished Plan Steps in its
   plan, each closed to one line: they are the evidence its playbook
   is written from. No playbook is written from the Concept
   Deliverer's plan. Its finished Plan Steps are history, and history
   is the devlog's. Its plan has no "Discovered along the way", since
   TODO takes a finding at once. It has no Decision index, since
   `docs/adr/` lists itself. The index in §3.3, *Where ADRs live*, is
   the CBC Run's.
5. **`ARCHITECTURE.md`.** It describes documents and delivery rather
   than a built system, where a CBC Run's describes modules, runtime
   invariants and a `src/` codemap. It aims at about two pages, as §8 asks (§8, *ARCHITECTURE.md*; ADR-0068). Its parts,
   each with what it holds and who reads it:

   - ***Overview*** — the repo in one view, for a newcomer after the
     README;
   - ***What is stated here*** — each Canonical Description beside
     what is made from it, the Idea Models, and the delivery by group,
     for whoever changes a Canonical Description and needs what is
     made from it;
   - ***The delivery and the CBC Runs*** — the table of CBC Runs, each
     by both its names, for the agent writing a Delivery Note
     (`docs/conventions/exchange/` §3.7, *The Delivery Note*);
   - ***What must stay true*** — each rule, where it is stated and
     what holds it, for the reviewer at commit review;
   - ***Codemap*** — where each thing lives, for anyone looking.

   A part no one reads goes. Its words are a record of their own,
   `docs/glossary.md`, as a CBC Run's are. A line known wrong is a
   known issue in `TODO.md` (§5, *TODO.md*).
6. **The ADRs' length.** They have no page limit. A CBC Run's ADR
   records one choice in its code. The Concept Deliverer's record the
   design of a method and its conventions: on 2026-11-01, at 78 ADRs,
   up to 12 numbered decisions each, a median of 4.5, and a median of
   102 lines. Their
   length is governed by "cut what adds nothing"
   (`docs/conventions/writing/` §2, *Why each rule*, rule 7).
7. **Conversation Memory.** It keeps the talk behind a TODO item
   beside the item, in `TODO-CONVERSATION-MEMORY.md`, on trial (§14,
   *Conversation Memory*; ADR-0060). A CBC Run gets it only if its
   trial here keeps it.

*Its story: ADR-0041; ADR-0057.*

## 1. The records at a glance

A summary of which record answers what, in both Convention Seats (ADR-0067).
Each item's home holds the record's full what and why. Where the
Convention Seats keep a record differently, *The seats* says how.

**Both Convention Seats**

1. `README.md`: what this is, how to use it, where the rest is (§7, *README.md*).
2. `PLAN.md`: where the work stands, what is next, what *done*
   means (§2, *PLAN.md*). The Convention Seats differ.
3. `TODO.md`: what is known and not yet done (§5, *TODO.md*).
4. `docs/adr/`: why it is built this way (§3, *The ADRs*). The Convention Seats differ.
5. `devlog/`: what happened, the dead ends, where to resume (§4, *The devlog*).
6. `ARCHITECTURE.md`: what stands now, and how its parts tie (§8, *ARCHITECTURE.md*).
   The Convention Seats differ.
7. `CHANGELOG.md`: what changed in each version, for whoever pins
   it (§6, *CHANGELOG.md*). The Convention Seats differ.
8. `.claude/decisions.md`: how the agent's setup was decided
   (`docs/conventions/agent-arrangement/` §3.4, *`.claude/decisions.md`*).
9. `COMMIT-PLAN.md`: the commits of a Change Set in flight, when
   present (`docs/conventions/commit-plan/` §1, *What a commit plan is*).
   Listed for its moment; it is the agent's file, committed with the
   arrangement, not a project record (`docs/conventions/commit-plan/`
   §2.1, *Not a record*).
10. `docs/glossary.md`: the Glossary Names, and what each means
    (`docs/conventions/writing/` §2, *Why each rule*, rule 9).

**The CBC Run's only**

11. `docs/system/`: what is promised, what must never happen, the
    Invariant Slices (`concept/03-cbc-framing.md`).
12. `RETRO.md`: what the next CBC Run does differently, when present
    (`docs/conventions/retrospective/` §4, *`RETRO.md`*). Ours has none
    (*The Concept Deliverer's seat*, item 1).

**Ours only**

13. `TODO-CONVERSATION-MEMORY.md`: the talk behind a TODO item, on
    trial (§14, *Conversation Memory*).

Each Convention Seat has a picture of how the records feed each
other. An arrow says what a record holds for the plan. When a record
is opened is in each Convention Seat's records table (§13, *The records table*).

*The CBC Run's seat:*

```
                    PLAYBOOK  (the Concept Deliverer's; a CBC Run holds none)
                       │  Plan Steps, at birth    ▲  lessons written back,
                       ▼                          │  through RETRO.md
   ┌────────────────  PLAN.md  ───────────────────┴────────────┐
   │  Step 0 [x] ── Step 1 [~] ── Step 2 [ ] ── ... ── Retro   │
   └───┬──────────────┬────────────────┬────────────────┬──────┘
       │              │                │                │
      why       what happened     not yet done     what changed
       │              │                │                │
       ▼              ▼                ▼                ▼
      ADR          DEVLOG             TODO          CHANGELOG
       │                                           (for users)
       └──► summed into ARCHITECTURE.md (the system as it stands)

   docs/system/ = what is promised, the Invariant Slices
   README.md    = the first page: what this is, where the rest is
```

*Our seat:*

```
   ┌───────────────────────  PLAN.md  ───────────────────────┐
   │  the one Plan Step being worked, and any it stopped     │
   └───┬──────────────┬────────────────┬────────────┬────────┘
       │              │                │            │
      why       what happened     not yet done  what changed
       │              │                │            │
       ▼              ▼                ▼            ▼
      ADR          DEVLOG             TODO      CHANGELOG
       │                               ┊      (the concept's versions)
       │              TODO-CONVERSATION-MEMORY.md (the talk behind an item)
       └──► summed into ARCHITECTURE.md (documents and delivery)

   Lessons are written back at each Plan Step's close: into the conventions,
   the playbook, the concept.
   README.md = the first page: what this is, where the rest is
```

The Entry File is the agent-arrangement manual's
(`docs/conventions/agent-arrangement/` §2, *The Entry File*). The
playbook is absent from a CBC Run on purpose: it lives in the repo that
owns the project type, never in a project born from it (§9, *The playbook*).

## 2. PLAN.md

The record the others point back to.

### 2.1 What a plan is

A plan is its Plan Steps. The whole of the work is sketched
coarsely, and the next 1–2 Plan Steps are detailed finely. The detail
moves forward as Plan Steps close. Each Plan Step has a Plan Step
Gate, its exit criteria, and a live status.

### 2.2 Why a plan

It answers "where are we, what's next, and what does *done* mean" at
any moment. Without it, those three questions live only in someone's
head. Plan Step Gates prevent Plan Steps from being declared finished by
fatigue. The completed plan is also what the retrospective and the
playbook are written from.

### 2.3 Where a plan lives

Repo root, `PLAN.md`. One per project.

### 2.4 How a plan is written

How a Plan Step is written, closed and stopped is the plan's form. In
a CBC Run, the form is the Record Stub's legend, and the Plan Step
Form copied from the playbook at birth,
`delivery/fills/cbc-run-pure-playbook.md` (§9, *The playbook*). In the
Concept Deliverer's Convention Seat, it is `PLAN.md`'s legend and its
Plan Step Form. Why the form is as it is:

- A Plan Step Gate holds facts, not intentions: "tests pass on a clean clone",
  not "code is good". A Plan Step is then not declared finished by
  fatigue.
- A closed Plan Step's line says what diverged from the plan: that is
  what the retrospective reads.
- A Plan Step links outward to its decisions and its devlog, so the plan
  stays the record the others point back to (§1, *The records at a glance*).
- A Plan Step that stops is not done and not dropped: it keeps its place
  and the work it did, and resumes where it stopped.
- "Discovered along the way" holds what a Plan Step finds and does not
  do. In a CBC Run, the look back is not the plan's: it is `RETRO.md`'s, under the
  retrospective manual (`docs/conventions/retrospective/`).

### 2.5 When a plan changes

Its moments are the records table's (§13, *The records table*). Its Plan Steps arrive from a
playbook at birth (§9, *The playbook*), and updating it *is* part of the work, not
paperwork after it.

### 2.6 A plan's anti-patterns

- Plan Steps without Plan Step Gates: it's just a wish list.
- Detailing Step 9 before Step 2 is done.
- Letting statuses go stale, so the plan lies.

---

## 3. The ADRs

The architecture decision records.

### 3.1 What an ADR is

One short document per significant decision: the context that forced
it, options considered, the decision, and its consequences. The
consequences include the downsides knowingly accepted.

### 3.2 Why an ADR

Code shows *what* was built; ADRs preserve *why*. Six months later,
"why is this Postgres and not Mongo" has an answer. And "we already
considered that and rejected it because…" stops the same debate from
recurring.

### 3.3 Where ADRs live

`docs/adr/NNNN-short-title.md`, numbered sequentially, never
renumbered. In a CBC Run, indexed with one line each in `PLAN.md`'s
Decision index.

### 3.4 How an ADR is written

How an ADR is written is its form. In a CBC Run, the form is the
Record Stub `docs/adr/0001-record-architecture-decisions.md`, copied
for each new one. In the Concept Deliverer's Convention Seat, it is
the header of `docs/adr/README.md`. Why the form is as it is:

- Context, options, decision, consequences: the options rejected
  are kept, so "we already considered that" ends a debate.
- Immutable: the history of why is the whole point, so a changed
  mind is a new ADR, never an edit.
- The threshold is a question a future reader would ask, not a
  size: a variable's name, no; a database, a framework, sync or
  async, build or buy, yes.
- Under a page, in a CBC Run: an ADR you won't write because it's heavy
  is worse than a terse one. The Concept Deliverer's have no page limit
  (*The seats*).

### 3.5 Numbers across repos

A bare `ADR-nnnn` names the decision in the repo where it is read. A
reference to another repo's decision carries that repo's Repo Tag before
the number: `CBC ADR-0012`, as a CBC Run cites the Concept Deliverer's.
A Repo Tag is a short upper-case name each repo declares once in its
README's decisions row (§7, *README.md*). A document written to be read in another repo
carries the Repo Tag on every citation (ADR-0020).

### 3.6 When an ADR is written

Its moment is the records table's (§13, *The records table*). Written *before* the
decision is made (status: Proposed), it is better still: the writing
often changes the decision.

### 3.7 An ADR's anti-patterns

- Editing old ADRs.
- ADRs so long nobody writes them.
- Recording the decision but not the rejected options: the
  rejections are half the value.

---

## 4. The devlog

The engineering journal.

### 4.1 What the devlog is

Dated, informal entries: what was worked on, what was tried, what
failed and why, open questions, hunches. The project's dated notes,
kept as written.

### 4.2 Why a devlog

Three payoffs:

1. Dead ends are recorded, so they are not explored again. "Tried
   caching at the repo layer, caused stale reads" saves the next
   attempt.
2. Resuming after a break takes minutes, not an hour of re-reading
   code.
3. It is what the records above it are written from: a devlog
   struggle becomes an ADR's context, a retrospective's lesson, a
   playbook warning.

### 4.3 Where the devlog lives

`devlog/2026-08.md` (file per month) or a single `devlog.md` for
small projects, split per month once it passes 300 lines. Newest entries on top.

### 4.4 How the devlog is written

How an entry is written is the devlog's form. In a CBC Run, the form
is the header comment and the first entry of the Record Stub,
`devlog/devlog.md`. In the Concept Deliverer's Convention Seat, it is
`devlog/README.md`. Why the form is as it is:

- Written for future-you, not an audience: short plain sentences,
  as every record is, and honest. "I don't understand why this
  works" is a legitimate and valuable entry.
- An entry names the Plan Step or the work it was part of, and a dead
  end is marked loudly: both are then greppable.
- A session ends with a "Resume:" line, the cheapest place to resume
  from. It marks a place in the work, not a time: sessions
  resume after walks, days or weeks.

### 4.5 When an entry is written

Its moments are the records table's (§13, *The records table*). An entry is never
cleaned up afterwards.

### 4.6 The devlog's anti-patterns

- Polishing it: the habit stops.
- Recording only successes: the failures are the valuable part.
- Letting it replace ADRs: decisions must still be promoted to their
  durable form.

---

## 5. TODO.md

The backlog.

### 5.1 What TODO holds

Everything known but not done: upcoming work not yet in a Plan Step,
bugs, ideas, and consciously deferred problems.

### 5.2 Why a TODO

A thing known and not written down costs attention; written down and
triaged, it costs nothing until its time comes. It also makes
deferral *explicit.* "We know about this and chose not yet" is a
decision, and this is where it's recorded.

### 5.3 Where TODO lives

`TODO.md` in the repo root for small/solo projects; an issue tracker
(GitHub Issues, Linear, Jira) when there's a team. The structure is
the same; the tool differs. Inline `TODO:`/`FIXME:` code comments are
allowed only with an issue/TODO reference attached, otherwise they
are forgotten.

### 5.4 How an item is written

How an item is written, and when it goes, is TODO's form: the
header comment and the headings of `TODO.md`, the Record Stub in a CBC Run and
the Concept Deliverer's own. Why the form is as it is:

- Prune ruthlessly. A 200-item "later" list is never read, and is
  not a plan; deleting an idea you'd re-derive anyway if it mattered
  costs nothing.
- Open work only: what closed is the devlog's, the ADRs' and git's
  to tell, and a closed entry kept here is a second copy of it.
- An item's Context is there so triage reads it without opening what its See names. The story is not there, because the devlog already holds it.
- Ideas are noted, never weighed, until the item is due: an idea
  written here is not lost to the session that had it, and not
  mistaken for a decision.
- The story is written when the item is added, so its See resolves
  at once and the reasons are written while they are fresh.
- An item that changes is rewritten true for today: a dated update
  stacked on it is history, and history is the devlog's.
- An item's Context is capped at what triage needs. When it was
  capped tighter, it lost meaning. When it is looser, an item grows
  back into its story.

*Its story: ADR-0040; devlog 2026-10-17, later; devlog 2026-10-29, the lessons' own stories: project-recording and agent-arrangement.*

### 5.5 When an item is written

Its moments are the records table's (§13, *The records table*). An item goes in when it
is found, so no one has to remember it (§11, *The flow between records*, rule 3).

### 5.6 TODO's anti-patterns

- Using it as the plan: it has no Plan Step Gates or sequence.
- Never deleting.
- Closed entries kept whole.
- Dated updates stacked on an open item.
- Inline code TODOs with no tracked counterpart.

---

## 6. CHANGELOG.md

### 6.1 What a changelog is

Human-written record of notable changes per released version,
addressed to *users* of the project (which may be your future self
or another team), not its developers.

### 6.2 Why a changelog

"What changed between 1.3 and 1.5, and will it break me?" must be
answerable without reading commit history. Commits are too granular
and developer-voiced; the changelog is the curated, user-voiced
digest.

### 6.3 Where the changelog lives

`CHANGELOG.md` in the repo root. Format: Keep a Changelog
(keepachangelog.com) with Semantic Versioning. What a version *is*
depends on the repo type. An application releases SemVer versions. A
concept or docs repo versions something else, and says what at its
framing. The discipline (curated, user-voiced, written per change)
carries unchanged.

### 6.4 How the changelog is written

How an entry is written, and how a release closes, is the
changelog's form: the header comment of `CHANGELOG.md`, the Record Stub in
a CBC Run and the Concept Deliverer's own, which versions the concept (*The
seats*). Why the form is as it is:

- Entries are written when the change is made, not reconstructed at
  release time; `[Unreleased]` gathers them, so a release is a
  rename.
- A breaking change is called out, because whoever pins this repo
  must see it before taking the version.

### 6.5 When the changelog changes

Its moment is each Convention Seat's records table's (§13, *The records table*).

### 6.6 The changelog's anti-patterns

- Dumping git log into it.
- Writing it from memory at release time.
- Developer-speak ("refactored OrderService") instead of user-speak
  ("order creation is ~3x faster").

---

## 7. README.md

The first page a person reads.

### 7.1 What a README is

What this project is, who it's for, how to run it, and where
everything else is.

README is the first page for people; the Entry File is the first for agents
(`docs/conventions/agent-arrangement/` §2, *The Entry File*). Two audiences, two
files, no shared text.

### 7.2 Why a README

It's the entry point for every newcomer including future-you. Its
quality determines whether the rest of the record system gets found
at all. A newcomer reads it first, then ARCHITECTURE, then PLAN,
then the ADRs as needed; the devlog and TODO are working documents,
read by no one cover to cover.

### 7.3 Where a README lives

Repo root, mandatory.

### 7.4 How a README is written

Which sections a README has, and when each arrives, is its form:
the header comment and the sections of `README.md`, the Record Stub in a
CBC Run and the Concept Deliverer's own. Why the form is as it is:

- The "Project records" table is how a newcomer finds the rest. Its
  decisions row declares the Repo Tag, the name its decisions are
  cited by from another repo (§3.5, *Numbers across repos*).
- A section arrives when it becomes true, not at birth (§7.5, *When a README changes*).
- A wrong README is worse than a sparse one, so what changes often
  lives elsewhere and is only linked from here.

### 7.5 When a README changes

Stubbed at birth; after that, its moment is the records table's
(§13, *The records table*). The README says only what is already true
(ADR-0038, 1d). The mechanism is a Plan Step Gate item where
relevant: a Plan Step whose Plan Step Gate makes true something the
README should say includes updating the README. Record upkeep is
already written so in Plan Step Gates in use ("`CLAUDE.md` read top
to bottom"). Never a standing
item on every Plan Step Gate: on 2026-11-01, 7 of the playbook's 9
Plan Steps made nothing true that the README says, and an item usually empty trains
ticking it unread. The Release Plan Step's Plan Step Gate includes "README
verified on a clean machine."

### 7.6 A README's anti-patterns

- Duplicating live status into it.
- Setup instructions that only work on the author's machine.

---

## 8. ARCHITECTURE.md

The current state, in one place.

### 8.1 What ARCHITECTURE is

A short prose description of the system as it *is now*: the main
components, their responsibilities, how they talk to each other,
where the important invariants live, and where in the codebase each
piece is found. It is what a later Invariant Slice may rely on. What
a closed Plan Step proved is history, in its Invariant Slice Record;
ARCHITECTURE holds what stands now. The Concept Deliverer's maps documents and delivery instead, and its
Convention Seat says how.

*Its story: devlog 2026-10-17, later; devlog 2026-10-29, the lessons' own stories: project-recording and agent-arrangement.*

### 8.2 Why ARCHITECTURE

ADRs are a history of individual choices; this is the synthesized
present. (Convention
popularized by matklad's "ARCHITECTURE.md" essay.)

### 8.3 Where ARCHITECTURE lives

`ARCHITECTURE.md` in the repo root (or `docs/`).

### 8.4 How ARCHITECTURE is written

What ARCHITECTURE holds, and when it changes, is its form: the header
comment and the sections of `ARCHITECTURE.md`. In a CBC Run, the Record Stub:
an overview, the components, the invariants and the codemap. The
Concept Deliverer's maps documents and delivery instead (*The seats*). Why
the form is as it is:

- One or two pages, the system as it is now: a newcomer reads it
  second, after the README (§7.2, *Why a README*).
- The why behind a design choice is the ADR's, linked, so ARCHITECTURE states
  and never argues.
- A Plan Step's close is when the structure it describes can have moved,
  so that is when ARCHITECTURE is checked.
- The invariants are a table, one row per invariant, never a paragraph:
  how an Invariant Slice got there is its Invariant Slice Record's.

*Its story: devlog 2026-10-17, later; devlog 2026-10-29, the lessons' own stories: project-recording and agent-arrangement.*

### 8.5 ARCHITECTURE's anti-patterns

- Describing the aspirational design instead of the real one.
- So much detail it goes stale in a week: it describes the whole, the
  code describes each part.

### 8.6 Local Maps

A Local Map is a directory's `README.md`, which ARCHITECTURE points
into. An area gets one when its parts relate in ways ARCHITECTURE
should not carry: how they connect, hand work to each other, or land
elsewhere. A Local Map holds relations only. It holds no count or list
ARCHITECTURE holds, and nothing a part says about itself; its first lines say
what it maps and point for the rest. The file keeps the tool's name,
`README.md`, and not every README is one: a README holding a folder's
rules is another kind (ADR-0045).

*Its story: devlog 2026-09-30, later still.*

---

## 9. The playbook

The Plan Steps every project of a type starts from.

### 9.1 What a playbook is

The reusable, versioned template written from completed plans of
the same project type: the full sequence of Plan Steps, their Plan
Step Gates, and what past CBC Runs taught each.

### 9.2 Why a playbook

It converts one project's experience into the next project's head
start. The first plan of a familiar project type is already written,
and past mistakes stand as warnings at the Plan Step where they
happened.

### 9.3 Where a playbook lives

In the repo that owns the type, the one a project's "Steps from" line
names. Never in the project born from it, which holds only
the copy in its plan. Here,
`delivery/fills/cbc-run-pure-playbook.md`. Versioned (v1, v2, …)
with a note of which project last updated it.

### 9.4 How a playbook is written

The full sequence, first Plan Step to last. The plan's Record Stub prescribes no
Plan Step; a playbook prescribes them all. Each keeps the plan's
form, and what past CBC Runs taught it, as its *Known already*. Its
Release Plan Step carries the type's own release facts. Its lifecycle
has four moments, and each says where its doer reads how:

1. **At birth:** the playbook's Plan Steps fill the plan, and its "Steps
   from" line records which playbook, at what version. A CBC Run born
   without one fills the placeholders of its plan's Record Stub in
   place. That Record Stub says how.
2. **Once the problem is framed:** the CBC Run confirms the Plan Steps
   against it, filling specifics, deleting what it has no use for,
   adding what it needs, renumbering; born without a playbook, it
   authors them. The playbook's Step 2 asks part of it: each later Plan Step is
   read against the CBC Framing Exports and reworded where it no longer
   fits. The TODO item "Read CBC Run 4 against `dac4dd1`" asks whether
   CBC Run 4 did it.
3. **Before the Release Plan Step:** the retrospective writes `RETRO.md`, each
   decision naming where its lesson lands
   (`docs/conventions/retrospective/`).
4. **Write back:** each surviving lesson lands in the playbook the
   plan's "Steps from" line names. How is the playbook's own header
   comment, `delivery/fills/cbc-run-pure-playbook.md`.

The lessons are written into the playbook because it is what the next CBC Run
starts from. The CBC Framing and Release Plan Steps have their own copies
there, so their lessons have a home.

### 9.5 When a playbook changes

Created after the *second* project of a type (the first time you
notice "I've done this before"); updated at every retrospective thereafter.

### 9.6 A playbook's anti-patterns

- Writing a playbook from theory before doing the project type even
  once.
- Never writing retrospectives back: a playbook that stops learning
  is just bureaucracy.
- Plan Step Gates so heavy people route around the playbook.

---

## 10. Supporting records

Used when scale demands.

### 10.1 Design docs and RFCs

For decisions too large for an ADR. An RFC is a multi-page proposal
written *before* building, circulated for comment, kept in
`docs/rfc/`. The
ADR that follows records the outcome; the RFC records the full
exploration. Solo projects rarely need them; teams making
cross-cutting changes do.

### 10.2 Commit messages

The finest-grained decision trail
(`docs/conventions/commit-messages/` §1, *What a commit message is*).

### 10.3 PR descriptions

Where a change's reasoning and its review discussion live. Link the
Plan Step and any ADR; the review thread often contains the "options
considered" that should be promoted into the ADR.

### 10.4 Runbooks

Operational procedures for a *running* system ("how to restore the
DB from backup," "release checklist"). A checklist, as a playbook is,
but for operating, not building. `docs/runbooks/`.

---

## 11. The flow between records

Each record is written from the one below it: the devlog holds what
happened, the records above it keep what lasts:

```
devlog (raw, daily)
  → ADR          when a struggle ends in a decision
  → TODO         when it surfaces future work
  → PLAN notes   when it explains why a Plan Step diverged
       → CHANGELOG      when the Plan Step ships something user-visible
       → ARCHITECTURE   when the Plan Step changed the system's structure
       → RETRO.md       before the Release Plan Step
            → PLAYBOOK  lessons made reusable
                 → next project's PLAN
```

The rules that make this work:

1. **Write once, at the source:** each fact has one home, and the
   other records link to it (`docs/conventions/facts-in-sync/` §1, *One home*).
2. **Promote, don't rely on memory.** A dead end noted in the devlog is
   safe; one merely remembered will be repeated. Same for decisions
   (→ADR) and lessons (→playbook).
3. **Update at natural moments, not on a schedule.** Bound to events,
   recording never becomes a separate chore to skip. *Which* moment
   belongs to which record is stated once, in the Entry File's records
   table (§13, *The records table*): that is where an agent meets it, and a second list here
   would be a copy that drifts.
4. **Cheap at the bottom, durable at the top.** The devlog may be messy;
   ADRs and the playbook must be clean. Effort belongs where the record
   will be re-read.
5. **Markdown, in the repo, versioned with git.** Records live next to
   the code they describe, so they branch, review and roll back with
   it.

## 12. The fewest records needed

Not every project needs all of it. Scale by stakes:

- **Throwaway / experiment:** devlog only (even that is worth it).
- **Solo, real project:** README, PLAN, TODO, devlog, ADRs when a real
  decision happens.
- **Anything with users or teammates:** add CHANGELOG and ARCHITECTURE.
- **Second project of the same type:** add the playbook.

The test for adding any record is always the same: *will someone, probably future-you, need this answer and be unable to
reconstruct it?*
If yes, it gets written down, once, in its designated home.

---

## 13. The records table

*Numbered by creation, not reading order: §13 is cited by number
from other conventions, and renumbering would break those citations
for a cosmetic gain.*

The Entry File is the one file loaded before any task. What it may
hold, and how it stays small, is the agent-arrangement manual's
(`docs/conventions/agent-arrangement/` §2, *The Entry File*). This convention owns one
part of it: the records table, which the Entry File holds and every
session loads (`docs/models/agent.md` §4.1, *Ambient
Channel*; *Why it arrives this way*).

### 13.1 What a records table row holds

**Every row of the records table names three things: the moment, what
the record holds, and its path.** Adding a record means adding its
row. What the record holds is a short summary of its item in the list of records
(§1, *The records at a glance*).

The moment is the part that is new, and the part that is load-bearing.
The table is then readable in both directions: *I just did X, where
does it go?* reads down the first column, *where is Y recorded?* reads
down the second. Both are real questions and a table answering only
one of them is half a table. A rule written only inside the record it
governs teaches the format but cannot teach the timing: "write a
devlog entry at session end" sits in `devlog.md`, and opening
`devlog.md` at session end is the thing you needed telling. A
moment is not a restatement. It says when to go, and contains
nothing about what to write.

### 13.2 Records table anti-patterns

Local status in the Entry File: where the work stands, what is next.
It belongs in `PLAN.md`; the table's row for `PLAN.md` is where the
Entry File says so.

---

## 14. Conversation Memory

The Concept Deliverer's, on trial.

The Conversation Memory is the talk that shaped a TODO item: what was
asked, the options weighed, what was said for and against, the
reviewer's own words. The item keeps what triage needs, and its story
is the devlog's; the talk is neither. In the Concept Deliverer's
Convention Seat it is kept beside the item, in
`TODO-CONVERSATION-MEMORY.md` at the root, next to `TODO.md`
(ADR-0060).

- **One file, a section per item:** a TODO item, or an open
  question another record holds. How a section and its parts are
  kept, when one is read and when it goes, is the file's header
  comment, its form.
- **A record that decides nothing and tells no story:** the item's
  ADR decides, and the devlog tells.
- **The item stands alone.** Its Context is enough for triage, and
  its See names the section. A lost section breaks no record.
- **The reviewer decides what is kept,** each time a talk raises or
  shapes an item, on the agent's recommendation: the talk is the
  reviewer's.
- **Read before the Ideas are weighed,** so the talk shapes the
  weighing.
- **Gone with its item,** so nothing outlives what it was about.

The trial is judged at the moment TODO's item "Judge the
Conversation Memory trial" names.
If it holds, it reaches CBC Runs through the Container Group; if not, it goes.

*On trial since 2026-10-21. The evidence is in the devlog: each
item worked with its section in hand, and whether the section
changed the work.*

## Why it arrives this way

A rule for filling in `PLAN.md` sits inside `PLAN.md`, so acting on
the record is what puts the rule in front of you; there is no trigger
to fire and nothing to remember. The Record Stub arrives as a file
(`docs/models/agent.md` §4.6, *Installed Channel*), and its rule is
read when the agent opens the record (`docs/models/agent.md` §4.2,
*Pulled Channel*). Timing
is the one exception: a rule saying when to open a record cannot live
inside it, so the Entry File's records table carries a moment per row
(§13, *The records table*). An Agent Skill would not do: it fires when the agent recognises the
moment, and failing to recognise the moment is the failure being
fixed. Restating a record's rules in the Entry File "so they are
always available" is the failure the agent-arrangement manual
measured (`docs/conventions/agent-arrangement/`, *What it is for*).

## What this does not cover

- **The Entry File as a whole: what it may hold, and how it stays
  small** — `docs/conventions/agent-arrangement/` §2, *The Entry File*.
- **How a commit is written, and why its body records the why** —
  `docs/conventions/commit-messages/`.
- **How work larger than one commit is sequenced** —
  `docs/conventions/commit-plan/`.
- **Where a fact lives, and how what relies on it stays in
  agreement** — `docs/conventions/facts-in-sync/`.
- **Why the records are never re-delivered to a CBC Run** —
  `docs/conventions/exchange/` §2.4, *The records' exception*.
- **What the Concept Deliverer's CHANGELOG versions** — the concept,
  ADR-0003 and `CHANGELOG.md`'s header comment.

## Where to look

- The Record Stubs: `delivery/container/`.
- The Entry File and its records table:
  `docs/conventions/agent-arrangement/`.
- Commit messages, the finest-grained record:
  `docs/conventions/commit-messages/`.
