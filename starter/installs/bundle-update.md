<!-- The bundle's update procedure, peer of pure-seed.md, which
     covers a run's birth and nothing after it. Authored 2026-09-17
     from the one lived case — run 3's re-pin to @ 7bbf49a on
     2026-09-15, which ran without a written procedure — and from
     ADR-0022, which decided what replaces the harvest lines the
     bundle's shipped files used to carry. Stays home: nothing in
     installs/ ships (ADR-0010). -->

# Install: the bundle update — a note and a copy

One idea: the run receives what changed and why, and decides for
itself. **What changed** is the files. **Why** is a note. Neither
substitutes for the other, and the run is handed no path to this
repo — what it needs to read is placed in its own `temp/`, so
there is nothing else within reach and nothing to forbid
(ADR-0022).

The run may have edited its copies since its pin. That is allowed,
under rules it keeps and logs, and it changes only one thing here:
the harvest reads a diff before the note is written.

Who does what: **this repo's agent** reads and writes the note;
**the operator** carries it and the files; **the run's agent**
evaluates, takes, and records. No agent reaches into another
repo's working tree.

---

**1. Set the paths and capture the pins.**

```bash
run_dir=~/IdeaProjects/<run-name>
bundle_dir=~/PycharmProjects/engineering/concept-garden/correctness-by-construction

new_pin=$(git -C "$bundle_dir" rev-parse --short HEAD)
# the run's current pin: the hash in its last bundle entry
grep -n "bundle updated @\|the five CbC skills, pin @" "$run_dir/.claude/decisions.md" | tail -2
```

The old pin is the run's, written in its own log. This repo does
not hold it.

**2. Read the run, then write the note.** (this repo's agent)

Read-only, and scoped: what the change touches, plus the records
around it — the step it lands in, the decisions log, the TODO. Not
the whole repo.

**One exception to the scoping, learned 2026-09-18.** When the
change renames or renumbers anything the run may have cited — a
section, a file, a rule — grep its whole tree for the old name
before writing, not only the records you expect it in. Our note of
that date named two stale `§8` citations and never-oversold found a
third, in its entry file, because we read its rules file and its
TODO and did not think to read its `CLAUDE.md`. A citation lives
wherever someone once needed it, and a diff cannot find it: the
stale text is in the run's own writing, not in the files it
receives.

If the run edited its copies, diff them against what it received,
using the run's own history, not ours:

```bash
git -C "$run_dir" diff <run's-delivery-commit> -- \
  .claude/skills/cbc-framing .claude/skills/cbc-bootstrap \
  .claude/skills/cbc-slice .claude/skills/infra-establish \
  .claude/skills/infra-serve docs/concept
```

The five and the concept chapters — the method half of what the
run holds from here. Named rather than globbed, as everywhere else
in this manual: a `cbc-*` pattern would also catch a skill of the
run's own.

**The container half updates by a different rule, and most of it
never updates at all.** Since ADR-0024 the run's container comes
from `starter/kit/` here, and its parts divide:

- **The four convention skills** are pinned copies and travel at a
  kit re-pin, the same way the five method skills do. They are the
  handbook's text, held here at a pin and passed on unedited; the
  run's own `convention-lifecycle` governs how it takes them.
- **The record stubs** — `PLAN.md`, `TODO.md`, `devlog/`,
  `ARCHITECTURE.md`, `CHANGELOG.md`, `.claude/decisions.md`, the
  first ADR — are the run's living records from its first session.
  They never travel again. Re-delivering one would overwrite the
  run's own work with a stub.
- **The two entry files and the hygiene files** are the run's own
  from birth on the same rule, the hygiene files having grown a
  stack overlay the moment the run bootstrapped.

So a kit re-pin delivers four files, not sixteen, and the note says
which of the four moved and what changed in them.

**Which repo is the run's "handbook".** The run's
`convention-lifecycle` §3 step 1 tells it to diff the handbook, and
a run born under one chain holds no handbook checkout. The same
paragraph answers it: "the handbook is a checkout on disk or the
payload a handoff carries; the protocol is git either way." This
delivery is that payload. The note names the kit hash the container
half is held at, which is the hash that procedure compares from.

Empty means no local layer. Non-empty is the hand-off: each hunk is
taken, reshaped or declined, in our own wording, in the commits
that take it.

Then write the note into this repo's `temp/`. What it carries is
below.

**3. Stage the copy and the note in the run's `temp/`.** (operator)

```bash
staged="$run_dir/temp/bundle-$new_pin"
mkdir -p "$staged"/concept "$staged"/conventions

# the method half — the five skills and the concept chapters
for s in cbc-framing cbc-bootstrap cbc-slice infra-establish infra-serve; do
  cp -r "$bundle_dir"/starter/bundle/"$s" "$staged"/
done
cp "$bundle_dir"/concept/*.md "$staged"/concept/

# the container half — the four convention skills, and only those
for c in commit-messages change-plans artifact-kinds convention-lifecycle; do
  cp -r "$bundle_dir"/starter/kit/.claude/skills/"$c" "$staged"/conventions/
done

cp "$bundle_dir"/temp/<the-note>.md "$run_dir/temp/"
```

Nothing is overwritten yet. The run sees what is coming before it
takes it.

**The container half is staged only when it moved**, and only these
four. The record stubs, the entry files and the hygiene files are
the run's own from birth and are never staged — a copy of one would
be an offer to overwrite the run's own work with a blank. A run
still taking its conventions from the handbook directly gets no
`conventions/` directory here, and the note says which case it is.

The concept chapters are staged every time, changed or not, so the
run compares rather than trusts a claim that they did not move.
They usually have not.

**4. The run evaluates and takes it whole.** (the run's agent)

It reads the note, reads its own records, and diffs the staged copy
against what it holds. Then it takes the whole thing:

```bash
for s in cbc-framing cbc-bootstrap cbc-slice infra-establish infra-serve; do
  rm -rf .claude/skills/$s && cp -r temp/bundle-<pin>/$s .claude/skills/
done
cp temp/bundle-<pin>/concept/*.md docs/concept/

# only if the container half was staged
for c in temp/bundle-<pin>/conventions/*/; do
  n=$(basename "$c"); rm -rf .claude/skills/$n && cp -r "$c" .claude/skills/
done
```

Whole, never re-derived. A pin names an exact state, and a copy the
run reworded would make it lie (ADR-0022). A declined edit of the
run's own is gone with the overwrite and is never edited back; what
the run still needs goes into the run's own records.

A change-plan only if the landing is a sequence — a copy and a log
entry is two commits and needs none.

**5. The run records the new pin.** (the run's agent)

One entry in its `.claude/decisions.md`: the new hash, the old one,
what moved, what the note said about its own edits, and what it
decided. Where the container half moved too, the entry names both
hashes — ours for what was delivered, the handbook's for the state
inside it — because one hash standing for two states would lie, and
because the run's convention copies are pinned by that second one. That entry is the run's memory of this exchange; nothing
in the files carries it.

Nothing in the run's history may carry it either. A run's `temp/`
need not behave like this repo's, which is tracked so that an
arrival shows as a diff: never-oversold's is excluded in
`.git/info/exclude`, local to that checkout and not committed, so
the staged copy and the note land invisibly and leave when they are
deleted with no trace at all. That is the run's arrangement to
make, not ours. It only means the decisions entry is the whole
record, not a pointer to one — so it says what the note said, not
that a note arrived (never-oversold, 2026-09-17, which handled this
unprompted).

**6. Delete what was served.** (operator or the run)

```bash
rm -rf "$run_dir/temp/bundle-$new_pin" "$run_dir/temp/<the-note>.md"
```

And here, delete the note from this repo's `temp/` once it has
landed — git history keeps it.

---

## What the note carries

Told, not delivered. Nothing in it is a rule the run owes
compliance to.

- **Where the run stands** — its pin, and what it has done since,
  read from its own records.
- **What changed** — the shape of it, not a file list the diff
  already gives.
- **Why it matters to this run** — the part a diff cannot carry.
- **Its own edits, answered** — each taken, reshaped or declined,
  and why. This is the verdict; there is no other channel.
- **What it recommends, in order** — and what is optional.

If the run has to reach for something the note and the files do not
carry, the note was thin. That is the diagnostic, and it is worth
more than a rule against reaching.

**It has a third outcome, found on its first real firing
(2026-09-18).** never-oversold reached for a handbook checkout, to
verify that the convention skills it was handed were byte-identical
to the handbook at the hash the note named — and could not, having
none. The note was not thin. The reach was unnecessary: the
handbook stopped being its upstream with that delivery, so its pin
is ours and the handbook hash inside it is provenance rather than a
claim to check. What was stale was its model of the relationship,
and the note had not thought to say so.

So a reach means one of three things, and the sender has to say
which: the note was thin; or what the run wanted does not exist;
or the run is working from a relationship that has changed and the
note did not name the change. The third is the sender's fault as
much as the first, and only the sender can see it.

## What this does not do

- No agent reads another repo. We read the run's records; the run
  reads what is in its own `temp/`.
- No partial pin. A pin naming some files at one hash and some at
  another answers "which version" with a list.
- No concept version bumps for an execution-only change, and
  CHANGELOG carries concept versions only (ADR-0003, ADR-0007).
