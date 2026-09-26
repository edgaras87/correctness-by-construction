# Commit plan: the exchange is placed, and convention-lifecycle leaves

## Summary — the state after all commits

One convention governs everything that passes between this repo and
a run, and it is held where each side does its part. The manual is
at `docs/conventions/exchange/README.md` and ships nowhere. The run's
rule, `delivered-copies.md`, ships in the container at
`.claude/rules/`. Our two skills, `exchange-read` and
`exchange-deliver`, and the reading's shape, `exchange-reading.md`,
sit in this repo's own `.claude/`. `convention-lifecycle` is gone
from our arrangement, from the container, and from the manuals;
`bundle-update.md` is gone, its one homeless lesson — the rename
sweep — landed in `commit-plan`'s close step first. The shipped
entry file no longer forbids what the shipped rule permits.
`master.md` describes all of this as fact rather than intent, two of
its four errata are closed, and ADR-0036 is Accepted.

Not in this set: the mirrored layout and the derivation field (a
second plan), `working-a-reading.md` (stays in `temp/` until its
second firing), and the delivery to run 3 (after both plans).

## Commits

**1. `docs(agent): add commit plan for the exchange`**
This file.

**2. `docs(adr): propose 0036 — the exchange replaces convention-lifecycle`**
The decision, Proposed: one convention for the whole exchange, a
manual and four artifacts split between the two arrangements; the
run's rule built from run 3's text; both coordinates held by the
run; bytes match at the pin; a copy cannot carry absence. Rejected
options recorded — widening `convention-lifecycle`, skeleton-sync, a
per-run table here, keeping notes verbatim on the run's side, a
second reading per movement, and the names `system`, `structure`,
`models` for the description's home. Comes first so the artifacts
that follow cite it, and so it can still be revised at a boundary.

**3. `docs: the exchange has a manual`**
`temp/exchange.md` → `docs/conventions/exchange/README.md`, header
comment de-drafted, the closing section's *intended* made plain
where it is now true. The conventions index gains its row. Nothing
is removed yet; the manual can stand beside the old one for two
steps.

**4. `chore(agent): the exchange's skills and shape are held here`**
`temp/exchange-read/` and `temp/exchange-deliver/` →
`.claude/skills/`; `temp/exchange-reading.md` →
`.claude/rules/exchange-reading.md` with `paths: ["temp/reading-*.md"]`
and its header de-drafted. Each cites CBC ADR-0036 in its Decisions
list, not the manual by path. One decisions-log entry: what arrived,
why a shape and two skills rather than a procedure, and where the
shape lives. This step crosses the `temp/` → `.claude/` boundary in
one commit — see Decisions below.

**5. `docs: the run's rule ships, and the container follows it`**
`temp/delivered-copies.md` → `delivery/container/.claude/rules/`,
citing CBC ADR-0036. The shipped `CLAUDE.md` loses "never edited in
place — a change is a new copy from the source". The shipped
`decisions.md` birth entry lists `exchange` where it listed
`convention-lifecycle`. `delivery/README.md`'s harvest paragraphs and
its "everything after birth is `bundle-update.md`" line point at the
exchange instead.
*Widened at its boundary, 2026-09-26:* the shipped birth entry still
carried two hashes — the bundle's and the handbook kit's — with a
comment saying one pin for two states would lie. Post-fork there is
one pin, and the rule this step ships says the entry carries **pin
and read-through**. A container whose rule and whose template
disagree on what the entry holds ships a contradiction in the two
files a newborn reads first. So: the template's second placeholder
becomes the read-through — the newborn's first commit — its comment
says why, and `pure-seed.md`'s three lines that fill "two pins"
follow (lines 87, 135–136, 319). The rest of `pure-seed.md` stands;
see Decisions.

**6. `docs: convention-lifecycle leaves the delivery`**
`delivery/container/.claude/skills/convention-lifecycle/` and
`docs/conventions/convention-lifecycle/` deleted; the index row
removed; the two live mentions swept — `docs/conventions/README.md`
§"remaining conventions" and its line 147, `delivery/README.md`'s
delta table row. Grep for the name across live text before
committing; history keeps every other mention.

**7. `chore(agent): convention-lifecycle leaves our arrangement`**
`.claude/skills/convention-lifecycle/` deleted. One decisions-log
entry: the receiver's protocol, held by a repo that is not a
receiver, never fired here; what replaces it and on which side.

**8. `docs: the rename sweep is commit-plan's close step`**
One line in the shipped master,
`delivery/container/.claude/skills/commit-plan/SKILL.md` §4 Close:
when a step renamed or renumbered anything, grep the whole span for
every old identifier before the close commit. The one lesson in
`bundle-update.md` with nowhere else to live, placed before the file
goes.

**9. `chore(agent): our commit-plan copy takes the sweep line`**
The same line in `.claude/skills/commit-plan/SKILL.md`; a
decisions-log entry naming the master it now equals.

**10. `docs: bundle-update.md goes`**
Deleted. Two TODO items close: the rename sweep (landed in 8), and
the split-and-write-the-inbound-half item, superseded by the
exchange. `ARCHITECTURE.md`'s two mentions of the file point at the
exchange.

**11. `docs: master.md catches up, and ADR-0036 is accepted`**
The records commit. `master.md`: §1.2 lists the seven with
`exchange` for `convention-lifecycle`; §2.3 counts three convention
skills and two rules, and the artifact-to-manual count re-done;
§2.5 keeps the facts and the diagram and cites the manual for the
mechanism; §3 unchanged, and the manual's §6 cites it; §4.1 and
§4.2 list the new holdings; §4.3's `convention-lifecycle` paragraph
becomes "designed, not accidental"; *what must stay true* cites the
manual's §1 for the exchange facts; *the words* gains
*read-through*; errata #2 and #3 close. ADR-0036 flips to Accepted.
The devlog carries the set.

**12. `docs(agent): close commit plan for the exchange`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **The shape lands in `.claude/rules/` with `paths:`, not
  `.claude/shapes/`.** Its moment is a file being written, which is
  what `paths:` is for; `.claude/shapes/` is for a shape opened at a
  gate, and a reading has no gate. Deferred twice by the reviewer to
  "when we move"; this is the move. Objection here changes step 4's
  destination and nothing else.
- **Step 4 crosses the agent/project line in one commit.** Moving
  three files from `temp/` into `.claude/` shows as renames only if
  both sides are in one commit; split, history breaks at the move.
  `temp/` is scratch, not a record, so the split rule's reason —
  agent changes reverting apart from project records — is not
  touched. Named so the reviewer can object.
- **Steps 5 and 6 are add then remove, not one swap.** The rule
  shipping and the old protocol leaving are different changes;
  reverting one should not undo the other.
- **The manual's `intended` italics are made plain at step 3 only
  where step 3 makes them true.** The artifacts' homes are named as
  intended until steps 4 and 5 land, and made plain in step 11 with
  the rest of the records — the paths stated as checkable, never
  ahead.
- **Skills cite the ADR, not the manual by path.** Every other skill
  here cites decisions as `CBC ADR-nnnn`; a manual's path can move,
  an ADR number cannot.
- **`pure-seed.md` is updated, not rewritten, in this set.** Birth
  has mechanics the exchange does not describe — `git init`, the
  hygiene commit, the `birth-seed` receipt branch, the fills, the
  newborn's agent finishing the birth — and they still hold. What
  the exchange makes false is the birth entry's shape, fixed here.
  What the exchange makes *better* — staging as one overlay of the
  groups — needs the mirrored layout, and lands with it in the
  second plan. Rewriting the seed twice would shape it once from
  intent.
