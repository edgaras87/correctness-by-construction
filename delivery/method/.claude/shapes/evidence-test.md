---
foundation: practice, under the shapes convention
---

# The Evidence Test Shape

**Governs:** how an Evidence Test is written: the first line of its
comment, the order of its assertions, and the labels on them. Its
form only. Which adversity a test creates, and which Invariant Slice
Guarantee it answers, come from the Invariant Slice Record.

<!-- An Output Shape: what a kind of output looks like, its form and never
     its content. Read at an Invariant Slice's Plan Step Gate, never
     while a test is written. How Output Shapes live is
     .claude/rules/shapes-lifecycle.md, and not repeated here. When a
     Red Run counts is the cbc-slice Agent Skill's Stage 3
     (.claude/skills/cbc-slice/SKILL.md), not this Output Shape's. -->

## What this document controls

**Three kinds of test.** Each sits beside an Invariant Slice's
evidence:
- an Evidence Test, which creates an adversity at the door and reads
  the State Witness;
- a Structural Wall Check, which reads the code;
- a Decision Test, which pins a decision and is not evidence.

A test this Output Shape accepts can still create the wrong adversity.
That is the Invariant Slice Record's business. What it leaves out is *What is
exempt, and why*.

**Two layers, marked apart.**
- *Skeleton:* what any project proving an invariant by tests would
  want, whatever its stack.
- *Illustration:* one form of it, from the method's worked example,
  a tiny order service, in Java. Every code block below is
  illustration.

A project takes the skeleton and writes its own illustration.

## The shape

### The first line says what the test is

```java
/**
 * SLICE-1 EVIDENCE-2 · GUARANTEE-3 — KILL-3: the reply is lost, and
 * the caller submits again.
 *
 * <p>Submit with key K, swallow the reply, submit K again. One order
 * exists for K after both, and the retry is answered with the first
 * reply. This fails if a second order is recorded for K, or the retry
 * is answered as new.
 */
```

A Decision Test says it is not evidence, and names the decision it pins:

```java
/**
 * Not evidence — a Decision Test for the choice in SLICE-1's record,
 * "A repeat gets the stored first reply": <the decision it pins>. It
 * guards the decided option, not the Falsifiable Promise, and
 * discharges no Enemy Collision Kill.
 */
```

*Skeleton:*

- **The first line names what the test is.** For an Evidence Test:
  the Invariant Slice, the Evidence Criterion, the Invariant Slice
  Guarantee, and the Enemy Collision Kill where it answers one (a
  test for an Invariant Slice Fold or a structural rule may answer
  none). For a Decision Test: "not evidence", and the decision it
  pins.
- **Then the story in plain words,** with the numbers it runs on,
  and what would make it fail.
- **The class says where its Invariant Slice Record is,** and which numbers
  its tests start from.

*Illustration:* `SLICE-<n> EVIDENCE-<m> · GUARANTEE-<k> — KILL-<j>`,
numbered as in the Invariant Slice Record. The Invariant Slice is
named because a test sits outside its record.

### The order of its assertions

```java
ResponseEntity<String> retry = submit(key, body);

Witness.Orders after = Witness.read(key);
assertThat(after.holds()).as("the promise: %s", after).isTrue();
assertThat(after.count()).as("one order for the key: %s", after).isEqualTo(1);
assertThat(after.body()).as("the first body kept: %s", after).isEqualTo(body);

assertThat(retry.getStatusCode()).isEqualTo(HttpStatus.OK);
assertThat(Body.of(retry.getBody()).stringAt("$.orderId")).isEqualTo(first.orderId());
```

*Skeleton:*

1. **The State Witness first.** Read it from where the truth is
   stored, never from the replies. When two of its numbers must
   agree with each other, read them in one read.
2. **Then the Falsifiable Promise,** on every State Witness Reading
   taken after the adversity, sampled ones included. A State Witness
   Reading taken before the adversity only checks the setup is in
   place. It owes nothing.
3. **Then the Invariant Slice's own invariant,** where it differs
   from the Falsifiable Promise.
4. **Then the exact numbers,** then the state of each thing the
   adversity touched.
5. **The door's answer last.**

*Illustration:*
- **The State Witness:** `Witness.read`, plain SQL from outside the
  service, as the identity the service runs as.
  `Witness.read(key)` reads the orders recorded for the key and
  their bodies in one statement.
- **The Falsifiable Promise:** `Witness.Orders.holds()`: the key's
  submission is exactly one recorded order.
- **An Invariant Slice's own invariant:** SLICE-1's is the
  Falsifiable Promise itself, so it owes none. SLICE-2's, "a retry
  after a crash ends in one order and one truthful answer", adds the
  answer, asserted beside the Falsifiable Promise.
- **The answer:** the status, then the body by JSON path.

### How its assertions read

*Skeleton:*

- **A label prints the State Witness Reading,** so a failure shows
  the whole state, not one number. Where it is the one value the
  assertion prints anyway, the label names it and adds nothing.
- **An answer's fields by their path, never by a substring.** A
  missing field by its name, never by a null.
- **The Invariant Slice Record's example numbers,** when the test
  tells its story, so the two can be read side by side.
- **A helper that may be refused returns the answer and asserts
  nothing.** The helper a setup relies on calls it, and asserts.

*Illustration:*
- **A label:** `.as("<what this number means>: %s", after)`.
- **Fields:** `Body.of(…).stringAt("$.orderId")`, and
  `Body.names("orderId")` for a missing one.
- **The example numbers:** fifty identical submissions released at
  one instant, one order recorded (the worked example's Runtime
  Ground).
- **A helper:** `trySubmit` beside `submit`.

### Why each rule is there

- **The State Witness before the answer.** A test that fails on a status
  code proves it reads status codes. A Red Run that stops at "expected
  409 but was 200" has never read the store.
- **The Falsifiable Promise before the exact numbers.** The numbers can be
  right for the story while the state is wrong somewhere else.
- **The Invariant Slice's invariant beside the Falsifiable
  Promise.** An Invariant Slice's invariant can be narrower than the
  Falsifiable Promise. A retry after a crash can leave one order in
  the store, so the Falsifiable Promise holds, and still be told the
  order does not exist, so the Invariant Slice's invariant is
  broken.
- **One read for what must agree.** Two reads can each be true and
  still not belong together: the order count read before a commit,
  its stored reply after it.
- **Every test says what it is,** so nobody has to ask what it is
  for, and a Decision Test is never counted as an Enemy Collision
  Kill.
- **The State Witness Reading in the labels,** so a failure read from the output
  alone says what the state was.

## What is exempt, and why

- **Structural Wall Checks:** a test that reads the store's own list
  of its constraints, or one that sends the store a refusal
  directly. They say *not evidence* at their class. They discharge
  no Enemy Collision Kill and need no State Witness.
- **Infrastructure tests:** health, the migration path, the
  Adversity Harness's own checks.

## What to check at a close

Read the Invariant Slice's tests and ask:

1. Does every test's first line say what it is?
2. On every State Witness Reading after the adversity, is the State
   Witness asserted before the answer?
3. Is the Falsifiable Promise, then the Invariant Slice's invariant
   where it differs, asserted before the exact numbers?
4. Is what must agree read in one read?
5. Does every label print the State Witness Reading?
6. Where a test differs from this Output Shape: did it drift, was the Output Shape
   wrong, did each have something, or is it a different kind of
   test? How each ends is the shapes-lifecycle Agent Rule's
   (`.claude/rules/shapes-lifecycle.md` §3, *A difference at the close*).
