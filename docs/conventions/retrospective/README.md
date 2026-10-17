# Retrospective

**A finished run looks back in two steps: first it decides what the
next run does differently, changing nothing; then it applies those
lessons to its own records, before Release, without changing what
it proved.**

## What it is for

So that what a run learned reaches the next run, written down with
an example and a place to land. The failure is lived, in run 3,
never-oversold. Its plan ended on a section, "Retrospective (fill at
project end)", with a few questions. Run 3 stopped before Release,
so the section's moment never came; the retrospective happened only
because the reviewer asked for one. It then did far more than the
section asked, and none of that was written down as a way of
working (its RETRO.md, D23):

- **It walked the run part by part,** in the order the run built
  them, and backed each finding with a quoted line or a count.
- **It decided one thing at a time,** each decision with what was
  rejected and where it lands.
- **It looked and changed nothing.** A step after it applied the
  lessons to run 3's own records before Release, and left what run
  3 had proved alone (D24).

Run 3 kept both as skills, and offered them. Taken on 2026-10-15
(ADR-0054).

## What this is made usable as

- **`delivery/container/.claude/skills/retrospective/SKILL.md` —
  the skill, shipped**, held at `.claude/skills/retrospective/` and
  opened when the run has finished building, before Release.
- **`delivery/container/.claude/skills/apply-retrospective/SKILL.md`
  — the skill, shipped**, held at `.claude/skills/apply-retrospective/`
  and opened when `RETRO.md` is closed, before Release.

The deliverer holds neither; its seat is on trial (below). This page
explains; the skills state. What derives from this page is that
list. A change here walks it; a change forced in one of them is
checked back against this page.

## The seats

### The run's seat

Two people work it: the agent and the reviewer. The agent reads,
measures, proposes and writes; the reviewer decides. The skills
stop at each of the reviewer's decisions. In summary, and the skills
are the source:

- **In the look back, the reviewer decides** whether small commits
  are free on the branch; each decision: agree, correct, or drop;
  each experiment: keep or drop; when the branch lands. **They
  get** `RETRO.md`, with every decision, its example, what was
  rejected and where it lands; TODO's *To the deliverer* pointing at
  it; and the next run's checks, listed for its plan.
- **In the apply step, the reviewer decides** each triage row; each
  new decision the triage raises; the commit plan before any change;
  each planned commit at its boundary; each revision of the plan
  that changes what lands; when the branch lands. **They get** the
  run's records improved where the triage said so, and `RETRO.md`'s
  *Applied to* section: what happened to each decision.

No guide ships beside the skills: it would repeat them, and the two
would drift. Run 3's apply guide restated nearly every rule of its
skill. *Reopened if a reviewer works without reading this repo, or
run 4's reading shows the missing guide cost something.*

### The deliverer's seat

On trial. This repo has no project end; its steps close on
"lessons folded back where they came from", which names no place
and no method. At the close of the step that runs the next birth,
it runs both skills on itself, from `delivery/container/`, in place
of that item: the parts are its own (the concept, the conventions,
the delivery, the exchange, its records), and the next step stands
where a run has its next run. The trial's verdict says whether this
repo holds its own copies, and what this seat is.

## 1. Two steps, not one

Looking and changing are kept apart on purpose. A retrospective that
may fix what it finds starts fixing the first thing, and stops
looking. Run 3's reviewer kept the two apart, and the look stayed
clear. But run 3 would then have been released while its records
still read in ways the retrospective had shown could be better. So
a second step applies the lessons, before Release (run 3's D24).

Both come before Release, so they happen even when Release is
skipped. That is the failure of a section filled at the project's
end.

## 2. How the look back decides

- **Every finding has an example from the run:** a quoted line, a
  file and line number, a count. No example, no finding.
- **Every decision says where it lands,** and the place is one the
  next run starts from: a skill, a rule, the playbook, a template,
  the reviewer's local file. "Remember to" is not a place, and a
  lesson that lands nowhere is repeated.
- **No decision without something that went wrong.** In run 3, "one
  kind of text per document" was drafted and dropped: nothing had
  gone wrong to fix.
- **Choices are shown on real text.** In run 3 the tag names were
  picked from tables of variants applied to real lines.
- **The reviewer's corrections are kept.** The agent's first
  version goes under "Considered and rejected", with the reason.
- **The old questions still ask:** which steps took longer or
  shorter, what needed to happen earlier, what was tried and
  dropped, what had no home, which gate items caught nothing; and
  the entry file read top to bottom, its only re-reading
  (`docs/conventions/agent-arrangement/` §2.6). They came from the
  plan's old Retrospective section, which the skill replaced, and
  are prompts now, inside the walk.

## 3. How the apply step decides

- **Apply what improves what the run hands over, without changing
  what it proved:** a plainer sentence, a fact kept once and linked.
- **What changes how a step runs waits for the next run.** The
  run's steps are closed.
- **History is never touched,** and the records later steps were
  built on change only by a dated revision entry.
- **New proof is not this step's.** A new test was never seen fail.
  A gap found here is listed, and the reviewer decides whether it
  earns a step of its own.
- **The order of the commits follows influence.** Repeats go before
  rewriting, so no text is polished and then deleted. Owners go
  before the records that summarize them, README last. Plain words
  last.
- **A fresh reader checks each rewrite** against the old text. The
  writer reads what they meant, not what is on the page.

*Measured in run 3, 2026-10-12 to 10-15: 27 triage rows, 11
applied, 14 partly, 2 next run only. Three new decisions came up in
the triage, not the retrospective. A fresh reader caught a rewrite
of README that had dropped "and only" from "first and only". A
first count of the tests said 195 where the run had 100: the report
folder kept old files, so tests are counted from this run's reports
only. Sixteen commit subjects over 50 characters were found only at
the close. A rewrap joined a heading to its paragraph, so a tool
that edits text is checked on what it must not touch.*

## 4. `RETRO.md`

The look back's record, at the run's root, one per run. It holds
every decision, the experiments, what was parked, and, after the
apply step, a row per decision saying what happened to it. The
records table names its moment. It is history once the run is
released: the next run starts from where its decisions landed, not
from the note.

## Why it arrives this way

Two skills, because each step is bound to a moment the agent would
otherwise have to notice: the run finishing its building, and the
note closing. A plan step opens each, and names the skill.

A section in the plan did not work: its moment was the project's
end, which a run that stops early never reaches, and a section can
hold questions but not a way of working. Two skills, not one,
because one step must change nothing in the run and the other
exists to change its records.

## What this does not cover

- **The records a run keeps, and when each is opened** —
  `docs/conventions/project-recording/`.
- **How the apply step's commits are planned** —
  `docs/conventions/commit-plan/`.
- **What a shape is, and how a gate reads it** —
  `docs/conventions/shapes/`.
- **How a run edits a delivered copy, and hands it back** —
  `docs/conventions/exchange/` §5.
- **How a text reads** — `docs/conventions/writing/`.

## Where to look

- The decision: ADR-0054.
- Run 3's record of both steps: its `RETRO.md`, D23 and D24.
