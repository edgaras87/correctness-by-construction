# Conventions redesign

**A redesign changes how the conventions are built, not only how
their text reads. It records the designs it may aim at as targets,
then changes the manuals in small iterations, each judged before
the next, starting from the conventions convention.**

## What it is for

A refinement brings text up to the rules
(`docs/conventions/refinement/`). When the way the conventions are
built is what makes them hard to keep up, refining against it fixes
text that the same structure will break again. A redesign changes
the structure first.

The need was written down on 2026-10-19. The refinement of this
repo had read three manuals for its rule check, and the reviewer
judged the structure, not the text, to be the trouble. That
session had met six pains (devlog 2026-10-19, the refinement
stops). The refinement stopped so the redesign could come first.

*On trial.* What would make it evidence: the redesign step in
`PLAN.md` closes, and the reviewer judges whether its iterations
left the manuals easier to keep up, to read, and to change again.
Look again at that step's close.

## What this is made usable as

Nothing yet: the close decides (`docs/conventions/first-time-work/`
§3). While a redesign is open, a repo holds:

- **its step in `PLAN.md`**, whose Notes list this page's stages;
- **its file, `temp/conventions-redesign-<date>.md`**, deleted at
  the close.

What derives from this page is that list. A change here walks it.

## The seats

No seat in a run, for now. This is first-time work of this repo
alone, so its trial is our own next redesign. A run that finds it
needs one offers it under *To the deliverer*. The rest of this page
is the deliverer's.

## 1. Its words

- **pain** — a way the conventions make upkeep hard, seen in
  practice. It names its case: what happened, when, and the commit
  or record that shows it. A pain with no case is a guess, and is
  not listed.
- **target** — a design the redesign may move toward, written as
  possible, never promised. An iteration moves toward a target, or
  shows it wrong.
- **iteration** — one change to one manual, judged before the next.
  Not a step, which is `PLAN.md`'s, nor `commit-plan`'s small steps
  inside a commit.
- **the conventions convention** — `docs/conventions/conventions/`,
  the manual that says how every manual is written. The first
  iterations change it.

## 2. The stages

A map of the stages. Each section holds its rule.

| Stage | Does | The redesign's file |
|---|---|---|
| 2.1 Record the targets | each design discussed, as possible | the targets, and the pains as tests |
| 2.2 Plan the iterations | a rolling list: the next firm, later ones provisional | the iterations |
| 2.3 One iteration | one change to one manual, then judged | its verdict; the list updated |
| 2.4 Spread | a form that held, to the other manuals | each manual's iterations |
| 2.5 The pattern | a form held across manuals, written once, with its rule | the pattern |
| 2.6 The words | names weighed once the form holds | the words |
| 2.7 The close | what the stopped work must reread | the manuals changed; deleted |

The file is data; this page says how it is made.

### 2.1 Record the targets

Each design idea discussed is written in the file as a target: what
it would change, and why it might help. A target is not a
commitment. It can be changed or dropped when an iteration shows it
wrong. The pains are kept beside the targets, each with its case,
as tests an iteration can be held to.

### 2.2 Plan the iterations

The iterations are a rolling list in the file, as a commit plan's
list may roll (`docs/conventions/commit-plan/`). The next one is
firm; later ones are provisional, and each names the target it
moves toward. The list is updated after each iteration, from what
that iteration showed.

### 2.3 One iteration

One change to one manual, in a commit, or a commit plan when it
needs more than one, through the foundation check. Then the
reviewer judges it on three questions:

1. **Maintenance:** does a change to this subject now touch fewer
   places?
2. **Readability:** does a reader find the subject and its
   sub-ideas faster?
3. **Future-proofing:** does it move toward a target, or make one
   easier to reach later?

The pains it touches are checked too. The verdict is one of three:
kept, changed, or reverted with `git revert` on the branch. The
file records it, and the list is updated.

### 2.4 Spread

Once the conventions convention's form holds, the iterations that
held go to the other manuals, one manual at a time, project-
recording first. Sources come before what derives from them
(`docs/conventions/refinement/` §2.5).

### 2.5 The pattern

A form that held across manuals is written once, as a part of the
conventions convention, with a rule made from it for building a
manual: `.claude/rules/convention-manual.md` follows.

### 2.6 The words

Once the form holds, the names are weighed: whether a manual is a
"concept", and the rest. A word already in use for something else
is not reused (`.claude/rules/writing.md`, rule 6).

### 2.7 The close

The file lists every manual the redesign changed, so work it
stopped knows what to read again. Then the file goes, in a commit
of its own, and the devlog names that commit.

## 3. Not known yet

- **Whether starting from the conventions convention holds.** A
  form is written from work that exists
  (`docs/conventions/shapes/` §1), and the form of a manual was not
  designed: two manuals grew it (`docs/conventions/conventions/`
  §3.3). Project-recording, at 2.4, tests what the first manual
  showed.
- **Whether the iterations reach a design, or only polish.** The
  targets say where; the verdicts show whether the manuals moved.
- **How big one iteration is.**
- **Whether a pain needs a form** of its own, beyond its case.
- **Whether a redesign comes again,** and what makes one due.

## Why it arrives this way

A manual on trial, by `docs/conventions/first-time-work/`. A skill
written before the work would describe a guess. The work corrects
this page as it goes, and the close chooses its lasting form.

## What this does not cover

- **Bringing text up to the rules** —
  `docs/conventions/refinement/`.
- **How a manual is written, and what derives from it** —
  `docs/conventions/conventions/`.
- **Checking one change at its commit** —
  `.claude/rules/foundation-check.md`.
- **How the work's commits are planned** —
  `docs/conventions/commit-plan/`.

## Where to look

- `docs/conventions/first-time-work/`
- `docs/conventions/refinement/`, the work this one stopped
