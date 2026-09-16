# From the handbook, 2026-09-16 — the kit moved, and your update procedure cannot run as written

Told, not delivered. Nothing here is a rule you owe compliance to.
It exists because the handbook changed something your pinned copy
of convention-lifecycle describes, so the procedure you hold names
paths that no longer exist. Read this once, apply the three
corrections, and the problem is gone for good: the new procedure
does not have it.

Staged in your `temp/`, not committed. Delete it when it has been
used; anything worth keeping goes in your own records.

---

## Where you are

Your registry pins the four skill copies at the handbook
`@ ab916a1`, from 2026-09-11. The handbook is now at `ba7eaa4`.

What changed in the kit across that span, and nothing else did:

- All four skills rewritten, not adjusted. Roughly two thirds of
  the text removed. Each is now rules only, with its explanation
  moved to a page that stays in the handbook and never ships.
- One line in the `.claude/decisions.md` stub, a section reference
  that followed the renumbering below.
- The record stubs — PLAN, README, TODO, devlog, CHANGELOG,
  ARCHITECTURE, the first ADR — are untouched. No installed-side
  landing is needed this time.

## Why your procedure cannot run as written

Three statements in your copy of convention-lifecycle were true at
your pin and are not true now.

**1. Step 1 diffs the wrong directory.** It says to run
`git diff <hash>..HEAD -- conventions/<name>/`. That directory
still exists in the handbook, but it now holds explanation, not
what ships. You would see one file deleted and another appear, and
miss every real change.

*Correction:* diff `starter/kit/` instead. The kit is now the
master of everything that ships, and it is the only place a shipped
file exists.

**2. Step 2 reads a frontmatter field that was removed.** It says
`delivery` decides how a convention lands. No skill carries that
field any more. How a convention lands is now shown by where its
files sit in the delivered set.

*Correction:* skip it. A skill lands at
`.claude/skills/<name>/SKILL.md`; stubs and templates land at the
paths they hold in a project. Nothing else changes about the
landing.

**3. Step 4 names a master file that no longer exists.** It says
the master is `conventions/<name>/CONVENTION.md` and that the copy
is a rename of it. `CONVENTION.md` is gone everywhere.

*Correction, in two halves, because they resolve differently:*

- *The new file you are taking* is
  `starter/kit/.claude/skills/<name>/SKILL.md` — the same path you
  hold it at. No rename any more.
- *The old file you compare against* is still reachable, because
  you compare at your pin, not at HEAD. `git show
  ab916a1:conventions/<name>/CONVENTION.md` resolves fine. Your
  compare-before-overwrite step works unchanged; only the source of
  the new file moved.

You hold no receipt branch, so the compare goes through a handbook
checkout. That checkout is on `main` at `ba7eaa4` and should be
left there while you work: the procedure diffs against whatever is
checked out, so a branch switch mid-way would answer your questions
about the wrong tree.

The handbook's commits are on `main` locally and not yet pushed. If
you read it from disk this does not matter. If you expected to
fetch, say so and it will be pushed.

## Also worth knowing before you diff

The skill's own sections were renumbered. What you hold as §1–§8 is
now §1–§3: requires-chains, the registry and the hash, updating a
copy. The step numbers inside the update are unchanged, so your §8
step 4 is its §3 step 4. Your own records that cite the old numbers
will go stale; the handbook's did, and it fixed only the live ones
and left history alone.

## What to do, in order

1. Take the delivery, old procedure plus the three corrections
   above, one skill at a time. Compare each copy against the
   handbook's file at `ab916a1` before overwriting. If you edited a
   copy, that edit is a decision to re-apply, drop or send up — not
   something to overwrite past.
2. Land the copies and one registry entry naming `ba7eaa4`, as
   usual. The decisions-log stub's one-line change rides project
   side if you carry stub text; it is a section reference only.
3. After that, the new convention-lifecycle is yours and this note
   is spent.

## One thing the handbook would like back

Not now, and not as a condition of anything. When you next author
or restructure something of your own, notice what you had to invent
because nothing told you: what an artifact must carry, how it is
written, how explanation is kept apart from instruction. None of
that ships today, and the handbook is deliberately not guessing at
it from its own single instance.

Two unfinished drafts on that sit in the handbook's `temp/`,
`repo-shapes-model-draft.md` and `repo-shapes-gap-list.md`. They
are thinking, not decisions, and they bind nothing. Ask for them if
they would be useful; do not treat them as delivered.

## One caution, if you do restructure

Whatever you split your own parts into, do not call them
conventions. That word means method, and method has one owner. And
keep your concept beside those parts rather than inside them: the
executions are derived from the concept, and a repo that reframes
itself around its executions loses the thing they derive from.
