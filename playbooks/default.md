<!-- Vendored copy — engineering-handbook starter/playbooks/default.md
     @ c670fe5 (copied 2026-09-05, v2; their ADR-0031 moved the
     playbooks out of the kit to starter/playbooks/ — first copied
     2026-09-02 @ 65dd7ee from the old kit path, replacing the
     pre-redesign TEMPLATE.md; ADR-0011). Pinned: do not edit
     here — changes happen in the handbook and arrive as a fresh
     pinned copy (ADR-0002). This is the base this repo's own
     retrospective folds into a typed playbook; the bundle's
     cbc-run playbook vendors its endpoint steps from the same
     master. -->

# Playbook: Default — the bare sequence

<!-- The default playbook (ADR-0028): Bootstrap, Framing, Release,
     and nothing between. Copied whole into the newborn PLAN.md at
     birth when no typed playbook fits — the middle steps are then
     authored at Framing. A new typed playbook starts as a copy of
     this file: middles inserted between Framing and Release,
     gates specialized but never weakened, the preamble's version
     lines kept. Step 0's gates are facts about the kit's
     contents, so this file changes when the kit does — and the
     change is carried into every playbook holding copies of
     these steps. -->

Playbook version: v2 (2026-09-05 — Framing's gate asks every
authored step for its projection; v1 created 2026-09-01)
Last updated from project: none — distilled from the pre-ADR-0028
PLAN stub.

## Step 0: Bootstrap                                [~]

<!-- First session, this step still open: you are bootstrapping.
     The repo, its hygiene commit and the birth entry's pin already
     exist; the gates below are the exit, and they are facts about
     the kit, the same in every birth. How you reach them — a
     briefing, a change-plan, a commit order — is the bundle's, and
     the manual that born you says it (ADR-0031). Two comment kinds
     in every stub: a fill-comment says its content replaces it;
     every other comment is a standing rule and stays. -->

Goal: the container exists — repo, records, arrangement — before content.
Gate:
- [ ] Repo initialized; hygiene base files present.
- [ ] Every placeholder filled, or explicitly deferred to a named
      step (the stack overlay defers to Framing, which confirms the
      steps that fill or delete it).
- [ ] No fill-comment remains: where a comment says its content
      replaces it, the content is there and the comment is not.
      Every other stub comment is a standing rule — it stays.
- [ ] Briefing committed: README purpose draft + devlog entry (a) —
      names given here may change at Framing; that is what it is for.
- [ ] Agent/project commit split held from the first commit: no
      commit mixes CLAUDE.md / .claude/ with the records.
- [ ] Birth entry in .claude/decisions.md filled: date and the
      copy-time handbook commit.
Notes:

## Step 1: Framing                                  [ ]

Goal: know what we're building and why, before code.
Gate:
- [ ] One-paragraph problem statement in README.
- [ ] Success criteria written (how we'll know it worked).
- [ ] Out-of-scope list written.
- [ ] Middle steps stand and the plan reads end-to-end once,
      coarsely — the playbook's confirmed against the framed
      problem where a typed one was copied in, written fresh here
      where the project was born on this bare default; birth
      materials brought with the briefing weigh in either way.
- [ ] Every step whose gate makes something true that the outside
      should see names its projection as a gate item — the README
      section, the ARCHITECTURE change. Projection follows truth,
      and the gate is where it is caught.
Notes:

## Steps 2..N-1: authored at Framing

<!-- This playbook deliberately has none (ADR-0028): the bare
     sequence cannot know a project type's steps. Born on this
     sequence, author them at Framing — keeping the form: a goal,
     a gate of verifiable facts, the records expected, and the
     projection where the step makes one true; detail only the
     next 1–2 steps finely. A typed playbook carries its own
     middles instead, and this section with them. -->

## Step N: Release                                  [ ]

Gate:
- [ ] CHANGELOG entry for the release.
- [ ] README true for a stranger; any commands verified on a clean
      machine.
- [ ] Known issues filed in TODO.md, not just remembered.
Notes:
