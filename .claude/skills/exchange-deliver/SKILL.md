---
name: exchange-deliver
description: Write the note and stage a delivery into a run's temp/. Use when the reviewer says to deliver — after a reading, or when something a run holds has changed here — and for a note alone when a reading found nothing to send.
foundation: the exchange convention
---

# Deliver

Two acts: the note, then the staging on the word. The same whether
a reading preceded it or we changed something on our own; the
verdicts and the read-through ride only when one did.

## 1. Write the note

In `temp/note-to-<run>-<date>.md`, told not delivered.

0. **If the run moved since the reading, run `exchange-read` on the new
   span.** The reading's first line names `R`; if `R..HEAD` is not
   empty, `exchange-read` steps 2–4 on it. The three things it reads are the
   filter — the run's own building yields nothing and the extension
   is empty in seconds; a copy edited or a line to us yields items,
   which take the next numbers and are worked before the note. The
   note then says the new `HEAD`. Both sides moved from one pin;
   this is where their side is read before the take merges it.

1. **What changed since the run's pin**, as paths the run can check
   against its own tree:

   ```sh
   git diff -M --stat P..HEAD -- concept/ \
     'delivery/*/.claude/skills/*' 'delivery/*/.claude/rules/*'
   ```

   Those are the copies, and only they travel after birth
   (`docs/conventions/exchange/` §3.2); the trailing `/*` is what
   makes git match inside them.

   Every path that differs, is new, is gone, or moved — deletions
   and renames named as such. The run will diff the staging against
   what it holds; the note says what that diff will show, and the
   run finds the note wrong if it does not.

2. **Why it matters to this run** — the part a diff cannot carry.
   What the change does to the run's next step, not what it does to
   the files.

3. **The verdicts**, if a reading preceded this — one for every
   line under *To the deliverer* and every edit, in the run's order,
   as the reading's items ended. A verdict is the decision and what
   the run owes now; never a description of our own practice, which
   the run cannot check; never "accepted" for something not decided.

4. **The read-through**, if a reading preceded this: `read through
   <run HEAD>`, from the reading's first line. A delivery without a
   reading carries none, and the run's stays where it was.

5. **What it recommends, in order**, and what is optional.

6. Nothing that needs our repo to verify. A claim the run cannot
   check from its own tree is a hedge it can never close. Where one
   cannot be avoided — a thin note, material outside the delivery, a
   negative claim — the note says so, in a clause.

7. **No ADR number, no path in this repo, no word of our own
   vocabulary.** The note is told text, and a citation the run cannot
   follow reads as its own. A shipped file carries `CBC ADR-nnnn`
   instead.

8. **A third repository gets both names**: ours, by ordinal, and the
   one it gave itself.

9. **Commit the note last.** The commit after this one is `H`, and
   the staging is named by it.

## 2. Stage

On the reviewer's word. If the agent stages, it runs 2.1 and 2.2,
reports, and waits for the word before 2.3.

1. **The run's tree is quiet:**

   ```sh
   git -C "$run" status --short     # must print nothing
   ls "$run"/temp                   # must be empty
   ```

2. **Overlay the copies of the groups the run takes**, after checking
   that no path is claimed twice:

   ```sh
   groups="container method spring-postgres"   # the run's groups
   copies() { (cd delivery/$1 && find .claude/skills .claude/rules \
                -type f 2>/dev/null); }
   for g in $groups; do copies $g; done \
     | sort | uniq -d                          # must print nothing
   stage=$(mktemp -d) && chmod 755 "$stage"
   for g in $groups; do
     copies $g | (cd delivery/$g && xargs cp --parents -t "$stage")
   done
   mkdir -p "$stage"/docs && cp -r concept "$stage"/docs/concept
   ```

   Each group's `.claude/skills/` and `.claude/rules/`, and nothing
   else of it: the container's records, entry files, decisions log
   and hygiene files went at birth and are the run's.

   `concept/` is the one path that is not a mirror, and this is the
   one line that says so.

   `mktemp -d` makes the folder owner-only, and the copy in 2.3
   carries its mode: a run that takes the staging's `.` onto its
   root gets 700 there, which git does not show. The `chmod` is why.

3. **Copy across, named by `H`, the note beside it:**

   ```sh
   cp -r "$stage" "$run"/temp/bundle-H
   cp temp/note-to-<run>-<date>.md "$run"/temp/
   ```

   The run's rule takes it from there. `temp/` is empty again when
   it has.

## 3. A note without files

A reading that found nothing addressed to us: the note is one line —
`read through <run HEAD>, nothing to answer, no files` — and step 2
copies only the note. One that found something and took none of it
is not this case: a declined item still owes its verdict, so its
note carries the verdicts and no files. The run records the
read-through; the pin does not move.

## 4. Gates

- The note is committed, and the staging is named by that commit.
- The run's tree was quiet and its `temp/` empty before anything
  was copied.
- No path was claimed by two groups.
- The run's `temp/` holds exactly the bundle and the note, and
  nothing tracked in the run changed.

## 5. What this does not do

- It does not decide verdicts. They come from the reading, as its
  items ended.
- It does not take. The run's rule does, from `temp/`, in its own
  time.
- Birth: the same overlay as 2.2 into the newborn's root, followed
  by the fills — `delivery/installs/pure-seed.md` has the rest.

---

## Decisions

- ADR-0036 — the exchange: the two numbers; staging on the
  reviewer's word; what goes and what a copy cannot carry; what the
  note is for
