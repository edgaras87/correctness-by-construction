---
foundation: practice, under the shapes convention
---

# The Invariant Slice Entry Shape

**Governs:** how one Invariant Slice Entry is written in the
Invariant Slice Registry: the fields CBC Framing gives it, and the
line each Invariant Slice Close adds. Its form, never its content:
what the invariant and the adversity are comes from CBC Framing, and
what an Invariant Slice Close answered comes from the Invariant
Slice Record.

<!-- An Output Shape: what a kind of output looks like, its form and never
     its content. Read at CBC Framing's Plan Step Gate, and at each
     Invariant Slice Close, never while the entry is written. How Output Shapes
     live is .claude/rules/shapes-lifecycle.md, and not repeated
     here. -->

## What this document controls

**The form of one Invariant Slice Entry,** and nothing else. An
entry this Output Shape accepts can still cut the wrong Invariant
Slice. That is CBC Framing's business. The Invariant Slice
Registry's other sections (its state, the count of Enemy Collision
Kills against Invariant Slices, the order) are their own.

**Two layers, marked apart.** *Skeleton:* what any project's
Invariant Slice Registry would want. *Illustration:* one form of it, from the
method's worked example, a tiny order service.

## The shape

```markdown
### SLICE-<n> — <the invariant, in a few words>  `<status>`

- **Invariant:** <one statement, true in every readable state>
- **Adversity to create:** <each attack the evidence must stage,
  with the Enemy Fact it comes from>
- **Area:** <the owner>. **Kills covered:** <KILL-ids>
- **Folds in:** <each Invariant Slice Fold this Invariant Slice consumes, or "none">
- **Evidence Precondition:** <a structural condition checked, never
  tested under adversity, whose silent violation voids the evidence;
  or "none">
- **Adversity Flag:** <what cannot be staged the normal way, and what
  the evidence does instead; or "none">
- **Presumes:** <the Invariant Slices this one stands on, and what it takes
  from each; or "nothing">
- **Judgment logged:** <why the Invariant Slice is cut this way; or "none">
- **Record:** <a link to the Invariant Slice Record>
- **Answered at close:** <one line per Adversity Flag or judgment the
  Invariant Slice settled: the answer in a sentence, and where in the
  record>
```

*Skeleton:*

- **Every field is present.** An empty one says "none" (or
  "nothing", for what an Invariant Slice presumes), so a reader can tell
  empty from forgotten.
- **The status sits in the heading,** one of the Invariant Slice
  Registry's status values, and a closed Invariant Slice gives its
  date.
- **The Invariant Slice Record is linked** from the entry, so a
  reader of the Invariant Slice Registry reaches it in one step.
- **At the Invariant Slice Close, one line per Adversity Flag or
  judgment the Invariant Slice settled,** under *Answered at close*.
  One sentence and a reference to the record. How the Invariant
  Slice got there is its record's. An entry with nothing to answer
  says "none".
- **CBC Framing's words stay as they were written.** A judgment the
  Invariant Slice proved wrong is not rewritten. Its answer sits
  beside it, so a reader sees both.

*Illustration, from the worked example's SLICE-1, closed:*

```markdown
### SLICE-1 — exactly once under duplicate delivery  `closed (<date>, evidence)`

- **Invariant:** N arrivals of one submission → exactly one recorded
  order.
- **Adversity to create:** sequential retries (FACT-CALLER-1),
  simultaneous duplicates (FACT-CALLER-2), lost responses
  (FACT-NETWORK-3), and a key reused with a different body
  (FACT-CALLER-5).
- **Area:** order intake. **Kills covered:** KILL-1 to KILL-3,
  KILL-5.
- **Folds in:** FOLD-1, the submission contract; its checks go with
  it.
- **Evidence Precondition:** none.
- **Adversity Flag:** none.
- **Presumes:** nothing.
- **Judgment logged:** races fold in here because duplicate
  delivery is the one Adversity Class, the concurrent case its
  hardest.
- **Record:** [SLICE-1](<the path to its record>)
- **Answered at close:**
  - The judgment held: the race needed no Structural Wall of its own. The
    unique constraint on the key holds the race as it holds the
    retry (record, SLICE-1 GUARANTEE-1 and GUARANTEE-2).
```

## What to check at a close

Read the entry and ask:

1. Is every field present, an empty one saying "none"?
2. Does the heading carry the status, and a closed Invariant Slice
   its date?
3. Is the Invariant Slice Record linked?
4. Does a closed Invariant Slice's entry answer each Adversity Flag
   and judgment it settled, one line each, with a reference?
5. Where the entry differs from this Output Shape: did it drift, was the
   Output Shape wrong, did each have something, or is it a different kind?
   How each ends is the shapes-lifecycle Agent Rule's
   (`.claude/rules/shapes-lifecycle.md` §3, *A difference at the close*).
