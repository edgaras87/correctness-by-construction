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
The skill's §1 gains the three rules as lines, where the note is
written. It is an agent file, so it gets a commit of its own.

**4. `docs: the runs' names go on the map`**
ARCHITECTURE §2.5 gains the runs: ours by ordinal, each run's own
name, where it sits on disk, and which one is live. "Run 3,
`never-oversold`, is the live one" folds into it.

**5. `docs(temp): temp/README says what temp/ is`**
The three rules and the table leave, now that each has its home, and
so does the history. What stays is what `temp/` is.

**6. `docs: devlog carries temp/README`**
The session's entry. The TODO item on `temp/` in the container gains
a line: the trimmed README is the seed of whatever convention comes
to own `temp/`.

**7. `docs(agent): close commit plan for temp/README`**
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
