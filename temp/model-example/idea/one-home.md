# One home per fact

<!-- Layer: the idea. Bound to no project
     (temp/model-example/layers.md). -->

## The problem

The same fact written in several places drifts. One copy changes, the
others do not, and readers meet two truths without knowing which holds.

## The idea

Each fact is written in one place, its home. Elsewhere, point at it.

## How it works

1. **A home** is the one place where the fact is written, and the only
   place that changes when the fact changes.
2. **A pointer** is a reference to the home, in a form a search can
   find.
3. **Each pointer says what it relies on,** in one line. A change to
   the home is checked against these lines, not against every
   paragraph that points.
4. **A retelling** is allowed where a reader must act on the fact
   without leaving the page. It carries a pointer, and is checked
   against the home when the home changes.
5. **A fact changes at its home.** Every pointer is found and checked.
   Where one no longer holds, one of three:
   - that place changes;
   - the fact splits, and each place points at the part it needs;
   - that place takes its own version, and stops pointing.
6. **A home that moves** takes every pointer with it, in the same
   change.

## Why

- One change, in one place.
- Two copies cannot quietly disagree.
- A reader knows where the truth is.

**Ways rejected:**

- **Copies kept in step by hand:** every copy must be known and found,
  and nothing says where they are.
- **Widening a fact until it fits every pointer:** it fits all and
  helps none.

## Limits

- **A fact with many pointers is costly to change.** Each pointer is
  judged, and a search cannot judge. Keep such facts few and stable.
- **Share small, settled facts,** such as a definition. Reasoning
  changes often; pointing at it spreads every change.
- **When places need different things, copy.** A little copying is
  cheaper than a pointer that forces agreement.
- **History is never a home.** A log records what was true then, and
  is not updated.

## What each project decides

1. What counts as a fact worth a home.
2. The form of a pointer.
3. Which kind of text is home to which kind of fact.
4. Where retellings are allowed.
5. How pointers are found.
6. How many pointers make a fact core, changed only on purpose.
7. Who checks a change: one agent, or several.

## Needs

1. **A way to search the texts** for a pointer's form.

## Changes

- 2026-11-02: drafted.
