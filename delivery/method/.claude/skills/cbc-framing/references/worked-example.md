# Worked example: a tiny order service through both workflows

*A demonstration run, invented for teaching, not a CBC Framing a CBC Run did.
It shows Part 1 (CBC Framing, Stages 0 to 6), the three CBC Framing
Exports it leaves behind, and how Part 2 (the cbc-slice Agent Skill)
consumes them. Kept deliberately small: one Falsifiable Promise, one
Responsibility Area.*

---

# Part 1 — the CBC Framing

## Stage 0 — Choose the Falsifiable Promise

Idea brought to the CBC Framing: "a backend where shops submit
customer orders."

Candidate Falsifiable Promises considered and recorded:
- "Fast order processing": rejected, a wish for a feature, not
  falsifiable.
- "Orders are never lost AND payment always completes": rejected,
  overloaded. Payment is a second purpose, so the choice was forced.

**Chosen Falsifiable Promise:** *One customer submission becomes
exactly one recorded order — no matter how many times it arrives.*

Falsifiable Promise Audience: the shop owner, the party the proof
matters to, since a double order is theirs to refund. Integrating
clients are callers. They enter the Enemy Census as actors, not the
CBC Framing Intent as its Falsifiable Promise Audience.

Falsifiable: the scenario that breaks it is concrete. A timeout
retry creates two orders, and a customer is charged twice.

Done, demonstrably:
- identical submissions really fired at once, and replayed after a
  lost response;
- the State Witness, recorded orders per submission read from the
  store, never above one;
- the path from this sentence to that test can be followed by the
  shop owner.

## Stage 1 — What must be ours? (LAYER-2-SYSTEM)

The System Possession Test on each candidate:

| Candidate | If someone else owned it, could they break the Falsifiable Promise? | Verdict |
|---|---|---|
| POSSESSION-1. The order records | Yes — they could double-record | **ours** |
| POSSESSION-2. The new-vs-repeat decision | Yes — a retrying caller deciding "I'm new" breaks it | **ours** |
| POSSESSION-3. The answer to a repeated submission | Yes — a wrong replay creates a second order | **ours** |
| Payment processing | No — the Falsifiable Promise stays true even if payment fails | refused, written |
| Product catalog correctness | No — someone else's fact | refused, written |
| Notifying the customer | No | refused, written |

Enemy Sketches used, for Stage 2 to make exact: a retrying caller,
a store that answers strangely. The boundary: submissions cross from
outside, so they are parsed and checked at the door.

## Stage 2 — Name the enemies (LAYER-1-ENVIRONMENT)

Follow one submission through its life: caller → network → our
process → store → network → caller. Everything beyond our control is
an actor. Enemy Facts, consequence first:

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

Trust Assumptions — accepted deliberately, not defended: **ASSUMPTION-1.**
Our service is the only writer of the order records; whoever holds the
store's own credentials writes none by hand.

Enemy Census check: one Trust Assumption, and it answers who besides
us writes what we store. "The store is atomic" does not appear: the
store appears only as something that can hurt us.

Enemy Census Saturation:
1. Enemy Census Probe 1, the assumption hunt ("what does 'recorded'
   quietly assume?"), found the Enemy Fact of the unknowable write;
2. Enemy Census Probe 2, the timeline stretched (a retry arriving a
   day later), found nothing new;
3. Enemy Census Probe 3, the resource lens, quantities at huge (a key reused thousands
   of times), found nothing new.

Two Enemy Census Probes in a row found nothing new: Enemy Census Saturation.

The Runtime Ground, beside the Enemy Facts:
1. the machine: one local machine;
2. a stranger's clean machine stands the system up from the README;
3. the instances: one instance of our process, since no Enemy Fact
   has two instances racing;
4. the store: a service on that machine, reachable by the instance
   and outliving it;
5. the clock: the machine's;
6. the size: one shop, up to ten thousand orders, each a record and
   its key kept for life, and fifty identical submissions racing at
   once, the count the evidence will use.

Revision check: did the Enemy Census reveal a missed System
Possession? No. LAYER-2-SYSTEM stands, and no CBC Framing Export
Revision is logged.

The lists the exit leaves:
- Scope Exclusions: **NOT-OURS-1** a shop edits or cancels an order
  after it is recorded: the subject of another Falsifiable Promise.
  **NOT-OURS-2** a caller submits as another shop: identity at the
  door, a new kind of difficulty. **NOT-OURS-3** a console or a
  script writes order records: the Trust Assumption says none does.
- Scope Verdicts: none.
- Enemy Census Gaps: clock skew between machines (one machine);
  deployment transitions (no second version ever runs beside the
  first).

## Stage 3 — Run the Enemy Collisions (LAYER-4-PROBLEMS)

Each Enemy Fact × each System Possession: what dies, never how it is
saved.

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
order exists for one submission.** What KILL-1 kills, the answer lost
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

Each enemy a Scope Exclusion covers, tried and stopped:

**HOLDS-1.** NOT-OURS-1, a shop editing or cancelling a recorded
order × POSSESSION-1 → the order changes after it is recorded:
nothing dies. The Falsifiable Promise is about recording one order,
not what happens to it after. Stopped by NOT-OURS-1.

**HOLDS-2.** NOT-OURS-2, a caller submitting as another shop ×
POSSESSION-2 → the submission is judged under the wrong shop's
keys: nothing dies. One submission still makes one order; who may
submit is identity at the door. Stopped by NOT-OURS-2.

**HOLDS-3.** NOT-OURS-3, a console or a script writing order
records × POSSESSION-1 → a record appears that no submission made:
nothing dies. The Trust Assumption says no console or script writes
order records. Stopped by NOT-OURS-3.

Merged by what each Enemy Fact does to us:
- KILL-1 to KILL-3 are one CBC Framing Concern: the same failure, a
  second order, caused three ways.
- KILL-4 and KILL-6 are one CBC Framing Concern, partial failure.
  Its proof obligation is "recovery converges", different from
  "duplicates collapse".
- KILL-5 stands alone: a lie, not a repeat.

An Invariant Slice Fold Candidate found with no enemy: "what a valid
submission is", the contract. It is shaped as a contract, with no
invariant under adversity, so it folds, and is not an Invariant
Slice.

## Stage 4 — Sort into owners (LAYER-3-AREAS)

All CBC Framing Concerns touch one state, the order records, and one
decision, new or repeat. A candidate Responsibility Area Seam was
examined: "key management" as its own Responsibility Area. It fails the
test: no separate state, no separate decision authority. Named, not
drawn. **Ownership: one Responsibility Area, order intake.** Confirmed
by sorting, not assumed.

## Stage 5 — Between owners (LAYER-5-INTERACTION)

**Empty, with reasons:** one Responsibility Area (Stage 4); no
sibling systems to coordinate (payment refused at LAYER-2-SYSTEM).
Each emptiness traces to a decision.

## Stage 6 — Cut the Invariant Slice Registry

The Invariant Slice Split Test: two Enemy Collision Kills are two
Invariant Slices only if their evidence must create *different
adversity*.

- **SLICE-1 — "exactly once under duplicate delivery."** Invariant:
  N arrivals of one submission → exactly one recorded order. Covers
  KILL-1 to KILL-3 and KILL-5: its evidence must create replays,
  races, AND the lie of a reused key. Judgment logged: races are merged
  here because duplicate delivery is the one Adversity Class, the
  concurrent case its hardest.
- **SLICE-2 — "recovery converges under partial failure."**
  Invariant: a crash at any point leaves the system where a retry
  ends in exactly one order and one truthful answer. Covers KILL-4
  and KILL-6. Its evidence is different, killing mid-transaction, not
  hammering, so it is an Invariant Slice of its own.

CBC Framing Reconciliation: the submission contract becomes FOLD-1,
an Invariant Slice Fold in SLICE-1's Correctness Specification, its
checks going with it. Nothing dropped: 6 Enemy Collision Kills → 2
Invariant Slices + 1 Invariant Slice Fold.

Invariant Slice Registry: SLICE-1 `chosen-next`. SLICE-2
presumes the uniqueness SLICE-1 builds. That is an expectation,
decided again at the Invariant Slice Close.

---

## What now exists (the three CBC Framing Exports)

1. **CBC Framing Intent:** the Falsifiable Promise in one sentence,
   its Falsifiable Promise Audience, what done demonstrably means, and the rejected
   candidates.
2. **System Definition:**
   - LAYER-1-ENVIRONMENT: the six Enemy Facts, one Trust Assumption,
     the Runtime Ground, three Scope Exclusions and the Enemy Census
     Gaps;
   - LAYER-2-SYSTEM: three System Possessions, three written System
     Refusals;
   - LAYER-3-AREAS: one Responsibility Area, one Responsibility Area
     Seam named and not drawn;
   - LAYER-4-PROBLEMS: six Enemy Collision Kills, three tried
     collisions where nothing dies (HOLDS-1 to HOLDS-3), and the CBC
     Framing Concerns;
   - LAYER-5-INTERACTION: empty, with reasons.
3. **Invariant Slice Registry:** 2 Invariant Slices + 1 Invariant
   Slice Fold, the CBC Framing Reconciliation, SLICE-1 `chosen-next`.

---

# Part 2 — SLICE-1 enters the cbc-slice Agent Skill

## Stage 1 — specify-correctness

Stage 1 takes the Invariant Slice Entry
*as written*, with no translation:

- Invariant: N arrivals of one submission → exactly one recorded order.
- Adversity, taken from the Enemy Census in LAYER-1-ENVIRONMENT, not
  invented: sequential retries, simultaneous duplicates, lost
  responses, key reuse with a different body.
- Invariant Slice Guarantee Challenge, "what would let this hold on
  paper yet break in fact?":
  - **GUARANTEE-1, uniqueness:** a key can never map to two orders;
  - **GUARANTEE-2, winner/loser:** of simultaneous duplicates,
    exactly one creates, and the rest observe it;
  - **GUARANTEE-3, safe replay:** a repeat receives the original
    outcome, changing nothing;
  - **GUARANTEE-4, key scope:** a repeat is only a repeat if the
    body matches. A mismatch is an error, never a silent success.
- Evidence Criteria:
  - **EVIDENCE-1:** a hammering test, many concurrent identical
    submissions (GUARANTEE-1 and GUARANTEE-2);
  - **EVIDENCE-2:** an injected-replay test, a retry after a
    lost response (GUARANTEE-3);
  - **EVIDENCE-3:** a mismatched-body test (GUARANTEE-4).

  Gate passed: zero mechanisms named.

## Stage 2 — plan

One Structural Wall per Invariant Slice Guarantee,
the strongest available:
- GUARANTEE-1: a database unique constraint on the key. *It defeats
  duplicates because the second insert cannot physically succeed.*
- GUARANTEE-2: the same constraint's winner, and the losers reading
  the winner's row;
- GUARANTEE-3: the stored original response, returned on conflict;
- GUARANTEE-4: a body hash stored with the key, compared on conflict.

Escape Hatch Hunt, against the Trust Assumption: every write path of
ours, an admin endpoint included, goes through the same
constraint-guarded table. There is no Escape Hatch. Someone at the
store's console is trusted, not walled against (NOT-OURS-3). Gate
passed: no Invariant Slice Guarantee without its Structural Wall.

## Stage 3 — build

Plain code, plus the evidence. Hammer it, inject
the replay, send the mismatched body, and watch the invariant survive,
one Invariant Slice Guarantee at a time. Each test has a Red Run,
its Structural Wall absent, failing on the State Witness, recorded
orders per submission read from the store, never on a status code
first. Beside them, the unique constraint is shown on its own: a
second row with the key, written straight to the store, is refused.
That is a Structural Wall Check, not evidence. Gate: green happy-path
tests close nothing. Only tests that create the adversity do.

## Stage 4 — document

The Invariant Slice Record completed, one
Invariant Slice Guarantee Block each. GUARANTEE-1 to GUARANTEE-4 each
hold its attack, its Evidence Criterion, its Structural Wall and the
tests that proved it. SLICE-1 closes in the Invariant Slice Registry
as `closed (date, evidence)`, and the Invariant Slice Registry
decides again what is next.

---

## What the example shows about the handoffs

- The Enemy Census (Stage 2) is where Part 2's Adversity Models come
  from: the Correctness Specification *took* its threats from
  LAYER-1-ENVIRONMENT.
- The Enemy Collision Kills (Stage 3) arrived in the Correctness
  Specification shaped as invariants: the handoff needs no
  translation.
- The System Refusals (Stage 1) are why the Correctness Specification
  never mentions payment.
- The thin LAYER-3-AREAS is why there is exactly one place the code
  and its Structural Walls live.
- The Invariant Slice Fold carried the contract's checks into SLICE-1
  instead of losing them.
