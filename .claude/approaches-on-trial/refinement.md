# Refinement

**A refinement brings text written before a rule up to that rule.
It goes in Refinement Rounds: what is true, then where it lives, then how it
reads. Each Refinement Round reads first and lists what it finds. Nothing
changes until the reviewer has ended each finding, and then the
text is fixed by a Change Set written from the list.**

## What it is for

A rule guards new and changed text only. Older text is rewritten
in work of its own (`.claude/rules/writing.md`, *Where it
applies*), and a refinement is that work.

Without it, older text keeps the habits a rule was written to
stop, and the agent copies what it reads. CBC Run 3's records came out
in the method's voice, though its memory said to explain plainly
(CBC Run 3's RETRO D2).

The need was written down on 2026-10-17. Most of this repo's text
then predated four rules:

- the writing and one-home Agent Rules;
- the Foundation Check (2026-10-17);
- a lesson written in general (`docs/conventions/conventions/`
  §2.6, *A lesson taken*, 2026-10-18).

Done once before, unnamed: the eval of 2026-09-30 to 2026-10-02
read the whole repo, listed 68 findings and 10 decisions in six
parts, and ended every one. Its file is in git at
`19f1d7b^:temp/eval-2026-09-30.md`.

*On trial,* after one use: its first evaluation kept every piece on
trial and placed none (ADR-0080). What would settle it is *Settled
when*, below.

## What this is made usable as

Nothing yet: each piece stays on trial (ADR-0080). While a refinement is open, a repo holds:

- **its Plan Step in `PLAN.md`**, whose Notes list this page's Approach on Trial Stages;
- **its file, `temp/refinement-<date>.md`**, deleted at the close.

What derives from this page is that list. A change here runs the Change Walk on it.

## The seats

No Convention Seat in a CBC Run, for now. This is first-time work of this repo
alone, so its trial is our own next refinement. A CBC Run that finds it
needs one offers it under *To the deliverer*. The rest of this page
is the Concept Deliverer's.

## 1. What it reads

A refinement reads Living Text (`docs/conventions/facts-in-sync/` §1.5,
*Living Text*) against the rules it names. It leaves out `docs/baselines/`, frozen on purpose,
and a CBC Run's own text in `temp/`, which its CBC Run Reading reads. Its
Finding Kinds are its own, so they are written in its file, not here.

Text another TODO item already plans to rewrite is read here too.
Fixed in the same pass, it is read once against every rule, not twice.

*Found 2026-11-02: Refinement Round 3 did the method's plain rewrite,
which a TODO item held, and the last read finished it; the item kept
only what no Finding Kind asked (ADR-0080).*

### 1.1 The refinement's words

The words of this page, each defined once:

- **Finding Kind** — one rule the refinement reads against, and the
  findings it makes. Written as what a finding of it is, the rule,
  and its Refinement Round.
- **Refinement Round** — the Finding Kinds whose fixes do the same to the text, read
  and fixed together before the next Refinement Round reads (§2.1, *Group the Finding Kinds*).
- **Refinement Layer** — a set of files listed together. Refinement Layers go in an order
  that puts a source before what derives from it (§2.2, *List the files*).

## 2. The Approach on Trial Stages

A map of the Approach on Trial Stages. Each section holds its rule.

| Stage | Does | The refinement's file |
|---|---|---|
| 2.1 Group the Finding Kinds | Finding Kinds from TODO, each in its Refinement Round | created, with the Finding Kinds |
| 2.2 List the files | every file of Living Text into a Refinement Layer, with counts | the Refinement Layer list |
| 2.3 Check the rules | before each Refinement Round: doubts found, and tried on a sample | each rule's result |
| 2.4–2.8 Each Refinement Round | read, list the findings, decide, work, close | the Refinement Round's section; its findings collapse at its close |
| 2.9 The last read | every Finding Kind, read until nothing is found | its section |
| 2.10 The close | the file goes; git keeps it | deleted |

The file is `temp/refinement-<date>.md`. It holds data; this page
says how it is made.

Each Refinement Round reads, lists, decides and fixes before the next one
reads, so it reads the text as the Refinement Round before left it. The
reviewer never decides a finding on text a later Refinement Round deletes.
The reviewer's time is what the extra reads save.

### 2.1 Group the Finding Kinds

Refinement Rounds are ordered so that no Refinement Round's fixes are undone or wasted
by a later Refinement Round. Finding Kinds whose fixes do not undo each other share a
Refinement Round.

Every refinement starts from three Refinement Rounds, by what a Finding Kind's fix
does to the text:

1. **Makes a line true.** A wrong line is not worth moving or
   rewording.
2. **Moves or removes text.** A retelling that becomes a Fact Reference goes, so it is not reworded first.
3. **Rewords what stays.**

A Refinement Round with no Finding Kind in it is left out. A Finding Kind that fits none of
the three gets a Refinement Round added or changed, by the rule above. The
file records the Refinement Rounds used, and why any differs from these
three.

The Finding Kinds are collected from the TODO items that asked for the
refinement. The agent puts each in its Refinement Round, and writes them into
a new file, the refinement's file. The reviewer confirms the Finding Kinds
and their Refinement Rounds.

### 2.2 List the files

The agent lists the files of Living Text (§1, *What it reads*) in the file, by Refinement Layer, with
their counts. Every refinement starts from these six Refinement Layers, in an
order that puts a source before what derives from it:

1. the conventions manual, `docs/conventions/conventions/`, which
   every other manual is read against;
2. project-recording, with its list of the records, which other
   text points to;
3. the other manuals, and the concept chapters;
4. `ARCHITECTURE.md`, `README.md` and the records;
5. our Agent Skills and Agent Rules, under `.claude/`;
6. `delivery/`, what ships.

Every file of Living Text falls in exactly one Refinement Layer. When the list finds a
file that fits none, a Refinement Layer is widened to hold it, or a new one
is added, and the file records it. Each Refinement Round shows from
this list that it covered every file. The reviewer confirms the
Refinement Layers.

### 2.3 Check the rules

A wrong rule makes every finding against it wrong. So, before each
Refinement Round reads, the reviewer confirms that no rule among its Finding Kinds is
in doubt. Before a later Refinement Round, the check reads only what changed
since the last one: a rule moved or rewritten, or a TODO item that
now names it. A doubt comes from the reviewer, or from
a TODO item that names the rule or its manual; the agent searches
TODO for each rule's name and its manual's path. A doubt that
names a manual covers every rule that stands on it.

A doubted rule is first read whole, with the manual it stands on.
A gap, or a line nobody means any more, is fixed in the manual,
and the Foundation Check carries the fix to the Agent Rules and Agent Skills
that derive from it. Where the doubt is about what a rule does to
text, the rule is also tried on a sample of the text it governs,
taken from the files' list (§2.2, *List the files*), and the reviewer judges the result.

A manual in doubt may be gone through section by section, top to
bottom. Before a fix adds anything, it looks for the place that
should already do the job: a section to fix, or a retelling to
remove. A fix in place comes before a new part. Each fix is judged
before the next, on four questions:

1. **Maintenance:** does a change to this subject now touch fewer
   places?
2. **Readability:** does a reader find what they came for faster?
3. **Future-proofing:** does it make the next change easier?
4. **Complexity:** does it add more than it removes?

The verdict is kept, changed or reverted, with numbers before and
after where they exist: the lines, and how many places a subject is
told.

Every fix lands before its Refinement Round reads, each in a commit of its
own. The file says, for each rule, whether it was in doubt and how
its check ended.

*Found 2026-10-19, in the redesign of the conventions that this
refinement stopped for: its two iterations on the conventions
manual were fixes of this kind. The first try added a section that
repeated what the opening statement and "What it is for" are for.
The redesign closed, and its way of judging each fix came here.*

*Found 2026-10-25, before Refinement Round 2: a convention TODO item
was due when Refinement Round 2 would read. Its fix would have moved
the rules the One home and Dependencies Finding Kinds stand on, in
the middle of the read. The check moved from the first Refinement
Round to each Refinement Round.*

### 2.4 Reading the Finding Kinds

Each Finding Kind is read on its own: a reader looks for one Finding Kind only,
so nothing else takes its attention. The Finding Kinds of one Refinement Round can be
read side by side. Most Finding Kinds read each file whole. One home also
needs a sweep across files, since one file alone cannot show it.

A finding names the rule the text breaks. Text that meets its
rules stays, even when it could be said better. A reader asked to
look always finds something to change. A broken rule makes it a
finding; taste does not. This matters most where the Finding Kind is about
how text reads.

A rule stays as it is while a Refinement Round reads against it. Changed
halfway, everything read before the change would be read again. A
finding against a rule itself waits in the list like any other.

Nothing is fixed during the read. One fix in a manual can change
what is right in every file derived from it. The whole list shows
those chains before any work is spent on them.

A reader's finding is checked against the tree before it is
listed. Each finding says how it stands: checked, resting on the
reader, or uncertain.

*Lived 2026-09-30, in the eval: six readers, one area each, and
every finding checked against the tree before it was listed. A
section two readers called wrong and right became one finding.*

### 2.5 List the findings

The findings go into the Refinement Round's section of the file. Each
finding is FINDING-n, numbered on across the Refinement Rounds, and says:

- where: the path, and lines;
- what the rule says, and what the text says;
- how it stands (§2.4, *Reading the Finding Kinds*);
- why the text breaks the rule, one of three: it is older than the
  rule; the checks at the change missed it, naming the check that
  should have caught it; or the rule is unclear or wrong.

A finding of the second or third cause carries a lesson. It goes to
the check or the rule the finding names, at the Plan Step's close,
with the Plan Step's other lessons. A finding older than its rule
teaches nothing: it is fixed, and that is all.

A finding that needs the reviewer's choice beyond "fix it" gets a
DECISION-n: the options, a recommendation, and the findings that
rest on it.

A Refinement Round's findings are listed by Refinement Layer, in the order the work
takes them (§2.2, *List the files*).

### 2.6 Deciding the findings

The reviewer sees the Refinement Round's whole list before any finding is
decided (`.claude/rules/foundation-check.md`, step 4). Each finding
then gets one ending:

- **fixed**, and its line names the commit;
- **stands by a decision**, naming the DECISION-n or the call;
- **declined**, with the reason;
- **moved** to a TODO item.

A finding is never deleted or renumbered while the file lives.

### 2.7 Working the findings

A Refinement Round's findings are worked as one Change Set
(`docs/conventions/commit-plan/`), written from its list. The list's
order by Refinement Layer (§2.2, *List the files*) shows which fixes
are sources. The plan groups the commits by what each change needs:

- **each shared fact first:** its home and every copy in one commit,
  so no commit leaves the repo disagreeing with itself;
- **then each file once:** all its findings in one edit.

Each commit names its findings. Once the work is done, the Refinement
Round's section names each finding's commit. A commit that touches a
Canonical Description goes through the Foundation Check.

*Found 2026-11-01: one commit plan for each Refinement Layer would
have opened most files of the last read two or three times, and left a
shared fact's copies disagreeing between Refinement Layers
(devlog 2026-11-01).*

A finding's ending is read from the decisions and the agent's calls
together before it is fixed. The finding's own entry still reads as
its reader proposed.

*Found 2026-11-01: Refinement Round 3's close read listed the agent's
calls after its last decision, and four findings were worked from
their entries against the call (devlog 2026-11-01).*

A fact told in several files is fixed in one commit, its home and
every copy. A copy that a Fact Reference can replace becomes one: a
deletion, not a rewrite.

A finding whose fix changes how a convention works, not only what
its text says, is a design change. It is made inside the
refinement, as a commit plan of its own on its branch; the
refinement does not stop for it. It goes as soon as the reviewer
has decided it, before the Refinement Round's other decisions, since other
findings may rest on it. The Foundation Check carries it to what
derives from the convention. It never changes a rule the Refinement Round
reads against (§2.4, *Reading the Finding Kinds*). A change with a goal of its own, too big for
one commit plan, is a Plan Step of its own, in `PLAN.md`.

*Found 2026-10-20: Refinement Round 1's DECISION-1 asked what "manual" means
in a CBC Run, and the answer was a change to how first-time work is
done, not to two sentences. The day before, the refinement had
stopped for a redesign of the conventions that proved to be its
own rule check. The reviewer had this one made inside the
refinement.*

### 2.8 A Refinement Round's close

Every finding of the Refinement Round has its ending. Then all the text the
Refinement Round covers is read again against its Finding Kinds, held to the rule for a finding (§2.4, *Reading the Finding Kinds*). Reading only the changed text is not
enough: a fix in one file can make an unchanged line in another
wrong. What the read finds is listed and decided like any finding,
and the Refinement Round's section counts:

- findings in text the Refinement Round changed, and in text it did not;
- findings by cause: older than the rule, missed at the change, the
  rule unclear;
- how many the reviewer took, and how many were declined as taste.

Then the Refinement Round's findings collapse: each list becomes one line
naming the commit that last holds it whole. The next Refinement Round reads
the text, not the findings, and every commit cites their numbers.
The setup, the decisions, the counts and anything left for a later
Refinement Round stay.

*Found 2026-10-21: after Refinement Round 1, the file held 1,639 lines, 1,450
of them closed findings that Refinement Round 2 would not read. Collapsed in
`a629f52`, it held 390.*

### 2.9 The last read

After the last Refinement Round, everything is read against every Finding Kind of
the refinement. It catches a later Refinement Round breaking an earlier one's
work: a reworded line no longer true, a Fact Reference reworded wrong.

The Finding Kinds are read on their own (§2.4, *Reading the Finding Kinds*), but in one read, with
no fixes between them. The order of the Refinement Rounds is for fixes, not
for reads: with nothing changing, a read gives the same result in
any order.

What it finds is listed by Refinement Round, by the Finding Kinds'
rule (§2.1, *Group the Finding Kinds*), then by Refinement Layer
(§2.5, *List the findings*). No read waits on a fix, so all of it is
worked as one Change Set written from that list (§2.7, *Working the
findings*). Where findings of two Refinement Rounds touch the same
lines, the edit takes them in Refinement Round order. Then everything is read
again, until a read finds nothing that breaks a rule. The rule for a finding (§2.4, *Reading the Finding Kinds*) is what makes this end.

### 2.10 The close

The file goes in a commit of its own, and the devlog names that
commit, so the file can be read from git.

## 3. Not known yet

- **Whether the order holds:** the first Refinement Round tests the Refinement Layers (§2.2, *List the files*); the last, whether the Refinement Rounds were worth their reads.
- **Whether a refinement comes again,** and what makes one due: a
  new rule, or a count of rules since the last.
- **Whether a refinement is the second check on text kept true.** The
  reviewer's view, 2026-10-31: the checks at each change are the
  first, a refinement the second, and a finding's cause the way back
  from the second to the first. Judged at the close, with where it is
  written: a convention of its own, or the facts-in-sync manual.
- **Whether the refinement's file needs an Output Shape.** It borrows the
  eval's form, which borrowed a CBC Run Reading's.
- **Whether the three Refinement Rounds hold.** They were drawn from one
  refinement's eight Finding Kinds. Wiring, which adds missing links, fitted
  Refinement Round 1; whether other added text fits is still to see.
- **Whether a Change Set written from the list holds.** The last
  read's is the first; its close says what diverged.
- **Approach on Trial Stages beside Agent Skill Stages.** The glossary gives this
  page's phases their own Name; whether the two hold apart is judged
  at the close.
- **Whether the full reads again paid.** The counts of findings in
  unchanged text decide whether a narrower read would have done. In
  the first refinement, 54 of the last read's findings were older than
  their rule, in text earlier reads had left. Its read again was
  skipped for budget, so it gave no count.
- **Whether the design change in place belongs to every Plan Step.**
  The work holds it for a refinement alone (§2.7, *Working the findings*) (`8c9aadf`), the only work
  that has lived it. A draft into both Plan Step Forms, ours and the
  container's, was undone before its commit.

## Settled when

A second refinement has run on it, and its evaluation changed nothing
in it. Each *Not known yet* item is then answered from two uses.

## Uses

*The Concept Deliverer, the first refinement, 2026-10-18 to 2026-11-02.*
Three Refinement Rounds and a last read; the last read's 385 findings
all ended, in one Change Set written from the list. The read again was
skipped once, for budget, and §2.9 stands. Taught: Refinement Rounds
and Refinement Layers order the read and the list, not the work
(§2.7, *Working the findings*); text another TODO item already plans to
rewrite is read in the same pass (§1, *What it reads*). Its file is in
git at `55e2bd0^:temp/refinement-2026-10-18.md`.

## Why it arrives this way

An Approach on Trial, first written as a manual on trial by
first-time work. An Agent Skill written before
the work would describe a guess. The work corrects this page as it
goes, and its evaluation at the close places its pieces
(`.claude/approaches-on-trial/approach-evaluation.md`).

## What this does not cover

- **Checking one change at its commit** —
  `.claude/rules/foundation-check.md`.
- **Reading a CBC Run** — `docs/conventions/exchange/` §6, *Up from the CBC Run*, and
  `.claude/rules/working-a-reading.md`.
- **How text reads, and where a fact lives** —
  `.claude/rules/writing.md`, `.claude/rules/one-home.md`.
- **How the work's commits are planned** —
  `docs/conventions/commit-plan/`.

## Where to look

- `.claude/approaches-on-trial/approach-drafting.md`
- `19f1d7b^:temp/eval-2026-09-30.md`, the eval, in git

---

## Decisions

- ADR-0053 — *What it is for*: the writing and one-home Agent Rules
- ADR-0056 — *Why it arrives this way*: first written as a manual on
  trial by first-time work
- ADR-0058 — *Why it arrives this way*: an Approach on Trial
- ADR-0080 — *What it is for*, §1 and *Uses*: every piece on trial
  after the first use; text another TODO item already plans to rewrite
  is read here
