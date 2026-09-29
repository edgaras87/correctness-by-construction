# Plan: correctness-by-construction

<!-- No playbook supplies these steps: each is written here when a
     milestone is named, and finished ones join Reached. -->

## Legend

`[ ]` planned  ·  `[~]` in progress  ·  `[x]` done (+date)  ·  `[!]` blocked (+what unblocks)  ·  `[-]` skipped (+why)

**Gate** = exit criteria: verifiable facts, not intentions. A step is done only when every gate item is true.
Detail only the next 1–2 steps finely; keep later steps coarse (rolling wave).

---

## Reached

<!-- Finished steps, one line each: the date, the step, where its
     story lives. The step numbers stay because other files cite
     them ("PLAN Step 2"). -->

- 2026-08-27  Step 0: Bootstrap — devlog; ADR-0001, 0002
- 2026-08-28  Step 1: Framing — devlog; README
- 2026-08-28  Step 2: Concept lands — devlog; ADR-0003
- 2026-08-28  Step 3: Executions land — devlog; ADR-0004
- 2026-08-28  Step 4: Practice executions land — devlog; ADR-0005, 0006
- 2026-08-28  Step 5: First harvest — devlog; ADR-0007
- 2026-08-28  Step 6: Templates from the lived run — devlog; ADR-0008
- 2026-09-17  Step 7: The delivery takes shape — devlog 09-01 to
              09-18; ADR-0009 to 0022
- 2026-09-18  Step 8: The kit comes here — devlog; ADR-0023 to 0026
- 2026-09-19  Step 9: The groups — devlog; ADR-0029

## Step 10: One delivery, run for real               [~]

Goal: the composed delivery used to birth and carry a project, so
the design has two shapes behind it rather than one.
Gate:
- [ ] A project born from this repo alone, holding one pin, with
      `exchange-birth` written while it runs (TODO, Now).
- [x] One update delivered to a run end to end, the note and the
      copy both — 2026-09-20, to never-oversold @ `6f2be1d`
      (devlog 2026-09-20).
- [x] The letter to the handbook sent with lived numbers —
      2026-09-18 (devlog 2026-09-18, evening; ADR-0038).
- [x] Run 3 on one pin, ours — 2026-09-20 (devlog 2026-09-20).
Notes: from the sketch — "use it for a project or two, then stop;
design nothing further until there is a second shape to design
from." The birth is that second shape.

## Step N: Release                                  [ ]

Goal: concept v1 consultable — a stranger (or future-you) can
read, cite, and copy from this repo without the archive.
Gate:
- [ ] CHANGELOG entry for the release.
- [ ] README true for a stranger.
- [ ] `docs/models/` checked against the repo, since `CLAUDE.md`
      sends a stranger there (TODO, Next).
- [ ] Known issues filed in TODO.md, not just remembered.

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
- ADR-0010: The bundle gathers under starter/
- ADR-0011: Playbook steps — vendored endpoints, harvested middles
- ADR-0012: The newborn derives its arrangement; snippet withdrawn
- ADR-0013: README direction at the skills' moments of need
- ADR-0014: The bundle ships assembled text; the derivation experiment closes
- ADR-0015: The shipped text is a whole template, copied not merged
- ADR-0016: Adopt the pure shape; the assembly walk is cancelled
- ADR-0017: Fills beside the bundle
- ADR-0018: The seed lands on a receipt branch
- ADR-0019: The entry files ship filled — the semi-pure delivery
- ADR-0020: This repo's decisions are cited from other repos as CBC ADR-nnnn
- ADR-0021: A Spring slice reference, held here and handed after the build (superseded in part by ADR-0033)
- ADR-0022: The notes go; the exchange is a note and a copy
- ADR-0023: The compare is a reading; the diff is its evidence
- ADR-0024: The kit is taken here, verbatim but for a stated delta
- ADR-0025: The kit is ours; the handbook becomes provenance
- ADR-0026: The models are ours; ADR-0002's clause goes
- ADR-0027: The architecture diagram is Mermaid, provisionally
- ADR-0028: The procedure gets a picture; the method becomes a skill
- ADR-0029: Three groups, three directories (Step 9)
- ADR-0030: decide-first, and two renames (superseded in part by the
  2026-09-24 discards)
- ADR-0031: The three become conventions (superseded in part —
  two of the three discarded 2026-09-24)
- ADR-0032: The chain is a section, and it is drawn
- ADR-0033: Every slice derives blind; the reading happens once, at the end
- ADR-0034: An edited copy carries no header line (Step 10)
- ADR-0035: What a shape is belongs to the container; each rides its group (Step 10)
- ADR-0036: The exchange replaces convention-lifecycle (Step 10)
- ADR-0037: Shapes are a convention, and the model is its manual (Step 10)
- ADR-0038: The handbook is history: its decisions become ours, and no re-sync is kept (Step 10)
- ADR-0039: Conventions are a convention, and every description follows one rule (Step 10)
- ADR-0040: A TODO holds open work, and an item has one shape (Step 10)

---

## Retrospective  (fill at project end)

Ran: <start> → <end>

1. Estimate vs reality — which steps took much longer/shorter, why?
2. Wrong order — what needed to happen earlier?
3. Dead ends — approaches tried and abandoned (→ playbook warnings).
4. Missing steps — work that had no home in the plan.
5. Useless gates — ceremony that caught nothing.
6. The entry file — read CLAUDE.md top to bottom; every line still
   passes its three tests, or leaves (agent-arrangement §2).

Then fold lessons into the playbook the steps came from — the
"Steps from" line at the top names it — in the repo that owns it,
and bump its version there.
