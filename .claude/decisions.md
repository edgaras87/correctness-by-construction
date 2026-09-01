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

- 2026-08-28 CHANGELOG stub repurposed: header and standing comment
  rewritten for the concept-version log role (ADR-0003).
  Why: the kit stub assumes an application repo — SemVer, user-speak
  examples, Deprecated/Security categories. A concept repo's
  changelog users are pinners (run repos, executions citing a
  version), and its versions are concept versions; the stub's rules
  had to be replaced, not filled. Candidate handbook feedback: the
  kit may want per-repo-type CHANGELOG stubs, or a stub that asks
  what a version is here instead of assuming SemVer.
  Rejected: keeping the stub and logging versions elsewhere — two
  version-shaped records where the repo needs one.

- 2026-08-30 The four candidate-handbook-feedback entries above
  graduated: delivered in the first upward handoff (temp/ channel)
  and triaged handbook-side the same day (their change set
  06cc06d..e3e45bd). Outcomes: commit order freed (their fix cites
  the 2026-08-27 entry's reasoning); comment discipline and
  attribution parked in their TODO with leanings; CHANGELOG stub
  parked, leaning one-stub-that-asks. Graduation ahead of the
  retrospective, at the user's call — the birth from the manual
  needed the kit bug fixed first, and the ledger items rode along.
  Rejected: holding them for a retrospective this endless repo will
  not have (the fold-back-at-gate-closes practice, devlog
  2026-08-27, applied to the ledger for the first time).

- 2026-09-01 change-plans convention updated in place from the
  handbook @ 65dd7ee (their ADR-0027): rolling commit lists,
  material-first step order, records steps planned by walking the
  records table, in-set ADRs Proposed by default; requires gains
  project-recording. First live-repo convention injection —
  procedure hand-supplied in their return item 11, deliberately
  unwritten on their side; our friction notes are the payload they
  asked back.
  Why: the vendored copy was stale against the convention now
  governing our own change sets; the next set would have been
  planned under superseded rules.
  Rejected: waiting for the next birth (births refresh kit copies,
  not a live repo's); re-deriving the changes locally (wrong tier —
  the handbook authors method, we consume it pinned).
