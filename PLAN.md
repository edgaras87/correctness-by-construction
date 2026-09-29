# Plan: correctness-by-construction

<!-- No playbook supplies these steps: each is written here when a
     milestone is named, and leaves when it is reached — the devlog
     entry that closes it names the step, and the story is there.
     With no project end, a milestone's last two gate items do what
     a retrospective would: fold its lessons back, and re-read the
     entry file. Findings go to TODO.md the moment they appear, and
     docs/adr/ lists the ADRs itself. -->

## Legend

`[ ]` planned  ·  `[~]` in progress  ·  `[x]` done (+date)  ·  `[!]` blocked (+what unblocks)  ·  `[-]` skipped (+why)

**Gate** = exit criteria: verifiable facts, not intentions. A step is done only when every gate item is true.
Detail only the next 1–2 steps finely; keep later steps coarse (rolling wave).

---

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
