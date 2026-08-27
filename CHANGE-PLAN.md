# Change-plan: framing (PLAN.md Step 1)

## Summary — the state after all commits

The project is framed: README states the problem, the success
criteria, and the out-of-scope list; PLAN.md carries the middle
steps end-to-end for the first time — concept lands, then the two
birth-material executions, then the practice executions, then the
first harvest — and Step 1 is closed against its gate. The Commands
deferral from Step 0 is resolved (this repo has no commands; the
stubs are deleted on both sides of the agent/project split). The
import work itself does NOT happen in this change set — each import
step runs later, under its own change-plan, per the briefing. What
framing adds is the knowledge the archive reading produced: what the
material actually is, what order it can land in, and what was found
that the briefing did not know (a third practice execution,
problem-framer).

## Commits

**1. `docs(agent): add change-plan for framing`**
The approved plan, committed after agreement, before the work
(change-plans §4).

**2. `docs: frame the project in README`**
The Step 1 gate's three README items:

- Problem statement: the existing purpose paragraph stands as the
  problem statement (it already says what this is, for whom, and
  why) — reviewed here rather than rewritten.
- **Success criteria** (new section): (1) the concept statement
  here is the single authoritative version — the archive copy is
  demoted to a historical snapshot; (2) the harvest loop has run
  end-to-end at least once — a real run's surprise recorded as a
  concept change with provenance and the affected execution
  re-derived (the checkout-system Boot 4.1 trap is queued as the
  first); (3) at least one new run is born from executions copied
  from this repo, not from the archive; (4) months-scale: the
  concept doc is consulted and updated after runs — the briefing's
  own done-ish.
- **Out of scope** (new section): running projects or experiments
  here (runs tier); authoring method or working-arrangement
  conventions (handbook's); garden machinery until the garden rule
  triggers (a second concept repo, a rule written twice);
  graduating an execution to its own concept repo (same named
  trigger); everything in the archive repo outside the two named
  directories.
- Prerequisites/Run/Test sections deleted — the Commands deferral
  resolved: a documents-only repo has no build/run/test commands
  (ADR-0024 assigned the call to Framing; this is the call).

**3. `chore(agent): drop Commands block from CLAUDE.md`**
The agent-side half of the same resolution — separate commit because
no commit mixes agent paths with project records. Also removes the
Step-0 parked question by settling it: CLAUDE.md gets no models
routing line; the moment-of-need pointers ride inside the middle
steps authored in commit 4 (agent model P2: a pointer at the moment
of need beats the same pointer in a session-start list).

**4. `docs: author middle steps in PLAN, triage TODO`**
Steps 2–5 written into PLAN.md, coarse per rolling wave (next step
fine, later steps coarse), each with goal, gate, records expected,
and pointers to the material and models it consumes:

- **Step 2 — Concept lands (mental layer).** The five chapters
  imported as the authoritative statement, layout decided (the
  archive's split answers "one document or several": several),
  provenance recorded, the concept-version scheme decided (the
  imported-and-fixed state becomes concept v1), CHANGELOG's role
  decided with it (the deferred question lands in this step: it is
  the natural home for the concept-version log).
- **Step 3 — Birth-material executions land.** cbc-framing,
  cbc-slice, the startup snippet; each stating "derives from
  concept v1"; import fixes recorded, not silently absorbed.
- **Step 4 — Practice executions land.** infra-establish (+
  infra-serve) and cbc-bootstrap, same provenance discipline.
  problem-framer/ is excluded as noise (reviewer's call — see
  Decisions).
- **Step 5 — First harvest.** The checkout-system Boot 4.1
  testing-trap improvement harvested: concept/execution updated
  with run provenance, execution re-derived, and the
  harvest/provenance open question answered from the lived case
  (local rules vs its own convention).
- **Step N — Release** reframed as "concept v1 consultable": kept
  gates plus a CHANGELOG entry for v1.

TODO triaged in the same commit (its own rule: assign each item to
a step): the import items assigned to Steps 2–4, the harvest
candidate to Step 5, the mental-layer open question closed by
Step 2's authoring.

**5. `docs: close Step 1 in PLAN`**
Gate check against the landed commits: problem statement ✓ (commit
2), success criteria ✓, out-of-scope ✓, middle steps authored and
the plan sketched end-to-end once ✓ (commit 4). Step 1 `[x]`.

**6. `docs(agent): close change-plan for framing`**
Deletes this file; body records what diverged.

## Decisions taken inside this plan

- **The name holds.** Framing had license to rename; the archive
  material itself calls the concept correctness-by-construction
  (CbC), so the working name is confirmed, not changed.
- **Commands: none.** A documents-only repo. README loses
  Prerequisites/Run/Test, CLAUDE.md loses the Commands block. If a
  derive/check script ever appears, the sections return with it.
- **Import order is dependency order.** Concept before executions —
  an execution states which concept version it derives from, so the
  version must exist first. Practice executions after
  birth-material ones: they sit further down the pipeline and their
  import questions (e.g. problem-framer) are heavier.
- **problem-framer is skipped completely.** Found during reading —
  a third directory under agents-from-practice/ the briefing did
  not name. The reviewer's verdict: it is noise, same status as the
  rest of the archive repo; it duplicates cbc-framing's territory
  from an older lineage. Not imported, not parked in TODO — the
  two named practice executions are the import set.
- **First harvest is its own step, early.** The harvest loop is
  this repo's core mechanism; exercising it once, end-to-end, on a
  real queued item proves the machinery while the import is fresh —
  and produces the evidence the harvest-discipline question needs.
- **No models line in CLAUDE.md.** The parked P2 question resolved:
  pointers ride the steps that need them (Step 2 points at
  tiers.md; Steps 3–4 point at agent.md for execution authoring).
- **ARCHITECTURE stays as-is this set.** Its sections fill at Steps
  2–4 as the shape becomes real ("update trigger: a step's gate
  closes and this no longer matches reality") — not speculatively
  at framing. Same for the ARCHITECTURE-vs-docs-repo handbook
  question: answered at those steps with evidence.
- **The briefing's "two executions" count is trusted over the
  directory's three.** The devlog session entry notes the finding
  and the verdict in one line, so a future reader of the archive
  is not surprised — nothing more.
