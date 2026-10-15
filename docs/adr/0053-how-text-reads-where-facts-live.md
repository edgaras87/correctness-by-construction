# 0053. How a text reads, and where a fact lives, are loaded rules

Date: 2026-10-15
Status: Proposed (under the commit plan for writing rules)

## Context

Run 3, never-oversold, wrote about 150,000 words of Markdown for
768 lines of production code. Its records were dense: long chained
sentences, coined words never defined. Its reviewer asked "explain
simpler" again and again. One step's story was told four times: in
PLAN, the devlog, the slice record and the commits.

The lessons were already written down, and still did not act:

- **"Explain plainly" sat in the agent's memory from 2026-09-20.**
  The records still came out in the skills' voice. The agent copies
  the voice it reads.
- **"Each fact has one home" is project-recording's §11, rule 1.**
  A manual is read when a convention is changed, not when a record
  is written, so nothing put it in front of the writer.

At its retrospective (its RETRO.md, D1 and D2) run 3 wrote two
rules with no `paths:`, so they load in every session:
`writing.md`, how a text reads, and `one-home.md`, where a fact
lives. Its Step 10 rewrote its records under them three times. It
offers both whole.

Our arrangement has no slot for them. `docs/conventions/agent-arrangement/`
§2.4 lets a line load on every task only when it is true of this
project and nowhere else, has no moment, and nothing else would
deliver it. Both rules fail the first test: they are true of any
project.

## Options considered

- **Keep the voice in memory or in `CLAUDE.local.md`.** Rejected:
  run 3 had it in memory, and its records still copied the skills.
  `CLAUDE.local.md` is one reviewer's, and reaches no run.
- **One rule for both questions.** Rejected: how a text reads and
  where a fact lives are two questions, and each rule stays one
  page.
- **Load them on Markdown paths only.** Rejected: chat has no path,
  and a `paths:` list loads when a file is read, not when one is
  written.
- **Leave the lessons in manuals.** Rejected: that is where they
  were when run 3 missed them.

## Decision

1. **Writing is a convention of its own**, the tenth:
   `docs/conventions/writing/`. Its manual holds the why of each
   rule; its artifact is the rule.
2. **One home per fact stays project-recording's.** Its manual is
   that convention's: §11, rule 1, is the why, and the loaded rule
   becomes one more of its artifacts.
3. **A convention whose moment is every task may ship as a rule with
   no `paths:`.** It passes §2.4 as a convention's artifact, not as
   an entry-file line. It is paid for in every session, so few
   qualify.
4. **Both ship in the container**, with examples from the worked
   example's order service in full-word tags. Neither names the
   method: any project would want them.
5. **This repo loads both too.** New text follows them from the
   commit that adds them. Old text is rewritten later, as the
   reading of run 3 decides; history keeps its words.

## Consequences

- Agent-arrangement's §2.4 and §3.2 gain the ambient slot.
- `ARCHITECTURE.md` counts ten manuals, and the container's file
  list gains two rules.
- Every session, here and in each run, carries two more pages.
- The glossary the writing rule points at is "the project's, where
  it keeps one": no container record is a glossary yet.
