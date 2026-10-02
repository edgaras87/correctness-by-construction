---
name: exchange-read
description: Read a run since the deliverer last read it, and write the reading. Use when the reviewer says to read a run, or before a delivery that should answer what the run asked.
foundation: the exchange convention
---

# Read a run

Four steps, and the fourth is a document. What happens to the
document afterwards is work, not this skill; when the work is done,
`exchange-deliver` carries the verdicts down.

## 1. The method

1. **Find where to start.** Open the run's `.claude/decisions.md`.
   Its last delivery entry carries the **pin** `P` — our commit its
   copies equal — and the **read-through** `R` — its commit we last
   read up to.

2. **The span is `R..HEAD`**, in the run:

   ```sh
   git -C "$run" log --oneline R..HEAD
   ```

   That `HEAD` is the read-through. Write it now as the reading's
   first line — a new reading's, or the open one's, moved — before
   anything is read.

3. **Read three things in the span**, and nothing else is required:

   - every entry in `.claude/decisions.md` — each edit and its why
   - the `## To the deliverer` section of `TODO.md` — every line is
     an ask
   - the diff of every copy against what was delivered:

     ```sh
     git -C "$run" diff <base> -- .claude/skills .claude/rules docs/concept
     ```

     `<base>` is the run's receipt branch for `P` when it cut one;
     otherwise the commit of its last delivery entry, the one that
     recorded `P`.

4. **Write the reading — or extend the one that is open.** If
   `temp/` holds a reading for this run, this read extends it: new
   items take the next numbers. Otherwise write
   `temp/reading-<run>-<date>.md`, to the shape that governs it: one
   line per edit, per ask, per finding — what it is, where it is, and
   nothing decided yet. One question every reading asks: what does
   the run teach the worked example (`docs/conventions/exchange/`
   §6.3)? The first line, written at step 2, is the read-through the
   next note will carry. One reading per run, open at a time.

## 2. Gates

- The reading exists, to its shape, and its first line names the
  run's `HEAD`.
- Every edit, ask and finding in the span has one line, and none of
  them is decided.
- Nothing in the run was written to. The run is read only.

## 3. What this does not do

- It does not decide. Each item ends as taken, declined or held in
  the work that follows, where the exchange says each lands.
- It does not send. `exchange-deliver` does — and a read that sends no note
  has not finished, because the run's read-through stays where it
  was and the run cannot tell it was read.

---

## Decisions

- ADR-0036 — the exchange: the two numbers and why both are in
  the run; what a reading is; the three verdicts and where each
  lands
