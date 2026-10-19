# Redesign

**A redesign changes how the conventions are built, not only how
their text reads. It starts from the pains of keeping them up,
rethinks the conventions convention first, and carries a pattern
from it to each manual where one fits.**

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
`PLAN.md` closes with each pain answered, and the reviewer judges
whether the pattern made the manuals easier to keep up. Look again
at that step's close.

## What this is made usable as

Nothing yet: the close decides (`docs/conventions/first-time-work/`
§3). While a redesign is open, a repo holds:

- **its step in `PLAN.md`**, whose Notes list this page's stages;
- **its file, `temp/redesign-<date>.md`**, deleted at the close.

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
- **pattern** — the parts and links that every manual has in the
  same way, so a maintainer finds the same thing in the same place
  in each.
- **the conventions convention** — `docs/conventions/conventions/`,
  the manual that says how every manual is written. Each other
  manual is read against it.

## 2. The stages

A map of the stages. Each section holds its rule.

| Stage | Does | The redesign's file |
|---|---|---|
| 2.1 List the pains | each pain, with its case | created, with the pains |
| 2.2 Rethink the conventions convention | an answer for each pain | each pain's answer |
| 2.3 Seek the pattern | every other manual read against it | each manual: follows, a variant, or its own |
| 2.4 Carry it to each manual | one manual at a time | each manual's change |
| 2.5 The close | what the stopped work must reread | the manuals changed; deleted |

The file is data; this page says how it is made.

### 2.1 List the pains

The pains come from work that exists: the session that asked for
the redesign, TODO items about how a convention is built, and
findings from readings. Each is written with its case. The
reviewer confirms the list before anything changes.

### 2.2 Rethink the conventions convention

For each pain, the conventions convention gets a rule that
prevents it, or a reason it stays. Its manual changes, and the
foundation check carries each change to what derives from it: its
rules and the index. The reviewer signs the new manual before any
other manual follows it.

### 2.3 Seek the pattern

Every other manual is read against the new conventions convention.
The file records, for each, which of its parts and links match,
and which differ. A difference ends one of three ways:

1. **the pattern:** the manual changes to it;
2. **a variant:** the pattern names it, for manuals that need it;
3. **its own:** the manual keeps it, and the file says why.

### 2.4 Carry it to each manual

One manual at a time, sources before what derives from them, in
the refinement's order of layers
(`docs/conventions/refinement/` §2.5). Each manual's change is a
commit plan of its own when it needs more than one commit, and
walks to what derives from it, in both seats.

### 2.5 The close

The file lists every manual the redesign changed, so work it
stopped knows what to read again. Then the file goes, in a commit
of its own, and the devlog names that commit.

## 3. Not known yet

- **The order of 2.2 and 2.3.** A form is written from work that
  exists (`docs/conventions/shapes/` §1), and the form of a manual
  was not designed: two manuals grew it
  (`docs/conventions/conventions/` §3.3). Reading the manuals first
  would draw the pattern from what they share. Rethinking the
  conventions convention first starts from the pains. The reviewer
  chose the conventions convention first; the first manual read in
  2.3 tests the choice.
- **Whether a pain needs a form** of its own, beyond its case.
- **How big one manual's change is.**
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
