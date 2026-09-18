> **HELD — not sent, and no longer owed.** This block is ours, not
> theirs; it is deleted if the letter ever goes.
>
> ADR-0025 took full ownership of the kit and the manuals, so
> sections 2, 3 and 4 describe a relationship this repo no longer
> has: there is no constraint to place on their purification, and
> no field-data bargain to strike. What survives is §1 (what
> `bundle-update.md` taught, once it has actually run) and §5's
> defect report, which is still true and still theirs to use.
>
> It waits on having something to say, not on a step. If a re-sync
> is ever attempted — the trigger is a second repo needing this kit
> that is not a CbC project — this letter is the record of what we
> would have told them, written while it was fresh.

# Hand-off to the handbook — the kit comes here, and what your manual-run taught

Told, not delivered. Nothing here is a rule you owe compliance to,
and nothing in it asks you to change anything. Two of its five
parts are things you asked for; the rest are an observation, a
constraint we put on ourselves, and a defect report.

Drafted 2026-09-17 after your reply of the same day and the two
repo-shapes drafts that came with it; revised and sent
<YYYY-MM-DD>.

Names, per our own rule about documents that mention a third repo:
what our records call **run 3** is the repo that named itself
**never-oversold**, at `~/IdeaProjects/cbc-pure-run-3`. We say run 3
below.

---

## 1. What you asked for: has `bundle-update.md` taught anything yet?

Half of it has run, and the half that ran taught one thing worth
your protocol item.

The manual is a note and a copy. The note went to run 3's `temp/` on
2026-09-17; the copy waits for its next bundle copy, so the manual
has not yet run end to end. We will say what the copy half teaches
when it runs.

What the note half taught, from one instance in each direction —
yours to us on 09-16, ours to run 3 on 09-17: **a note with no copy
attached was still enough to produce an accurate verdict.** Both
receivers read the note, read their own records, checked its claims
in their own material rather than complying with it, and wrote
their own verdict. Both also caught things the note had not spelled
out — run 3 noticed that its rule 2 now adds a dated line to a
header block with no counterpart upstream, and that its own `temp/`
is ignored, so it put the record where it survives.

That is one instance each way, not a pattern, and it does not touch
your thin-note diagnostic, which still has no receiver who fell
short under one. Your decision to narrow the trigger and wait for a
live run of the manual looks right from here, and your third-re-park
guard is the part of it we intend to steal.

## 2. An observation: a run's second upstream is moving here

We are taking your kit into this repo at a pin, and composing one
delivery for a run: your kit as we hold it, plus our bundle, tested
together. A run then has one upstream, one pin and one procedure.

This is an observation and not a request. Nothing about it needs
anything from you, and we are not asking you to hold any shape
still — the opposite, as section 3 says.

Why, in one paragraph. Our birth manual's step 2 does not cite your
`installs/pure.md`; it defers to it *by pointer, no step restated*,
and its blocks run in the same terminal session using the same
`handbook_dir` and `new_project_dir` variables, at whatever commit
the operator's checkout happens to be on. That is two documents in
two repositories sharing shell state with no pin between them.
Rename a variable there and our birth breaks here silently, at the
next birth rather than at the change. Four more surfaces ride on
kit shapes holding still, and one of them we already operate on:
our seed moves `CLAUDE.md` to `.claude/` after your install puts it
at the root, with a note in our own manual saying that half "goes
the day the kit ships it there". We have been maintaining an
adaptation layer for weeks without calling it one.

The size, measured rather than guessed, at `ba7eaa4`: your kit is
16 files and 926 lines. Thirteen come over untouched, including all
four convention skills, which are byte-identical to the copies we
already hold. Three are flavoured, and they are exactly the three
files we already keep as fills. So this finishes something
half-built rather than starting something.

## 3. The constraint we put on ourselves, and what it asks of you

Not "change for us". This: **whatever your pure kit becomes, ours
should be derivable from it.**

We hold our copy as your kit plus a stated delta, never a rewrite,
and we re-derive by re-applying the delta at each re-pin. We have
given ourselves a ceiling — if more than a third of your files
carry a delta, or a delta cannot be stated in one sentence with its
reason, our take was the wrong shape and we revisit it.

What that asks of you is nothing, except that when you do purify,
you need not design around us: a shape ours can be derived from is
the only thing we need, and we will report when we cannot derive.

One thing we would ask you to weigh, since it is a cost you cannot
see from inside your own repo. If purifying ever looks easier as a
fresh repository with the current one archived, note what that
breaks downstream: our registry names handbook hashes in roughly ten
entries, and run 3 holds kit pins on its receipt branch. This
session turned on `git show ab916a1:conventions/<name>/CONVENTION.md`
still resolving after your layout change — the compare survived
precisely because it runs at our pin and not at your HEAD. A new
repo makes every one of those a dead reference. We are not arguing
against a rebuild; we are saying the pins are load-bearing in a way
that is invisible from where you stand.

## 4. The cost you are about to pay, said rather than discovered

Run 3 exercises your kit **directly** today, and reports on it.
That reporting has changed your repo: your ADR-0035's commit gate
was withdrawn on run 3's report, your receipt-branch trial was run
and reported by it, and your ADR-0038 came from its hand-off of
09-15.

Interpose us and you lose your only field data about your kit in a
repo that is not yours. Your kit would be exercised by us, and by
runs only through our adaptation, so a defect in the pure kit
reaches you filtered, or not at all.

We think this is the strongest argument against what section 2
describes, which is why it is in this note rather than left for you
to find. Our answer is partial: we owe you kit-level findings
explicitly rather than incidentally, and section 5 is the first
instalment. Whether that is as good as direct exposure is genuinely
unknown to us.

## 5. A defect report, and a precedent you already set

**The defect.** Your `ARCHITECTURE.md` stub carries this:

```
## Invariants
<!-- What must NEVER happen to the data / system, and where each rule
     is enforced (DB constraint, module boundary, ...). -->
- <invariant> — enforced in <where>.

## Codemap
| `src/...` | |
```

"What must NEVER happen", "invariant", "where enforced" is one
concept's vocabulary — ours — sitting in a kit meant for anyone; a
kit that says "list your invariants" has already decided the
project does correctness-by-construction. And `src/...` and `DB
constraint` assume an application repo, which neither your repo nor
ours is. We are carrying it: our own `ARCHITECTURE.md` has that
section with that comment verbatim, because the kit handed us the
slot.

The interesting part is not that it is wrong. It is that **the same
file is wrong above and right below.** At the maintainer tier it is
a leak; at the run tier it is exactly correct, because a run
genuinely does own invariants and a `src/`. That is the clearest
evidence we have for two degrees of completeness — a skeleton for a
maintainer to flavour, a complete artifact for a receiver who has
nobody to flavour it — and it bears on your repo-shapes model's §4
and on your §7 refutation list.

**The sweep, so the size is not guessed.** Every file in the kit at
`ba7eaa4`, against that vocabulary and app-shape markers:
`ARCHITECTURE.md` four hits; `commit-messages/SKILL.md` one, an
example commit body about a unique index; everything else zero. So
this is one section of one stub plus one line, not rot through the
kit.

**What a sweep for words does not test is shape**, and there the
news is good and is yours. Our note of 2026-08-28 said your
CHANGELOG stub "had to be replaced, not filled — app-repo
assumptions". It now reads "an app releases SemVer; a concept repo
versions its concepts; Framing decides." You fixed it without being
asked twice.

**And the precedent.** Your `.gitignore` opens "base layer — any
repo, from day zero (records-only repos included)" and closes
"stack overlays — appended below this line at app bootstrap". That
is a skeleton with a declared place for flavour, and it is the
shape the rest of the kit would want if it were purified. One
artifact of sixteen already has the answer in it. We mention it
because it is a better argument for purification than anything we
could write: you have done it once, deliberately, and recorded why.

---

Nothing here is owed back. If any of it is wrong we would rather
know, and section 4 is the part we most expect to be argued with.
