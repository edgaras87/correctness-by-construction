---
paths:
  - ".claude/skills/**"
  - ".claude/rules/**"
  - "docs/concept/**"
  - "temp/**"
---

# Delivered copies: pinned, edited in place, re-pinned

<!-- What this run holds from its deliverer, and what it may do to
     it. The deliverer's side of the same exchange is not here; the
     run never needs it. -->

1. **Every file delivered here is a copy pinned at the deliverer's
   commit** — the hash in the decisions log's last delivery entry.
   One pin covers all of it: the skills and rules under `.claude/`,
   and `docs/concept/`. The concept chapters are copies too, and are
   never edited here — nothing in a chapter is run, so nothing in it
   can fail a step; a lesson about one is a prose line in the
   backlog. The records — `PLAN`, `TODO`, the devlog, the entry file
   — were delivered once as stubs and are this run's own; they are
   not copies and this file does not govern them.

2. **A copy may be edited in place during a step when all three
   hold.** Something happened in this project that the copy did not
   foresee — never a speculation. The edit asks a question or demands
   an outcome any project would want — never this project's answer,
   never anything project-specific. One entry in
   `.claude/decisions.md` per edit, or per copy per step, saying
   what changed, which step found it, and why. Nothing is written
   into the copy but the edit itself: a comment in an artifact says
   how to use it or what a part is, never what changed — that is
   history, and the diff against the pin and the log already hold
   it.

3. **What this project needs that no copy should carry goes into
   the project's records** where that kind of thing already lives —
   a gate item in PLAN, an ADR, a slice record, the entry file. The
   copy stays general.

4. **At every step's close, the hand-off.** One TODO line per edited
   copy: "deliverer: evaluate this run's changes to `<copy>` since
   `<pin>`". The line is the request — without it the deliverer finds a
   changed file and must guess; the edits describe themselves in the
   diff and the log. The deliverer reads this repo read-only when it
   reads it — at a hand-off, or at the retrospective — not at every
   step's close; a faster answer needs a hand-off document. It diffs
   the copy against its own tree at the pin, takes, reshapes or
   declines each hunk in its own words, and writes its reply. The
   line is done at the re-pin.

5. **After the reply, the re-pin — the take.** The deliverer's new
   version arrives staged in this repo's own `temp/`: a directory
   named for the hash, the note beside it. In this order, before
   anything moves: **check the note against the staging** — diff
   every delivered file against what this run holds; the note says
   how many differ, the diff says how many, and a mismatch is
   reported first. Then diff each held copy against this run's own
   delivery commit to find its own edits, and read the note's
   verdict on each. Then copy whole, empty `temp/`, and write one
   decisions entry carrying the new hash; the copy is pristine
   again; the TODO line leaves with the hash. A
   declined edit is gone with the re-pin — never edited back in. If the
   project still needs what was declined, that need goes into
   records per rule 3, and the decisions entry says so.

6. **If a step opens before the reply**, work continues on the edited
   copy, and edits keep landing under rule 2. They stack on this side
   only; the deliverer diffs against the pin either way, and the re-pin
   still lands whole. Behind the deliverer is acceptable; behind this
   run's own lessons is not.

7. **A copy this project has finished with is edited the same
   way.** A restarted step may re-run on it, the deliverer takes or
   declines an exact hunk rather than a translated note, and one
   process serves every copy. The one difference: the problem was
   lived either way, but the fix's wording is never used by a later
   step here — a running skill's fix is exercised by the next step,
   a finished skill's fix is first used by the deliverer. Say so in the
   log entry.

The pin is the truth of origin, the log is the why, and the diff
between the pin and the copy is the whole of what this run changed
— which is what the deliverer reads.
