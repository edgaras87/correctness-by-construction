# Agent decisions

<!-- The working arrangement's decision log (handbook ADR-0020,
     provisional). Append-only, newest last. One entry per
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
     graduates to the handbook, stays local, or dies.

     The placeholder on the "@" line below is replaced at copy
     time by the install block in the handbook's manual. It pins
     which handbook state — and so which version of every
     convention — this project was born from (convention-lifecycle
     §7). If that line still shows a placeholder instead of a
     commit hash, the install block was not run from the handbook;
     fix it before the bootstrap commit. -->

- 2026-08-27 Born from the engineering-handbook starter kit
  @ 4fe8083.
  Conventions: project-recording, commit-messages, repo-hygiene,
  artifact-kinds, change-plans.
  Why: handbook defaults.
  Rejected: none — see the handbook's ADRs.

- 2026-08-27 Step 0 commit order: working arrangement installed
  before the project records.
  Why: the arrangement that governs the series belongs on record
  before the work it governs; the agent-scoped commits then sit
  together at the head of the set. Nothing mechanically depends on
  the order.
  Rejected: the kit stub's prescribed order (plan open → project
  records → agent install → plan close). Candidate handbook
  feedback at retrospective: the stub's comment may want updating.

- 2026-08-27 Stub comment discipline: left as delivered, but the
  rule defining it is about to lose its only home.
  Why: the stubs use two comment kinds — fill-comments (marked
  "Fill-comment:", replaced by content) and standing rules (stay
  forever) — yet the only text stating that distinction is PLAN's
  Step 0 bootstrap comment, deleted when Step 0 closes. The
  discipline should also state that comment voice is actor-neutral:
  addressed to whoever edits the record, never to a named agent —
  already true of every stub, but nowhere written. Candidate
  handbook feedback: give both rules a stated home (likely
  project-recording); this repo does not author method (tiers
  model).
  Rejected: defining it locally as a project convention — wrong
  tier. Also rejected: visible text or admonitions instead of
  comments — the rules address the raw-file editor, not the
  rendered reader (agent model: installed, self-enforcing
  delivery).

- 2026-08-27 Commit attribution: agent trailers (Co-Authored-By,
  session link) stripped from this repo's history and disabled
  globally in the agent's settings.
  Why: commits are the author's; whether tool involvement is
  visible in public history is the author's call, and here the
  call is no. Trailers are plain message text — with them gone,
  nothing in git records agent involvement.
  Rejected: keeping the tool default. Candidate handbook feedback:
  the arrangement should state an attribution policy at birth (in
  the kit/install block), so it is decided once instead of
  discovered at the first commit.
