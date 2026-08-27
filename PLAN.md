# Plan: correctness-by-construction

<!-- Written fresh from the kit stub — no concept-repo playbook exists yet. -->

## Legend

`[ ]` planned  ·  `[~]` in progress  ·  `[x]` done (+date)  ·  `[!]` blocked (+what unblocks)  ·  `[-]` skipped (+why)

**Gate** = exit criteria: verifiable facts, not intentions. A step is done only when every gate item is true.
Detail only the next 1–2 steps finely; keep later steps coarse (rolling wave).

---

## Step 0: Bootstrap                                [~]

<!-- First session, this step still open: you are bootstrapping.
     Take the briefing. Before touching anything else, draft
     CHANGE-PLAN.md per the change-plans skill (shipped in the
     kit). The plan's substance is the per-project content: what
     each placeholder becomes, which records this project will
     actually keep current (delete the rest), the birth entry's
     date and handbook commit filled in .claude/decisions.md.
     The middle steps are absent by design (ADR-0024): Framing
     authors them, from a playbook or fresh — the change-plan
     here covers Step 0 only.
     Commit order for this set: plan open → project records →
     agent install → plan close; the repo and its hygiene commit
     already exist. The gates below are the exit — draft against
     them. -->

Goal: the container exists — repo, records, arrangement — before content.
Gate:
- [ ] Repo initialized; hygiene base files present.
- [ ] Every placeholder filled, or explicitly deferred to a named
      step (Commands and the stack overlay defer to Framing, which
      authors the steps that fill or delete them).
- [ ] No fill-comment remains: where a comment says its content
      replaces it, the content is there and the comment is not.
      Every other stub comment is a standing rule — it stays.
- [ ] Briefing committed: README purpose draft + devlog entry (a) —
      names given here may change at Framing; that is what it is for.
- [ ] Agent/project commit split held from the first commit: no
      commit mixes CLAUDE.md / .claude/ with the records.
- [ ] Birth entry in .claude/decisions.md filled: date and the
      copy-time handbook commit.
Notes: Deferred to Framing (Step 1): Commands — CLAUDE.md's Commands
block and README's Prerequisites/Run/Test (ADR-0024); ARCHITECTURE
below the Overview (components, invariants, codemap — nothing has a
shape until content lands); CHANGELOG's role (may become the
concept-version log — its "users" are run repos pinning versions).

## Step 1: Framing                                  [ ]

Goal: know what we're building and why, before code.
Gate:
- [ ] One-paragraph problem statement in README.
- [ ] Success criteria written (how we'll know it worked).
- [ ] Out-of-scope list written.
- [ ] Middle steps authored and the plan sketched end-to-end once,
      coarsely — copied from a playbook (playbooks/) where one fits,
      written fresh where none does; birth materials brought with
      the briefing weigh in here.
Notes:

## Steps 2..N-1: authored at Framing

<!-- Deliberately absent from the stub (ADR-0024): a step sequence
     is engineering knowledge, not arrangement, so the stub cannot
     know it. At Framing, copy the middle steps from a playbook
     (playbooks/) where one fits, write them fresh where none does —
     keeping the form: a goal, a gate of verifiable facts, the
     records expected. Detail only the next 1–2 steps finely. -->

## Step N: Release                                  [ ]

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

---

## Retrospective  (fill at project end)

Ran: <start> → <end>

1. Estimate vs reality — which steps took much longer/shorter, why?
2. Wrong order — what needed to happen earlier?
3. Dead ends — approaches tried and abandoned (→ playbook warnings).
4. Missing steps — work that had no home in the plan.
5. Useless gates — ceremony that caught nothing.

Then fold lessons into playbooks/<type>.md and bump its version.
