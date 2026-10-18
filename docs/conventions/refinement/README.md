# Refinement

**A refinement brings text written before a rule up to that rule.
It reads first and lists what it finds. Nothing changes until the
reviewer has ended each finding, and then the text is fixed one
group at a time.**

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
groups, and ended every one. Its file is in git at
`19f1d7b^:temp/eval-2026-09-30.md`.

*On trial.* What would make it evidence: the refinement step in
`PLAN.md` closes with every finding ended, and the reviewer judges
whether reading first, then fixing in groups, held. Look again at
that step's close.

## What this is made usable as

Nothing yet: the close decides (`docs/conventions/first-time-work/`
§3). While a refinement is open, a repo holds:

- **its step in `PLAN.md`**, whose Notes list this page's stages;
- **its findings file in `temp/`**, deleted at the close.

What derives from this page is that list. A change here walks it.

## The seats

No seat in a run, for now. This is first-time work of this repo
alone, so its trial is our own next refinement. A run that finds it
needs one offers it under *To the deliverer*. The rest of this page
is the deliverer's.

## 1. What it reads

Living text: every file but history. History is the devlog, closed
ADRs and commit bodies (`.claude/rules/one-home.md`). Also left
out:

- `docs/baselines/`, frozen on purpose;
- a run's own text in `temp/`, which its reading reads.

Each refinement names the rules it reads against. Each rule is one
kind of finding. This one's eight kinds:

| Kind | What a finding is | The rule |
|---|---|---|
| Dependencies | a retelling where a pointer would do | `docs/conventions/conventions/` §3.1 |
| Seats | a deliverer seat that says more than how its convention works here | `docs/conventions/conventions/` §3.4 |
| Writing | text older than ADR-0053, against the whole rule | `.claude/rules/writing.md` |
| Stale lines | a line no longer true | `PLAN.md`, the step form's close |
| One home | a fact told in more than one place | `.claude/rules/one-home.md` |
| Foundations | a `foundation` line that disagrees with its manual | `.claude/rules/foundation-check.md` |
| Lessons | a case written as the rule | `docs/conventions/conventions/` §3.7 |
| Words | "run" as a verb for a skill or a step; "small steps" in `commit-plan` | `.claude/rules/writing.md`, rule 6 |

## 2. The stages

### 2.1 Scope

The reviewer confirms the kinds and the areas. The agent lists
each area's files with their counts, so the read can show it
covered them.

### 2.2 Read

Each file is read whole, against every kind. One home and words
also need a sweep across files, since one file alone cannot show
them.

A reader's finding is checked against the tree before it is
listed. Each finding says how it stands: checked, resting on the
reader, or uncertain.

*Lived 2026-09-30, in the eval: six readers, one area each, and
every finding checked against the tree before it was listed. A
section two readers called wrong and right became one finding.*

### 2.3 List

The findings go into one file, `temp/refinement-<date>.md`. Each
finding is FINDING-n, and says:

- where: the path, and lines;
- what the rule says, and what the text says;
- how it stands, as in §2.2.

A finding that needs the reviewer's choice beyond "fix it" gets a
DECISION-n: the options, a recommendation, and the findings that
rest on it.

Findings are grouped by the files they edit, so one group's work
touches one set of files.

### 2.4 Decide

The reviewer sees the whole list before any finding is decided
(`.claude/rules/foundation-check.md`, step 4). Each finding then
gets one ending:

- **fixed**, and its line names the commit;
- **declined**, with the reason;
- **moved** to a TODO item.

A finding is never deleted or renumbered while the file lives.

### 2.5 Work

One group at a time, each a commit plan
(`docs/conventions/commit-plan/`). A commit
that touches a description goes through the foundation check.

### 2.6 Close

Every finding has its ending. The file goes in a commit of its
own, and the devlog names that commit, so the file can be read
from git.

## 3. Not known yet

- **The order of the read:** file by file against every kind, or
  kind by kind across all files.
- **The method's texts:** `delivery/method/`,
  `delivery/spring-postgres/` and `concept/` have a plain rewrite
  of their own in TODO, due before run 5's birth. Whether the
  writing kind reads them here, or leaves them to it.
- **Whether a refinement comes again,** and what makes one due: a
  new rule, or a count of rules since the last.
- **Whether the findings file needs a shape.** It borrows the
  eval's form, which borrowed a reading's.
- **How big a group is.**

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
