<!-- DRAFT, 2026-09-25. The deliverer's half of the exchange: read a
     run, write the note, stage. Derived from temp/exchange.md §2,
     §3 and §6 and explains nothing — the why is there. Replaces
     delivery/installs/bundle-update.md and the harvest section of
     delivery/README.md. Never shipped.

     Written for the mirrored layout (exchange §3): every path under
     delivery/<group>/ is the path it lands at. Until the move lands,
     step 3.2 does not run as written. -->

# Read, note, stage

Three acts, in this order, and every read ends with a note. A pin
is one of our commits held by the run; a read-through is one of the
run's commits, also held by the run. We hold nothing per run.

## 1. Read the run

1. Open the run's `.claude/decisions.md`. Its last delivery entry
   carries the **pin** `P` and the **read-through** `R`.

2. The span is `R..HEAD`, in the run:

   ```sh
   git -C "$run" log --oneline R..HEAD
   ```

3. Read three things in that span, and nothing else is required:

   - every entry in `.claude/decisions.md` — each edit and its why
   - the `## To the deliverer` section of `TODO.md` — every line is
     an ask
   - the diff of every copy against what was delivered:

     ```sh
     git -C "$run" diff kit-P -- .claude/skills .claude/rules docs/concept
     ```

     `kit-P` is the run's receipt branch when it cut one; otherwise
     the commit of the registry entry that recorded `P`.

4. Give each edit and each ask one verdict: **taken**, **declined**
   with why — never because a description says otherwise —, or
   **held** with the trigger that would settle it. Write them down;
   they go into the note as they are.

5. For every *taken*: change the master here, in `delivery/` or
   `concept/`, and commit. The run's edit is absorbed, so the next
   delivery carries it and overwrites nothing the run wanted.

6. Note the run's `HEAD` as read. That is the new read-through.

## 2. Write the note

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

2. **A verdict for every line under *To the deliverer*** and every
   edit found in step 1.3, in the run's order, as written in 1.4.

3. **The read-through**: `read through <run HEAD>`.

4. Nothing that needs our repo to verify. A claim the run cannot
   check from its own tree is a hedge it can never close.

5. **Commit the note last.** The commit after this one is `H`, and
   the staging is named by it.

## 3. Stage

On the reviewer's word. If the agent stages, it runs 3.1 and 3.2,
reports, and waits for the word before 3.3.

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

## 4. An empty read

Step 1 found nothing addressed to us and no edit: the note is one
line — `read through <run HEAD>, nothing to answer, no files` — and
step 3 copies only the note. The run records the read-through; the
pin does not move.

## Birth

The same overlay as 3.2, into the newborn's root instead of
`temp/`, followed by the fills. `pure-seed.md` has the rest; the
first registry entry it writes carries the pin and a read-through
of the newborn's first commit.
