# Change-plan: concept lands (PLAN Step 2)

## Summary — the state after all commits

The mental layer exists: the five concept chapters live in `concept/`
at the repo root, each under a provenance header naming its archive
source, the archive commit, and what changed on the way in. The
concept is citable as **v1**: ADR-0003 defines what a concept version
is and how executions cite one, and CHANGELOG.md is repurposed as the
concept-version log, opening with the v1 entry. ARCHITECTURE is no
longer provisional — overview confirmed, mental-layer component and
codemap filled. PLAN Step 2 is closed and Step 3 (executions land) is
detailed finely. The archive's concept/ directory is, from this point,
a historical snapshot: this repo is the authoritative statement.

## Commits

**1. `docs(agent): add change-plan for concept import`**
The approved plan, committed before work so the series can be read
against it.

**2. `docs(concept): import concept chapters from archive`**
`concept/00-cbc.md` … `04-cbc-slice.md`, copied from
`archive/cbc/system-design-method/birth-materials/concept/` @
`fe0075d`, each with a provenance header (source path, archive
commit, import date, changes on import). Content otherwise verbatim
unless the close read reveals a defect — any fix is named in the
header, never silently absorbed. Archive filenames and numbering
kept: the numbers encode reading order, and identical names keep the
archive mapping checkable. The birth-materials README is *not*
imported — it describes the copy-me bundle for run repos, which is
Step 3's question.

**3. `docs: adopt concept versioning, declare v1`**
ADR-0003 (concept versioning scheme) plus CHANGELOG.md carrying the
decision: header amended to say versions here are concept versions,
and the v1 entry written. One step because reverting the ADR alone
would leave the CHANGELOG using a scheme no record decided.

**4. `docs(agent): queue CHANGELOG stub feedback for handbook`**
A .claude/decisions.md entry: the kit's CHANGELOG stub assumes an
application repo (SemVer, user-facing categories); a concept repo
repurposes it as the concept-version log. Evidence for the handbook
that the stub may want a per-repo-type variant. Own commit — the
agent/project split forbids mixing .claude/ with project records.

**5. `docs: de-provisionalize architecture`**
Overview's provisional marker dropped (the Step 0 hunch held).
Components gains the mental layer (executions arrive Steps 3–4 and
are added then — ARCHITECTURE describes the system as it is).
Codemap filled: `concept/`, `docs/models/`, `docs/adr/`, records.
This is where the layout decision (several documents, at `concept/`)
is recorded, satisfying that gate item.

**6. `docs: close Step 2 in PLAN, detail Step 3`**
Gate items checked with the dates and facts that make them true;
Notes record what the import surfaced. Step 3 detailed finely per
rolling wave (its Notes say "detail at Step 2's close"). TODO's
Step 2 line removed. One step: the plan rolling forward is one
coherent change.

**7. `docs(agent): close change-plan for concept import`**
Deletes this file; body is the retrospective — what diverged, or
that nothing did.

## Decisions taken inside this plan

- **Layout: `concept/` at repo root, archive names kept.** The
  mental layer is this repo's primary content, so it does not hide
  under `docs/` (which holds support material: vendored models,
  ADRs). Several documents, as the archive's own split already
  answered at Framing.
- **Concept version = whole-number tag over the mental layer as a
  whole** (v1, v2, …). Executions derive from the concept as a unit,
  so per-chapter versions would multiply pinning bookkeeping with no
  consumer, and SemVer's compatibility semantics don't map to prose.
  A bump is any change that could invalidate a derived execution;
  editorial fixes that couldn't, don't bump. Full reasoning and
  rejected options go in ADR-0003.
- **CHANGELOG is the concept-version log** (resolving the Step 0
  deferral). Its "users" are run repos and executions pinning
  versions; each entry says what changed in the concept, why (run
  provenance when harvested), and which executions were re-derived.
- **v1 identity: the five chapters as imported** — the archive
  statement, unchanged in substance. Declared in CHANGELOG's v1
  entry; executions will cite "concept v1" in their provenance
  headers (Step 3).
- **Provenance pins the archive HEAD at copy time** (`fe0075d`, tree
  clean), same pattern as the vendored handbook models — "copied
  from state X", not "content last touched at X".
