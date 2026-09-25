<!-- DRAFT, 2026-09-25. Our half of the exchange, first procedure:
     read a run and write the reading. Derived from temp/exchange.md
     §2 and §6 and explains nothing. Replaces the harvest section of
     delivery/README.md. Never shipped. -->

# Read a run

Four steps, and the fourth is a document. What happens to the
document afterwards is work, not this procedure; when the work is
done, `deliver.md` carries the verdicts down.

1. **Find where to start.** Open the run's `.claude/decisions.md`.
   Its last delivery entry carries the **pin** `P` — our commit its
   copies equal — and the **read-through** `R` — its commit we last
   read up to.

2. **The span is `R..HEAD`**, in the run:

   ```sh
   git -C "$run" log --oneline R..HEAD
   ```

3. **Read three things in the span**, and nothing else is required:

   - every entry in `.claude/decisions.md` — each edit and its why
   - the `## To the deliverer` section of `TODO.md` — every line is
     an ask
   - the diff of every copy against what was delivered:

     ```sh
     git -C "$run" diff kit-P -- .claude/skills .claude/rules docs/concept
     ```

     `kit-P` is the run's receipt branch when it cut one; otherwise
     the commit of the registry entry that recorded `P`.

4. **Write the reading**, `temp/reading-<run>-<date>.md`, to the
   shape that governs it: one line per edit, per ask, per finding —
   what it is, where it is, and nothing decided yet. Its first line
   names the run's `HEAD` as read; that is the read-through the next
   note will carry. The reading is revised as its items close and
   deleted when the work does; history keeps it.

Then the work: each item ends as taken, declined or held, where
`exchange.md` §6 says each lands. Then `deliver.md` — with files if
anything was taken, without if not. **A read that sends no note has
not finished**: the run's read-through stays where it was, and the
run cannot tell it was read.
