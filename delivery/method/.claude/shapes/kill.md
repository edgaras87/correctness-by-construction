---
foundation: practice, under the shapes convention
---

# The shape of a kill

**Governs:** how a kill is written in the definition's collisions
layer: one way the promise can break, found by setting one fact
against one possession. Its form, never its content: which fact
meets which possession, and what dies, come from the collision.

<!-- A shape: what a kind of output looks like, its form and never
     its content. Read at framing's closing gate, never while the
     kills are written. How shapes live is
     .claude/rules/shapes-lifecycle.md, and not repeated here. -->

## What this document controls

**The form of one kill in the numbered list of kills,** and nothing
else. A kill this shape accepts can still be the wrong kill; that
is the collision's business. The concerns the kills are grouped
into, the folds, and what the fences stopped are their own.

**Two layers, marked apart.** *Skeleton:* what any project's kills
would want. *Illustration:* one form of it, from the method's worked
example, a tiny order service, its tags and its numbers.

## The shape

```markdown
**KILL-<n>.** <the fact> × <the possession it attacks> → <what
happens>: **<what dies, in its own words>**. <optional: "KILL-<m>'s
death, <how this case differs>.">
*Say:* <real numbers from this system, from the state before to the
state that breaks>
```

A kill with more than one case:

```markdown
**KILL-<n>.** <the fact> × <the possession> → <what happens>, two
ways:
(a) <the first case>: **<what dies>**.
(b) <the second case>: stopped by <fence>: <why, optional>.
*Say:* <numbers for each case that dies>
```

A collision that breaks nothing:

```markdown
**KILL-<n>.** <the fact> × <the possession> → <what happens>:
**nothing dies.** <why the promise holds>. Stopped by <fence>.
```

*Skeleton:*

- **It starts with the fact and the possession it attacks,** by
  their tags, then what happens when they meet.
- **Every kill states its own death, in bold, in its own words.** A
  kill whose death is another kill's says so after its own:
  "KILL-1's death, the racers our own instances". A reader landing
  on any kill sees what breaks without reading another.
- **A kill may have cases,** labelled (a), (b), when one fact meets
  one possession in more than one way. Each case ends in its death,
  in bold, or in the fence that stops it.
- **A fenced case says "stopped by"** and the fence, or fences:
  "stopped by NOT-OURS-1", "stopped by NOT-OURS-2 and
  SYSTEM-BOUNDARY-5". A reason may follow after a colon.
- **A collision that breaks nothing stays in the list,** saying
  "**nothing dies**", why, and the fence. It shows the pair was
  tried, and the count of kills stays honest.
- **Every kill that dies carries a `*Say:*` line** with real
  numbers from this system: the state before, the collision, the
  state that breaks the promise.

*Illustration, from the worked example:* the tags are its
definition's: facts FACT-CALLER-1 to FACT-STORE-6, possessions
POSSESSION-1 to POSSESSION-3, fences NOT-OURS-1 to NOT-OURS-3.

```markdown
**KILL-2.** FACT-CALLER-2 × POSSESSION-2 → two identical submissions
each decide "new" before either is recorded: **two orders exist for
one submission.**
*Say:* fifty identical submissions released at one instant; each
finds no order for its key; the store holds two orders for the key,
or fifty.

**KILL-4.** FACT-PROCESS-4 × POSSESSION-1 → we die between
recording and replying, two ways:
(a) recorded, then killed before the reply: **an order exists that
its caller cannot confirm.**
(b) replied, then killed before the record commits: **an order is
confirmed that does not exist.**
*Say:* (a) a submission with key K is recorded; the process is
killed; the store holds one order for K, and the caller holds no
reply. (b) the caller holds "created" for K; the store holds none.

**KILL-<n>.** NOT-OURS-1, a shop cancelling a recorded order ×
POSSESSION-1 → the order changes after it is recorded: **nothing
dies.** The promise is about recording one order, not what happens
to it after. Stopped by NOT-OURS-1.
```

## What is exempt, and why

- **The concerns, the folds, and what the fences stopped,** which
  follow the kills: they group and count the kills; they are not
  kills.

## What to check at a close

Read the kills and ask:

1. Does every kill start with the fact and the possession, by
   their tags?
2. Does every kill state its own death, in bold, or say "nothing
   dies"?
3. Is every case labelled, and does each end in a death or "stopped
   by" a fence?
4. Does every kill that dies have a `*Say:*` line with real
   numbers?
5. Where a kill differs from this shape: did it drift, was the
   shape wrong, did each have something, or is it a different kind?
   The shapes rule says how each ends.
