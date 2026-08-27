# Devlog

<!-- Newest entries on top. 2–5 minutes at the end of each session.
     For future-you: fragments fine, honesty mandatory. Never clean up.
     Mark dead ends loudly with "DEAD END:" so they're greppable.
     End every session with a "Resume:" line — cheapest save-point there is.
     When this file gets long, split into devlog/2026-08.md per month. -->

## 2026-08-27  (Step 0: bootstrap)

- Project started. Repo initialized from the starter kit
  (handbook @ 4fe8083).
- Briefing: one repo for one concept being learned — correctness by
  construction, the design principle that correctness is built into
  the structure of a thing rather than tested in afterwards. Working
  name correctness-by-construction ("cbc" in prose); framing may
  rename. The problem: the understanding lives in a head and
  scattered notes and does not improve in any recorded way when
  things are tried. Wanted: one authoritative place for the
  plain-words statement, its rationale, open questions, and a log of
  what changed it and why. Hunches, not decisions: the concept
  splits into a mental layer (the statement itself) and executions
  derived from it — agent skills, checklists, templates — each
  stating which concept version it derives from; runs and
  experiments happen in other repos, pinned to a concept version,
  and their surprises come back here as harvested concept changes,
  after which executions are re-derived. This repo is the middle
  tier of the workspace (handbook → concepts → runs), under
  concept-garden/, a plain folder. Existing material (input to
  Framing, not pre-agreements): a drafted concept statement and two
  workflow executions in ~/PycharmProjects/archive/cbc/
  system-design-method/birth-materials/ (five concept chapters,
  cbc-framing and cbc-slice skills, a startup snippet); two more
  executions from practice in the same repo's agents-from-practice/
  (infrastructure establishment, system bootstrap) — only those two
  directories matter, the rest of that repo is noise. One live run:
  ~/IdeaProjects/checkout-system, born 2026-08-27 with executions
  copied from the archive snapshot; its decisions log already
  records one improvement (a Boot 4.1 testing trap) that the
  archive copy lacks — the first harvest candidate. Whether an
  execution later graduates to its own concept repo is open, with a
  named trigger (the garden rule: a second concept, a rule written
  twice). Done-ish: months from now the concept doc is consulted
  and updated after runs, and at least one derived execution was
  used in a real project.
- Open: what granularity a "concept version" is; whether
  harvest/provenance discipline is local rules or its own
  convention; whether the mental layer is one document or several.
- Session close: Step 0 done — six-commit change set landed as
  planned (plan open → agent install → records → models → step
  close → plan close); three decisions.md entries queued as
  handbook feedback (commit order, stub comment discipline,
  attribution — trailers stripped from history and disabled before
  anything was pushed). Agreed working practice, not yet recorded
  anywhere binding: this repo has no project end, so
  playbook/retrospective fold-back happens at step-gate closes —
  log it as a decisions.md deviation the first time it is
  exercised. Parked for Framing: whether CLAUDE.md gets a models
  routing line (agent model P2 — pointer at the moment of need vs
  ambient), and whether ARCHITECTURE's Components/Invariants/
  Codemap sections fit a docs-only repo (fill with structural
  invariants, or delete).
- Resume: Framing (PLAN Step 1) — read the two archive directories
  (birth-materials/, agents-from-practice/), then problem statement,
  success criteria, out-of-scope, middle steps authored; the archive
  import is project work there and gets its own change-plan.
