---
foundation: practice, under the shapes convention
---

# The Enemy Collision Kill Shape

**Governs:** how an Enemy Collision Kill is written in the System
Definition's LAYER-4-PROBLEMS: one way the Falsifiable Promise can
break, found by setting one Enemy Fact against one System
Possession. Its form, never its content: which Enemy Fact meets
which System Possession, and what dies, come from the Enemy
Collision.

<!-- An Output Shape: what a kind of output looks like, its form and never
     its content. Read at CBC Framing's Plan Step Gate, never while the
     Enemy Collision Kills are written. How Output Shapes live is
     .claude/rules/shapes-lifecycle.md, and not repeated here. -->

## What this document controls

**The form of one Enemy Collision Kill in the numbered list,** and
nothing else. An Enemy Collision Kill this Output Shape accepts can
still be the wrong one. That is the Enemy Collision's business. What
this Output Shape does not govern is listed under *What is exempt, and why*.

**Two layers, marked apart.** *Skeleton:* what any project's Enemy
Collision Kills would want. *Illustration:* one form of it, from the
method's worked example, a tiny order service, its tags and its
numbers.

## The shape

```markdown
**KILL-<n>.** <the Enemy Fact> × <the System Possession it attacks> → <what
happens>: **<what dies, in its own words>**. <optional: "what KILL-<m>
kills, <how this case differs>.">
*Say:* <real numbers from this system, from the state before to the
state that breaks>
```

An Enemy Collision Kill with more than one case:

```markdown
**KILL-<n>.** <the Enemy Fact> × <the System Possession> → <what happens>, two
ways:
(a) <the first case>: **<what dies>**.
(b) <the second case>: stopped by <Scope Exclusion>: <why, optional>.
*Say:* <numbers for each case that dies>
```

An Enemy Collision that breaks nothing:

```markdown
**KILL-<n>.** <the Enemy Fact> × <the System Possession> → <what happens>:
**nothing dies.** <why the Falsifiable Promise holds>. Stopped by <Scope Exclusion>.
```

*Skeleton:*

- **It starts with the Enemy Fact and the System Possession it
  attacks,** by their tags, then what happens when they meet.
- **Every Enemy Collision Kill states what dies, in bold, in its own
  words.** One whose loss is another's says so after its own: "what
  KILL-1 kills, the answer lost rather than late". A reader landing
  on any of them sees what breaks without reading another.
- **An Enemy Collision Kill may have cases,** labelled (a), (b), when
  one Enemy Fact meets one System Possession in more than one way.
  Each case ends in what dies, in bold, or in the Scope Exclusion
  that stops it.
- **A case a Scope Exclusion stops says "stopped by"** and the Scope
  Exclusion or Scope Verdict that stops it, or several: "stopped by NOT-OURS-1", "stopped by
  NOT-OURS-2 and SYSTEM-BOUNDARY-5". A reason may follow after a
  colon.
- **An Enemy Collision that breaks nothing stays in the list,**
  saying "**nothing dies**", why, and the Scope Exclusion. It shows
  the pair was tried, and every pair is counted.
- **Every Enemy Collision Kill where something dies carries a
  `*Say:*` line** with real numbers from this system: the state
  before, the Enemy Collision, the state that breaks the Falsifiable
  Promise.

*Illustration, from the worked example:* the tags are its System
Definition's: Enemy Facts FACT-CALLER-1, FACT-CALLER-2,
FACT-NETWORK-3, FACT-PROCESS-4, FACT-CALLER-5 and FACT-STORE-6, System
Possessions POSSESSION-1 to POSSESSION-3, Scope Exclusions NOT-OURS-1
to NOT-OURS-3.

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
dies.** The Falsifiable Promise is about recording one order, not what happens
to it after. Stopped by NOT-OURS-1.
```

## What is exempt, and why

- **The CBC Framing Concerns, the Invariant Slice Folds, and what
  the Scope Exclusions stopped,** which follow the Enemy Collision
  Kills. They group and count them, and are not Enemy Collision
  Kills themselves.

## What to check at a close

Read the Enemy Collision Kills and ask:

1. Does each start with the Enemy Fact and the System Possession,
   by their tags?
2. Does each state what dies, in bold, or say "nothing dies"?
3. Is every case labelled, and does each end in what dies or
   "stopped by" a Scope Exclusion?
4. Does each where something dies have a `*Say:*` line with real
   numbers?
5. Where one differs from this Output Shape: did it drift, was the
   Output Shape wrong, did each have something, or is it a different
   kind? How each ends is the shapes-lifecycle Agent Rule's
   (`.claude/rules/shapes-lifecycle.md` §3, *A difference at the close*).
