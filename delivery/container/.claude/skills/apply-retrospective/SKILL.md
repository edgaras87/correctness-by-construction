---
name: apply-retrospective
description: Apply a finished retrospective to the run it looked back on, before Release. Use when RETRO.md is closed and the reviewer asks to apply it to this run, or to "fix the records before Release". Do NOT use to decide what the next run does differently (that is retrospective), or to add new proof.
requires: commit-messages, commit-plan
foundation: the retrospective convention
---

# Apply the retrospective

The retrospective decided and changed nothing. This step applies it
to the run itself, before Release, so the run is not released while
its records read worse than they have to. What the run proved does
not change.

The reviewer decides everything. The agent reads, proposes, builds
and checks.

## 0. Open

1. **Cut a branch** from main, and ask the reviewer whether small
   commits are free on it.
2. **Open a PLAN step,** its gate written before any work. Its own
   items come from the goal: every decision has a row; every
   applied row names its commits; the run's proof unchanged (where
   the project has tests: green, as many as at the last close);
   history untouched; the records later steps were built on changed
   only by dated revision entries; each delivered copy edited has
   its log entry and its hand-off line; what trying taught is
   written back.

## 1. Triage

1. **One decision at a time.** For each, propose: **applied**,
   **partly** (and which part), or **next run only**, with a reason
   and a size (words, lines, counts of links).
2. **Read before claiming.** A suspected gap is checked in the files
   before it is shown.
3. **Rows go into RETRO.md,** under "Applied to <run>", one row each,
   committed as the reviewer agrees.
4. **A question can become a new decision,** written in the note's
   form, with its own row. **A row can change an earlier decision**
   (the decision gets a dated line) **or an earlier row.**

**How a row is decided:**
- **Apply here** what improves what the run hands over without
  changing what it proved: a plainer sentence, a fact kept once and
  linked.
- **Next run only** what changes how a step runs: the run's steps are
  closed.
- **Never** history: devlog entries, closed ADRs, closed gates,
  released CHANGELOG versions, migrations, comments included.
- **The records later steps were built on** change only by a dated
  revision entry.
- **Signed text a reader still uses,** such as a slice record, may
  change, with one sign-off line naming the commit where the signed
  text is.
- **New proof is not this step's.** A gap found here is listed, and
  the reviewer decides whether it earns a step of its own.
- **Delivered copies** may be edited under the delivered-copies rule;
  a copy this run has finished with is marked untried.

## 2. Commit plan

Built from the applied rows and their sizes, under `commit-plan`.
The reviewer approves it before any change. Order the commits by
influence:
- remove repeats before rewriting, so nothing is polished and then
  deleted;
- regroup before rewriting; fix tags before the words around them;
- move a fact to its home before its copy goes;
- **owners before summaries:** a record that summarizes others comes
  after them, README last;
- plain words last.

## 3. Build

One planned commit at a time, staged and shown, committed on the
reviewer's word. Small fix-ups to a commit already made are their
own small commits.

- **A move is checked by a script,** not by reading: the same lines
  before and after. A move commit changes no words.
- **Links point at labels,** never section numbers: "SLICE-4
  GUARANTEE-2", not "§8".
- **The records check,** every link, path and cited number exists,
  runs before the build, after anything that moves files, and at
  the close.

**The plain pass,** where the triage applies one:
1. **Pass 1, one commit per record, owners first.** Rewrite only the
   paragraphs that fail the writing rule or tell a fact outside its
   home. Then a **fresh reader** with no part in the rewrite checks
   the before and after: meaning lost, the writing rule, home. A
   second fresh read if the fixes were more than a few, never a
   third. Show the reviewer the changes, what each read found, and
   what was skipped as taste.
2. **Pass 2, every record again, same order, no rewriting.** Fresh
   readers read each record against the revised records it links
   or summarizes, and report only mismatches. It takes in the
   cross-record checks: the records check, stale "now / today / not
   yet" lines, coined words missing from the project's glossary. One
   commit per record that changes.
3. **The stop rule.** If pass 2 changed only small things, the pass
   ends. If it changed something real, pass 3 runs over those
   records only, and the pass ends there.

**A tool that edits text** (a rewrap, a replace) is checked on what
it must not touch: front matter, code blocks, headings, dated
history lines.

## 4. Close

1. **The checks:** the records check; history untouched on the
   branch; `temp/` checked; where the project has tests, the full
   suite, with as many tests as at the last close, counted from this
   run's reports only.
2. **The shape reading.** What the step produced is read against
   every shape that governs it. Each difference is shown with its
   two lines and a recommended ending from the shapes rule, grouped
   into a few decisions for the reviewer. Records closed before a
   shape changed are named, not reopened.
3. **The skills this step taught,** each edited under the
   delivered-copies rule with its log entry: `commit-plan` from how
   the plan ran, and this skill from how the step ran.
4. **RETRO.md:** each row names its commits; what trying a decision
   taught is written back, dated, on the decision.
5. **TODO's hand-off:** one line per delivered copy edited, untried
   where the copy was finished; the step's triage of TODO's own
   items.
6. **The devlog entry and PLAN's close,** the gate ticked.
7. **The look back.** See the landed commits as a whole and propose
   a regroup by kind, agent files apart from project files, every
   commit following commit-messages. On the reviewer's word: keep
   the small commits on `<branch>-detail`, land by fast-forward, and
   close the commit plan.

## Between sessions

PLAN's "Now:" line and the commit plan say where the step stands.
The branch's log against the commit plan says which commits landed.

---

## Decisions

- CBC ADR-0054 — the retrospective is a convention, its look and
  its apply step two skills, taken from never-oversold's
