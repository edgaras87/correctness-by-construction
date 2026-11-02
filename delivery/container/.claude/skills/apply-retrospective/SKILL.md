---
name: apply-retrospective
description: Apply a finished retrospective to the CBC Run it looked back on, before Release. Use when RETRO.md is closed and the reviewer asks to apply it to this CBC Run, or to "fix the records before Release". Do NOT use to decide what the next CBC Run does differently (that is the retrospective Agent Skill), or to add new proof.
foundation: the retrospective convention
---

# Apply the retrospective

This Plan Step applies the finished retrospective to the CBC Run
itself, before Release, so the CBC Run is not released while its
records read worse than they have to. The retrospective decided and
changed nothing. What the CBC Run proved does
not change.

The reviewer decides everything. The agent reads, proposes, builds
and checks.

## Stage 0 — open

1. **Cut a branch** from main, and ask the reviewer whether small
   commits are free on it.
2. **Open a Plan Step,** its Plan Step Gate written before any work.
   Its own items come from the goal:
   - every decision has a row;
   - every applied row names its commits;
   - the CBC Run's proof is unchanged (where the project has tests:
     green, as many as at the last close);
   - history is untouched;
   - the records later Plan Steps were built on changed only by
     dated revision entries;
   - each delivered copy edited has its Decisions Log entry and its
     CBC Run Ask;
   - what trying taught is written back.

## Stage 1 — triage

1. **One decision at a time.** For each, propose: **applied**,
   **partly** (and which part), or **next CBC Run only**, with a reason
   and a size (words, lines, counts of links).
2. **Read before claiming.** A suspected gap is checked in the files
   before it is shown.
3. **Rows go into RETRO.md,** under "Applied to <run>", one row each,
   committed as the reviewer agrees.
4. **A question can become a new decision,** written in RETRO.md's
   decision form, with its own row. **A row can change an earlier decision**
   (the decision gets a dated line) **or an earlier row.**

**How a row is decided:**
- **Applied:** what improves what the CBC Run hands over without
  changing what it proved: a plainer sentence, a fact kept once and
  linked.
- **Next CBC Run only:** what changes how a Plan Step runs: the CBC Run's Plan Steps are
  closed.
- **Never** history (`.claude/rules/one-home.md`, *Not a second home*),
  and with it closed Plan Step Gates and migrations.
- **The records later Plan Steps were built on** change only by a dated
  revision entry.
- **Signed text a reader still uses,** such as an Invariant Slice Record, may
  change, with one sign-off line naming the commit where the signed
  text is.
- **New proof is not this Plan Step's.** A gap found here is listed, and
  the reviewer decides whether it earns a Plan Step of its own.
- **Delivered copies** may be edited under the delivered-copies Agent Rule
  (`.claude/rules/delivered-copies.md`, rule 2, *A copy may be edited in place…*);
  a copy this CBC Run has finished with is marked untried.

## Stage 2 — commit plan

Built from the applied rows and their sizes, under the commit-plan Agent Skill.
The reviewer approves it before any change. Order the commits by
influence:
- remove repeats before rewriting, so nothing is polished and then
  deleted;
- regroup before rewriting;
- fix tags before the words around them;
- move a fact to its home before its copy goes;
- **owners before summaries:** a record that summarizes others comes
  after them, README last;
- plain words last.

## Stage 3 — build

One planned commit at a time, staged and shown, committed on the
reviewer's word. Small fix-ups to a commit already made are their
own small commits.

- **A move is checked by a script,** not by reading: the same lines
  before and after. A move commit changes no words.
- **Links carry a label,** and where there is one, its section
  number and title: "SLICE-4 GUARANTEE-2", never a bare "§8".
- **The records check,** the Plan Step Form's closing item on
  links, paths and pairs of copies, runs before the build, after
  anything that moves files, and at the close.

**The plain pass,** where the triage applies one:
1. **Pass 1, one commit per record, owners first.** Rewrite only the
   paragraphs that fail the writing rule or tell a fact outside its
   home. Then a fresh reader with no part in the rewrite checks
   the before and after: whether meaning was lost, whether the writing rule is met, whether each fact is at its home. A
   second fresh read if the fixes were more than five, never a
   third. Show the reviewer the changes, what each read found, and
   what was skipped as taste.
2. **Pass 2, every record again, same order, no rewriting.** Fresh
   readers read each record against the revised records it links
   or summarizes, and report only mismatches. It takes in the
   cross-record checks: the records check, stale "now / today / not
   yet" lines, Glossary Names missing from the project's glossary. One
   commit per record that changes.
3. **The stop rule.** If pass 2 changed only wording, the pass
   ends. If it changed a fact, pass 3 runs over those
   records only, and the pass ends there.

**A tool that edits text** (a replace, a move) is checked on what
it must not touch: front matter, code blocks, headings, dated
history lines.

## Stage 4 — close

1. **The checks:**
   - the records check;
   - history untouched on the branch;
   - `temp/` checked;
   - where the project has tests, the full suite, with as many tests
     as at the last close, counted from this CBC Run's reports only.
2. **The Output Shape reading.** What the Plan Step produced is read against
   every Output Shape that governs it. Each difference is shown with its
   two lines and a recommended ending from the shapes-lifecycle Agent Rule
   (`.claude/rules/shapes-lifecycle.md` §3, *A difference at the close*), grouped
   into a few decisions for the reviewer. Records closed before an
   Output Shape changed are named, not reopened.
3. **The Agent Skills this Plan Step taught,** each edited under the
   delivered-copies Agent Rule (`.claude/rules/delivered-copies.md`, rule 2, *A copy may be edited in place…*) with its Decisions Log entry: the commit-plan Agent Skill from how
   the plan ran, and this Agent Skill from how the Plan Step ran.
4. **RETRO.md:** each row names its commits; what trying a decision
   taught is written back, dated, on the decision.
5. **TODO's CBC Run Asks:** one line per delivered copy edited, untried
   where the copy was finished; the Plan Step's triage of TODO's own
   items.
6. **The devlog entry and PLAN's close,** the Plan Step Gate ticked.
7. **Land it.** The closing look at the landed commits, and the
   `-detail` branch that keeps what was tried, are the commit-plan Agent Skill's
   (`.claude/skills/commit-plan/SKILL.md` §4, *The lifecycle*, and §6.2, *Small commits*). The branch
   reaches main by fast-forward, on the reviewer's word (`PLAN.md`,
   *The Plan Step Form*, *At the close*), and the commit plan closes.

## Between sessions

PLAN's "Now:" line and the commit plan say where the Plan Step stands.
The branch's log against the commit plan says which commits landed.

---

## Decisions

- ADR-0054 — the retrospective is a convention, its look and
  its apply step two Agent Skills, taken from CBC Run 3's
