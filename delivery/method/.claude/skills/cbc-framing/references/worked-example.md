# Worked example: a tiny order service through both workflows

*A demonstration run, invented for teaching — not a lived framing. It shows
part 1 (framing, stages 0–6), the three artifacts it leaves behind, and how
part 2 (the slice workflow) consumes them. Kept deliberately small: one
promise, one area.*

---

# Part 1 — the framing

## Stage 0 — Choose the promise

Idea brought to the walk: "a backend where shops submit customer orders."

Candidate promises considered and banked:
- "Fast order processing" — rejected: a feature-wish, not falsifiable.
- "Orders are never lost AND payment always completes" — rejected:
  overloaded; payment is a second purpose, forced to choose.

**Chosen promise:** *One customer submission becomes exactly one recorded
order — no matter how many times it arrives.*
Audience: the shop owner — the party the proof matters to, since a double
order is theirs to refund. Integrating clients are callers: they enter the
census as actors, not the intent as audience.
Falsifiable: the breaking scenario is concrete — a timeout retry creates
two orders, a customer is charged twice.
Done, demonstrably: identical submissions genuinely fired at once and
replayed after a swallowed response; the witness — recorded orders per
submission, read from the store — never above one; and the path from this
sentence to that test followable by the shop owner.

## Stage 1 — What must be ours? (LAYER-2-SYSTEM)

Hostage test on each candidate:

| Candidate | If someone else owned it, could they break the promise? | Verdict |
|---|---|---|
| POSSESSION-1. The order records | Yes — they could double-record | **ours** |
| POSSESSION-2. The new-vs-repeat decision | Yes — a retrying caller deciding "I'm new" breaks it | **ours** |
| POSSESSION-3. The answer to a repeated submission | Yes — a wrong replay creates a second order | **ours** |
| Payment processing | No — promise stays true even if payment fails | refused, written |
| Product catalog correctness | No — someone else's fact | refused, written |
| Notifying the customer | No | refused, written |

Sketch-enemies used (debt for stage 2): a retrying caller, a store that
answers strangely. Edge note: submissions cross from outside → parsed and
checked at the door.

## Stage 2 — Name the enemies (LAYER-1-ENVIRONMENT)

Follow one submission through its life: caller → network → our process →
store → network → caller. Everything beyond our control is an actor. Facts,
consequence-first:

- **FACT-CALLER-1.** Callers resend the same submission after a timeout →
  we face the same order twice.
- **FACT-CALLER-2.** Two identical submissions can arrive at the same
  instant → we face a race, not just a repeat.
- **FACT-NETWORK-3.** A response can be lost *after* we recorded the order
  → the caller doesn't know, will retry, and we must answer again without
  creating again.
- **FACT-PROCESS-4.** Our process can die between accepting and recording,
  or between recording and responding → we face half-done work at every
  boundary.
- **FACT-CALLER-5.** A caller can reuse an idempotency key with a
  *different* order body → we face a lie: "this is a repeat" when it isn't.
- **FACT-STORE-6.** A write's outcome can be unknowable (store timeout) →
  we face uncertainty about our own state.

Trust assumptions — accepted deliberately, not defended: **ASSUMPTION-1.**
Our service is the only writer of the order records; whoever holds the
store's own credentials writes none by hand.

Census check: one trust line, and it answers who besides us writes what we
store; "the store is atomic" does not appear — the store appears only as
something that can hurt us. Saturation: probe 1 (assumption hunt — "what
does 'recorded' quietly assume?") surfaced the unknowable-write fact; probe
2 (timeline stretched — a retry arriving a day later) surfaced nothing new;
probe 3 (quantities at huge — a key reused thousands of times) surfaced
nothing new. Two dry probes → saturated.

The runtime ground, beside the facts: one local machine; a stranger's clean
machine stands the system up from the README; one instance of our process
— no census line races two of us; the store a service on that machine,
reachable by the instance and outliving it; the clock the machine's; built
for one shop — up to ten thousand orders, each a record and its key kept
for life, and fifty identical submissions racing at once, the hammering's
own count.

Return trip check: did the census reveal a missed possession? No —
LAYER-2-SYSTEM stands, no revision logged.

The ledgers the exit leaves:
- Fence list — **NOT-OURS-1** a shop edits or cancels an order after it is
  recorded: another promise's territory. **NOT-OURS-2** a caller submits as
  another shop: identity at the door, a new kind of difficulty.
  **NOT-OURS-3** a console or a script writes order records: the trust line
  says none does.
- Not probed — clock skew between machines (one machine); deployment
  transitions (no second version ever runs beside the first).

## Stage 3 — Run the collisions (LAYER-4-PROBLEMS)

Each fact × each possession — what dies (never how it's saved):

**KILL-1.** FACT-CALLER-1 × POSSESSION-1 → a submission resent after
a timeout is recorded again: **a second order exists for one
submission.**
*Say:* order 1 is recorded for key K; its caller times out after five
seconds and resends K; the store holds orders 1 and 2 for K.

**KILL-2.** FACT-CALLER-2 × POSSESSION-2 → two identical submissions
each decide "new" before either is recorded: **two orders exist for
one submission.**
*Say:* fifty identical submissions released at one instant; each
finds no order for its key; the store holds two orders for the key,
or fifty.

**KILL-3.** FACT-NETWORK-3 × POSSESSION-3 → the order is recorded,
its answer is lost, and the retry is answered as new: **a second
order exists for one submission.** KILL-1's death, the answer lost
rather than late.
*Say:* order 1 is recorded for key K and "created" is sent; the
network drops it; the caller resends K; the store holds orders 1 and
2 for K.

**KILL-4.** FACT-PROCESS-4 × POSSESSION-1 → we die between
recording and replying, two ways:
(a) recorded, then killed before the reply: **an order exists that
its caller cannot confirm.**
(b) replied, then killed before the record commits: **an order is
confirmed that does not exist.**
*Say:* (a) a submission with key K is recorded; the process is
killed; the store holds one order for K, and the caller holds no
reply. (b) the caller holds "created" for K; the store holds none.

**KILL-5.** FACT-CALLER-5 × POSSESSION-2 → a key reused with a
different body is judged a repeat: **the wrong order is silently
confirmed as a "repeat."**
*Say:* key K records an order for two mugs; the caller sends K again
for five plates; it is answered "repeat" with the order for two mugs,
and no order for five plates exists.

**KILL-6.** FACT-STORE-6 × POSSESSION-1 → a write times out and its
outcome cannot be known: **we ourselves don't know if the order
exists.**
*Say:* the write for key K times out after two seconds; the store
holds one order for K or none, and nothing we hold says which.

Fenced facts collide with nothing: NOT-OURS-1 to NOT-OURS-3 stop at the
fence.

Dedup by attack surface: KILL-1 to KILL-3 are one concern: the same
failure, a second order, caused three ways. KILL-4 and
KILL-6 are one concern (partial failure — the proof obligation is "recovery
converges," different from "duplicates collapse"). KILL-5 stands alone (a
lie, not a repeat). Fold-candidate found with no enemy: "what a valid
submission is" (the contract) — contract-shaped, no
invariant-under-adversity → folds, not a slice.

## Stage 4 — Sort into owners (LAYER-3-AREAS)

All concerns touch one state (the order records) and one decision
(new-vs-repeat). Candidate seam probed: "key management" as its own area —
fails the bar: no separate state, no separate decision authority. Named,
not drawn. **Ownership: one area — order intake.** Confirmed by sorting,
not assumed.

## Stage 5 — Between owners (LAYER-5-INTERACTION)

**Empty, with reasons:** one internal area (stage 4); no sibling systems to
coordinate (payment refused at LAYER-2-SYSTEM). Each emptiness traces to a
decision.

## Stage 6 — Cut the slice surface

Operational test — two kills are two slices only if their evidence must
create *different adversity*:

- **SLICE-1 — "exactly once under duplicate delivery."** Invariant: N
  arrivals of one submission → exactly one recorded order. Covers
  KILL-1 to KILL-3 and KILL-5 (its evidence must create replays, races, AND
  the reused-key lie). Judgment logged: races fold in here because duplicate
  delivery is the one adversity class, the concurrent case its hardest.
- **SLICE-2 — "recovery converges under partial failure."** Invariant: a
  crash at any point leaves the system where a retry ends in exactly one
  order and one truthful answer. Covers KILL-4 and KILL-6. Different
  evidence: kill-mid-transaction, not hammering — hence its own slice.

Folds, reconciled: the submission contract → folds into SLICE-1's spec, as
FOLD-1 (its checks ride along). Nothing dropped: 6 kills → 2 slices + 1
fold.

**Registry:** SLICE-1 chosen-next (SLICE-2 presumes SLICE-1's uniqueness
ground — an expectation, re-decided at close).

---

## What now exists (the three artifacts)

1. **Intent:** the promise, one sentence, its audience and what done
   demonstrably means, plus banked rejections.
2. **System definition:** LAYER-1-ENVIRONMENT the six facts, one trust
   line, the runtime ground, three fences and the not-probed ledger ·
   LAYER-2-SYSTEM three possessions, three written refusals ·
   LAYER-3-AREAS one area, one seam named-not-drawn · LAYER-4-PROBLEMS the
   concerns · LAYER-5-INTERACTION empty-with-reasons.
3. **Slice registry:** 2 slices + 1 fold, reconciliation line, SLICE-1
   chosen-next.

---

# Part 2 — SLICE-1 enters the slice workflow

**specify-correctness** consumes the registry entry *as written* — zero
translation:

- Invariant: N arrivals of one submission → exactly one recorded order.
- Adversity (pulled from the LAYER-1-ENVIRONMENT census, not invented):
  sequential retries, simultaneous duplicates, lost responses, key reuse
  with different body.
- Guarantee challenge — "what would let this hold on paper yet break in
  fact?": **GUARANTEE-1, uniqueness** — a key can never map to two
  orders; **GUARANTEE-2, winner/loser** — of simultaneous duplicates,
  exactly one creates, the rest observe it; **GUARANTEE-3, safe replay** —
  a repeat receives the original outcome, changing nothing;
  **GUARANTEE-4, key scope** — a repeat is only a repeat if the body
  matches; a mismatch is an error, never a silent success.
- Evidence criteria: **EVIDENCE-1** a hammering test (many concurrent
  identical submissions; GUARANTEE-1 and GUARANTEE-2), **EVIDENCE-2** an
  injected-replay test (retry after a swallowed response; GUARANTEE-3),
  **EVIDENCE-3** a mismatched-body test (GUARANTEE-4). Gate passed: zero
  mechanisms named.

**plan** — one structural owner per guarantee, strongest wall available:
GUARANTEE-1, a database unique constraint on the key — *defeats
duplicates because the second insert cannot physically succeed*;
GUARANTEE-2, the same constraint's winner + losers reading the winner's
row; GUARANTEE-3, the stored original response, returned on conflict;
GUARANTEE-4, a body-hash stored with the key, compared on conflict.
Escape-hatch hunt, against the trust line: every write path of ours — an
admin endpoint included — goes through the same constraint-guarded table,
no side door; a hand at the store's console is trusted, not walled
(NOT-OURS-3). Gate passed: no unowned guarantee.

**build** — boring code plus the evidence: hammer it, inject the replay,
send the mismatched body — watch the invariant survive, guarantee by
guarantee. Each test is seen red with its wall absent, failing on the
witness — recorded orders per submission, read from the store — never on a
status code first. Beside them, the unique constraint shown on its own: a
second row with the key written straight to the store, refused — the
wall's own check, not evidence. Gate: green happy-path tests close nothing;
only adversity-creating tests do.

**document** — the record completed, one block per guarantee: each of
GUARANTEE-1 to GUARANTEE-4 holds its attack, its evidence criterion, its
owner and the tests that proved it. SLICE-1 closes in the registry as
evidence-closed; the registry re-decides what's next.

---

## What the example shows about the seams

- The census (stage 2) is where part 2's adversity models come from — the
  spec *pulled* its threats from LAYER-1-ENVIRONMENT.
- The kills (stage 3) arrived in the spec invariant-shaped — the
  zero-translation handoff.
- The refusals (stage 1) are why the spec never mentions payment.
- The thin LAYER-3-AREAS is why there is exactly one place the code and its
  walls live.
- The fold carried the contract checks into SLICE-1 instead of losing them.