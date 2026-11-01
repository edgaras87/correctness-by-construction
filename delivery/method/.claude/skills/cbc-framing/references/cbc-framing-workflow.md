# CBC Framing workflow — layering the system

*The first part of the method: how a standing idea becomes a System
Definition in layers and an Invariant Slice Registry. It ends exactly
where `.claude/skills/cbc-slice/references/cbc-slice-workflow.md`
begins: its output is that workflow's input.*

*When an Agent Skill Stage's required output changes here,
`.claude/skills/cbc-framing/references/worked-example.md` beside this
file changes in the same commit. The agent running a CBC Framing is
sent to it to see what an Agent Skill Stage's output looks like. This
file owns the worked example. The copy,
`.claude/skills/cbc-slice/references/worked-example.md`, follows it.*

---

## The unit

A CBC Framing is one Falsifiable Promise worked into an Invariant
Slice Registry. Input: a standing idea, such as a need or a candidate
problem. Output: the three CBC Framing Exports:

- the CBC Framing Intent, the Falsifiable Promise;
- the System Definition, its five System Layers filled in;
- the Invariant Slice Registry, the work, cut and ready.

A CBC Framing may end in **no project**. That is a valid
exit, not a failure.

## The order, and why it differs from the presentation

The System Layers are *presented* from LAYER-1-ENVIRONMENT to
LAYER-5-INTERACTION, from the outside in. They are *derived* in a
different order, and the difference is deliberate:

```
Stage 0  choose the Falsifiable Promise  (CBC Framing Intent)   — one claim worth proving
Stage 1  what must be ours?              (LAYER-2-SYSTEM)       — System Possession Test
Stage 2  name the enemies                (LAYER-1-ENVIRONMENT)  — the Enemy Census
Stage 3  run the Enemy Collisions        (LAYER-4-PROBLEMS)     — Enemy Facts × System Possessions
Stage 4  sort into owners                (LAYER-3-AREAS)        — only if Enemy Collisions force it
Stage 5  check between owners            (LAYER-5-INTERACTION)  — only if owners exist
Stage 6  cut the Invariant Slice Registry                       — theorems vs contracts
```

Two swaps of order, used in all six CBC Framings so far: two CBC
Framings made before the first CBC Run, and those of CBC Runs 3 to 6.

- **LAYER-2-SYSTEM before LAYER-1-ENVIRONMENT.** The Falsifiable
  Promise can be derived on rough Enemy Sketches. The full Enemy
  Census comes after, and makes the sketches exact.
- **LAYER-4-PROBLEMS before LAYER-3-AREAS.** Responsibility Areas are
  *found* by sorting Enemy Collisions, never drawn first on
  intuition.

## How the layers communicate

Four rules govern every handoff:

1. **Downward, each Agent Skill Stage consumes exactly the previous
   one's output:**
   - the Falsifiable Promise feeds the System Possession Test;
   - the System Possessions set what the Enemy Census covers;
   - Enemy Facts × System Possessions feed the Enemy Collisions;
   - the Enemy Collision Kills feed the sort into owners;
   - the owners feed the Responsibility Area Seams;
   - everything feeds the cut.

   An Agent Skill Stage whose input is not the previous one's output
   is out of order.
2. **Upward only through a CBC Framing Export Revision, never a
   scheduled one.** The Enemy Census (Stage 2) may reveal a missed
   System Possession or an unwritten System Refusal. Then
   LAYER-2-SYSTEM gets a CBC Framing Export Revision. If not, LAYER-2-SYSTEM
   stands. There is no routine scheduled re-read back up: that
   reopens settled layers forever.
3. **Reasoning may cross layers; statements may not.** Talk of
   enemies is allowed inside a *derivation* ("ours *because* a
   retrying caller could break the Falsifiable Promise"). The
   resulting LAYER-2-SYSTEM statement stays purely LAYER-2-SYSTEM.
   Every recorded statement sits in exactly one System Layer.
4. **Every "outside" is written:** a System Refusal, a deferral, a
   rejected candidate Falsifiable Promise
   (`.claude/skills/cbc-framing/SKILL.md`, *The mode — non-negotiable*).

---

## Tags — one name per thing, in full words

Every numbered item in the CBC Framing Exports gets a tag: its kind
in capitals, then a domain where it helps, then the number. It has
one spelling everywhere, at the source and in every citation, so a
search finds every use. Numbers run once through a CBC Framing
Export, never restarting per section.

| Item | Tag | Example |
|---|---|---|
| a System Possession (Stage 1) | POSSESSION-<n> | POSSESSION-4 |
| an Enemy Fact (Stage 2), with its actor | FACT-<ACTOR>-<n> | FACT-STORE-19 |
| a Trust Assumption (Stage 2) | ASSUMPTION-<n> | ASSUMPTION-4 |
| a Scope Exclusion (Stage 2) | NOT-OURS-<n> | NOT-OURS-2 |
| a Scope Verdict (Stage 2) | SYSTEM-BOUNDARY-<n> | SYSTEM-BOUNDARY-5 |
| an Enemy Collision Kill (Stage 3) | KILL-<n> | KILL-15 |
| an Invariant Slice Fold (Stage 6) | FOLD-<n> | FOLD-1 |
| an Invariant Slice (Stage 6) | SLICE-<n> | SLICE-4 |
| a System Layer, its number before its name, as `docs/concept/01-layered-system.md` has them | LAYER-<n>-<NAME> | LAYER-4-PROBLEMS |

A CBC Framing Concern that becomes exactly one Invariant Slice is
called by that Invariant Slice's tag from Stage 6 on. A CBC Framing
Concern that does not is called by a letter: A, B and on. A number local to
one record carries its owner outside it
(`.claude/rules/writing.md`, rule 6): "SLICE-4 GUARANTEE-1".

## Stage 0 — Choose the Falsifiable Promise (CBC Framing Intent)

*Question: what claim does this project make, and to whom does the
proof matter?*

Name the capability. Name who values it. Name what "done"
demonstrably means. Filter out candidate Falsifiable Promises that are really features:
*could this claim be false, and would proving it true matter to the
Falsifiable Promise Audience?* A second real purpose is not a second Falsifiable Promise. A
CBC Framing Intent carrying two is overloaded: force the choice.

Three sharpenings, each written into the CBC Framing Intent:

- **The Falsifiable Promise Audience is who the claim is made to:**
  the party for whom the proof matters. Those who use the running
  system, callers and services, cannot be made a claim. They create
  adversity, and enter the Enemy Census as actors, never the CBC
  Framing Intent as its Falsifiable Promise Audience.
- **Worth proving is two questions, both answered concretely:**
  - could it be false? Its negation is named as an event, not a
    vague worry;
  - would proving it true matter to the Falsifiable Promise Audience?
- **What "done" demonstrably means, spelled out:**
  - the named adversity is really created, never sequential replay
    pretending to be it;
  - the State Witness, read from outside on the stored state, never
    shows the Falsifiable Promise broken;
  - the Falsifiable Promise Audience can follow the path from claim
    to proof.

**Exit:** one Falsifiable Promise, one sentence, falsifiable, worth
proving.
**Hands down:** the Falsifiable Promise. **Residue (written):** the
rejected candidates and the purposes not chosen, recorded in
`intent.md`.

## Stage 1 — What must be ours? (LAYER-2-SYSTEM)

*Question: to keep that Falsifiable Promise, what must we own, and
what do we refuse?*

The test is the System Possession Test. For each candidate System
Possession: *"if somebody else owned this, could they break the
Falsifiable Promise without us being able to stop them?"* Yes: ours.
No: run the System Refusal Test, *"can the Falsifiable Promise stay
true even if this goes wrong elsewhere?"* Yes: refused, in writing.

The tests run on Enemy Sketches, such as a retrying caller or a lying
store. They are informal, concrete just enough for the test. Stage 2
makes them exact.

**Exit:** the owned responsibilities stated; the System Refusals
stated.
**Hands down:** the System Possessions, which say what the Enemy
Census must cover, and the Enemy Sketches still to be made exact.
Stage 1 also sets the boundary. Every crossing from outside is
where untrusted becomes trusted: check at the door.

## Stage 2 — Name the enemies (LAYER-1-ENVIRONMENT)

*Question: who and what touches us, and how does each fail, lie, or
repeat?*

List the actors by following one request through its whole life.
Everything it touches beyond our control is an actor: typically
callers, the network, our own process, the store. For each, the
three negations: **vanishes, duplicates, lies**. Keep only *Enemy
Facts*, concrete enough to attack with ("responses get lost", not
"networks are unreliable"). State each consequence first: what the
Enemy Fact leaves *us* facing.

**The mistake to avoid:** an Enemy Census is not a list of
assumptions. Listing what you *trust* ("the store is atomic"), in
place of what can *hurt* ("a write's outcome can be unknowable"),
passes a casual reading and fails Stage 2's Exit. The store is an
actor that can hurt you, not a helper whose tools always work.

Two labelled blocks are allowed beside the Enemy Facts, never in
their place.

**The first block is the Trust Assumptions,** under the label
**"Trust Assumptions — accepted deliberately, not defended"**. It is
the opposite of hidden trust. Each line is a deliberate acceptance a
reviewer can challenge ("the store durably holds a commit it
acknowledged"). The block is kept short. Once it is easier to extend
than the list of Enemy Facts, it has become the mistake above.

The block must answer one question, either way, in any system that keeps
state: **who besides the system can write what it stores?** It may
be a console, a script, another service, or the store's superuser.
- Trusted: the writer is a line in this block, and what it does not
  cover is a Scope Exclusion.
- Defended: the writer is an actor in the Enemy Census, and every
  Invariant Slice builds a Structural Wall against it.

Left unsaid, each Invariant Slice answers it alone. The cautious
answer, defend against anyone who might write, has no end: a writer
who can remove a Structural Wall cannot be walled against.

**The second block is the Runtime Ground,** under the label **"The
Runtime Ground"**. The work that establishes the Runtime Ground,
after CBC Framing, requires it. It says what the system assumes
about where it runs, so the Runtime Ground is derived from need
rather than habit. It has six lines:

1. **the machine:** one local machine, or not;
2. **a stranger's clean machine,** if the system must stand up from
   one by the README's commands;
3. **the instances:** whether more than one instance of our process
   runs on that machine. It is an Enemy Fact, not a deployment
   choice, when the Enemy Census has the instances race;
4. **the store:** a service on that machine, reachable by every
   instance and outliving any of them. What it is stays the decision of
   the work that establishes the Runtime Ground;
5. **the clock:** the machine's, shared by the instances unless the
   evidence skews it;
6. **the size it is built for:** how many of the things it counts,
   how many records one of them gathers over its life, how many
   instances, how many requests racing at once. At least the
   evidence's size, so that a later plan can say what each
   Structural Wall's cost assumes.

Beyond that size nothing is promised about speed, unless the
Falsifiable Promise says so. Six lines, not a design. System
Readiness, the check before Invariant Slice work begins
(`.claude/skills/cbc-slice/references/system-readiness.md`), reads
this block first. A CBC Framing that leaves it out writes it later,
by a CBC Framing Export Revision. Two CBC Runs left it out and wrote it later.

**How Enemy Census Saturation is reached.** The first listing ran on
one Enemy Census Probe Lens, actors × the three negations. It only
finds Enemy Facts shaped like "someone misbehaves". An Enemy Census
Probe deliberately takes up a **different Enemy Census Probe Lens**
and scans the same Enemy Census again. What a new one catches, the
old one missed. There are three, each mechanical:

1. **The assumption hunt.** For each line of the Enemy Census,
   finish *"this line is only true or complete if ___"*. The blank is
   the hidden assumption. Then ask *what if that is false?* Look for
   **silent singulars**: every "the X", could there be two? Look for
   **silent successes**: every action taken for granted, what is the
   other branch?
2. **The timeline stretched.** Look far ahead in time, with three
   questions:
   - *what accumulates?* Anything that only grows.
   - *what expires or is forgotten?* Forgetting collides with late
     arrivals.
   - *what arrives very late?*

   Shortest form: take every noun and ask *"what does this look like
   after a year?"*
3. **The resource lens.** List every *quantity*, set each to **zero /
   many / huge**, and watch what breaks. A literal grid works. Cells
   with nothing in them are evidence, not failure.

**The three Enemy Census Probe Stamps.** Every Enemy Census Probe
result gets one, said out loud:

- **new fact:** the Enemy Census grows;
- **nothing new:** naming which line already covers it, which forces
  the actual check;
- **out of scope:** written out.

A silent Enemy Census Probe is no Enemy Census Probe. The Enemy
Census Probe Stamps are
what make "did we miss something?" answerable.

**The Enemy Census Audit Checklist.** The reviewer checks the agent's
Enemy Census without deriving it all again:

1. Did each line get the assumption question?
2. Was every quantity in the grid?
3. Did anything accumulate without being asked about?
4. Does every Enemy Census Probe result carry an Enemy Census Probe
   Stamp?

**Exit, by Enemy Census Saturation:** run the Enemy Census Probe
Lenses until **two consecutive ones yield zero new Enemy Facts**. It
is a number, not a feeling. **The Enemy Census Probe Log is recorded
in LAYER-1-ENVIRONMENT:** each Enemy Census Probe's Enemy Census Probe Lens, its Enemy Census Probe Stamps,
and what it found, or "nothing new". So a later reader can check the
Enemy Census Saturation claim, not just read it. An Enemy Fact out of scope gets a
written refusal or deferral line, never silence.

**What the exit leaves behind, three lists, written:**

- **The Scope Exclusions.** Every exclusion as a numbered line:
  NOT-OURS-1, NOT-OURS-2, and so on. A Scope Exclusion is a working
  boundary, not a disclaimer. It is worth writing because it
  *visibly stops Enemy Facts* at Stage 3, where an excluded Enemy
  Fact collides with nothing.
- **The Enemy Census Gaps.** What was *not* examined, named:
  clock skew, deployment transitions, and the like. So a later reader
  knows where the Enemy Census ends, not just what it holds. An Enemy
  Census Gap is raised at the Agent Skill Stage's close, never
  silently carried.
- **The Scope Verdicts.** Each boundary question the Enemy Census
  found is put as a named verdict, with a recommendation and its
  reason. The three values:
  - *in*: more of the same named kind, a richer demonstration;
  - *out*: a new kind of difficulty, the subject of another
    Falsifiable Promise;
  - *censused-and-excluded*: the Enemy Facts stay, and the boundary
    holds.

  Who decides each is the mode's rule
  (`.claude/skills/cbc-framing/SKILL.md`, *The mode — non-negotiable*).

**Hands down:** the list of Enemy Facts and the three lists.
**Hands up (conditional, logged):** a missed System Possession or
unwritten System Refusal becomes a CBC Framing Export Revision of LAYER-2-SYSTEM.

## Stage 3 — Run the Enemy Collisions (LAYER-4-PROBLEMS)

*Question: for each Enemy Fact × each System Possession, what
distinct Enemy Collision Kill?*

Collide one System Possession at a time against every Enemy Fact
that can reach it. State each Enemy Collision Kill as **what dies,
never how it is saved.** A mechanism is set aside the moment it comes
up.

Split two Enemy Collision Kills into two CBC Framing Concerns only
when their *proof obligations* differ. Merge duplicates by what an
Enemy Fact does to us, not whose fault it is. Gaps in the wording of
LAYER-2-SYSTEM's own System Possessions, CBC Framing Concerns with no
enemy, are marked as Invariant Slice Fold Candidates, not Invariant
Slices. A System Possession can have no Enemy Collision Kill of its own:
each Enemy Fact that reaches it may already be counted in another's. That is normal.

**Exit:** a full pass across all Enemy Facts × System Possessions
yields nothing new.
**Hands down:** Enemy Collision Kills stated as invariants, adversity
named. The cbc-slice Agent Skill's Stage 1, specify-correctness, takes
them with no translation.

## Stage 4 — Sort into owners (LAYER-3-AREAS)

*Question: do the Enemy Collisions force distinct owners, or does one
Responsibility Area own everything?*

For each CBC Framing Concern, name the state and decisions it
touches. A division is real only if it would hold **separate state
AND separate decision authority**. The count of CBC Framing Concerns
is not the count of Responsibility Areas. Where a plausible
Responsibility Area Seam fails the test, name it and refuse to draw
it. A Responsibility Area Seam named and not drawn is a better record than silence.

**Exit:** ownership stated, even if the statement is "one
Responsibility Area". A thin or empty LAYER-3-AREAS, reached by
sorting real Enemy Collision Kills, is a *confirmed* answer, not a
gap. **Hands down:** the owners, or the one owner.

## Stage 5 — Check between owners (LAYER-5-INTERACTION)

*Question: did Stage 4 create Responsibility Area Seams?*

If not: record **empty, with its reasons**. Each emptiness follows
from an earlier decision, such as one Responsibility Area, or
sibling systems refused at LAYER-2-SYSTEM. It is never a blank.

If so: name what must hold across the Responsibility Area Seams that
no single Responsibility Area's System Guarantee covers. Examples:
ordering across a boundary, failure that must be coordinated,
consistency across the Responsibility Area Seams. LAYER-5-INTERACTION takes
LAYER-3-AREAS's boundaries and LAYER-4-PROBLEMS's local System Guarantees
as given. It never redefines them.

**Exit:** LAYER-5-INTERACTION empty with its reasons, or its
constraints across Responsibility Areas stated.

## Stage 6 — Cut the Invariant Slice Registry

*Question: which CBC Framing Concerns are theorems, which are
contracts?*

An Invariant Slice is one invariant × one adversity that needs
its own proof. The Agent Skill Stage runs as **three passes**, each
with its test and its record:

1. **The sort.** Every CBC Framing Concern gets one of two labels,
   with a written *because* for each:
   - **theorem:** it carries an invariant under adversity of its
     own. Proof means *creating* that adversity and the State
     Witness showing the invariant survive;
   - **contract:** it is declared and checked, with no adversity to
     create against it.

   The *because* means a CBC Framing Concern that almost got the
   other label has its doubt answered in the record. When Stage 3's
   discipline held, Enemy Collision Kills arrive already shaped as
   theorems, and this pass confirms them. That is the discipline
   working, not the pass skipped.
2. **The dedupe.** Pairwise on the theorems, the Invariant Slice
   Split Test: two Enemy Collision Kills are two Invariant Slices
   only when their evidence must *create different adversity*. A
   proof that sequential replay creates is not the proof contention
   demands. The same adversity to create means one Invariant Slice,
   merged visibly. Different adversity means both stand. Splits set
   aside earlier as visible choices are settled here.
3. **The folds.** Each contract becomes an Invariant Slice Fold in
   the first Invariant Slice that consumes it, its check going with
   it. The Invariant Slice Registry is written, carrying the CBC
   Framing Reconciliation: every CBC Framing Concern accounted for as
   Invariant Slices and Invariant Slice Folds, so nothing is silently
   dropped.

The order is an *expectation*, not a commitment. Derive a presumption
order, by what each proof takes as already standing. Decide the
actual next Invariant Slice again at each Invariant Slice Close.
Stage 6's deliverable is the cut, not a sequence.

**Exit:** the Invariant Slice Registry stands, its first Invariant
Slice `chosen-next`.
**Hands off to:** the Runtime Ground and the skeleton, then
`.claude/skills/cbc-slice/references/cbc-slice-workflow.md`, one
Invariant Slice at a time.

---

## What this workflow refuses to contain

Implementation, technology, repo structure, environment setup and
work tracking all live downstream. Naming a mechanism here is the
same mistake as naming one in a Correctness Specification. And
coming up with the idea lives upstream: this workflow sharpens a
standing idea, and does not invent one.

## Open (to be settled by CBC Runs)

- Stage 0 from a raw idea: all six CBC Framings so far started from
  an idea already shaped, CBC Runs 3 to 6 each from a CBC Run
  Briefing.
- How the Falsifiable Promise generalizes for systems that compute or
  relay rather than own facts, such as a renderer or a proxy.
- The case with several owners, end to end. The two CBC Framings made
  before the first CBC Run and CBC Run 3's found one Responsibility Area each. CBC
  Run 5's found two, CBC Run 6's three, each with a filled
  LAYER-5-INTERACTION, and both CBC Runs went on through their
  Invariant Slices. CBC Run 4's is not yet read. What the case
  teaches is for each CBC Run's CBC Run Reading.
