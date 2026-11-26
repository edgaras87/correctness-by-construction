# 0089. CBC Runs 4, 5 and 6 judged by today's exchange

Date: 2026-11-26
Status: Accepted (2026-11-26, the reviewer, in the session that postponed the model work; unchanged since). Supersedes 0082 in part: decision 4's "by the simulation's Judge".

## Context

On 2026-11-26 the reviewer stopped evolving the Maintainer Repo, to get back to the projects. The model work waits at its triggers; the reading of CBC Runs 4, 5 and 6 comes next (`d7ace896`).

ADR-0082, decision 4, says their findings are judged together, "by the simulation's Judge, by meaning". The TODO item names the judge-copy-changes Agent Skill. That Agent Skill was added on 2026-11-24. It is the layers model's Adapted Case for judging a Backend Repo's Copy Changes. It asks how deep each lesson goes, from depth a to depth f, and stops at depths c, d and e, not yet walked.

CBC Runs 4, 5 and 6 were born from 2026-10-15 to 2026-10-29, from the kit of their day. The Backend Kit did not exist yet. The reviewer: these repos do not fit the new model's Agent Skills.

## Options considered

- **Judged by the judge-copy-changes Agent Skill,** as ADR-0082 and the TODO item said. Rejected: it judges a Backend Repo's Copy Changes by the layers model, and the CBC Runs were built on today's kit. Its depths c, d and e would stop the judging at each lesson that reaches an idea.
- **Read by the read-copy-changes Agent Skill.** Rejected for the same reason: it reads a Backend Repo against its Kit Version.

## Decision

1. **A CBC Run read now is read by the exchange-read Agent Skill.**
2. **Their findings are judged together, by working-a-reading.** Each item ends taken, declined or held (`docs/conventions/exchange/` §6.5, *Verdicts*).
3. **A taken item changes no text now.** It is kept for the rewrite, and lands with the text it changes. No Delivery Note is sent. This departs from §6.5, where a taken item changes a Master Copy at once, until the rewrite.
4. **No Agent Skill of the layers model is used on the CBC Runs:** not read-copy-changes, judge-copy-changes or deliver-the-kit-update.

The rest of ADR-0082, decision 4, stands: each CBC Run read apart, the findings judged together and kept for the rewrite.

## Consequences

- ADR-0082's status names this ADR.
- The TODO item "Read and judge CBC Runs 4, 5 and 6" judges by working-a-reading.
- A held item takes its line in TODO, as §6.5 says.
- The layers model's Agent Skills are first used on a Backend Repo, not on a CBC Run.
