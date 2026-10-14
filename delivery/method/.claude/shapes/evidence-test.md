---
foundation: practice, under the shapes convention
---

# The shape of an evidence test

**Governs:** how an evidence test is written: the first line of its
comment, the order of its assertions, and the labels on them. Its
form only. Which adversity a test creates, and which guarantee it
answers, come from the slice record.

<!-- A shape: what a kind of output looks like, its form and never
     its content. Read at a slice's closing gate, never while a test
     is written. How shapes live is .claude/rules/shapes-lifecycle.md,
     and not repeated here. When a red run counts is cbc-slice's
     build gate, not this shape's. -->

## What this document controls

**Three kinds of test.** Each sits beside a slice's evidence:
- a test that creates an adversity at the door and reads the
  witness;
- a structural test, which reads the code;
- a tripwire, which pins a decision and is not evidence.

A test this shape accepts can still create the wrong adversity.
That is the slice record's business.

**Not covered: a test of one wall on its own,** such as a catalog
check, or the store refusing a statement sent to it directly. It
says so at its class, and its form is its own.

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

A tripwire says it is not evidence, and names the decision it pins:

```java
/**
 * Not evidence — a tripwire for the choice in SLICE-1's record, "A
 * repeat gets the stored first reply": <the decision it pins>. It
 * guards the decided option, not the promise, and discharges no kill.
 */
```

*Skeleton:*

- **The first line names what the test is.** For evidence: the
  slice, the criterion, the guarantee, and the kill where it answers
  one (a test for a fold or a structural rule may answer none). For
  a tripwire: "not evidence", and the decision it pins.
- **Then the story in plain words,** with the numbers it runs on,
  and what would make it fail.
- **The class says where its slice record is,** and which numbers
  its tests start from.

*Illustration:* `SLICE-<n> EVIDENCE-<m> · GUARANTEE-<k> — KILL-<j>`,
numbered as in the slice record. The slice is named because a test
sits outside its record.

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

1. **The witness first.** Read it from where the truth is stored,
   never from the replies. When two of its numbers must agree with
   each other, read them in one read.
2. **Then the promise,** on every reading taken after the
   adversity, sampled readings included. A reading taken before the
   adversity only checks the scene is set; it owes nothing.
3. **Then the slice's own invariant,** where it differs from the
   promise.
4. **Then the exact numbers,** then the state of each thing the
   adversity touched.
5. **The door's answer last.**

*Illustration:*
- **The witness:** `Witness.read`, plain SQL from outside the
  service, as the identity the service runs as.
  `Witness.read(key)` reads the orders recorded for the key and
  their bodies in one statement.
- **The promise:** `Witness.Orders.holds()`: the key's submission
  is exactly one recorded order.
- **A slice's own invariant:** SLICE-1's is the promise itself, so
  it owes none. SLICE-2's, "a retry after a crash ends in one order
  and one truthful answer", adds the answer, asserted beside the
  promise.
- **The answer:** the status, then the body by JSON path.

### How its assertions read

*Skeleton:*

- **A label prints the reading,** so a failure shows the whole
  state, not one number. Where the reading is the one value the
  assertion prints anyway, the label names it and adds nothing.
- **An answer's fields by their path, never by a substring.** A
  missing field by its name, never by a null.
- **The record's example numbers,** when the test tells the
  record's story, so the two can be read side by side.
- **A helper that may be refused returns the answer and asserts
  nothing.** The helper a scene relies on calls it, and asserts.

*Illustration:*
- **A label:** `.as("<what this number means>: %s", after)`.
- **Fields:** `Body.of(…).stringAt("$.orderId")`, and
  `Body.names("orderId")` for a missing one.
- **The example numbers:** fifty identical submissions released at
  one instant, one order recorded (the worked example's runtime
  ground).
- **A helper:** `trySubmit` beside `submit`.

### Why each rule is there

- **The witness before the answer.** A test that fails on a status
  code proves it reads status codes. A red that stops at "expected
  409 but was 200" has never read the store.
- **The promise before the exact numbers.** The numbers can be
  right for the story while the state is wrong somewhere else.
- **The slice's invariant beside the promise.** A slice's invariant
  can be narrower than the promise. A retry after a crash can leave
  one order in the store, so the promise holds, and still be told
  the order does not exist, so the slice's invariant is broken.
- **One read for what must agree.** Two reads can each be true and
  still not belong together: the order count read before a commit,
  its stored reply after it.
- **Every test says what it is,** so nobody has to ask what it is
  for, and a tripwire is never counted as a kill.
- **The reading in the labels,** so a failure read from the output
  alone says what the state was.

## What is exempt, and why

- **A wall's own checks:** a catalog test, or the store's refusals
  sent directly. They say *not evidence* at their class. They
  discharge no kill and need no witness.
- **Infrastructure tests:** health, the migration path, the
  harness's own checks.

## What to check at a close

Read the slice's tests and ask:

1. Does every test's first line say what it is?
2. On every reading after the adversity: is the witness asserted
   before the answer, and the promise (then the slice's invariant,
   where it differs) before the exact numbers? Is what must agree
   read in one read?
3. Does every label print the reading?
4. Where a test differs from this shape: did it drift, was the shape
   wrong, did each have something, or is it a different kind of
   test? The shapes rule says how each ends.
