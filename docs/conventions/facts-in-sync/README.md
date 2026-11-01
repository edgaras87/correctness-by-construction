---
foundation: the idea-to-output model
---

# Facts in sync

**How each fact keeps one home, and how every text that relies on it
stays in agreement with it.**

## What it is for

So that a fact read anywhere in a repo is the fact as its home
states it today, and a change at the home reaches every line that
relies on it. What went wrong without it:

- duplicated facts diverged, and diverged records stopped being
  trusted;
- the Entry File of the handbook, the repo the arrangement came from,
  now history (ADR-0038), held three disagreeing copies of one rule
  (`docs/conventions/agent-arrangement/`, *What it is for*);
- CBC Run 3 told one Plan Step's story in four records: `PLAN.md`,
  the devlog, the Invariant Slice Record and the commits (its RETRO.md,
  D1).

The rules against it were written early, but spread over two
manuals, the project-recording manual and the conventions manual.
Refinement Round 2 found two Finding Kinds, One home and
Dependencies, the checks of a fact's home and of what a text stands
on, resting on rules split that way, and the rules came here before it
read (ADR-0065).

## What this is made usable as

- **`delivery/container/.claude/rules/one-home.md` — an Agent Rule,
  shipped**, held at `.claude/rules/one-home.md` with no `paths:`,
  so it loads at the start of every session: one home, and the CBC Run's
  Convention Seat (§1, *One home*; *The CBC Run's seat*).
- **`.claude/rules/one-home.md` — the Concept Deliverer's**, loaded in
  every session: one home, point and derive, the Fact Reference, and
  the Concept Deliverer's Convention Seat's question at each commit (§1, *One home*;
  §2, *Point and derive*; §3.1, *What a Fact Reference is*; *The Concept Deliverer's seat*).
- **`.claude/rules/foundation-check.md` — the Concept Deliverer's**, loaded
  in every session and acting before a commit is staged, the Foundation Check: the grep for a moved name, the
  Change Walk and the disagreement (§3.3, *The rename grep*; §4, *A Canonical
  Description's rule*; §5, *A disagreement*).

What derives from this page is that list. A change here runs the Change Walk on it;
a change forced in one of them is checked back against this page.

## The seats

### The CBC Run's seat

A CBC Run holds the shipped one-home Agent Rule: one home per fact, a link
elsewhere, and a copy that cannot be avoided made a follower. It may
retell a fact beside its id where the reader acts on it in place. An
id, such as SLICE-4 or KILL-12, is a CBC Run's Fact Reference, written
bare. When the fact changes at its home, the CBC Run greps the id and
re-reads each line that carries it, in the same commit (ADR-0070).
A CBC Run cannot open this repo's manuals, so a shipped line that relies
on one stands alone (§3.1, *What a Fact Reference is*). A CBC Run meets the Change Walk and the disagreement (§4, *A Canonical
Description's rule*; §5, *A disagreement*) through the CBC Run Reading we write of what it sends back
(`docs/conventions/exchange/` §6, *Up from the CBC Run*).

### The Concept Deliverer's seat

The Concept Deliverer holds its own, wider one-home Agent Rule and the Foundation
Check. It may retell a fact where the reader acts on it in place
(§1, *One home*). Its Fact Reference is a document's path, section and title
(§3.1, *What a Fact Reference is*), and the Change Walk before every commit re-reads it
(§4, *A Canonical Description's rule*). The Change Walk finds only lines
that carry a Fact Reference, so at each commit each new or changed
line is asked whether it relies on a fact written elsewhere, and
whether it says where (ADR-0070).

*Its story: devlog 2026-10-24.*

## 1. One home

Each fact has one home; other texts *link* to it, and copy it only
as a follower. In practice:

- **A summary says it is one.** It names its owner, and nobody
  reads it in the owner's place.
- **A fact changes at its home.** The links to it do not change,
  unless the home itself moves. Each retelling whose Fact Reference
  names it is found and re-read, with the paragraph around it. A
  retelling that sits in a Canonical Description sets off that text's
  Change Walk in turn.
- **A copy is a follower.** One is the owner and the other follows
  it. Two cases: a copy that cannot be avoided, as the CHANGELOG
  follows the version in the build file; and a retelling beside its
  Fact Reference, where the reader acts on the fact in place. A follower
  carries a Fact Reference to the home (§3.1, *What a Fact Reference is*). Without one it is a
  second home.
- **History is not a second home.** The devlog, closed ADRs, commit
  bodies, the entries of `.claude/decisions.md` and a CHANGELOG's
  released entries record what was true then. So do the parts of `TODO-CONVERSATION-MEMORY.md`, which
  only the Concept Deliverer keeps. They are never updated, so they cannot
  drift.
- **Living Text** is every text but history: text kept true as things
  change. Each file's header comment is Living Text, the header
  comments of the history files included.
- **History is not a first home either.** A fact stated only in
  history gets a home in Living Text before anything retells it: nothing
  changes at a history entry, so nothing would re-read what tells it
  (ADR-0070).
- **Comments and config count too,** not only records.

*Its story: ADR-0053; ADR-0059; devlog 2026-10-27, late night.*

## 2. Point and derive

A convention's subject is stated in its manual and nowhere else.
Text that touches the subject points at the manual and does not
restate it: another manual, a Local Map, `ARCHITECTURE.md`, an ADR's
context, an Entry File. Text that makes the subject usable derives
from the manual and names it in `foundation`. Two relations, two
verbs: point and derive. A reader who finds the subject stated
twice has found a defect. The measured case is `docs/conventions/agent-arrangement/`'s, its
*What it is for*. A retelling with a Fact
Reference to its section, where the reader acts on it in place, is
a follower, not a second statement (§1, *One home*; ADR-0059).

## 3. The Fact Reference

### 3.1 What a Fact Reference is

A line that relies on a fact written elsewhere carries a **Fact
Reference**: the address of the fact's home. It has two readers.
The agent may follow it to read the fact whole, with no guarantee
that it will (`docs/models/agent.md` §12.2, *Claims on the Pulled Channel*, claim P1). The Change Walk
re-reads the line when the home changes (§4, *A Canonical Description's rule*). A fact has one home,
so a Fact Reference has one target: the home of the fact its line
relies on. The line above relies on a claim about agents, so it
names the Agent Model, not a convention that applies the claim.

That home sits at the line's own level or above: a Canonical Description's
line points at a Canonical Description or an Idea Model, never at an Agent Skill or a
record for a fact. A line that only names a text, such as the
record a manual describes, is not a Fact Reference, and names any
level (`docs/models/idea-to-output.md` §3.2, *The direction of a link*).

A Fact Reference is written in one form, always in parentheses:

- **in the same repo:** (`<path>` §<number>, *<title>*), such as
  (`docs/conventions/conventions/` §2.4, *The seats*);
- **in the same document:** (§<number>, *<title>*);
- **to another repo:** that repo's Repo Tag first, such as (CBC
  `docs/conventions/exchange/` §3.4, *One group per file*);
- **a section with no number:** its title alone, such as
  (`docs/conventions/exchange/`, *What it is for*);
- **a whole document:** its path alone;
- **a numbered step inside a section:** the step after the title,
  such as (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 3);
- **a numbered rule in a file of rules:** the rule's number and its
  bold lead as the title, such as
  (`.claude/rules/delivered-copies.md`, rule 8, *An Agent Skill
  Template is…*).

In a comment, an HTML one or a line of YAML or SQL, the title takes
no asterisks: there they show as written. In a list whose items are
only addresses, such as a manual's *What this does not cover* and
*Where to look*, the address stands without parentheses; a section
in it still carries its title.

The path runs from the repo root, so a document finds everything
pointing at it with one grep. An Agent Skill names its own files the same
way: two Agent Skills may hold a file of the same name. The number lands
the reader on a paragraph rather than on the whole document. The title says what is
there without opening it, and a number and title that no longer
match show a stale reference. A section's title is 30 characters or
fewer and is carried whole (`docs/conventions/writing/` §2, *Why each
rule*, rule 10); a numbered rule's bold lead over 30 characters is cut
at a word boundary to 30 or fewer, ending in "…". The parentheses give the Change Walk and the reader one pattern to
find; the sentence says its point in words, and the reference gives
only the address.

In a shipped file, a reference to this repo's text leads with CBC
and serves this repo's Change Walk alone. A CBC Run cannot open our manuals, so
the line says what the CBC Run needs without it.

The Agent Model calls any text that sends an agent to a file a
pointer (`docs/models/agent.md` §12.2, *Claims on the Pulled Channel*, claim P1). A
Fact Reference is one kind of pointer, and this page calls it only
by its own name.

Never a relative link: a relative path means a different thing the moment a file is
read from a different root, which is every copy and every shipped
file. A name in prose is not a Fact Reference, because names are
words. A Fact Reference beside a retelling always names the
section: the Change Walk re-reads only the retellings of the section that
changed (§4, *A Canonical Description's rule*), and one with no section would be re-read at every
change.

### 3.2 Numbering a section's parts

A section divided into labelled parts numbers them, `### N.M`. So
does every section of the same form in the document, whether
anything points there yet or not. A Fact Reference names the
number, and a reader meets one structure throughout. Bold emphasis
inside running prose is not a part. A bold-led bullet is a part when
it holds a paragraph of its own, with its own reason or story.
A short list item, a phrase and a line, is not.

*Its story: devlog 2026-09-30, later; devlog 2026-10-29, the lessons' own stories: conventions and facts-in-sync; devlog 2026-10-27, night.*

### 3.3 The rename grep

A commit that renames a file, renumbers or retitles a section, or
moves a fact to a new home greps all Living Text for each old path,
number and title, and fixes what points at them in the same commit.
Placing an Approach on Trial into a convention is such a move
(ADR-0070). A commit plan's sweep looks again before its close
(`docs/conventions/commit-plan/` §2.10, *The sweep*).

*Its story: devlog 2026-10-19.*

### 3.4 A decision citation

A text that rests on a decision cites the ADR that took it. The ADR
is the home of the why, so a citation is a kind of Fact Reference.
Where it goes depends on who reads the text, and the same holds in
both Convention Seats:

1. **A manual cites a decision inside its sentences.** Its reader
   asks why, and the citation stands beside the claim it backs.
2. **A record does the same.** A record tells what is or what
   happened, and its reader follows the citation where it stands.
3. **A Work Approach lists the decisions it rests on once,** in a
   footer headed *Decisions* below a `---` line, and never inside a
   sentence. Its reader acts on the rule at the moment of work, and a
   citation there gives nothing to act on. The footer keeps the why
   one look away for whoever changes the file. A footer line names
   the section it backs, unless it backs the whole file, so a change
   to a section finds its decision.
4. **Each Convention Seat cites its own decisions as `ADR-nnnn`.** A
   Convention Seat can open only its own ADRs, and both number theirs from
   0001, so a bare number means the reader's own. A decision this
   repo inherited is adopted before anything here cites it
   (ADR-0038): a citation points at a decision this repo holds.
   Another repo's decision carries its Repo Tag
   (`docs/conventions/project-recording/` §3.5, *Numbers across repos*).
5. **A copy we deliver has its footer stripped at delivery.** A CBC
   Run cannot open our ADRs, so our footer is a pointer it cannot
   follow. We keep it, since we are the ones who change the file. The
   strip is the Exchange Convention's (`docs/conventions/exchange/`
   §3.8, *The footer at delivery*).
6. **A Record Stub and an Agent Skill Template cite nothing.** The
   project fills them, and a citation of ours would become a line of
   its own record that points at nothing it can open.

*Its story: ADR-0078.*

## 4. A Canonical Description's rule

A Canonical Description is how we understand a thing
today, written down (`docs/models/idea-to-output.md` §2, *The kinds*): the
concept, each Idea Model, each manual, this page included. It states what is true today; how it came to be
is history's: the ADRs, the devlog and commit bodies. It may be
wrong or incomplete. It is canonical regardless: everything derived
from it agrees with it until it changes. It changes only for a reason
recorded, and practice is the evidence. What derives from it is not a
Canonical Description: it applies, it does not explain. The rule is the same
for all of them, and this is where it is stated:

1. A Canonical Description lists what derives from it. An Idea Model leaves its
   list to the grep in step 3: repos it never sees stand on it too.
2. Each derived thing names its Canonical Description once, in its
   one Foundation Line: the document the whole file stands on.
   Which files carry it, where, and what each holds is the conventions manual's
   (`docs/conventions/conventions/` §1.3, *The Foundation Line*). Every line that uses a part of
   a document, the Foundation Line's document included, carries a Fact Reference to that
   part (§3.1, *What a Fact Reference is*).
   Where all of a section's lines use one part of the Foundation Line's document, the
   section carries it once, not each line (ADR-0072). The Foundation Line
   says which document to open when the file changes, and the whole
   file is re-read: that finds what no single line shows, a fact
   gone missing or a file that no longer holds together. A Fact
   Reference says which line to re-read when the part changes.
3. A change to the Canonical Description walks the list in the same commit,
   or in the next when one side is an agent file and the other is
   not (`docs/conventions/commit-messages/` §2.3, *The `agent` scope*). It greps for the
   Canonical Description's path, to find what points at it, and for its name
   in Foundation Lines, to find what stands on it: `the <name>
   convention`, `the <name> model`, or `concept v1`. Each retelling
   whose Fact Reference names a changed section is re-read with the
   paragraph around it. A Canonical Description that changes for it
   has its own Change Walk in turn (step 5). The greps and these re-reads are **the Change Walk**.
4. A change forced in a derived thing is checked back against the
   Canonical Description.
5. A disagreement is raised and decided (§5, *A disagreement*); if the Canonical Description
   changes, the Change Walk runs again.

Steps 1, 2 and the greps in 3 are checkable today: every shipped
Agent Skill and Agent Rule carries `foundation`, every manual names what
derives from it in *What this is made usable as*, and a path and a
`foundation` value are tokens (`docs/conventions/conventions/` §1.3, *The Foundation Line*).
The Foundation Check makes this repo do the rest, the re-reads in
step 3 and steps 4 and 5, before every such commit
(`.claude/rules/foundation-check.md`). Where a manual and the concept
are handled differently is ADR-0039; the concept's edges are ADR-0003
and `CHANGELOG.md`'s standing comment.

*Its story: devlog 2026-09-25, later; devlog 2026-10-29, the lessons' own stories: conventions and facts-in-sync; devlog 2026-10-19.*

## 5. A disagreement

A derived thing, a Fact Reference or practice saying other than its
Canonical Description: two linked texts that disagree, either of which may be
the wrong one (`docs/models/idea-to-output.md` §3.3, *Settling a disagreement*). It is raised
where it is found, in one of four places:

- a finding in a CBC Run Reading;
- an edit a CBC Run made to its copy;
- a question at a boundary;
- the Foundation Check at a commit.

It is decided, never defaulted. Neither side is right for being the
Canonical Description, nor for being newer. Practice is the
evidence. When the Canonical Description changes, the Change Walk runs again (§4, *A Canonical Description's rule*);
when the derived thing changes, it follows in the same commit, or in the next, as the Change Walk's step 3 says (§4, *A Canonical
Description's rule*, step 3). The decision is recorded where the
repo records decisions: a commit body, or an ADR when options were
weighed.

**A finding is declined only for not being general** — this CBC Run's
alone, an exception, or not worth the change. It is never declined
because the Canonical Description says otherwise: a Canonical Description is
downstream of practice like everything else, and a CBC Run that
contradicts one may have found the Canonical Description's flaw rather than
its own. When practice and a statement disagree, the statement is
a candidate for change, not the judge. That includes this page.

It has happened: CBC Run 3 showed a clause of `convention-lifecycle`,
the receiver's protocol then, wrong on the day it first ran under it,
and the clause changed (ADR-0034).

The concept's meaning has changed once since v1 (`CHANGELOG.md`).
Whether it changes rarely because it is right, or because nothing has
been read against it hard enough, is not known.

*Its story: ADR-0034; ADR-0035; ADR-0048; devlog 2026-10-29, the lessons' own stories: six places.*

## Why it arrives this way

Two rules, each loaded in every session, with no `paths:`
(`docs/conventions/agent-arrangement/` §3.9, *An Agent Rule always loaded*). The one-home Agent Rule's moment is
every text written. A fact is retold in the record being written.
That record's Record Stub says nothing of the record the fact was
taken from, so no Record Stub is open at the moment. The
project-recording manual held the rule from the start, and CBC Run 3
still told one Plan Step's story in four records (*What it is for*).
The Foundation Check's moment is every commit that touches a
Canonical Description or what derives from it. An Agent Rule with
`paths:` loads only when a file is touched with the agent's tools: an
edit made by script never loads it
(`docs/conventions/agent-arrangement/` §5.6, *Rules files*). Both
moments are every task, so both Agent Rules go through the Ambient
Channel (`docs/models/agent.md` §8, *Choosing a channel*).

## What this does not cover

- **Which record owns which kind of fact** —
  `docs/conventions/project-recording/` §13, *The records table*.
- **Which copy is the Master Copy, and how a copy reaches a CBC Run** —
  `docs/conventions/exchange/`.
- **What a convention is, and the form of a manual** —
  `docs/conventions/conventions/`.
- **The Repo Tag a citation carries, `CBC ADR-nnnn`** —
  `docs/conventions/project-recording/` §3.5, *Numbers across repos*.
- **What a link is, and that either side may be wrong** —
  `docs/models/idea-to-output.md` §3.1, *The four Chain Links* and §3.3, *Settling a disagreement*.

## Where to look

- The links this keeps: `docs/models/idea-to-output.md` §3.1, *The four Chain Links*.
- The two Agent Rules: `.claude/rules/one-home.md` and
  `.claude/rules/foundation-check.md`.
