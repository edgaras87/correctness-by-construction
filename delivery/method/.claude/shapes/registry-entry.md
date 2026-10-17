---
foundation: practice, under the shapes convention
---

# The shape of a registry entry

**Governs:** how one slice's entry is written in the slice
registry: the fields framing gives it, and the line each close
adds. Its form, never its content: what the invariant and the
adversity are comes from framing, and what a close answered comes
from the slice's record.

<!-- A shape: what a kind of output looks like, its form and never
     its content. Read at framing's closing gate, and at each
     slice's close, never while the entry is written. How shapes
     live is .claude/rules/shapes-lifecycle.md, and not repeated
     here. -->

## What this document controls

**The form of one slice's entry,** and nothing else. An entry this
shape accepts can still cut the wrong slice; that is framing's
business. The registry's other sections (its state, the count of
kills against slices, the order) are their own.

**Two layers, marked apart.** *Skeleton:* what any project's
registry would want. *Illustration:* one form of it, from the
method's worked example, a tiny order service.

## The shape

```markdown
### SLICE-<n> — <the invariant, in a few words>  `<status>`

- **Invariant:** <one statement, true in every readable state>
- **Adversity to create:** <each attack the evidence must stage,
  with the fact it comes from>
- **Area:** <the owner>. **Kills covered:** <KILL-ids>
- **Folds in:** <each definition this slice consumes, or "none">
- **Rider:** <a structural condition checked, never battle-tested,
  whose silent violation voids the evidence; or "none">
- **Flag riding:** <what cannot be staged the normal way, and what
  the evidence does instead; or "none">
- **Presumes:** <the slices this one stands on, and what it takes
  from each; or "nothing">
- **Judgment logged:** <why the slice is cut this way; or "none">
- **Record:** <a link to the slice's record>
- **Answered at close:** <one line per flag or judgment the slice
  settled: the answer in a sentence, and where in the record>
```

*Skeleton:*

- **Every field is present.** An empty one says "none" (or
  "nothing", for what a slice presumes), so a reader can tell
  empty from forgotten.
- **The status sits in the heading,** one of the registry's status
  values, and a closed slice gives its date.
- **The record is linked** from the entry, so a reader of the
  registry reaches the slice in one step.
- **At a close, one line per flag or judgment the slice settled,**
  under *Answered at close*. One sentence and a pointer; how the
  slice got there is its record's. An entry with nothing to answer
  says "none".
- **Framing's words stay as they were written.** A judgment the
  slice proved wrong is not rewritten; its answer sits beside it,
  so a reader sees both.

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
- **Folds in:** FOLD-1, the submission contract; its checks ride
  along.
- **Rider:** none.
- **Flag riding:** none.
- **Presumes:** nothing.
- **Judgment logged:** races fold in here because duplicate
  delivery is the one adversity class, the concurrent case its
  hardest.
- **Record:** [SLICE-1](<the path to its record>)
- **Answered at close:**
  - The judgment held: the race needed no wall of its own. The
    unique constraint on the key holds the race as it holds the
    retry (record, SLICE-1 GUARANTEE-1 and GUARANTEE-2).
```

## What to check at a close

Read the entry and ask:

1. Is every field present, an empty one saying "none"?
2. Does the heading carry the status, and a closed slice its date?
3. Is the record linked?
4. Does a closed slice's entry answer each flag and judgment it
   settled, one line each, with a pointer?
5. Where the entry differs from this shape: did it drift, was the
   shape wrong, did each have something, or is it a different kind?
   The shapes rule says how each ends.
