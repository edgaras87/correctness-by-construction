<!-- The light read of run 4 for run 5's birth, and what the
     reviewer decided from it. Data for the step "Birth run 5, on
     full auto"; how it is made is
     .claude/approaches-on-trial/auto-run.md, stage 1. Goes when the
     step closes. -->

# Run 5's preparation

## The light read of run 4

Read 2026-10-21, at run 4's `7637a79`: run 3's hand-off to it
(`temp/RUN-4.md`), its `CLAUDE.local.md`, `PLAN.md`, devlog,
decisions log, `docs/decision-log.md`, `RETRO.md`, `TODO.md`, its
branches and tags, its framing records and slice records beside
run 3's. Three readers, side by side; each claim below was checked
against run 4's tree. Not run 4's reading: its lessons and its
edited copies wait for that, after the refinement.

### Keep

1. **A gate before the work,** ticked only with evidence.
2. **Small and Real questions;** a Real one's options tried on
   `try/` branches before deciding: 14 branches, 2 tries changed
   the answer.
3. **The decision log,** each decision with what it rejected.
4. **Copies edited in place,** each edit logged: 16 fixes to the
   method.
5. **Agent and project apart, no push, every branch kept.**
6. **The `keep-going` stop hook;** it sent the agent back once.

### Change

7. **New work becomes an approach on trial.** Run 4's hand-off
   asked for "a provisional manual for the chosen way, and a PLAN
   step" (`CLAUDE.local.md`:25-35); none was written. Release, the
   seed's landing, a reviewer's message mid-run and a bulk rewrite
   of tags were each new work with no way. Tools it writes live in
   the repo, logged.
8. **Lighter records from the start.** 39k words of records against
   457 lines of main Java; `docs/decision-log.md` holds 879 lines,
   93 entries still "Review: open". Full-word tags and a glossary
   from framing; a sign-off is one log line; a budget for the
   decision log and the devlog.
9. **No regroup.** Run 4's was nominal, 12 commits against 12, and
   it moved an ADR ahead of its code so a gate would pass. Step
   branches fast-forward as they are; the close is tagged; history
   is never reordered.
10. **The fresh-clone check from the skeleton on,** not only at
    Release, where it found a broken README seven steps late.

### Add

11. **A channel for the reviewer's messages mid-run.** Run 4 took
    one well, as Step 2b; how a message is taken is written down.
12. **Isolation the run cannot step around.** Its deny rules
    covered `Read` alone, and it read with Bash (292 calls, 1
    Read).
13. **Analysis that shows.** Run 4 read the shapes at birth, whose
    examples were run 3's real kills; its framing, written in 15
    minutes and committed at 04:50–04:51, copies KILL-1 and KILL-5
    word for word and SLICE-4's entry nearly so. Its slices
    discovered for real: SLICE-1 tried 4 walls and rejected run
    3's design. "Red first" was never met as written: each red was
    made afterwards, on an uncommitted tree. Run 5 commits each
    probe before its verdict, banks the promises it rejects, fills
    LAYER-5-INTERACTION with kills where areas meet and a slice
    whose test stages them, keeps each red tree on a `red/` branch
    with its output, and tries a wall on a branch where a slice has
    a choice.
14. **The stack's traps, as facts:** the podman socket; Jackson
    reading 1.5 as 1; a killed instance never warmed. Facts about
    the environment, not the problem.
15. **A commit plan's look-back at the way,** tried: before a plan
    closes, ask whether the work could have been done meaningfully
    better, and if so try it and compare (TODO).

### Not carried over

Run 4's settled list and its comparison with run 3: run 5's
problem is new.

## The reviewer's decisions, 2026-10-21

- **The regroup:** dropped (9).
- **The stack's traps:** in the hand-off, as facts (14).
- **The model:** Fable 5.1 to start; Opus 5.5 if it stalls or the
  credits run out, and the run logs the switch as a decision.
- **No watcher:** a notice the reviewer could not act on until the
  next day is not worth a script.
- **Isolation:** no reading run 3 or run 4 (12).
- **The shapes:** delivered, read at the gate only (ADR-0061).
- **Visible analysis:** as in 13.
- **Examples in the method:** kept for run 5; whether they stay is
  TODO's.
- **`temp/`:** shipped, tracked (`cd69ed7`).
