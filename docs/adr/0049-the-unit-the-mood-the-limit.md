# 0049. The commit rules: a plan's unit, the mood, the limit

Date: 2026-10-09
Status: Accepted (2026-10-09, at the set's records commit; opened
Proposed under the commit plan for commit rules and revised once,
when the reviewer kept the past-tense ban at commit 5)

## Context

Five questions about how commits are written and planned waited in
TODO, three of them since September; they are one subject, and are
settled together.

- **"Step" meant two things.** A `PLAN.md` step is a milestone; in
  a commit plan, a step was one commit — 28 times in the
  `commit-plan` skill, and in the reviewer's own "stop at every
  step's boundary". On 2026-10-08 a session sat inside PLAN's Step
  10 while working commit plan steps 1 to 13.
- **Run 3 asked for a name** for a PLAN step run as a series of
  commits, as it ran its framing (2026-09-20). Naming it seemed to
  collide with the convention's claim that the commits which exist
  are the steps done.
- **The sweep before a close missed four times** a phrase the file
  wraps across two lines — a `§7` in a `§8` hunt, a renumbering, a
  phrase, "(model §10)".
- **The 50-character limit was broken constantly**: 174 of 453
  subjects from 2026-09-20 to 10-02, with `commit-messages` opened
  at every commit. Unenforced, or mis-set (the agent model's A1)?
  Since 2026-10-08 `commit-plan` counts subjects when the plan is
  written, and the 35 subjects after it all fit.
- **The skill asks for the imperative, and practice split by
  itself.** A code change is written as a command — run 3's "feat:
  free expired holds before each decision" — and a record as what
  became true — "docs: TODO asks for a glossary", "the devlog
  splits by month". Here and in run 3 alike, unprompted; only the
  commit-plan forms stayed imperative, because the skill gives them.

## Options considered

For the double meaning:
- **PLAN's step renamed**, "plan stage". Rejected: it is the older,
  wider word, in every run's PLAN and playbook, and "stage" is
  already taken three ways — the skills' stages, git's staging
  area, a delivery staged into `temp/`.
- **A commit plan's unit becomes "commit"** — chosen. The plan
  already heads its list *Commits*.

For run 3's question:
- **A name for a step run as commits.** Rejected: once a plan's unit
  is a commit, such a step is a step with a commit plan, which the
  convention already describes.

For the limit:
- **Raise it, or shorten commit-plan's revision form.** Rejected:
  counted where they are first written, subjects fit; the limit was
  never checked, not set wrong.

For the mood:
- **Statements everywhere**, the plan's forms rewritten to match.
  Rejected: it would turn a code change's natural command into "the
  ledger frees expired holds".
- **Commands everywhere**, as the skill says. Rejected: every
  record commit would be rewritten against a habit both repositories
  reached alone.
- **Either mood; the subject says what changes and reads alone** —
  chosen. The old worry, that allowing two moods means sorting each
  commit first, holds only where a mood is required.

## Decision

1. **A commit plan counts commits.** "Step" is `PLAN.md`'s word
   alone; within a commit plan the unit is a commit.
2. **A PLAN step done in several commits gets a commit plan**, and
   no name of its own.
3. **The sweep before a close greps the text unwrapped**, joined
   across its line breaks.
4. **The subject's limit stays 50 characters**, counted when a plan
   writes it.
5. **A subject may take either mood, in the present tense.** It
   says what the commit changes and makes sense alone in `git log
   --oneline`. Past tense stays barred, as the old test barred it:
   "fixed race" reports the author, not the repo, and neither habit
   reaches for it.

## Consequences

- The commit-plan and commit-messages manuals, the container's two
  skills and our copies change; a run takes them at its next
  delivery, and its note answers run 3's held line on commit series
  and the imperative.
- "Step" in a commit-plan sense survives in history — this repo's
  devlog, its closed plans, older commit bodies — and is not
  rewritten.
