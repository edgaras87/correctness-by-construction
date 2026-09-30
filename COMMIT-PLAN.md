# Commit plan: temp/README says what temp/ is

## Summary — the state after all commits

`temp/README.md` says what `temp/` is: drafts on their way
somewhere, tracked, deleted once served, and not records. That is a
folder's own description, the kind ADR-0045 says a README may be
without being a local map.

The three rules it held for anything sent to a run live where a
note is written. Their why is in the exchange's §3.7, "The note",
and the rule is in `exchange-deliver` §1, "Write the note":
- No ADR numbers, paths or vocabulary of this repo, with the scope
  ADR-0020 gave it stated: told text, meaning a note or a prompt.
  Shipped files carry `CBC ADR-nnnn` instead.
- Mark a claim the receiver has no material to check, merged with
  the verdict line already there.
- Give both names when naming a third repo.

The table of the runs' names and paths is on the map, in
ARCHITECTURE §2.5, where "which runs exist, and where" belongs. The
history goes: "tracked since 2026-09-07", and the handbook's mix-up
of 2026-09-17, which the devlog and ADR-0022 keep.

## Commits

**1. `docs(agent): add commit plan for temp/README`**
This plan.

**2. `docs(conventions): the note's three rules`**
The exchange's §3.7 gains the why for each rule, and where it came
from (ADR-0020 for the first). The second merges with what §3.7
already says about verdicts on what a run cannot check.

**3. `chore(agent): exchange-deliver writes by them`**
The skill's §1 gains the rules as lines, where the note is written.
It is an agent file, so it gets a commit of its own. Only the cases
an update can meet are listed: a thin note, material outside the
delivery, a negative claim. An update never goes to a newborn.

**4. `docs: the newborn case goes to the birth`**
The reviewer's question at step 3's boundary: why does an update
note mention a newborn? It should not. Step 2 copied rule 2's four
cases into the exchange's §3.7, which is about the update's note,
and one of them, "anything said to a newborn", happens only at
birth. It leaves §3.7, and goes into `delivery/installs/pure-seed.md`
step 6, where the birth first tells the newborn anything. A newborn
holds no pin, so "this changed since" has nothing to land on.

**5. `docs: the runs go on the map`**
ARCHITECTURE §2.5 gains the runs: ours by ordinal, each run's own
name, where it sits on disk, and which one is live. "Run 3,
`never-oversold`, is the live one" folds into it. ARCHITECTURE's
words gain **newborn**, a run at its birth, from its seed until its
agent finishes the birth, beside **run**. It holds what the seed put
there, one pin included, and no earlier state. The word is used
correctly in about fifteen live places and defined in none. §3.7 of
the exchange points to the names from here.

A check at step 5's start: this plan first said a newborn holds no
pin. The seed names the pin in every commit and fills it into the
birth entry. What a newborn lacks is earlier state, which is what
step 4 already says.

**6. `docs(temp): temp/README says what temp/ is`**
The three rules and the table leave, now that each has its home, and
so does the history. What stays is what `temp/` is.

**7. `docs: devlog carries temp/README`**
The session's entry. The TODO item on `temp/` in the container gains
a line: the trimmed README is the seed of whatever convention comes
to own `temp/`.

**8. `docs(agent): close commit plan for temp/README`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **The rules go where a note is written, not where drafts sit.**
  `temp/` is where a note waits. `exchange-deliver` is where it is
  written, and that is the moment the rule has to be met.
- **Each rule moves before the README loses it**, so no commit leaves
  one without a home.
- **Who owns `temp/` is not decided here.** It is the open TODO item,
  due before the next birth, and this set only makes the README
  ready to seed it.
