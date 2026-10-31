---
name: exchange-read
description: Read a CBC Run since the Concept Deliverer last read it, and write the Run Reading. Use when the reviewer says to read a CBC Run, or before a delivery that should answer what the CBC Run asked.
foundation: the exchange convention
---

# Read a CBC Run

Four steps, and the fourth is a document. What happens to the
document afterwards is work, not this skill; when the work is done,
`exchange-deliver` carries the verdicts down.

## 1. How a CBC Run is read

Why the read is done so: (`docs/conventions/exchange/` §6.1, *Reading a CBC Run*).

1. **Find where to start.** Open the CBC Run's Decisions Log, `.claude/decisions.md`.
   Its last delivery entry carries the **Delivery Pin** `P` — our commit its
   copies equal — and the **Read-Through Commit** `R` — its commit we last
   read up to.

2. **The span is `R..HEAD`**, in the CBC Run:

   ```sh
   git -C "$run" log --oneline R..HEAD
   ```

   That `HEAD` is the Read-Through Commit. Write it now as the Run Reading's
   first line — a new Run Reading's, or the open one's, moved — before
   anything is read.

3. **Read three things in the span.** They give every item:

   - every entry in `.claude/decisions.md` — each edit and its why
   - the `## To the deliverer` section of `TODO.md` — every line is
     a Run Ask
   - the diff of every copy against what was delivered:

     ```sh
     git -C "$run" diff <base> -- .claude/skills .claude/rules \
       .claude/shapes .claude/approaches-on-trial docs/concept \
       docs/glossary
     ```

     `<base>` is the CBC Run's receipt branch for `P` when it cut one;
     otherwise the commit of its last delivery entry, the one that
     recorded `P`.

   Two checks follow, and neither gives an item:

   - **The CBC Run's tree.** Work staged or changed but not committed
     is named in the Run Reading's Notes, and no verdict is written
     against what it undoes (`docs/conventions/exchange/` §6.1, *Reading a CBC Run*):

     ```sh
     git -C "$run" status --short
     ```

   - **A hash the CBC Run cites is on the branch read.** A CBC Run may
     cite commits from a branch beside it, such as a `-detail`
     branch of small commits. Before trusting such a hash, check
     that what it changed is the same on the branch read. A branch
     and a tag may share a name; `refs/heads/<name>` says which.

4. **Write the Run Reading — or extend the one that is open.** If `temp/`
   holds a Run Reading for this CBC Run, this read extends it: new items take
   the next numbers. Otherwise write `temp/reading-<run>-<date>.md`,
   to its form, `.claude/rules/exchange-reading.md`: one line per
   edit, per Run Ask, per finding — what it is, where it is, and nothing
   decided yet. One question every Run Reading asks: what does the CBC Run
   teach the worked example (`docs/conventions/exchange/` §6.3, *The Run Reading*)? The
   first line, written at step 2, is the Read-Through Commit the next Delivery Note
   will carry. One Run Reading per CBC Run, open at a time.

## 2. Gates

- The Run Reading exists, to its form, and its first line names the
  CBC Run's `HEAD`.
- Every edit, Run Ask and finding in the span has one line, and none of
  them is decided.
- The CBC Run's uncommitted work, if any, is named in the Run Reading.
- Nothing in the CBC Run was written to. The CBC Run is read only.

## 3. What this does not do

- It does not decide. Each item ends as taken, declined or held in
  the work that follows, where the Exchange Convention says each lands.
- It does not send. `exchange-deliver` does — and a read that sends no Delivery Note
  has not finished, because the CBC Run's Read-Through Commit stays where it
  was and the CBC Run cannot tell it was read.

---

## Decisions

- ADR-0036 — the Exchange Convention: the two numbers and why both are in
  the CBC Run; what a Run Reading is; the three verdicts and where each
  lands
