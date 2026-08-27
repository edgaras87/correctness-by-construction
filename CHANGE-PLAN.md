# Change-plan: bootstrap correctness-by-construction (PLAN.md Step 0)

## Summary — the state after all commits

The container exists and is committed: the working arrangement
(CLAUDE.md, .claude/) lands first with its birth entry dated, the
record stubs from the starter kit land filled with this project's
content, the handbook's two models (tiers, agent) arrive as pinned
copies under docs/models/, and PLAN.md Step 0 is closed against its
gate. No concept content is in yet — importing the archive's birth
materials and agents-from-practice executions is project work,
planned at Framing as its own change set. What the repo gains: a
purpose a stranger can read in README, the briefing preserved in the
devlog, the open questions and the first harvest candidate on record
in TODO.md instead of in a head, the workspace's tier picture and
the agent channel model available locally for Framing and for
execution authoring, and a provisional statement of the repo's shape
in ARCHITECTURE.md that points at the tiers model instead of
restating it.

## Commits

**1. `docs(agent): add change-plan for bootstrap`**
The approved plan, committed after agreement and before any work, so
the series can be read against it afterwards (change-plans §4).

**2. `chore(agent): install working arrangement`**
CLAUDE.md and .claude/ (skills verbatim from the kit; decisions.md
birth entry dated 2026-08-27, handbook commit 4fe8083 already pinned
at copy time). CLAUDE.md: title filled; Commands block left as stub
(defers to Framing with the rest of the commands question); the
conventions placeholder line and the empty "How to work here" /
"Local rules" sections deleted. decisions.md also gets one new
entry: this set installs the arrangement *before* the project
records, deviating from the kit stub's prescribed order (see
Decisions) — logged so the retrospective can carry it back to the
handbook. Separate from the records commits because no commit mixes
agent paths with project records (commit-messages, "Scope note").

**3. `docs: add project records filled from briefing`**
Lands the kit's project-record stubs with their placeholders filled:

- `README.md` — title `correctness-by-construction`; purpose
  paragraph drafted from the briefing (one authoritative home for the
  concept: plain-words statement, rationale, open questions, log of
  what changed it; middle tier of handbook → concepts → runs;
  executions derived from the concept for use in run repos).
  Prerequisites/Run/Test left as stubs — Commands defer to Framing
  (ADR-0024, named in the Step 0 gate).
- `PLAN.md` — title filled; provenance comment resolved to "written
  fresh from the kit stub — no concept-repo playbook exists yet".
  Step 0 stays `[~]`; deferrals recorded in Step 0 Notes (see
  Decisions below).
- `devlog/devlog.md` — entry (a), 2026-08-27: the briefing in its
  own words — problem, hunches (mental layer / executions split,
  runs pinned to concept versions, harvest loop), existing material
  paths, first harvest candidate, done-ish, open questions. Resume
  line points at Framing.
- `TODO.md` — seeded: **Next** — import birth materials and
  agents-from-practice from the archive (step placement is Framing's
  call); harvest candidate — checkout-system's decisions log records
  a Boot 4.1 testing-trap improvement its archive copy lacks.
  **Later** — the three open questions (concept-version granularity;
  harvest/provenance as local rules vs its own convention; mental
  layer as one document or several).
- `ARCHITECTURE.md` — Overview paragraph filled provisionally: what
  this repo is (one concept repo on the concepts tier, mental layer
  plus derived executions), pointing at `docs/models/tiers.md` for
  the workspace picture rather than restating it (agent model M1:
  hand-written summaries are lossy). Diagram reduced to the two
  layers and the pin/harvest flows; Components/Invariants/Codemap
  defer to Framing.
- `CHANGELOG.md` — lands as-is; its role is deferred (Decisions).
- `docs/adr/0001` — date filled (2026-08-27).
- `playbooks/TEMPLATE.md` — lands as-is (retrospective folds lessons
  into a playbook; a concept-repo playbook may be born here).

**4. `docs: vendor handbook models as pinned copies`**
`docs/models/tiers.md` and `docs/models/agent.md`, copied from
`engineering-handbook/models/` with a provenance header each (source
path, handbook commit at copy time, DRAFT status preserved), plus
`docs/adr/0002` recording the decision and the rejected options.
One step because the ADR explains the copies' presence — reverting
either alone leaves the repo incoherent (change-plans §3). Why this
repo needs them: the tiers model is the stated picture behind this
repo's whole shape (Framing reasons against it), and the agent model
is the design vocabulary for the executions this repo exists to
derive (skills, checklists — channel choice, delivery, claims).

**5. `docs: close Step 0 in PLAN`**
Every gate item is verifiable only after commits 2–4 exist, so the
close is its own commit: gate boxes checked, Step 0 `[x]` 2026-08-27,
the spent bootstrap instruction comment removed (it is scaffolding
for a one-time event, not a standing rule).

**6. `docs(agent): close change-plan for bootstrap`**
Deletes this file; the commit body records what diverged from plan,
or that nothing did.

## Decisions taken inside this plan

- **Agent install lands before the project records**, deviating from
  the kit stub's prescribed order (plan open → project records →
  agent install → plan close). Mechanically nothing depends on the
  order — the files are in the working tree either way — but the
  arrangement that governs the series belongs on record before the
  work it governs, and the two agent commits then sit together at
  the head of the set. The deviation is logged in .claude/decisions.md
  as handbook feedback (the stub's comment may want updating).
- **The handbook models are vendored, pinned, project-side.**
  Vendored rather than referenced: the tiers model itself rules that
  nothing downstream tracks upstream by reference — delivery is a
  pinned copy. Rather than summarized: agent model M1/M2 — a
  hand-written summary is lossy on arrival and can drift while both
  files look current. Project-side (`docs/models/`, not `.claude/`)
  because here they are reference material for the project's own
  deliverables — executions are this repo's *content*, so the model
  that informs their design is project reference, not arrangement.
  ADR-0002 records this; the pin hash is read from the handbook's
  HEAD at copy time.
- **Six commits, not the stub's four.** Beyond the reorder: closing
  Step 0 edits PLAN.md — a project record — and the change-plan
  close is agent-scoped; the split rule forbids mixing them, so the
  step close is its own commit. The models delivery is its own step
  by the revert test.
- **All six records kept; none deleted.** For a concept repo each
  still answers its question — with two roles deferred to Framing:
  CHANGELOG.md may become the concept-version log ("users" here are
  run repos pinning versions), and ARCHITECTURE.md describes the
  repo's tier shape rather than code. Both deferrals are written
  into Step 0 Notes so the gate's "explicitly deferred to a named
  step" is on record.
- **`playbooks/backend-service.md` is not landed** (stays deleted).
  It is a playbook for a different project type and would be noise
  here; TEMPLATE.md stays. Recoverable from the handbook if wrong.
- **ARCHITECTURE Overview filled now, not deferred.** The
  fill-comment gate is absolute ("the content is there and the
  comment is not"), and the briefing plus the tiers model give
  enough for a deliberately provisional paragraph. Everything below
  Overview defers.
- **CLAUDE.md "How to work here" and "Local rules" deleted** rather
  than deferred: no content exists for either. Local rules may
  return if Framing decides harvest/provenance discipline is local
  rules — that open question lives in TODO.md, so the trail is kept.
- **No archive material is read or imported in this change set.**
  The briefing calls the import project work; it weighs in at
  Framing (PLAN Step 1 gate already names birth materials) and gets
  its own change plan there.
- **Names are provisional.** Repo and record names may change at
  Framing; the Step 0 gate says that is what the briefing commit is
  for.
