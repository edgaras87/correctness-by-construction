# Plan: correctness-by-construction

<!-- No playbook supplies these steps: each is written here when a
     milestone is named, and finished ones join Reached. With no
     project end, a milestone's last two gate items do what a
     retrospective would: fold its lessons back, and re-read the
     entry file. Findings go to TODO.md the moment they appear, and
     the ADRs are listed by docs/adr/ itself. -->

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
- [ ] Lessons folded back where they came from — conventions,
      playbooks, the concept.
- [ ] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`docs/conventions/agent-arrangement/`
      §2).
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
- [ ] Lessons folded back where they came from — conventions,
      playbooks, the concept.
- [ ] `CLAUDE.md` read top to bottom; each line still passes its
      three tests, or leaves (`docs/conventions/agent-arrangement/`
      §2).
