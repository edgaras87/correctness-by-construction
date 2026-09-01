# TODO

<!-- Add items the moment they're discovered — that's what empties your head.
     Triage when closing a step or weekly. Prune "Later" ruthlessly:
     deleting an idea you'd re-derive anyway costs nothing.
     Rule: inline TODO:/FIXME: comments in code must reference an item here. -->

## Now (current plan step)

- [ ] Next handbook handoff — queued 2026-09-01, deliver when the
      bundle-side set closes (more may accrue there). Two items:
      1. Injection friction log — the field data their return item
         11 asked back, from the first live convention injection
         (change-plans @ 65dd7ee): the copy is also a rename
         (CONVENTION.md → SKILL.md); the byte-identity claim
         needed a diff mandated before overwrite; whether an
         injection needs a change-plan is unstated (we judged no:
         independent mechanical commits); whether the injection
         entry may ride the overwrite commit is unstated (our
         decisions log's standing rule says no); the records-table
         row text came without a table position; frontmatter
         compatibility worked only because the convention file is
         authored skill-shaped — a written procedure must check
         each of these, not inherit our luck.
      2. default.md naming collision: starter/installs/default.md
         (the handbook's own direction — a bundle manual) and
         starter/kit/playbooks/default.md (the bare sequence — the
         absence of direction) share a name meaning opposite
         things. Their own reply used the bare name in context and
         disambiguation cost a session detour. Suggest renaming
         one side; their call which.
- [ ] Re-birth under the scenario, after the bundle-side set
      closes: safe-reservations (born
      2026-08-30, zero project commits) stopped and discarded
      2026-08-31 — the birth design changed under it
      (executions/birth-scenario.md trial); deleting the born repo
      is the user's act, outside this repo. Surviving, held for
      the re-birth: the briefing (deliberately baseline-blind) —
      the re-birth takes it unchanged, so the scenario's first
      walk is a fair test — and the standing protocol below.
      Standing protocol, owned here, not by the run: the run is a
      blind replication of safe-reservations-v1 (archived) — its
      briefing omits the baseline deliberately so the derivation
      cannot steer by it. This repo opens both repos at phase
      closes (framing, ground, bootstrap, each slice stage),
      records the deltas here, and judges run 1's held insights at
      those readings (their named promotion path). The baseline at
      ~/IdeaProjects/safe-reservations-v1 stays read-only.

## Next (upcoming steps — assign each to a step when triaged)

- [ ] Bundle-side set — unblocked 2026-09-01 by the handbook
      reply; designed against the slimmed stubs and the starter
      redesign (their ADR-0026/0028). Two halves, one set:
      (a) Moment-of-need reintroduction: infra-establish gains the
      README Prerequisites step when the ground stands,
      cbc-bootstrap gains Run/Test when the harness is real, with
      the section skeletons as template fragments inside each
      skill (ADR-0008). Wording discipline (their return item 9):
      restate the stub rule only in the adopted form — container
      stays, direction goes.
      (b) cbc-run playbook rebuilt as a full sequence on
      playbooks/default.md's base: kit endpoint steps
      (Bootstrap/Framing/Release) vendored with provenance and
      pin, specialized never weakened; our harvested middles
      (Define, Ground, harness Bootstrap, Slices) inserted
      unchanged; the ownership decision lands as the set's
      Proposed ADR. The bundle README's playbook-usage lines
      (table row "copied at Framing", Birth step 6) update in the
      same set — deferred from the absorption set because the
      master was still middles-shaped.
- [ ] Playbook overlap, fires at the next birth (return handoff
      item 6): the kit ships playbooks/backend-service.md, the
      bundle overlays cbc-run.md beside it — the born project holds
      two playbooks and its Framing must know whether to copy from
      one, both, or merge. The handbook holds the same question
      from its side; the trigger fires at our birth, where the
      handbook is not in the room. Decide there, in the room, and
      note the outcome on both sides. (2026-09-01) The starter
      redesign likely dissolves this: playbooks now hold full
      sequences, one chosen and copied whole at birth — a CbC
      birth chooses cbc-run.md and the others stay uncopied.
      Confirm at the birth; still note the outcome both sides.

## Later / someday

- [ ] Prebuilt CbC stub — a cache of the birth scenario's output,
      versioned, so a birth becomes one copy plus a briefing with
      a single composite pin. Parked with its trigger: when births
      come faster than harvests. Until then the cache would be
      stale more often than used, and the scenario walks fresh
      from the masters (2026-08-31 discussion; the ADR-0009
      objection weakens when the stub is derived by a written
      scenario, but the staleness cost stands).
- [ ] First lived use of the practice skills in their imported form
      is owed (archive STATUS: they are distillations, exercised as
      agent-driven skills never, as skills-without-agents never) —
      expect corrections; harvest them when they come.
- [ ] Second service family: when a non-PostgreSQL service first
      gets stood up in a run, decide whether it earns its own
      walkthrough beside postgres-setup-walkthrough.md (the test:
      long, sequenced, likely to recur).
- [ ] Trigger descriptions of the practice skills are unoptimized
      (archive STATUS); if they under- or over-fire in runs, the
      descriptions are the knob.
- [ ] The postgres image tag floats: the ground template and the
      harness reference both say postgres:17, so ground and harness
      can pull different minors at different times — noticed while
      discussing the harness reference. If a run ever hits a
      minor-drift surprise, decide whether both should pin tighter
      (full version or digest); until then the shared major is the
      deliberate coupling.
- [ ] Two-tier harvest idea, from safe-reservations' close: its
      flow-back split sure adoptions (landed in the masters) from
      insights held as evidence with a named promotion path (the
      next run's comparison confirms or kills them). ADR-0007 has
      only the first tier. Consider whether a held-insight tier
      earns a place in the harvest discipline — an ADR-0007
      amendment, decided deliberately, not in passing.
- [ ] The define phase's skill-level half is still open: the
      cbc-run playbook now carries Define as a step (2026-08-30,
      ADR-0009 change set), but no skill walks it the way
      cbc-framing walks framing — naming rule, verdict protocol.
      Consider a small addition when cbc-bootstrap next gets
      touched, or when a run's Define step chafes without one.
- [ ] Handbook suggestion, parked with its trigger: an overlay
      marker in the kit PLAN stub's Framing step (the hygiene
      files' append-below-the-marker pattern), so a method bundle
      can add gate items first-class. Propose it if a CbC run's
      Framing ever needs a gate the generic step cannot express,
      or when a second method bundle appears. Until then the
      generic gates are the interface and cbc-framing meets them
      (bundle doc, Birth section).
- [ ] The projection law's deeper lifecycle is unharvested: public
      docs beyond the README, earned by demonstrated substance and
      refreshed at slice closes — cbc-slice-close territory, seen
      in the safe-reservations node's projection model
      (2026-08-30) but never lived by a run of ours. Harvest when
      a run first reaches the milestone that fires it.
- [ ] checkout-system reads the db port as CHECKOUT_DB_PORT while
      its .env.example names POSTGRES_PORT — two env keys for one
      fact, found at template extraction. If it is a defect, fix it
      in the run first, then harvest; the templates carry it as
      lived.

- [ ] Watch the first Step 0 walk for stub-vs-manual overlap
      friction: the kit's PLAN Step 0 comment and starter/README
      steps 3–7 partially restate each other. The user's instinct
      is to slim the stub comment and carry the logic in the first
      prompt; counter-argument on record (2026-08-31 session): the
      prompt doesn't persist across sessions and the manual isn't
      copied — if anything shrinks, it's the manual deferring to
      the stub (stub-teaches-itself, their ADR-0004). If the walk
      shows lived friction either way, it becomes a handoff item
      with evidence.
- [ ] Birth-walker skill for this repo's arrangement: a thin skill
      in .claude/skills/ that reads the two birth manuals at use
      time (executions/README.md Birth section, which defers to the
      handbook's starter/README.md) and walks them with review
      stops — never restating the steps (the handbook's ADR-0014
      pointer idiom; a skill body that copies the manual is a
      second master). Trigger: distill it from the first lived
      birth, not before — the manual is unwalked (2026-08-30), and
      the skill should carry what the walk teaches, not
      speculation. Whether the handbook wants its own walker over
      its manual is its call — FYI delivered 2026-08-30; the return
      handoff (item 7) adds: the handbook has its own parked walker
      candidate, and if both ever exist they walk composing manuals
      (kit first, bundle second), so shape them together, not
      derived twice — dual-noted on their birth-skill entry.
      (2026-08-31) executions/birth-scenario.md is now this skill's
      precursor: the skill distills from the scenario once walks
      stabilize the draft, not from the manuals directly.
- [ ] The bundle's not-copied boundary is weaker than the kit's:
      the handbook keeps its manual outside the shipped directory
      (starter/README.md beside kit/, their ADR-0016 — structural,
      nothing drifts in by accident), while executions/README.md
      sits among the files that copy and stays home only because
      the table does not list it. Same effect for one file; if the
      bundle ever grows more stay-home files, adopt the
      directory-boundary shape (noticed 2026-08-30, comparing the
      two manuals).

## Known issues (deferred deliberately — each entry: what, why accepted, when to revisit)
