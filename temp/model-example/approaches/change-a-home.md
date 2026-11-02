# Change a home

<!-- Layer: the Work Approach. From:
     temp/model-example/this-repo/one-home.md. -->

**When:** you change a fact that other texts point at.

## Steps

1. **Find the pointers.** Search for the home's path. List each
   pointer with its "relies on" line.
2. **Check each.**
   - **5 or fewer:** read each "relies on" line against the new fact.
     Where a pointer has none, read its sentence.
   - **More than 5:** start one checker per pointer. Give each the old
     fact, the new fact, and its pointer's line. Each answers: holds,
     or breaks, and what it would need.
3. **For each that breaks, pick one:**
   - change that place;
   - split the fact, each place pointing at its part;
   - give that place its own version, and remove its pointer.

   Never widen the fact until it fits all.
4. **Commit the change and every fix together.**
5. **A fix that changed another home** is a change of its own: start
   again from step 1 for it.

## Done when

Every pointer holds, or has the reviewer's decision.

## Stop and ask

- A break where no pick is clearly right: show the reviewer the
  options.
- A core fact, more than 5 pointers: the reviewer agrees before the
  change.
