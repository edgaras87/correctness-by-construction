<!-- The refinement of this repo, opened 2026-10-18 on
     refinement-2026-10-18. Data only: how this file is made is
     docs/conventions/refinement/ §2. It grows a part at each
     stage, and goes at the close. -->

# Refinement, 2026-10-18

## Before round 1

### Kinds and rounds (§2.1)

Collected from TODO's refinement item, at `b3b2018`. The three
default rounds hold: every kind fits one, and each round has a
kind.

| Round | Kind | What a finding is | The rule |
|---|---|---|---|
| 1 | Stale lines | a line no longer true | none needed: a false line is wrong |
| 1 | Foundations | a `foundation` line that disagrees with its manual | `.claude/rules/foundation-check.md` |
| 2 | One home | a fact told in more than one place | `.claude/rules/one-home.md` |
| 2 | Dependencies | a retelling where a pointer would do, or a pointer not needed | `docs/conventions/conventions/` §3.1 |
| 2 | Seats | a deliverer seat that says more than how its convention works here | `docs/conventions/conventions/` §3.4, in doubt |
| 2 | Lessons | a case written as the rule | `docs/conventions/conventions/` §3.7 |
| 3 | Writing | text older than ADR-0053, against the whole rule | `.claude/rules/writing.md` |

Not a kind: the item's two "words" ideas, "run" as a verb for a
skill or a step, and "small steps" in `commit-plan`. Each is
already found, so nothing is searched for. Round 3 lists them as
Writing findings, against `.claude/rules/writing.md`, rule 6.

Seats is in doubt: §3.4 says what a seats section holds, not that
it holds no more. The rule check (§2.3) settles it before round 1
reads.

Also in round 2, joined from its own TODO item: the map of the
records, project-recording §1, in project-recording's layer.

Confirmed by the reviewer: not yet.
