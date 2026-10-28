---
foundation: the idea-to-output model
---

# Facts in sync

**How each fact keeps one home, and how every text that relies on it
stays in agreement with it.**

## What it is for

So that a fact read anywhere in a repo is the fact as its home
states it today, and a change at the home reaches every line that
relies on it. What went wrong without it: duplicated facts
diverged, and diverged records stopped being trusted; the
handbook's entry file held three disagreeing copies of one rule
(`docs/conventions/agent-arrangement/`, *What it is for*); run 3
told one step's story in four records (its RETRO.md, D1). The rules
against it were written early, but spread over two manuals,
project-recording and the conventions manual. Round 2 of the
refinement found its One home and Dependencies kinds standing on
rules split that way, and the rules came here before it read
(ADR-0065).

## What this is made usable as

- **`delivery/container/.claude/rules/one-home.md` — a rule,
  shipped**, held at `.claude/rules/one-home.md` with no `paths:`,
  so it loads at the start of every session: one home, and the run's
  seat (§1, *One home*; *The run's seat*).
- **`.claude/rules/one-home.md` — the deliverer's**, loaded in
  every session: one home, point and derive, the fact reference, and
  the deliverer's seat's question at each commit (§1, *One home*;
  §2, *Point and derive*; §3.1, *What it is*; *The deliverer's seat*).
- **`.claude/rules/foundation-check.md` — the deliverer's**, loaded
  in every session and acting before a commit is staged: the grep for a moved name, the
  walk and the disagreement (§3.3, *A rename is grepped…*; §4, *The
  rule for every description*; §5, *A disagreement*).

What derives from this page is that list. A change here walks it;
a change forced in one of them is checked back against this page.

## The seats

### The run's seat

A run holds the shipped one-home rule: one home per fact, a link
elsewhere, and a copy that cannot be avoided made a follower. It may
retell a fact beside its id where the reader acts on it in place. An
id, such as SLICE-4 or KILL-12, is a run's fact reference, written
bare. When the fact changes at its home, the run greps the id and
re-reads each line that carries it, in the same commit (ADR-0070).
A run cannot open this repo's manuals, so a shipped line that relies
on one stands alone (§3.1, *What it is*). The walk and the disagreement (§4, *The rule
for every description*; §5, *A disagreement*) reach a run as the exchange's reading of what it sends back
(`docs/conventions/exchange/` §6, *Up*).

### The deliverer's seat

The deliverer holds its own, wider one-home rule and the foundation
check. It may retell a fact where the reader acts on it in place
(§1, *One home*). Its fact reference is a document's path, section and title
(§3.1, *What it is*), and the walk before every commit re-reads it
(§4, *The rule for every description*). The walk finds only lines
that carry a fact reference, so at each commit each new or changed
line is asked whether it relies on a fact written elsewhere, and
whether it says where (ADR-0070).

*Found 2026-10-24: the 11 manuals' channel sections reasoned from
the agent model with no fact reference. No walk could see them, and
a read found them.*

## 1. One home

Each fact has one home; other texts *link* to it, and copy it only
as a follower. Duplicated facts diverge, and diverged records stop
being trusted. In practice:

- **A summary says it is one.** It names its owner, and nobody
  reads it in the owner's place.
- **A fact changes at its home.** The links to it do not change,
  unless the home itself moves. Each retelling whose fact reference
  names it is found and re-read, with the paragraph around it; a
  retelling whose host is itself a source walks on.
- **A copy is a follower.** One is the owner and the other follows
  it: where two copies cannot be avoided, as the version in the
  build file is followed by the CHANGELOG, or where the reader acts
  on the fact in place, retold beside its fact reference. A follower
  carries a fact reference to the home (§3.1, *What it is*). Without one it is a
  second home.
- **History is not a second home.** The devlog, closed ADRs, commit
  bodies and the entries of `.claude/decisions.md` record what was
  true then. So do the parts of `TODO-CONVERSATION-MEMORY.md`, which
  only the deliverer keeps. They are never updated, so they cannot
  drift. Each file's header comment is living text.
- **History is not a first home either.** A fact stated only in
  history gets a living home before anything retells it: nothing
  changes at a history entry, so nothing would re-read what tells it
  (ADR-0070).
- **Comments and config count too,** not only records.

*Added 2026-10-15, from run 3: its loaded one-home rule said these
five things, and project-recording's rule did not (ADR-0053).*

*Widened 2026-10-20: a line cut to a fact reference left its reader
without the picture at the moment of use. The reviewer judged
three cases, each retold and pointed, and the retellings read
better (ADR-0059).*

*Widened 2026-10-27: round 2 of this repo's refinement had to say
whether the decisions log and the conversation memory were history.
Both are dated and never rewritten, and the list named neither.*

## 2. Point and derive

A convention's subject is stated in its manual and nowhere else.
Text that touches the subject points at the manual and does not
restate it: another manual, the index, `ARCHITECTURE.md`, an ADR's
context, an entry file. Text that makes the subject usable derives
from the manual and names it in `foundation`. Two relations, two
verbs — point and derive — and a reader who finds the subject stated
twice has found a defect; the measured case is `docs/conventions/agent-arrangement/`'s, its
*What it is for*. A retelling with a fact
reference to its section, where the reader acts on it in place, is
a follower, not a second statement (§1, *One home*; ADR-0059).

## 3. The fact reference

### 3.1 What it is

A line that relies on a fact written elsewhere carries a **fact
reference**: the address of the fact's home. It has two readers.
The agent may follow it to read the fact whole, with no guarantee
that it will (`docs/models/agent.md` §4.2, *pulled*, claim P1). The walk
re-reads the line when the home changes (§4, *The rule for every description*). A fact has one home,
so a fact reference has one target: the home of the fact its line
relies on. The line above relies on a claim about agents, so it
names the agent model, not a convention that applies the claim.

That home sits at the line's own level or above: a description's
line points at a description or a model, never at a skill or a
record for a fact. A line that only names a text, such as the
record a manual describes, is not a fact reference, and names any
level (`docs/models/idea-to-output.md` §3.2, *Every link points
up*).

A fact reference is written in one form, always in parentheses:

- **in the same repo:** (`<path>` §<number>, *<title>*), such as
  (`docs/conventions/conventions/` §2.4, *The seats*);
- **in the same document:** (§<number>, *<title>*);
- **to another repo:** that repo's tag first, such as (CBC
  `docs/conventions/exchange/` §3.4, *Every shipped file is…*);
- **a section with no number:** its title alone, such as
  (`docs/conventions/exchange/`, *What it is for*);
- **a whole document:** its path alone;
- **a numbered step inside a section:** the step after the title,
  such as (`docs/conventions/facts-in-sync/` §4, *The rule for every
  description*, step 3);
- **a numbered rule in a file of rules:** the rule's number and its
  bold lead as the title, such as
  (`.claude/rules/delivered-copies.md`, rule 8, *A skill's template
  is copied…*).

In a comment, an HTML one or a line of YAML or SQL, the title takes
no asterisks: there they show as written. In a list whose items are
only addresses, such as a manual's *What this does not cover* and
*Where to look*, the address stands without parentheses; a section
in it still carries its title.

The path runs from the repo root, so a document finds everything
pointing at it with one grep. A skill names its own files the same
way: two skills may hold a file of the same name. The number lands
the reader on a paragraph rather than a wall. The title says what is
there without opening it, and a number and title that no longer
match show a stale reference. A title over 30 characters is cut at
a word boundary to 30 or fewer, ending in "…". The parentheses give the walk and the reader one shape to
find; the sentence says its point in words, and the reference gives
only the address.

In a shipped file, a reference to this repo's text leads with CBC
and serves this repo's walk alone. A run cannot open our manuals, so
the line says what the run needs without it.

The agent model calls any text that sends an agent to a file a
pointer (`docs/models/agent.md` §12.2, *On pulled*, claim P1). A
fact reference is one kind of pointer, and this page calls it only
by its own name.

Never a relative link: a relative path means a different thing the moment a file is
read from a different root, which is every copy and every shipped
file. A name in prose is not a fact reference, because names are
words. A fact reference beside a retelling always names the
section: the walk re-reads only the retellings of the section that
changed (§4, *The rule for every description*), and one with no section would be re-read at every
change.

### 3.2 A section's parts are numbered

A section divided into labelled parts numbers them, `### N.M`, and
so does every section of the same form in the document, whether
anything points there yet or not: a fact reference names the
number, and a reader meets one structure throughout. Bold emphasis
inside running prose is not a part. A bold-led bullet is a part when
it holds a paragraph of its own, with its own reason or dated case.
A short list item, a phrase and a line, is not.

*Decided in the walk, 2026-09-29, when the conventions manual's §3
held six rules as bold paragraphs and every reference into it said
"§3"; it lived in the devlog alone until 2026-09-30. Written there
first as "a part other text points at", it would have numbered one
section of project-recording beside seven built the same way; the
reviewer caught it at the boundary, and it was reworded the same
day, by form.*

*Found 2026-10-27, at round 2's close read: commit-plan §2's
bold-led bullets had been numbered in `79bc4a2`, and 16 more
sections in 10 documents were built the same way. The rule said
nothing of a bold-led bullet, so each could be read two ways.*

### 3.3 A rename is grepped at its commit

A commit that renames a file, renumbers or retitles a section, or
moves a fact to a new home greps all living text for each old path,
number and title, and fixes what points at them in the same commit.
Placing an approach on trial into a convention is such a move
(ADR-0070). A commit plan's sweep looks again before its close
(`docs/conventions/commit-plan/` §2.10, *The sweep, before the close…*).

*Found 2026-10-19: the refinement's manual was renumbered three
times on 2026-10-18, outside any commit plan, so no close sweep
ran. A fact reference in TODO stood stale for five commits. The grep
moved from a plan's close to the commit that renumbers.*

## 4. The rule for every description

This page included. A description is how we understand a thing
today, written down (`docs/models/idea-to-output.md` §2, *The kinds*): the
concept, each model, each manual. It states what is true today; how it came to be
is history's: the ADRs, the devlog, commit bodies, and a lesson's
dated italic (`docs/conventions/conventions/` §2.6, *A lesson taken*). It may be
wrong or incomplete, and it is
canonical regardless — everything derived from it agrees with it
until it changes, and it changes only for a reason recorded,
practice being the evidence. What derives from it is not a
description: it applies, it does not explain. The rule is the same
for all of them, and this is where it is stated:

1. A description lists what derives from it. A model leaves its
   list to the grep in step 3: repos it never sees stand on it too.
2. Each derived thing names its description, once: one
   `foundation` per file, its root, what the whole of it stands on.
   Which files carry it, where, and what each holds is the conventions manual's
   (`docs/conventions/conventions/` §1.3, *The `foundation` line*). Every line that uses a part of
   a document, its root included, carries a fact reference to that
   part (§3.1, *What it is*), the root's parts as much as any other's. The root
   says which document to open when the file changes, and the whole
   file is re-read: that finds what no single line shows, a fact
   gone missing or a file that no longer holds together. A fact
   reference says which line to re-read when the part changes.
3. A change to the description walks the list in the same commit,
   or in the next when one side is an agent file and the other is
   not (`docs/conventions/commit-messages/` §2.3, *The agent's files never share…*). It greps for the
   description's path, to find what points at it, and for its name
   in `foundation` lines, to find what stands on it: `the <name>
   convention`, `the <name> model`, or `concept v1`. Each retelling
   whose fact reference names a changed section is re-read with the
   paragraph around it; a host that changes for it is walked in
   turn (step 5). The greps and these re-reads are **the walk**.
4. A change forced in a derived thing is checked back against the
   description.
5. A disagreement is raised and decided (§5, *A disagreement*); if the description
   changes, the walk runs again.

Steps 1, 2 and the greps in 3 are checkable today: every shipped
skill and rule carries `foundation`, every manual names what
derives from it in *What this is made usable as*, and a path and a
`foundation` value are tokens (`docs/conventions/conventions/` §1.3, *The `foundation` line*).
The foundation check makes this repo do the rest, the re-reads in
step 3 and steps 4 and 5, before every such commit
(`.claude/rules/foundation-check.md`). Where a manual and the concept
are handled differently — versioning, shipping, the kind of
derivative, the seats, what each asserts — is ADR-0039; the
concept's edges are ADR-0003 and `CHANGELOG.md`'s standing
comment.

*Before 2026-10-17 the rest ran twice by hand: the correspondence
check of 2026-09-25, and the walk of `a337674^:docs/master.md` at
the exchange plan's close, both because the reviewer asked, not
because anything made anyone look.*

*Found 2026-10-19: project-recording's deliverer seat retold
`PLAN.md`'s step form, and nothing linked the two, so a change on
either side never reached the other. The reviewer had a record's
form name its description, as a skill does.*

## 5. A disagreement

A derived thing, a fact reference or practice saying other than its
description: two linked texts that disagree, either of which may be
the wrong one (`docs/models/idea-to-output.md` §3.3, *A disagreement is settled*). It is raised
where it is found — a finding in a reading, an edit a run made to
its copy, a question at a boundary, the foundation check at a
commit — and decided, never defaulted: neither side is right for
being the description, nor for being newer. Practice is the
evidence. When the description changes, the walk runs again (§4, *The rule for every description*);
when the derived thing changes, it follows in the same commit, or in the next, as the walk's step 3 says (§4, *The rule for every
description*, step 3). The decision is recorded where the
repo records decisions: a commit body, or an ADR when options were
weighed.

**A finding is declined only for not being general** — this run's
alone, an exception, or not worth the change. It is never declined
because the description says otherwise: a description is
downstream of practice like everything else, and a run that
contradicts one may have found the description's flaw rather than
its own. When practice and a statement disagree, the statement is
a candidate for change, not the judge. That includes this page.

*Where it has already happened, so the rule reads as a record and
not a wish. ADR-0034: run 3 argued down a clause of
`convention-lifecycle` on the day it first ran under it — taken,
against the text as shipped. ADR-0035: run 3 made a thing the
vocabulary had no word for; the vocabulary gained one, and the
next day went, on the same evidence read further. `cbc-slice`,
three times: every in-place edit run 3 made to the method was
taken whole. And the concept has bent from the runs three times.
Twice editorially, leaving it at v1: chapter 03's sentence on when
technology enters (`211bd0f`), and chapter 01's layer tags in full
words, from run 3's RETRO D6 (`41d4fc3`). Once in substance:
chapter 02's top rung of the walls, which run 3 met at SL-3, makes
the concept v2 when it is released (`86ed0c4`, ADR-0048).*

Whether the concept bends this rarely because it is right, or
because nothing has been read against it hard enough, is not known.

## Why it arrives this way

Two rules, each loaded in every session, with no `paths:`
(`docs/conventions/agent-arrangement/` §3.9, *A rule loaded in every session*). One home's moment is
every text written: a fact is retold in the record being written,
and that record's stub says nothing of the record the fact was taken
from, so no stub is open at the moment. project-recording held the
rule from the start, and run 3 still told one step's story in four
records: PLAN, the devlog, the slice record and the commits (its
RETRO.md, D1). The check's moment is every commit that touches a
description or what derives from it, and a rule with `paths:` loads
only when a file is touched with the agent's tools: an edit made by
script never loads it (`docs/conventions/agent-arrangement/` §5.6, *Rules files*).
Both moments are every task, so both rules are ambient
(`docs/models/agent.md` §8, *Choosing a channel*).

## What this does not cover

- **Which record owns which kind of fact** —
  `docs/conventions/project-recording/` §13, *The records table…*, the records table.
- **Which copy is the master, and how a copy reaches a run** —
  `docs/conventions/exchange/`.
- **What a convention is, and the form of a manual** —
  `docs/conventions/conventions/`.
- **The repo prefix a citation carries, `CBC ADR-nnnn`** —
  `docs/conventions/project-recording/` §3.5, *A number is local to one repo*.
- **What a link is, and that either side may be wrong** —
  `docs/models/idea-to-output.md` §3.1, *The four links* and §3.3, *A disagreement is settled*.

## Where to look

- The links this keeps: `docs/models/idea-to-output.md` §3.1, *The four links*.
- The two rules: `.claude/rules/one-home.md` and
  `.claude/rules/foundation-check.md`.
