# Devlog

<!-- Newest entries on top. 2–5 minutes at the end of each session.
     For future-you: fragments fine, honesty mandatory. Never clean up.
     Mark dead ends loudly with "DEAD END:" so they're greppable.
     End every session with a "Resume:" line — cheapest save-point there is.
     When this file gets long, split into devlog/2026-08.md per month. -->

## 2026-08-29  (session: framing check run 2 — safe-reservations read)

- Run 2 of the TODO framing check executed: the safe-reservations
  problem-framing-node read in full, read-only, at
  archive .../worksites/safe-reservations/problem-framing-node. The
  custom maintenance language (walks, labs, forks, flow-back,
  D/F-numbers) identified and ignored throughout; underneath it the
  node is the method's birthplace — our skill is its distillation,
  so the check became "what did the distillation lose."
- Origin fact worth keeping: the walk log records why the
  every-verdict-human rule exists — an informal walk 0 where the
  agent derived competently but the human "did not control the
  process and did not see the decisions being taken." The rule's
  lived origin; checkout later proved recorded delegation workable.
  Both stances now sit in our skill (default + delegated mode).
- Harvest candidates banked (verdicts owed, none landed yet):
  (1) probe machinery as teachable procedure — three lenses
  (assumption hunt / stretched timeline / resource grid), the
  three-stamp rule (new fact · nothing new naming the covering
  line · out of scope written), the audit checklist for verifying
  the framer without re-deriving — born from the user's own demand;
  (2) numbered fences (W-list) for written-out scope, visibly doing
  work at step 3; (3) the "not probed" honest ledger; (4) scope
  verdicts as a named step-2 output, each with recommendation and
  reason; (5) richer intent shape — audience (claim-buyer vs
  consumers), worth-proving, what done demonstrably means;
  (6) registry refinements beyond checkout's — adversity-class
  grouping as headings-never-boundaries, riders whose silent
  violation voids a slice's evidence, evidence-shape flags, the
  written zero; (7) step 6 as three visible passes (sort with a
  because per stamp → pairwise dedupe → folds); (8) a two-tier
  harvest idea (sure adoptions vs held insights with a promotion
  path) beside ADR-0007; (9) a small define phase (project name,
  repo name, repo description, decided with verdicts) between
  framing and bootstrap — currently covered by no skill.
- Evidence for the record-shape decision (TODO item): the lived
  pipeline was per-step pairs (completion = what the step earned,
  pure, verdict-closed, feeds the next step; derivation = how it
  ran, kept for audit) → at close composed into the three exports
  by a written export plan — committed to the project repo in
  derivation order, eight commits, so the project's git history
  tells the derivation story — under a residue filter: no lab
  vocabulary or paths ever project-side, conclusions re-grounded.
  The user's one-doc-translated-at-close idea matches the
  composition half; the open half is whether the working record is
  one growing doc or per-step files.
- Doc-projection confirmed real and separate (model + guide live in
  the node; README derived from internal masters at milestones) —
  stays parked in TODO as its own later check.
- Resume: the record-shape decision (options + recommendation),
  then the harvest change-plan for the banked candidates, then
  doc-projection.

## 2026-08-29  (session: framing check run 1 — checkout harvested)

- The TODO framing-check direction opened (24f9e5f queued it) and
  run 1 of 2 executed: checkout-system's framing artifacts read
  read-only against the cbc-framing skill. Verdict: no violations —
  every per-step gate checkably satisfied, terminology fully ours.
  Five lived-beyond-the-skill findings; four harvested as a
  seven-commit change set (aaad989 plan → bba4755 registry
  template + skill-side outcomes → 01e9422 living exports with
  logged revisions → d87a4ed recorded saturation log → b30e76e
  labeled trust list → c365890 delegated-verdict mode → db06098
  close, no divergence), user reviewing at each boundary.
- The delegation decision, since it changes how future auto runs
  read the skill: human verdicts stay the default; a run may
  delegate only via an explicit decision in its own
  .claude/decisions.md naming the delegation and its cost. A config
  flag was rejected — it would hide a decision that must stay
  visible. The user plans more fully-auto runs; this is the
  sanctioned path.
- Finding 2 deliberately NOT harvested: checkout already splits
  pure exports from derivation record (ADR-0002 carries the kill
  list), but the record is thin — the process itself is lost. Held
  as evidence for the one-derivation-doc-translated-to-three-exports
  decision, parked in TODO until safe-reservations (run 2) is read.
- Resume: framing check run 2 — safe-reservations at
  archive .../worksites/safe-reservations/problem-framing-node,
  read-only, old custom language distinguished and never adopted;
  then the record-shape decision; then the doc-projection node.

## 2026-08-29  (session: app-structure reference adopted)

- Yesterday's parked decision decided: adopt. Four-commit change
  set landed (plan → reference → walkthrough routing → close),
  the user reviewing at each boundary. app-structure.md now sits
  in cbc-bootstrap/references: the lived default authoritative
  (package-by-feature, package-private, depth earned per feature —
  harvested from checkout's nine slices), the decision rule
  (decided at bootstrap, logged with its why; a stated practice
  intent is a legitimate deciding input), and the four named
  alternatives in two lines each, all marked unlived. The
  slice-reach question resolved without coupling skills: the
  decision travels through the run's own log, which slice work
  already operates under; the doc states its reach in one line.
- CORRECTION, recorded as a new fact (the old entry stands —
  never clean up): the previous entry refers to a TODO Later
  trigger line "parked 2026-08-28". That line was never committed
  — the in-session claim was made without the edit actually
  happening; only the postgres tag-drift note (e783a33) was real.
  Nothing existed to absorb; the change-plan and its close carry
  the same statement.
- Standing expectations after this set: the next run tests the
  harness reference on the lived stack line and the default
  structure (one variable at a time); the first run to live an
  alternative structure upgrades its vocabulary entry with a
  harvest line.
- Resume: Step N (release) remains the next PLAN step.

## 2026-08-29  (session: app-structure question opened, undecided)

- Q&A session, no change set. Discussed application structure
  against checkout's lived shape (package-by-feature,
  package-private boundaries, depth earned per feature): classic
  layered, hexagonal/onion/clean, vertical slice, modular monolith
  named and weighed. Two positions reached, neither enacted yet:
  structure is a bootstrap decision recorded like the stack
  decision (default = the lived shape; a named pattern is legal
  when the run's log carries the why — practicing a pattern counts
  as a deciding input if stated); and a short app-structure
  reference in cbc-bootstrap/references likely earns its place —
  decision hook + recall + user↔agent shared vocabulary, NOT a
  patterns survey (pros/cons essays stay re-derivable). If adopted
  it absorbs the TODO Later trigger line parked 2026-08-28.
- The user's closing observation, not to lose: the structure
  choice also shapes how slice work writes code against its
  planned requirements — so the decision's reach is beyond
  bootstrap. Weigh tomorrow whether the reference (or the run-log
  decision it prescribes) needs routing where cbc-slice work sees
  it, not only at bootstrap.
- Resume: decide the app-structure reference — yes/no, its home,
  its pointers (including the slice-side reach above); if yes, run
  it as a change set. Next PLAN step remains Step N (release).

## 2026-08-28  (post-Step 6: the harness reference adopted)

- Two workbench-era docs handed over (temp/, uncommitted, deleted
  after use). The pom convention was superseded — our Step 4 import
  is its cleaned descendant; diffed section by section, nothing to
  take. The harness reference was the find: the stage 4–5 recurring
  artifacts as code, exactly the test-support gap TODO'd in Later.
- ADR-0008's second-run trigger judged fired: the doc itself proves
  two pre-repo passes, checkout-system re-derived the shape a third
  time. Landed as a *reference* (imitated, never pasted) —
  ADR-0008's own boundary, not a rule change. spring-harness-
  reference.md now sits beside the walkthrough, which routes to it
  from stages 4–5.
- The confirmation pass against checkout's bootstrap (read-only,
  d732b53 and 83262b5) corrected the handed doc in five places —
  the load-bearing one: the container as a faithful miniature
  carrying the ground's authority split (bootstrap.sql mounted,
  migrate as migrator, context as runtime, identity asserted);
  the second pass had run the whole harness as the Testcontainers
  superuser. Also: two bases not three; MigrationPathIT joins the
  set; the probe round-trips current_user; the pool is sized to
  the count. The old virtual-threads claim and the
  failOnMissingLocations guard survive as variation points, each
  attributed to the pass that lived it.
- The old maintenance language (genre labels, workbench mastering,
  flow-back, node/seat vocabulary) stripped on import, per the
  standing rule from the earlier archive read: identify, never
  adopt.
- Resume: Step N (release) still next in PLAN.

## 2026-08-28  (post-Step 6: harvest from the archived run)

- On request, read safe-reservations' project-replica (the run that
  predates this repo, in the ai-context-system archive worksite) —
  read-only, fenced to that one directory — and compared it against
  all seven template masters. Verdict: the old run is the templates'
  ancestor, same lineage through checkout-system; every divergence
  bar two was our later decision already. Its own maintenance
  language (worksite/node/replica layout, numbered log entries, the
  internal-masters doctrine) identified and deliberately not
  adopted; the shared ground vocabulary (Execution Environment,
  service constraints) already lives here via infra-establish.
- The two divergences worth keeping harvested as their own change
  set (ADR-0007), four commits, nothing diverged: the verify
  suite's \echo banners and readable object-type names; the runtime
  password key renamed <PROJECT>_RUNTIME_PASSWORD across
  .env.example and application.yaml (one commit — declaring and
  reading sides of one key). The masters now diverge from
  checkout-system's lived key by intent; its copy picks the rename
  up only by copying anew. Non-adopted divergences are named in the
  verify master's harvest line, so the question does not reopen.
- Resume: Step N (release) is still the next PLAN step.

## 2026-08-28  (Step 6: templates from the lived run)

- Step 6 done in one session, nine commits, none diverged. Seven
  copy-and-fill masters now live inside their skills (five under
  infra-establish/templates/, two under cbc-bootstrap/templates/),
  each verified by substituting checkout's identities back in and
  diffing against the lived file — deltas matched the declared
  generalizations exactly. Both walkthroughs shrank to whys, traps,
  and pointers; the bodies live once.
- ADR-0008 got the load-bearing distinctions: templates ride inside
  the skill (self-containment); a fill becomes the run's own file,
  not a pinned copy; fills never harvest back, shape changes do;
  and the boundary rule — imitated content stays an example under
  references/, pasted content becomes a template, application
  source is neither until a second run re-derives the same shape
  (test-support Java parked in TODO Later on that trigger).
- The blind-trust question at review produced the off-template
  rule (assumptions differ → derive from the model, record, expect
  a harvest — never bend a decided constraint to fit a template)
  and the fill-trail line in the handoff. The guards that already
  existed: decisions upstream of templates, Verified: gates
  downstream, harvest loop around it all.
- Second harvest landed en route: the lived .env carries a fourth
  key (runtime application password) the walkthrough predated.
  Extraction also surfaced a run inconsistency (CHECKOUT_DB_PORT
  vs POSTGRES_PORT) — kept as lived in the templates, TODO'd:
  fix in the run first, then harvest.
- Also this session, advisory: close read confirmed
  the-whole-system-in-plain.md agrees with concept v1 (four minor
  compressions noted, no rewrite owed); archive deprecation needs
  no header changes — the headers already deny it authority —
  frozen beats deleted so pins stay checkable; ARCHITECTURE
  invariant now says retired.
- Resume: Step N (Release) — CHANGELOG release entry, README true
  for a stranger, known issues filed in TODO. The harvest-loop
  success criterion was met at Step 5; templates were the last
  authored step.

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
