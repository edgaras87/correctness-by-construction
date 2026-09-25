<!-- DRAFT, 2026-09-25. Our half of the exchange, second procedure:
     write the note and stage. Derived from temp/exchange.md §2 and
     §3 and explains nothing. The same whether a reading preceded it
     or we changed something on our own. Replaces
     delivery/installs/bundle-update.md. Never shipped.

     Written for the mirrored layout (exchange §3): every path under
     delivery/<group>/ is the path it lands at. Until the move lands,
     step 3.2 does not run as written. -->

# Deliver

Two acts: the note, then the staging on the word. A pin is one of
our commits held by the run; a read-through is one of the run's
commits, also held by the run. We hold nothing per run.

## 1. Write the note

In `temp/note-to-<run>-<date>.md`, told not delivered.

1. **What changed since the run's pin**, as paths the run can check
   against its own tree:

   ```sh
   git diff -M --stat P..HEAD -- delivery/ concept/
   ```

   Every path that differs, is new, is gone, or moved — deletions
   and renames named as such. The run will diff the staging against
   what it holds; the note says what that diff will show, and the
   run finds the note wrong if it does not.

2. **The verdicts**, if a reading preceded this — one for every
   line under *To the deliverer* and every edit, in the run's order,
   as the reading's items ended.

3. **The read-through**, if a reading preceded this: `read through
   <run HEAD>`, from the reading's first line. A delivery without a
   reading carries none, and the run's stays where it was.

4. Nothing that needs our repo to verify. A claim the run cannot
   check from its own tree is a hedge it can never close.

5. **Commit the note last.** The commit after this one is `H`, and
   the staging is named by it.

## 2. Stage

On the reviewer's word. If the agent stages, it runs 2.1 and 2.2,
reports, and waits for the word before 2.3.

1. **The run's tree is quiet:**

   ```sh
   git -C "$run" status --short     # must print nothing
   ls "$run"/temp                   # must be empty
   ```

2. **Overlay the groups the run takes**, after checking that no path
   is claimed twice:

   ```sh
   groups="container method spring-postgres"   # the run's groups
   for g in $groups; do (cd delivery/$g && find . -type f); done \
     | sort | uniq -d                          # must print nothing
   stage=$(mktemp -d)
   for g in $groups; do cp -r delivery/$g/. "$stage"/; done
   mkdir -p "$stage"/docs && cp -r concept "$stage"/docs/concept
   ```

   `concept/` is the one path that is not a mirror, and this is the
   one line that says so.

3. **Copy across, named by `H`, the note beside it:**

   ```sh
   cp -r "$stage" "$run"/temp/bundle-H
   cp temp/note-to-<run>-<date>.md "$run"/temp/
   ```

   The run's rule takes it from there. `temp/` is empty again when
   it has.

## 3. A note without files

A reading that found nothing to take: the note is one line — `read
through <run HEAD>, nothing to answer, no files` — and step 2 copies
only the note. The run records the read-through; the pin does not
move.

## Birth

The same overlay as 2.2, into the newborn's root instead of
`temp/`, followed by the fills. `pure-seed.md` has the rest; the
first registry entry it writes carries the pin and a read-through
of the newborn's first commit.
