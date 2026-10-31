---
name: exchange-deliver
description: Write the Delivery Note and stage a delivery into a CBC Run's temp/. Use when the reviewer says to deliver — after a Run Reading, or when something a CBC Run holds has changed here — and for a Delivery Note alone when a Run Reading found nothing to send.
foundation: the exchange convention
---

# Deliver

Two Skill Stages: the Delivery Note, then the Delivery Staging on the word. The same whether
a Run Reading preceded it or we changed something on our own; the
verdicts and the Read-Through Commit ride only when one did.

## Stage 1 — write the Delivery Note

What a Delivery Note holds, and why: (`docs/conventions/exchange/` §3.7, *The Delivery Note*).

In `temp/note-to-<run>-<date>.md`, told not delivered.

0. **If the CBC Run moved since the Run Reading, run `exchange-read` on the new
   span.** The Run Reading's first line names `R`; if `R..HEAD` is not
   empty, `exchange-read` steps 2–4 on it. The three things it reads are the
   filter — the CBC Run's own building yields nothing and the extension
   is empty in seconds; a copy edited or a line to us yields items,
   which take the next numbers and are worked before the Delivery Note. The
   Delivery Note then says the new `HEAD`. Both sides moved from one Delivery Pin;
   this is where their side is read before the Delivery Take merges it.

1. **What changed since the CBC Run's Delivery Pin**, as paths the CBC Run can check
   against its own tree:

   ```sh
   git diff -M --stat P..HEAD -- concept/ \
     'delivery/*/.claude/skills/*' 'delivery/*/.claude/rules/*' \
     'delivery/*/.claude/shapes/*' \
     'delivery/*/.claude/approaches-on-trial/*'
   ```

   Those are the copies, and only they travel after birth
   (`docs/conventions/exchange/` §3.2, *What goes*); the trailing `/*` is what
   makes git match inside them.

   Every path that differs, is new, is gone, or moved — deletions
   and renames named as such. The CBC Run will diff the Delivery Staging against
   what it holds; the Delivery Note says what that diff will show, and the
   CBC Run finds the Delivery Note wrong if it does not.

   Leave out a path whose only change is its *Decisions* footer: the
   copy is staged without it (step 2 of Stage 2), so the CBC Run's
   diff shows nothing there
   (`docs/conventions/exchange/` §3.8, *The footer at delivery*):

   ```sh
   footer_only() {   # true when $1 changed since $P only in its footer
     python3 - "$1" "$P" <<'PY'
   import re, subprocess, sys
   path, pin = sys.argv[1], sys.argv[2]
   cut = lambda t: re.sub(r'\n+---\n+## Decisions\n.*\Z', '\n', t, flags=re.S)
   show = lambda ref: subprocess.run(["git", "show", f"{ref}:{path}"],
                                     capture_output=True, text=True).stdout
   sys.exit(0 if cut(show(pin)) == cut(show("HEAD")) else 1)
   PY
   }
   ```

2. **Why it matters to this CBC Run** — the part a diff cannot carry.
   What the change does to the CBC Run's next Plan Step, not what it does to
   the files.

3. **The verdicts**, if a Run Reading preceded this — one for every
   Run Ask under *To the deliverer* and every edit, in the CBC Run's order,
   as the Run Reading's items ended. A verdict is the decision and what
   the CBC Run owes now; never a description of our own practice, which
   the CBC Run cannot check; never "accepted" for something not decided.

4. **The Read-Through Commit**, if a Run Reading preceded this: `read through
   <run HEAD>`, from the Run Reading's first line. A delivery without a
   Run Reading carries none, and the CBC Run's stays where it was.

5. **What it recommends, in order**, and what is optional.

6. Nothing that needs our repo to verify. A claim the CBC Run cannot
   check from its own tree is a hedge it can never close. Where one
   cannot be avoided — a thin Delivery Note, material outside the delivery, a
   negative claim — the Delivery Note says so, in a clause.

7. **No ADR number, no path in this repo, no word of our own
   vocabulary.** The Delivery Note is told text, and a citation the CBC Run cannot
   follow reads as its own.

8. **A third repository gets both names**: ours, by ordinal, and the
   one it gave itself.

9. **Commit the Delivery Note last.** The commit after this one is `H`, and
   the Delivery Staging is named by it.

## Stage 2 — stage and copy across

Why it is staged so: (`docs/conventions/exchange/` §3.1, *Delivery Staging*).

On the reviewer's word. If the agent stages, it runs steps 1 and
2, reports, and waits for the word before step 3.

1. **The CBC Run's tree is quiet, and nothing of ours is in its
   `temp/`:**

   ```sh
   git -C "$run" status --short -- ':!temp'      # must print nothing
   ls -d "$run"/temp/{bundle-,note-to-}* 2>/dev/null  # must print nothing
   ```

   `temp/` is the CBC Run's, tracked, and may hold its own drafts, so the
   status check leaves it out; only a Delivery Staging or Delivery Note of ours there
   means a Delivery Take has not happened.

2. **Overlay the copies of the groups the CBC Run takes**, after checking
   that no path is claimed twice:

   ```sh
   groups="container method spring-postgres"   # the run's groups
   copies() { (cd delivery/$1 && find .claude/skills .claude/rules \
                .claude/shapes .claude/approaches-on-trial \
                -type f 2>/dev/null); }
   for g in $groups; do copies $g; done \
     | sort | uniq -d                          # must print nothing
   stage=$(mktemp -d) && chmod 755 "$stage"
   for g in $groups; do
     copies $g | (cd delivery/$g && xargs cp --parents -t "$stage")
   done
   mkdir -p "$stage"/docs && cp -r concept "$stage"/docs/concept
   find "$stage" -name '*.md' -exec python3 -c '
   import re, sys
   for p in sys.argv[1:]:
       t = open(p, encoding="utf-8").read()
       n = re.sub(r"\n+---\n+## Decisions\n.*\Z", "\n", t, flags=re.S)
       if n != t: open(p, "w", encoding="utf-8").write(n)
   ' {} +
   ```

   The last command strips every copy's *Decisions* footer, the `---`
   line and the section below it, and nothing else; a second run
   changes nothing (`docs/conventions/exchange/` §3.8, *The footer at delivery*).

   Each group's `.claude/skills/`, `.claude/rules/`,
   `.claude/shapes/` and `.claude/approaches-on-trial/`, and nothing
   else of it: the Container Group's
   records, entry files, Decisions Log and hygiene files went at
   birth and are the CBC Run's.

   `concept/` is the one path that is not a mirror
   (`docs/conventions/exchange/` §3.3, *A group's place in the tree*).

   `mktemp -d` makes the folder owner-only, and the copy in step 3
   carries its mode: a CBC Run that takes the Delivery Staging's `.` onto its
   root gets 700 there, which git does not show. The `chmod` is why.

3. **Copy across, named by `H`, the Delivery Note beside it:**

   ```sh
   cp -r "$stage" "$run"/temp/bundle-H
   cp temp/note-to-<run>-<date>.md "$run"/temp/
   ```

   The CBC Run's Agent Rule takes it from there. The Delivery Staging and the Delivery Note
   leave `temp/` when it has; whatever else is there is the CBC Run's.

## A Delivery Note without files

Why every read ends with one: (`docs/conventions/exchange/` §6.6, *The Delivery Note after a read*).

A Run Reading that found nothing addressed to us: the Delivery Note is one line —
`read through <run HEAD>, nothing to answer, no files` — and
Stage 2 copies only the Delivery Note. One that found something and took
none of it is not this case: a declined item still owes its
verdict, so its Delivery Note carries the verdicts and no files. The CBC Run
records the Read-Through Commit; the Delivery Pin does not move.

## Gates

- The Delivery Note is committed, and the Delivery Staging is named by that commit.
- The CBC Run's tree was quiet and its `temp/` held nothing of ours
  before anything was copied.
- No path was claimed by two groups.
- The CBC Run's `temp/` gained exactly the bundle and the Delivery Note, and
  nothing tracked in the CBC Run changed.

## What this does not do

- It does not decide verdicts. They come from the Run Reading, as its
  items ended.
- It does not take. The CBC Run's Agent Rule does, from `temp/`, in its own
  time.
- Birth: every file of each group into the Newborn Run's root, not
  only the copies Stage 2's step 2 takes, followed by the Delivery Fills —
  `delivery/installs/pure-seed.md` has the rest.

---

## Decisions

- ADR-0036 — the Exchange Convention: the two numbers; Delivery Staging on the
  reviewer's word; what goes and what a copy cannot carry; what the
  Delivery Note is for
