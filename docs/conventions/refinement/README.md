# Refinement

**A refinement brings text written before a rule up to that rule.
It goes in rounds: what is true, then where it lives, then how it
reads. Each round reads first and lists what it finds. Nothing
changes until the reviewer has ended each finding, and then the
text is fixed one layer at a time.**

## What it is for

A rule guards new and changed text only. Older text is rewritten
in work of its own (`.claude/rules/writing.md`, *Where it
applies*), and a refinement is that work.

Without it, older text keeps the habits a rule was written to
stop, and the agent copies what it reads. Run 3's records came out
in the method's voice, though its memory said to explain plainly
(run 3's RETRO D2).

The need was written down on 2026-10-17. Most of this repo's text
then predated four rules:

- writing, and one home per fact (ADR-0053);
- the foundation check (2026-10-17);
- a lesson written in general (`docs/conventions/conventions/`
  §3.7, 2026-10-18).

Done once before, unnamed: the eval of 2026-09-30 to 2026-10-02
read the whole repo, listed 68 findings and 10 decisions in six
parts, and ended every one. Its file is in git at
`19f1d7b^:temp/eval-2026-09-30.md`.

*On trial.* What would make it evidence: the refinement step in
`PLAN.md` closes with every finding ended, and the reviewer judges
whether rounds, each read first and fixed layer by layer, held.
Look again at that step's close.

## What this is made usable as

Nothing yet: the close decides (`docs/conventions/first-time-work/`
§3). While a refinement is open, a repo holds:

- **its step in `PLAN.md`**, whose Notes list this page's stages;
- **its file, `temp/refinement-<date>.md`**, deleted at the close.

What derives from this page is that list. A change here walks it.

## The seats

No seat in a run, for now. This is first-time work of this repo
alone, so its trial is our own next refinement. A run that finds it
needs one offers it under *To the deliverer*. The rest of this page
is the deliverer's.

## 1. What it reads, and its words

A refinement reads living text against the rules it names. Its
kinds are its own, so they are written in its file, not here.

The words of this page, each defined once:

- **living text** — every file but history. History is the
  devlog, closed ADRs and commit bodies
  (`.claude/rules/one-home.md`). Also left out: `docs/baselines/`,
  frozen on purpose, and a run's own text in `temp/`, which its
  reading reads.
- **kind** — one rule the refinement reads against, and the
  findings it makes. Written as what a finding of it is, the rule,
  and its round.
- **round** — the kinds whose fixes do the same to the text, read
  and fixed together before the next round reads (§2.1).
- **layer** — a set of files fixed together. Layers go in an order
  that puts a source before what derives from it (§2.5).

## 2. The stages

A map of the stages. Each section holds its rule.

| Stage | Does | The refinement's file |
|---|---|---|
| 2.1 Group the kinds | kinds from TODO, each in its round | created, with the kinds |
| 2.2 List the files | every living file into a layer, with counts | the layer list |
| 2.3 Check the rules | doubts found, and tried on a sample | each rule's result |
| 2.4–2.8 Each round | read, list the findings, decide, work, close | the round's section |
| 2.9 The last read | every kind, read until nothing is found | its section |
| 2.10 The close | the file goes; git keeps it | deleted |

The file is `temp/refinement-<date>.md`. It holds data; this page
says how it is made.

Each round reads, lists, decides and fixes before the next one
reads, so it reads the text as the round before left it. The
reviewer never decides a finding on text a later round deletes.
The reviewer's time is what the extra reads save.

### 2.1 Group the kinds

Rounds are ordered so that no round's fixes are undone or wasted
by a later round. Kinds whose fixes do not undo each other share a
round.

Every refinement starts from three rounds, by what a kind's fix
does to the text:

1. **Makes a line true.** A wrong line is not worth moving or
   rewording.
2. **Moves or removes text.** A retelling that becomes a pointer
   goes, so it is not reworded first.
3. **Rewords what stays.**

A round with no kind in it is left out. A kind that fits none of
the three gets a round added or changed, by the rule above. The
file records the rounds used, and why any differs from these
three.

The kinds are collected from the TODO items that asked for the
refinement. The agent puts each in its round, and writes them into
a new file, the refinement's file. The reviewer confirms the kinds
and their rounds.

### 2.2 List the files

The agent lists the living files (§1) in the file, by §2.5's
layers, with their counts. Every living file falls in exactly one
layer. When the list finds a file that fits none, a layer is
widened to hold it, or a new layer is added. Each round shows from
this list that it covered every file. The reviewer confirms the
layers.

### 2.3 Check the rules

A wrong rule makes every finding against it wrong. So, before the
first round reads, the reviewer confirms that no rule among the
file's kinds is in doubt. A doubt comes from the reviewer, or from
a TODO item that names the rule or its manual; the agent searches
TODO for each rule's name and its manual's path. A doubt that
names a manual covers every rule that stands on it.

A doubted rule is first read whole, with the manual it stands on.
A gap, or a line nobody means any more, is fixed in the manual,
and the foundation check carries the fix to the rules and skills
that derive from it. Where the doubt is about what a rule does to
text, the rule is also tried on a sample of the text it governs,
taken from §2.2's list, and the reviewer judges the result.

Every fix lands before the first round reads, each in a commit of
its own. The file says, for each rule, whether it was in doubt and
how its check ended.

### 2.4 Read

Each kind is read on its own: a reader looks for one kind only,
so nothing else takes its attention. The kinds of one round can be
read side by side. Most kinds read each file whole. One home and
words also need a sweep across files, since one file alone cannot
show them.

A finding names the rule the text breaks. Text that meets its
rules stays, even when it could be said better. A reader asked to
look always finds something to change. A broken rule makes it a
finding; taste does not. This matters most where the kind is about
how text reads.

A rule stays as it is while a round reads against it. Changed
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

The findings go into the round's section of the file. Each
finding is FINDING-n, numbered on across the rounds, and says:

- where: the path, and lines;
- what the rule says, and what the text says;
- how it stands, as in §2.4.

A finding that needs the reviewer's choice beyond "fix it" gets a
DECISION-n: the options, a recommendation, and the findings that
rest on it.

A round's findings are listed by layer, in the order the work
takes them. Every refinement
starts from these six; the file records a layer widened or added
(§2.2):

1. the conventions manual, `docs/conventions/conventions/`, which
   every other manual is read against;
2. project-recording, with the map of the records, which other
   text points to;
3. the other manuals, and the concept chapters;
4. `ARCHITECTURE.md`, `README.md` and the records;
5. our skills and rules, under `.claude/`;
6. `delivery/`, what ships.

### 2.6 Decide

The reviewer sees the round's whole list before any finding is
decided (`.claude/rules/foundation-check.md`, step 4). Each finding
then gets one ending:

- **fixed**, and its line names the commit;
- **declined**, with the reason;
- **moved** to a TODO item.

A finding is never deleted or renumbered while the file lives.

### 2.7 Work

One layer's findings at a time, in §2.5's order, each a commit plan
(`docs/conventions/commit-plan/`). A source comes before what
derives from it, so a fix is carried down once and never redone.
A commit that touches a description goes through the foundation
check.

A fact told in several layers is fixed with its home's layer.
Its other copies become pointers in the same commit plan: a
deletion, not a rewrite, so the order holds.

### 2.8 A round's close

Every finding of the round has its ending. Then all the text the
round covers is read again against the round's kinds, held to
§2.4's rule for a finding. Reading only the changed text is not
enough: a fix in one file can make an unchanged line in another
wrong. What the read finds is listed and decided like any finding,
and the round's section counts:

- findings in text the round changed, and in text it did not;
- how many the reviewer took, and how many were declined as taste.

Then the next round reads.

### 2.9 The last read

After the last round, everything is read against every kind of
the refinement. It catches a later round breaking an earlier one's
work: a reworded line no longer true, a pointer reworded wrong.

The kinds are read on their own, as in §2.4, but in one read, with
no fixes between them. The order of the rounds is for fixes, not
for reads: with nothing changing, a read gives the same result in
any order.

What it finds is put in rounds by §2.1's rule and fixed in that
order, a round only where a finding needs one. Then everything is read
again, until a read finds nothing that breaks a rule. §2.4's rule
for a finding is what makes this end.

### 2.10 The close

The file goes in a commit of its own, and the devlog names that
commit, so the file can be read from git.

## 3. Not known yet

- **Whether the order holds:** the first round tests §2.5's
  layers; the last, whether the rounds were worth their reads.
- **Text another TODO item already plans to rewrite:** read here,
  or left to that item. On 2026-10-19 the reviewer had the writing
  kind read the method's texts, which TODO's plain-rewrite item
  covers. The refinement's close weighs what that item still
  needs, and whether one pass was the better way.
- **Whether a refinement comes again,** and what makes one due: a
  new rule, or a count of rules since the last.
- **Whether the refinement's file needs a shape.** It borrows the
  eval's form, which borrowed a reading's.
- **Whether the three rounds hold.** They were drawn from one
  refinement's eight kinds. Adding missing text is the first that
  may not fit.
- **Whether one layer's findings fit one commit plan.**
- **"Stage" in `ARCHITECTURE.md`'s *The words*** is one phase of a
  skill. This page uses it for its own phases. The close widens
  that definition, or this page takes another word.
- **Whether the full reads again paid.** The counts of findings in
  unchanged text decide whether a narrower read would have done.

## Why it arrives this way

A manual on trial, by `docs/conventions/first-time-work/`. A skill
written before the work would describe a guess. The work corrects
this page as it goes, and the close chooses its lasting form.

## What this does not cover

- **Checking one change at its commit** —
  `.claude/rules/foundation-check.md`.
- **Reading a run** — `docs/conventions/exchange/` §6, and
  `.claude/rules/working-a-reading.md`.
- **How text reads, and where a fact lives** —
  `.claude/rules/writing.md`, `.claude/rules/one-home.md`.
- **How the work's commits are planned** —
  `docs/conventions/commit-plan/`.

## Where to look

- `docs/conventions/first-time-work/`
- `19f1d7b^:temp/eval-2026-09-30.md`, the eval, in git
