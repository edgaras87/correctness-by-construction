# Devlog

<!-- Newest entries on top. 2–5 minutes at the end of each session.
     For future-you: fragments fine, honesty mandatory. Never clean up.
     Mark dead ends loudly with "DEAD END:" so they're greppable.
     End every session with a "Resume:" line — cheapest save-point there is.
     When this file gets long, split into devlog/2026-08.md per month. -->

## 2026-08-28  (Step 5: first harvest)

- The loop the repo exists for ran once, end to end: checkout-
  system lived a Boot 4.1 trap (RANDOM_PORT alone provides no
  TestRestTemplate bean; @AutoConfigureTestRestTemplate required),
  recorded it in its decision log, fixed its own copy — and this
  repo read that record and took the lesson into the authoritative
  spring-boot-walkthrough.md in the run's own wording. Body now
  byte-identical to the run's lived copy. Run repo read, never
  edited. Six commits, none diverged.
- Harvest discipline settled from the lived case (ADR-0007): the
  execution's provenance header is its change log — one dated
  harvest line per change, traveling with every future copy; no
  concept bump for execution-only changes; CHANGELOG stays the
  pure concept-version log; archive visibly stale by design.
  Local rule in the bundle doc's Harvest section; promotion to
  the handbook waits for the garden rule's trigger.
- Worth remembering: the harvest was a two-hunk diff — smaller
  than any plan around it. That is the loop working: the run pays
  the hunt once, everyone downstream inherits it at birth.
- Templates question resolved at plan review: checkout-system's
  lived ground files put extraction past the don't-author-
  speculatively bar, so Step 6 (templates extracted from the
  lived run) was authored at this step's close — templates as
  master, both walkthroughs re-derived to point at them, pom
  excluded by its own convention.
- README success criterion "harvest loop run once end-to-end" is
  now met; noted in PLAN for release time.
- Resume: Step 6 (templates) — draft its change-plan: read
  checkout-system's compose/bootstrap-SQL/verify-suite/env files
  read-only, land them as pinned master templates, re-derive the
  two walkthroughs to keep whys and point at the templates
  (harvest lines record it, ADR-0007).

## 2026-08-28  (Step 4: practice executions land)

- Step 4 done in one session — ten commits, one mid-set revision,
  the change set that proved the boundaries. The pipeline is
  complete: infra-establish (+ absorbed record defaults),
  infra-serve, cbc-bootstrap under executions/ as skills, pinned
  "checked against concept v1" (ADR-0005 — practice-born
  executions get honest pins, not derives-from claims).
- The form debate, worth remembering whole: the archive ships the
  practice phases as skills driven by agent seats. At the commit-3
  boundary the over-engineering question was raised; a ten-file
  skills+agents staging was reverted unlanded. First swing: guides
  + plan-step pointers (P2 — the phases are planned, pointers at
  the moment of need fire). Counter-swing: re-entry is unplanned —
  "we need Redis now" has no plan step waiting, and a guide then
  depends on human memory (P1). Settled: skills minus agents
  (ADR-0006) — one delivery mechanism, triggers covering the
  unplanned case, the never-lived seat layer left behind.
- DEAD END: the guides-shaped revision (drafted, staged, replaced
  at the same boundary before landing). Not wasted — its P2
  reasoning survives in ADR-0006's rejected-options.
- Import fixes finally fired: the archive keeps infra-establish at
  skills/SKILL.md against its own STATUS diagram (unregisterable
  as a named skill) — normalized, recorded in headers; the
  groundskeeper's record-path defaults absorbed into the SKILL as
  a recorded addition.
- STATUS/LAYOUT stayed behind; their open/owed items are in TODO
  Later, joined by the templates idea from review: extract
  copy-and-fill templates (compose, bootstrap SQL, verify suite —
  not the pom) from the next lived run, template as master.
- Plan-prose slip caught at staging: "twelve files" where the
  enumeration said ten. Never landed; retro'd in the close.
- Resume: Step 5 (first harvest) — draft its change-plan: read
  checkout-system's Boot 4.1 testing-trap entry (read-only),
  bring it into spring-boot-walkthrough.md with run provenance,
  decide the post-import change discipline (execution changes vs
  the concept-version log) and the harvest-discipline question.

## 2026-08-28  (Step 3: executions land)

- Step 3 done in one session, seven-commit change set, none
  diverged. The derived layer exists: nine files under
  executions/ (cbc-framing and cbc-slice with their references,
  the startup snippet), each header opening "derives from concept
  v1" plus provenance @ fe0075d. A run can now be born from this
  repo's copies — executions/README.md carries the birth mapping
  and the authoritative-vs-pinned rule.
- Home decision (ADR-0004): executions/ at the repo root as
  content, not .claude/skills/ — this repo never frames or slices
  itself, the skills could only misfire here, and content commits
  would land agent-scoped. Committed the ADR before the placement
  it governs; the pattern read well at review.
- Close-read finding, marked not fixed: the two worked-example.md
  files are byte-identical — bundle design, each installed skill
  self-contained. Twin note in both headers so a change to one
  lands in both. Divergence between them would otherwise be
  invisible (agent model O1).
- Mechanical detail worth keeping: SKILL.md pin headers sit below
  the YAML frontmatter so a verbatim run-repo copy still parses
  as a skill; the pin line names the concept repo so it stays
  self-contained in a copy.
- Step 4's close read surfaced two honest questions now in its
  gate: practice-born executions may not truthfully say "derives
  from concept v1" (they grew from practice), and the archive's
  STATUS/LAYOUT companion docs need a decided fate.
- Resume: Step 4 (practice executions land) — draft its
  change-plan: import infra-establish (+ infra-serve) and
  cbc-bootstrap; decide the pin phrasing and the companion-doc
  fate; update the bundle doc; problem-framer/ stays out.

## 2026-08-28  (Step 2: concept lands)

- Step 2 done in one session, seven-commit change set, none
  diverged. The mental layer exists: five chapters at concept/,
  archive names kept, each verbatim below a provenance header
  pinned to archive fe0075d. Close read found no defects — the
  plan's provision for recorded fixes went unused. Archive concept/
  is now a historical snapshot.
- Versioning: whole-number concept versions over the mental layer
  as a whole (ADR-0003); rejected SemVer (false precision over
  prose), per-chapter versions (no consumer), commits-as-versions
  (indiscriminate). CHANGELOG is the concept-version log, opened
  at v1 = the chapters as imported. Bump rule: could it invalidate
  a derived execution.
- Repurposing the CHANGELOG stub meant replacing its rules, not
  filling them (app-repo assumptions) — fourth handbook-feedback
  entry queued in decisions.md.
- Call worth remembering: chapter provenance headers deliberately
  omit any versioning reference — the import commit landed before
  the scheme was decided, and a forward reference would have
  reverted incoherently. ADR-0003 governs; headers carry
  provenance only.
- ARCHITECTURE de-provisionalized: the Step 0 hunch held. The
  no-version-entry-no-change invariant is named a review-grade
  wall — the repo's own concept says what to think of that.
- Resume: Step 3 (executions land) — draft its change-plan:
  import cbc-framing, cbc-slice, startup snippet pinned to concept
  v1; decide the executions' home (content, not this repo's
  arrangement) and the bundle question (what a run repo copies at
  birth). Consumes docs/models/agent.md.

## 2026-08-28  (Step 1: framing)

- Framing done in one session (spanned midnight; gates closed
  2026-08-28). Six-commit change set: README framed (success
  criteria, out-of-scope, command stubs deleted — no-commands
  resolved on both sides of the agent/project split), middle steps
  authored (Steps 2–5: concept → birth-material executions →
  practice executions → first harvest), Step 1 closed.
- Read the two archive directories for the first time. Findings:
  the concept is mature — five chapters that read as the mental
  layer's seed, and their split answers the one-doc-or-several
  question (several). The executions form a pipeline: cbc-framing
  → infra-establish → cbc-bootstrap → cbc-slice, each refusing to
  run without the previous one's artifacts. The startup snippet
  cleanly separates method from project decisions.
- Finding: agents-from-practice/ holds three executions, not the
  briefed two. The third, problem-framer/, is a framing method
  from an older lab/walk lineage overlapping cbc-framing —
  excluded completely as noise at review, same status as the rest
  of the archive.
- Decisions: import order is dependency order (concept before the
  executions that pin to its version); first harvest gets its own
  early step to prove the loop; no models routing line in
  CLAUDE.md — pointers ride the steps that need them (agent model
  P2); the name held (the material itself says CbC).
- Resume: Step 2 (concept lands) — draft its change-plan: import
  the five chapters with provenance, decide the concept-version
  scheme (v1) and CHANGELOG's role, de-provisionalize
  ARCHITECTURE.

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
