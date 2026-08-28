# Plan: correctness-by-construction

<!-- Written fresh from the kit stub — no concept-repo playbook exists yet. -->

## Legend

`[ ]` planned  ·  `[~]` in progress  ·  `[x]` done (+date)  ·  `[!]` blocked (+what unblocks)  ·  `[-]` skipped (+why)

**Gate** = exit criteria: verifiable facts, not intentions. A step is done only when every gate item is true.
Detail only the next 1–2 steps finely; keep later steps coarse (rolling wave).

---

## Step 0: Bootstrap                                [x] 2026-08-27

Goal: the container exists — repo, records, arrangement — before content.
Gate:
- [x] Repo initialized; hygiene base files present.
- [x] Every placeholder filled, or explicitly deferred to a named
      step (Commands and the stack overlay defer to Framing, which
      authors the steps that fill or delete them).
- [x] No fill-comment remains: where a comment says its content
      replaces it, the content is there and the comment is not.
      Every other stub comment is a standing rule — it stays.
- [x] Briefing committed: README purpose draft + devlog entry (a) —
      names given here may change at Framing; that is what it is for.
- [x] Agent/project commit split held from the first commit: no
      commit mixes CLAUDE.md / .claude/ with the records.
- [x] Birth entry in .claude/decisions.md filled: date and the
      copy-time handbook commit.
Notes: Deferred to Framing (Step 1): Commands — CLAUDE.md's Commands
block and README's Prerequisites/Run/Test (ADR-0024); ARCHITECTURE
below the Overview (components, invariants, codemap — nothing has a
shape until content lands); CHANGELOG's role (may become the
concept-version log — its "users" are run repos pinning versions).

## Step 1: Framing                                  [x] 2026-08-28

Goal: know what we're building and why, before code.
Gate:
- [x] One-paragraph problem statement in README.
- [x] Success criteria written (how we'll know it worked).
- [x] Out-of-scope list written.
- [x] Middle steps authored and the plan sketched end-to-end once,
      coarsely — copied from a playbook (playbooks/) where one fits,
      written fresh where none does; birth materials brought with
      the briefing weigh in here.
Notes: Written fresh — no concept-repo playbook existed to copy
from. The name held (the material itself says CbC). problem-framer/
excluded as noise at review.

## Step 2: Concept lands (mental layer)             [x] 2026-08-28

Goal: the concept statement lives here as the authoritative
version, citable as concept v1.
Gate:
- [x] The five chapters imported from the archive
      (birth-materials/concept/ @ fe0075d), each with a provenance
      header. Close read found no defects — all verbatim below
      their headers, and each header says so.
- [x] Layout decided and recorded: several documents at concept/,
      archive names kept; in ARCHITECTURE's codemap.
- [x] Concept-version scheme decided, v1 identity stated: ADR-0003
      (whole-number versions over the mental layer as a whole;
      executions cite "derives from concept v1").
- [x] CHANGELOG's role decided: it is the concept-version log,
      opening at v1 (ADR-0003).
- [x] ARCHITECTURE overview no longer provisional; components,
      invariants, codemap filled for what exists.
Records: ADR-0003, provenance headers, devlog.
Notes: The CHANGELOG stub's rules had to be replaced, not filled
(app-repo assumptions) — queued as handbook feedback in
.claude/decisions.md. The archive birth-materials README was not
imported; the bundle question it answers moves to Step 3.

## Step 3: Executions land (birth materials)        [ ]

Goal: cbc-framing, cbc-slice, and the startup snippet live here,
each pinned to concept v1.
Gate:
- [ ] The three imported with the same provenance discipline as
      Step 2 (source path, archive commit, changes on import —
      fixes recorded, never silently absorbed), each stating
      "derives from concept v1".
- [ ] Executions' home decided and recorded (ADR if warranted):
      they are content this repo delivers, not its own working
      arrangement — this repo never runs cbc-framing on itself —
      so .claude/skills/ placement needs an argument, not a habit.
- [ ] The bundle question answered: what a run repo copies at
      birth and how (the archive README's job), recorded where a
      run birth will find it.
- [ ] ARCHITECTURE: executions component added, codemap updated.
Records: provenance headers, devlog, ADR if the home warrants one.
Notes: consumes docs/models/agent.md (channel and delivery
vocabulary for execution form). Own change-plan.

## Step 4: Practice executions land                 [ ]

Goal: infra-establish (+ infra-serve) and cbc-bootstrap live here,
same discipline as Step 3.
Gate:
- [ ] Same provenance and version-pinning discipline as Step 3.
- [ ] problem-framer/ stays out (excluded as noise at Framing).
Records: provenance, devlog.
Notes: coarse — detail at Step 3's close.

## Step 5: First harvest                            [ ]

Goal: the harvest loop exercised end-to-end on a real item.
Gate:
- [ ] checkout-system's Boot 4.1 testing-trap improvement recorded
      as a concept/execution change with run provenance.
- [ ] The affected execution re-derived and re-pinned.
- [ ] The harvest-discipline question answered from the lived case
      (local rules vs its own convention) and recorded.
Records: the harvest record itself, ADR or local rule, devlog.
Notes: coarse — detail at Step 4's close.

## Step N: Release                                  [ ]

Goal: concept v1 consultable — a stranger (or future-you) can
read, cite, and copy from this repo without the archive.
Gate:
- [ ] CHANGELOG entry for the release.
- [ ] README true for a stranger; any commands verified on a clean
      machine.
- [ ] Known issues filed in TODO.md, not just remembered.
Notes:

---

## Discovered along the way

<!-- Non-blocking findings. Triage each into TODO.md: assign to a step,
     park in Later, or drop. Then delete the line here. -->
- <YYYY-MM-DD> <finding> → <where it went>

## Decision index

- ADR-0001: Record architecture decisions (Step 0)
- ADR-0002: Vendor handbook models as pinned copies (Step 0)
- ADR-0003: Whole-number concept versions, logged in CHANGELOG (Step 2)

---

## Retrospective  (fill at project end)

Ran: <start> → <end>

1. Estimate vs reality — which steps took much longer/shorter, why?
2. Wrong order — what needed to happen earlier?
3. Dead ends — approaches tried and abandoned (→ playbook warnings).
4. Missing steps — work that had no home in the plan.
5. Useless gates — ceremony that caught nothing.

Then fold lessons into playbooks/<type>.md and bump its version.
