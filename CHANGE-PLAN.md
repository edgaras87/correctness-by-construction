# Change-plan: absorb the third handbook reply (handbook @ f9371e4)

## Summary — the state after all commits

The reply's consequences are landed: this repo holds six conventions
(convention-lifecycle injected by its own §8 — the procedure our
friction built, now run as written for the first time), the
requires-chain is current (artifact-kinds updated from its one-line
drift, the check §8 added and the reply's missed-check lesson made
lived), the first-ever installed-path update has run on
project-recording (compare kit stub to kit stub, carry what our
records lack — likely nothing, since both earlier replies were
absorbed as they came; the verification and the new pin are the
product), and the installs/handbook.md rename is swept through the
living docs. Friction from both §8 runs is gathered in TODO for the
next handoff — the field data they asked back. Both temp/ copies are
deleted. The seed of cbc-newborn is unblocked on a kit re-read at
f9371e4.

## Commits

**1. `docs(agent): add change-plan for third-reply absorption`**
This plan.

**2. `chore(agent): inject convention-lifecycle @ f9371e4`**
The sixth convention, first injection under written §8, and first
commit so the procedure governs the rest of the set. One commit per
§8 step 5: copy (conventions/convention-lifecycle/CONVENTION.md →
.claude/skills/convention-lifecycle/SKILL.md), registry entry in
.claude/decisions.md, CLAUDE.md Conventions row. Known friction
already visible: our CLAUDE.md deleted the kit's placeholder line
(as the stub itself permits), so "row at the placeholder line" has
no anchor here — row lands at the list's end, friction noted.

**3. `chore(agent): update artifact-kinds to f9371e4`**
The chain-currency catch: requires names artifact-kinds, ours is
@ 4fe8083 with one exemplar-line drift since. §8 step 4: diff our
copy against the pinned master first (expect identical — no local
edits on record), overwrite, registry entry. One commit, skill
delivery.

**4. `chore(agent): register project-recording update @ f9371e4`**
The first lived installed-path update, run per §8 step 4's
by-argument paragraph: compare kit stubs at 4fe8083 and f9371e4,
carry changed comment text our records lack. Expectation: nothing
to carry — both replies were absorbed when they came (stub slimming
2026-09-01, playbook rebuild 2026-09-02) — so what lands is the
verification and the registry entry pinning project-recording
@ f9371e4. Provisional: if the compare surfaces missed text, it
lands project-side as its own `docs:` commit before this one (the
two sides never share a commit, §8 step 3), and the plan is revised
to say so.

**5. `docs: sweep the installs/handbook.md rename`**
Their ADR-0029: installs/default.md is installs/handbook.md. Living
docs only — starter/installs/cbc.md (two mentions), starter/README.md
(one), ARCHITECTURE.md (one). History (devlog, closed ADR bodies,
old PLAN steps) stays. Vendored playbook pins stay @ 65dd7ee —
the kit's playbooks/ did not change between the pins (verified),
so the pins remain honest and no refresh churn is owed.

**6. `docs: close records for the third-reply absorption`**
The records walk, planned at drafting: TODO — handoff item closes
(replied and absorbed); playbook-overlap item shrinks (their side
closed it as overtaken; ours keeps only the birth confirmation);
new item queues the §8 field data for the next handoff (the
injection-round-2 and installed-path friction, plus the placeholder
line finding); re-birth item notes the seed unblocked, kit re-read
@ f9371e4, newborn will hold six conventions. Devlog entry with
Resume (the seed is next). Walked and cleared: CHANGELOG (mental
layer unchanged), ARCHITECTURE (rename sweep is commit 5; shape
unchanged), PLAN (no project ADR in this set — every decision is
arrangement-side, recorded in the registry entries, or upstream in
their ADRs 0029/0030).

**7. `docs(agent): close change-plan for third-reply absorption`**
Deletes this file; body is the retro. Both temp/ copies (our
handoff draft, their reply) are deleted here too — untracked
staging, no commit content, noted in the body.

## Decisions taken inside this plan

- **Inject first, then run the procedure it delivers.** Commit 2
  lands convention-lifecycle before the updates that use its §8 —
  the arrangement that governs a series belongs on record before
  the work it governs (our decisions log's standing precedent).
- **Take the sixth convention now, not at leisure.** The reply says
  not urgent; we do it in this set because the re-birth's newborn
  holds six, and this repo testing §8 first means the newborn
  inherits a procedure with two lived runs behind it.
- **No project ADR.** The set decides nothing at project tier: the
  injections are arrangement decisions (registry entries carry the
  why), the sweep and the installed update apply upstream decisions
  (their ADR-0029/0030). The records walk names this deliberately.
- **Pins stay at 65dd7ee where the files did not move.** Re-pinning
  everything to f9371e4 would claim a re-verification we would not
  actually perform per file; the playbooks diff was checked empty,
  so the existing pins remain checkable truth.
- **Friction is gathered, not sent.** The next handoff's trigger is
  not set here — the field data queues in TODO and rides whenever
  the next handoff fires (likely at or after the re-birth trial).
