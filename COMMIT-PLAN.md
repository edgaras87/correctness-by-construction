# Commit plan: the groups mirror the run's tree, and every shipped file says what it stands on

## Summary — the state after all commits

ADR-0036 decision 7, landed. Inside `delivery/method/` and
`delivery/spring-postgres/` every path is the path it lands at in a
run: `delivery/method/.claude/skills/cbc-framing/` lands at
`.claude/skills/cbc-framing/`, as `delivery/container/` already
does. Staging a delivery is copying each group the run takes on top
of the last, so `exchange-deliver` §2.2 runs as written and the seed
stages the same way; the mapping table in `delivery/README.md` is
reduced to its one exception, `concept/` → `docs/concept/`. Every
shipped skill and rule carries one frontmatter field, `foundation`,
holding a live claim about what it stands on now — the method
skills on concept v1, the stack practice on practice checked against
it, the container's skills and the copies rule on their
convention — and the line-6 comments that said it in two verbs are
gone, with the nine template lines that repeated it. Our three convention copies equal the masters again. The
exchange's manual says all of this as fact rather than as intended,
and the records describe the field where they described a header.

A run sees only the field: its own paths do not move, so the next
note carries nine changed files and no renames.

Not in this set: the shapes convention (after this, before the
delivery); `shapes-lifecycle.md`'s field, which waits for that
manual; the concept chapters' provenance headers (ADR-0022 left
them, and nothing here reopens it); `working-a-reading.md`; the
delivery to run 3.

## Commits

**1. `docs(agent): add commit plan for the mirrored layout`**
This file.

**2. `docs: the method and the stack practice mirror the run's tree`**
Five `git mv`: each skill directory under `delivery/method/` and
`delivery/spring-postgres/` moves under `.claude/skills/` inside its
group. Nothing inside a skill changes. `delivery/README.md`'s
pinned-copies table shrinks to the concept row, its "they flatten
into `.claude/skills/` all the same" paragraph goes, and the
sentence above the table says the rule instead — each group is a
piece of the run's tree. `ARCHITECTURE.md`'s executions component
and codemap row name the new paths. The exchange manual's §3 italic
— *today `container/` already mirrors and the other two do not* —
is made plain. Verified before the commit by running §2.2 of
`exchange-deliver` into a scratch directory and listing it: the
result must be a run's tree with five skills, three skills, two
rules and `docs/concept/`, and the duplicate-path check must print
nothing.

**3. `docs: the seed stages the groups as one overlay`**
`pure-seed.md` step 4: the loop over `method/*/` and
`spring-postgres/*/` becomes the same overlay as `exchange-deliver`
§2.2 — the groups named once, each copied on top of the last, the
concept line beside it — and the commit subject on `birth-seed`
follows ("the method and stack groups" for "the five CbC skills").
The checkable list and the prompt's "five skills" follow where they
count files. Provisional in wording: the seed has not run since
ADR-0024 and this step touches only the lines the layout makes
false. If the rewrite wants more than that, §5 revises here.
*Revised at its boundary, 2026-09-26, before staging:* the manual
still says the birth entry takes three placeholders, the kit pin
among them, that naming both is the point, and, twice, that which
handbook state the container holds is the birth entry's to say —
one paragraph, one line in the fired prompt, one closing sentence
of step 4. The last set's step 5 fixed the lines that *fill* a
second pin and missed the lines that *explain* one. And
`delivery/README.md` still says the seed reads the kit pin from its
Kit-pin line, which the last set stopped it doing. This step takes
those too: same file, same reading, and a seed manual that says one
pin in its script and two in its prose is the contradiction the
last set was closing. Five passages, no new mechanics.

**4. `docs: every shipped skill and rule says what it stands on`**
One frontmatter field, `foundation`, beside `name` and `description`:
in the two method skills, `concept v1`; in the three stack skills,
`practice, checked against concept v1`; in the three container
skills, `the <name> convention`; in `delivered-copies.md`, `the
exchange convention`, beside its `paths`. The five line-6 comments
go — the field is the one place. The nine templates lose the line of
their opening comment that said *checked against concept v1* and
keep the copy-and-fill instruction and the ADR they cite (see
Decisions). `shapes-lifecycle.md` gets nothing and
the exchange manual's §3 paragraph on the field, made plain in this
commit, says why: it has no manual to name. `docs/conventions/README.md`
§"A skill file" lists the field. The records stop saying *header*
where they mean this: `master.md` §2.1 and §2.2, `ARCHITECTURE.md`'s
executions paragraph and its "never lands without stating" invariant,
`delivery/README.md`'s opening sentence.

**5. `chore(agent): our three convention copies take the field`**
`.claude/skills/commit-messages`, `commit-plan` and
`visual-comparison` copied whole from `delivery/container/`,
`cmp`-identical afterwards. One decisions-log entry: the field, why
our copies carry a claim about a convention we hold the manual of,
and that a copy changes by being copied anew.

**6. `docs: the records catch up`**
`master.md` §2.4 stops naming `bundle-update.md`, deleted on
2026-09-26 and found still named there while this plan was read —
the sweep that step did not reach `master.md`. The sweep for this
set: every old path (`delivery/method/<skill>/`,
`delivery/spring-postgres/<skill>/`) and every *header* that meant
the derivation line, across live text; `TODO.md` line 1684's
template path follows. The devlog carries the set. No PLAN gate
closes here.

**7. `docs(agent): close commit plan for the mirrored layout`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **No new ADR.** The layout and the field were decided in ADR-0036
  decision 7 and deferred to "a second plan"; this is it. The two
  calls below are how, not whether, and are named here for
  objection. If either is judged a decision with rejected options,
  it becomes an ADR opened Proposed at step 2 and the plan is
  revised.
- **The field is named `foundation`: what the file stands on now.**
  The manual asks for one field holding a live claim, and forbids
  `source`. Chosen by the reviewer over three others: `source`
  collides with the deliverer in the manual and with source code in
  every run; `origin` says where a thing came from, which is
  history, and is a git word; `derivation` reads wrong on the stack
  skills, the one kind that is not derived. The value keeps
  ADR-0005's distinction where it matters: a stack skill's
  foundation is practice, checked against the concept, which is
  what `master.md` §2.2 already says in words.
- **The templates lose their *checked against* line.** A skill
  travels whole (ADR-0029), so the claim on its `SKILL.md` covers
  its references and templates; a second copy of the claim in nine
  files is the drift the field exists to end. What stays is
  instruction under ADR-0022 — copy into a run and fill, the master's
  ADR. Agreed with the reviewer at planning.
- **`shapes-lifecycle.md` is the one shipped file without the
  field**, said in the manual rather than filled with a guess. Its
  convention does not exist yet; the shapes plan that follows this
  one gives it the name.
- **The run's paths do not move, so the next note carries no
  renames.** The mirror is a fact about our tree. Named because the
  exchange makes renames the note's job, and a reader of step 2
  might expect one.
- **Step 3 is its own commit, not part of step 2.** The move and
  the seed's rewrite are different changes: revert the seed's
  overlay and the layout still stands, with the old loop simply
  wrong — which is where the seed is today.
- **Steps 3 and 6 fix stale lines the last set missed.** `master.md`
  §2.4 naming a deleted file, and the seed manual's prose about a
  second pin, are defects of the 09-26 close, not of this set, and
  are fixed here because they were found here and each is a few
  lines in a file the step already touches.
