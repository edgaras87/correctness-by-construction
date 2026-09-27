# Agent decisions

<!-- The working arrangement's decision log. Append-only, newest
     last. One entry per
     arrangement decision — a skill added or changed, a rule tuned,
     a workflow adopted. Three lines: what, why, what was rejected.

     Division of labor: the standing rule rides as a comment in the
     artifact it governs — this log keeps the why and the rejected
     options, and neither repeats the other. Commit bodies stay
     ordinary commit bodies.

     This file is agent-side: a commit touching it is scoped `agent`
     and touches nothing else (the commit-messages skill carries
     that rule).

     At the project retrospective, read top to bottom: each entry
     graduates to the deliverer, stays local, or dies.

     The two placeholders in the birth entry below — the date and
     the "@" hash — are replaced at copy time by the deliverer's
     seed. The hash is the pin: the deliverer's commit every copy
     here equals. Beside it the entry carries the read-through, the
     commit of this project the deliverer last read up to; at birth
     nothing has been read, and the first note sets it. Every later
     delivery entry carries both (.claude/rules/delivered-copies.md,
     rule 1). If the placeholder still shows, the seed was not run;
     fix it before the bootstrap commit. -->

- <YYYY-MM-DD> Born from the correctness-by-construction delivery,
  pin <bundle-commit>; read-through none — nothing read before the
  first note.
  Conventions: project-recording, commit-messages, repo-hygiene,
  commit-plan, exchange, agent-arrangement, visual-comparison,
  shapes.
  Why: the deliverer's defaults. Their decisions are cited
  CBC ADR-nnnn and are the deliverer's to explain.
  Rejected: none — see the deliverer's ADRs.
