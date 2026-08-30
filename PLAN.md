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

## Step 3: Executions land (birth materials)        [x] 2026-08-28

Goal: cbc-framing, cbc-slice, and the startup snippet live here,
each pinned to concept v1.
Gate:
- [x] Nine files imported (two skills + references, the snippet)
      with the Step 2 discipline, each header opening "derives
      from concept v1". Close read found no defects; one finding
      marked, not fixed: the two worked-example.md files are
      byte-identical by bundle design — both headers carry a Twin
      note so a change to one lands in both.
- [x] Home decided and recorded: executions/ at the repo root as
      content, not .claude/skills/ (ADR-0004). SKILL.md headers
      sit below the frontmatter so run-repo copies still parse.
- [x] Bundle question answered: executions/README.md states the
      birth mapping and the authoritative-vs-pinned rule.
- [x] ARCHITECTURE: executions component, codemap row, pinning
      invariant added.
Records: ADR-0004, provenance headers, devlog.
Notes: consumed docs/models/agent.md — P2 placed the bundle doc,
the installed/content distinction shaped ADR-0004.

## Step 4: Practice executions land                 [x] 2026-08-28

Goal: infra-establish (+ infra-serve) and cbc-bootstrap live here,
same discipline as Step 3.
Gate:
- [x] Eight files imported under executions/ with the Step 3
      header discipline; two fixes recorded, never silent: the
      infra-establish layout normalized to the named-skill shape
      (the archive disagreed with its own STATUS diagram), and the
      groundskeeper record-defaults section absorbed into that
      SKILL.md.
- [x] Pin phrasing decided: practice-born executions read "checked
      against concept v1", not "derives from" (ADR-0005).
- [x] Companion docs decided: STATUS/LAYOUT stay behind — layout
      superseded by the bundle doc, open/owed items triaged to
      TODO, translation history archived.
- [x] Bundle doc updated: copy-all-at-birth, whole pipeline in the
      birth table, plan-step working advice.
- [x] problem-framer/ stayed out; the agent definitions also stay
      out (ADR-0006 — form revised at review: skills minus agents).
- [x] ARCHITECTURE: forward note removed; codemap current.
Records: ADR-0005, ADR-0006, provenance headers, devlog.
Notes: the change-plan was revised mid-set — the packaging
question (skills+agents vs guides vs skills-only) was settled at a
commit boundary, exactly what the boundaries are for.

## Step 5: First harvest                            [x] 2026-08-28

Goal: the harvest loop exercised end-to-end on a real item.
Gate:
- [x] The Boot 4.1 TestRestTemplate trap brought from
      checkout-system's decision record (2026-08-27) into
      spring-boot-walkthrough.md in the run's own wording; body
      now byte-identical to the run's lived copy; run repo read,
      never edited.
- [x] Post-import change discipline decided: the execution's
      header is its change log — one dated harvest line per
      change (ADR-0007); "changes on import" stays an import-time
      statement.
- [x] Harvest-discipline question answered: local rule in the
      bundle doc's Harvest section, ADR-0007 keeping the why;
      promotion to a handbook convention waits for the garden
      rule's trigger.
- [x] Archive staleness confirmed acceptable: the snapshot's job
      is to be visibly stale; no action.
Records: ADR-0007, the harvest header line, devlog.
Notes: the loop the repo exists for has now run once end-to-end —
the README success criterion is met by this step.

## Step 6: Templates extracted from the lived run   [x] 2026-08-28

Goal: the repeating ground and harness files exist here as
copy-and-fill templates, so no run re-derives them from prose.
Gate:
- [x] Sources read read-only from checkout-system's lived files.
- [x] Seven templates landed as master copies with pin+provenance
      headers in each file's own comment syntax: compose.yaml,
      bootstrap.sql, verify-database-model.sql, .env.example,
      flyway.conf (infra-establish); testcontainers.properties,
      application.yaml (cbc-bootstrap). flyway.conf and
      application.yaml joined the original five at plan review.
      Not the pom (its convention refuses code ahead of earning);
      not the test-support Java (TODO Later, second-run trigger).
- [x] Both walkthroughs re-derived: whys and traps kept, embedded
      file bodies replaced by pointers; off-template rule and
      fill-trail line added at boundary review; Re-derived and
      Harvested header lines record it (ADR-0007). A second
      harvest landed en route: .env's fourth key, the runtime
      application password, from the lived .env.example.
- [x] Bundle doc updated: Templates paragraph — birth, fill, and
      harvest relations.
- [x] ARCHITECTURE current: executions component names the
      templates; no codemap change — templates live inside their
      skills (ADR-0008). Archive invariant marked retired.
Records: ADR-0008, provenance headers, harvest lines, devlog.
Notes: own change-plan. Authored at Step 5's close —
checkout-system makes the extraction lived, not speculative, and
ADR-0007 gives it its discipline.

## Step N: Release                                  [ ]

Goal: concept v1 consultable — a stranger (or future-you) can
read, cite, and copy from this repo without the archive.
Gate:
- [ ] CHANGELOG entry for the release.
- [ ] README true for a stranger; any commands verified on a clean
      machine.
- [ ] Known issues filed in TODO.md, not just remembered.
Notes: the success criterion "harvest loop run once end-to-end"
was met at Step 5.

---

## Discovered along the way

<!-- Non-blocking findings. Triage each into TODO.md: assign to a step,
     park in Later, or drop. Then delete the line here. -->
- <YYYY-MM-DD> <finding> → <where it went>

## Decision index

- ADR-0001: Record architecture decisions (Step 0)
- ADR-0002: Vendor handbook models as pinned copies (Step 0)
- ADR-0003: Whole-number concept versions, logged in CHANGELOG (Step 2)
- ADR-0004: Executions live as content under executions/ (Step 3)
- ADR-0005: Practice-born executions pin as checked-against (Step 4)
- ADR-0006: Practice executions as skills, without agent seats (Step 4)
- ADR-0007: Harvest discipline for executions (Step 5)
- ADR-0008: Templates live inside their skill (Step 6)
- ADR-0009: CbC delivered as an overlay on the handbook kit

---

## Retrospective  (fill at project end)

Ran: <start> → <end>

1. Estimate vs reality — which steps took much longer/shorter, why?
2. Wrong order — what needed to happen earlier?
3. Dead ends — approaches tried and abandoned (→ playbook warnings).
4. Missing steps — work that had no home in the plan.
5. Useless gates — ceremony that caught nothing.

Then fold lessons into playbooks/<type>.md and bump its version.
