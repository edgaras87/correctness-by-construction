# Glossary: the concept's and the method's Names

<!-- The Names the concept, docs/concept/, and the method's Agent
     Skills and Output Shapes are written in, each from this
     project's side: one plain sentence, with its owner where it has
     one. A pinned copy, like every delivered file: changed only as
     .claude/rules/delivered-copies.md says. This project's own Names
     are docs/glossary.md's.
     foundation: the writing convention -->

## The concept's

- **CBC Inversion** — asking what must never happen before asking
  what a system should do; the System Guarantees come first, the
  structure from them, the features last (`docs/concept/00-cbc.md`).
- **System Never-Event** — a thing that must never happen: money
  counted twice, an order created twice (`docs/concept/00-cbc.md`).
- **System Guarantee** — a System Never-Event stated against a named
  source of adversity; the system holds it by structure
  (`docs/concept/00-cbc.md`).
- **System Guarantee Erosion** — the first way the concept fails: new
  features ship without the System Guarantees they might break being
  checked again (`docs/concept/00-cbc.md`).
- **Escape Hatch** — the second way the concept fails: an admin path or a raw script goes
  around the one enforced code path, and a System Guarantee stops
  being true (`docs/concept/00-cbc.md`).
- **Testing Theater** — the third way the concept fails: System Guarantees move out of
  structure and back into tests, which sample where structure forbids
  (`docs/concept/00-cbc.md`).
- **Theory Swamp** — the fourth way the concept fails: deep rigor tried before the layers
  have made the problem small (`docs/concept/00-cbc.md`).
- **Layered System** — the concept's model of the world: five nested
  layers, from the environment the system lives in to what emerges
  between its Responsibility Areas (`docs/concept/01-layered-system.md`).
- **System Layer** — one of the five layers of the Layered System,
  LAYER-1-ENVIRONMENT to LAYER-5-INTERACTION
  (`docs/concept/01-layered-system.md`).
- **Falsifiable Promise** — one commitment about the facts the system
  is the authority on, made to a named audience, whose breaking can be
  pictured concretely (`docs/concept/01-layered-system.md`).
- **Responsibility Area** — one of the system's internal divisions by
  ownership, LAYER-3-AREAS; made only when the Enemy Collisions
  force it
  (`docs/concept/01-layered-system.md`, `docs/concept/03-cbc-framing.md`).
- **System Guarantee Inventory** — the few System Never-Events whose
  breaking is costly or cannot be undone, each against a named
  adversity (`docs/concept/02-guarantees-and-walls.md`).
- **Structural Wall** — what makes one System Guarantee impossible to
  break; each gets the strongest one available, ranked by who it
  binds, from the store's refusal down to hope
  (`docs/concept/02-guarantees-and-walls.md`).
- **CBC Framing** — the first part of the work: an idea turned
  into a defined system on paper, before any code or technology
  choice (`docs/concept/03-cbc-framing.md`).
- **CBC Framing Export** — one of the three documents CBC Framing
  produces: the CBC Framing Intent, the System Definition and the
  Invariant Slice Registry (`docs/concept/03-cbc-framing.md`).
- **CBC Framing Intent** — the first CBC Framing Export: the
  Falsifiable Promise and the purposes refused
  (`docs/concept/03-cbc-framing.md`).
- **System Definition** — the second CBC Framing Export: the system's authority,
  boundary, adversary and owners (`docs/concept/03-cbc-framing.md`).
- **Invariant Slice Registry** — the third CBC Framing Export: the work cut into
  Invariant Slices, in an order that evidence may change
  (`docs/concept/03-cbc-framing.md`).
- **Enemy Fact** — one attackable fact about something outside the
  system's control: it can vanish, duplicate or lie
  (`docs/concept/03-cbc-framing.md`).
- **Enemy Census** — the list of Enemy Facts, done when fresh attacks
  on it stop finding anything new (`docs/concept/03-cbc-framing.md`).
- **System Possession** — a fact or responsibility the system must
  own, since someone else owning it could break the Falsifiable
  Promise
  (`docs/concept/03-cbc-framing.md`).
- **Enemy Collision** — one Enemy Fact set against one System
  Possession, to see what dies (`docs/concept/03-cbc-framing.md`).
- **Enemy Collision Kill** — what dies in an Enemy Collision, named
  without its cure: "a retry lands twice and the order exists twice"
  (`docs/concept/03-cbc-framing.md`). Its form is the Enemy Collision
  Kill Shape's (`.claude/shapes/kill.md`). An Enemy Collision tried
  where nothing dies is no Kill, and is tagged HOLDS-n.
- **Invariant Slice** — the second part of the work and its unit:
  one System Never-Event from the System Guarantee Inventory made
  real end to end, closed when it survives its attack
  (`docs/concept/04-cbc-slice.md`).

## The method's

- **Demonstration Mode** — CBC Framing with its reasoning fully shown,
  to teach the moves; every verdict stays the reviewer's
  (`.claude/skills/cbc-framing/SKILL.md`).
- **Delegated-Verdict Mode** — CBC Framing with the reviewer's verdicts
  handed to the agent, by a decision recorded in the CBC Run's
  Decisions Log (`.claude/skills/cbc-framing/SKILL.md`).
- **Falsifiable Promise Audience** — who the Falsifiable Promise is
  made to; never someone who only uses the running system
  (`.claude/skills/cbc-framing/SKILL.md`).
- **System Possession Test** — the question each candidate System
  Possession must pass: if someone else owned this, could they break
  the Falsifiable Promise? (`.claude/skills/cbc-framing/SKILL.md`).
- **System Refusal** — a fact or responsibility the system
  deliberately does not own, written down as a decision
  (`.claude/skills/cbc-framing/SKILL.md`).
- **System Refusal Test** — the question a candidate System Refusal
  must pass: can the Falsifiable Promise stay true if this goes wrong
  elsewhere? (`.claude/skills/cbc-framing/SKILL.md`).
- **Enemy Sketch** — a rough enemy that the cbc-framing Agent Skill's Stage 1 works with,
  replaced by Enemy Facts at Stage 2
  (`.claude/skills/cbc-framing/SKILL.md`).
- **Enemy Census Probe** — one fresh scan of the Enemy Census through
  an Enemy Census Probe Lens
  (`.claude/skills/cbc-framing/references/cbc-framing-workflow.md`).
- **Enemy Census Probe Lens** — the angle an Enemy Census Probe scans
  by; the workflow names three, each worked by fixed moves
  (`.claude/skills/cbc-framing/references/cbc-framing-workflow.md`).
- **Enemy Census Probe Stamp** — one of three marks on every Enemy
  Census Probe result: a new fact, nothing new, or out of scope; every
  result gets one
  (`.claude/skills/cbc-framing/references/cbc-framing-workflow.md`).
- **Enemy Census Probe Log** — each Enemy Census Probe's Enemy Census Probe Lens, Enemy Census Probe Stamps
  and findings, written into LAYER-1-ENVIRONMENT
  (`.claude/skills/cbc-framing/references/cbc-framing-workflow.md`).
- **Enemy Census Saturation** — the Enemy Census's end: two Enemy
  Census Probes in a row find no new Enemy Fact
  (`.claude/skills/cbc-framing/references/cbc-framing-workflow.md`).
- **Enemy Census Audit Checklist** — the reviewer's four questions for
  checking the agent's Enemy Census
  (`.claude/skills/cbc-framing/references/cbc-framing-workflow.md`).
- **Enemy Census Gap** — a place the Enemy Census did not examine,
  named so it is not taken as examined
  (`.claude/skills/cbc-framing/references/cbc-framing-workflow.md`).
- **Trust Assumption** — something deliberately accepted as true and
  not defended against, written beside the Enemy Facts; ASSUMPTION-n
  (`.claude/skills/cbc-framing/references/cbc-framing-workflow.md`).
- **Scope Exclusion** — a written decision that some facts are outside
  the system, so they visibly stop at the cbc-framing Agent Skill's Stage 3;
  NOT-OURS-n
  (`.claude/skills/cbc-framing/references/cbc-framing-workflow.md`).
- **Scope Verdict** — a boundary question answered by a named verdict:
  in, out, or censused and excluded; SYSTEM-BOUNDARY-n
  (`.claude/skills/cbc-framing/references/cbc-framing-workflow.md`).
- **Runtime Ground** — where the system runs: the machine, the
  instances, the store, the clock, the size; the System Definition
  names it, and the work after CBC Framing sets it up
  (`.claude/skills/cbc-framing/references/cbc-framing-workflow.md`).
- **Responsibility Area Seam** — the line between two Responsibility
  Areas, drawn or noted as not drawn
  (`.claude/skills/cbc-framing/references/cbc-framing-workflow.md`).
- **CBC Framing Concern** — one item that the cbc-framing Agent Skill's Stage 6 sorts:
  Enemy Collision Kills that share a proof, or a gap in wording with
  no enemy
  (`.claude/skills/cbc-framing/references/cbc-framing-workflow.md`).
- **Invariant Slice Split Test** — the check that two Enemy Collision
  Kills are two Invariant Slices only if their evidence must create
  different adversity
  (`.claude/skills/cbc-framing/references/cbc-framing-workflow.md`).
- **Invariant Slice Fold** — a CBC Framing Concern with no enemy,
  folded into the first Invariant Slice that uses it, its checks
  carried with it; FOLD-n
  (`.claude/skills/cbc-framing/references/cbc-framing-workflow.md`).
- **Invariant Slice Fold Candidate** — a CBC Framing Concern marked at the cbc-framing Agent Skill's Stage 3 as one that may become an Invariant Slice Fold
  (`.claude/skills/cbc-framing/SKILL.md`).
- **CBC Framing Reconciliation** — the Invariant Slice Registry's line
  that accounts for every Enemy Collision Kill as Invariant Slices,
  Invariant Slice Folds, deferrals or Scope Exclusions, a count of
  zero included
  (`.claude/skills/cbc-framing/SKILL.md`).
- **CBC Framing Derivation** — `docs/system/framing/derivation.md`:
  how each Agent Skill Stage of CBC Framing ran, kept for good
  (`.claude/skills/cbc-framing/SKILL.md`).
- **CBC Framing Derivation Appendix** — a file beside the CBC Framing
  Derivation, only for bulky sweep output
  (`.claude/skills/cbc-framing/SKILL.md`).
- **CBC Framing Export Filter** — the rule that a CBC Framing Export
  never refers to the CBC Framing Derivation's working
  (`.claude/skills/cbc-framing/SKILL.md`).
- **Agent Language** — words that name an Agent Skill, an Agent
  Skill Stage or the CBC Run's arrangement; a CBC Framing Export never holds
  them (`.claude/skills/cbc-framing/SKILL.md`).
- **CBC Framing Export Revision** — a dated change to a CBC Framing
  Export: what changed, why, and what set it off, during CBC Framing
  or after (`.claude/skills/cbc-framing/SKILL.md`).
- **Correctness Specification** — the cbc-slice Agent Skill's Stage 1
  output: the invariant, its Invariant Slice Guarantees, their
  Evidence Criteria and the Adversity Model
  (`.claude/skills/cbc-slice/references/cbc-slice-workflow.md`).
- **Invariant Slice Guarantee** — one property the Invariant Slice's
  invariant needs, found by attacking it, stated without a mechanism;
  GUARANTEE-n (`.claude/skills/cbc-slice/SKILL.md`).
- **Invariant Slice Guarantee Challenge** — the attack on the
  invariant that yields its Invariant Slice Guarantees, kept up until
  no new answer comes (`.claude/skills/cbc-slice/SKILL.md`).
- **Evidence Criterion** — what test would create an Invariant Slice
  Guarantee's adversity and show the invariant surviving, named before
  the test is built; EVIDENCE-n (`.claude/skills/cbc-slice/SKILL.md`).
- **Adversity Model** — the part of the Correctness Specification that
  says what attacks and how the evidence creates it
  (`.claude/skills/cbc-slice/references/cbc-slice-workflow.md`).
- **Adversity Class** — a kind of adversity an Invariant Slice needs
  created: contention, duplicate delivery, partial failure
  (`.claude/skills/cbc-slice/references/system-readiness.md`).
- **Adversity Harness** — the test machinery that can create an
  Adversity Class, and fail when it does
  (`.claude/skills/cbc-slice/references/system-readiness.md`).
- **System Readiness** — the six checks a system passes before an
  Invariant Slice opens
  (`.claude/skills/cbc-slice/references/system-readiness.md`).
- **Structural Wall Backstop** — what stands behind a Structural Wall,
  seen catching at the Red Run or left unproven
  (`.claude/skills/cbc-slice/SKILL.md`).
- **Escape Hatch Hunt** — the search, at the cbc-slice Agent Skill's
  Stage 2, for any path around the Structural Wall
  (`.claude/skills/cbc-slice/SKILL.md`).
- **Evidence Test** — a test that creates the adversity and reads the
  State Witness; written by the Evidence Test Shape
  (`.claude/skills/cbc-slice/SKILL.md`).
- **State Witness** — the state read from outside, where the truth is
  stored, that shows whether the invariant held
  (`.claude/skills/cbc-slice/SKILL.md`).
- **State Witness Reading** — one read of the State Witness
  (`.claude/skills/cbc-slice/SKILL.md`).
- **Red Run** — an Evidence Test run with its Structural Wall absent,
  failing on the State Witness; it never lands in history
  (`.claude/skills/cbc-slice/SKILL.md`).
- **Red Run Tree** — the working tree of a Red Run
  (`.claude/skills/cbc-slice/SKILL.md`).
- **Structural Wall Check** — a test that sends a Structural Wall its
  refusal directly, or reads it where it is defined; not evidence
  (`.claude/skills/cbc-slice/SKILL.md`).
- **Decision Test** — a test that pins a decided option, not the
  Falsifiable Promise, and cannot fail for the invariant; not evidence
  (`.claude/skills/cbc-slice/SKILL.md`).
- **Adversity Flag** — a note that the adversity cannot be created the
  normal way, and what the evidence does instead
  (`.claude/skills/cbc-slice/SKILL.md`).
- **Invariant Slice Close** — the moment an Invariant Slice is closed
  in the Invariant Slice Registry, with its answers
  (`.claude/skills/cbc-slice/SKILL.md`).
- **Standing Guard** — one of three watches named at the Invariant
  Slice Close, one for each of System Guarantee Erosion, Testing
  Theater and the Escape Hatch (`.claude/skills/cbc-slice/SKILL.md`).
- **Invariant Slice Record** — one record per Invariant Slice, written
  as its Agent Skill Stages go, in the form the Invariant Slice
  Record Shape sets
  (`.claude/skills/cbc-slice/references/cbc-slice-workflow.md`).
- **Invariant Slice Guarantee Block** — one Invariant Slice
  Guarantee's section of the Invariant Slice Record
  (`.claude/shapes/slice-record.md`).
- **Invariant Slice Entry** — one Invariant Slice's entry in the
  Invariant Slice Registry; written by the Invariant Slice Entry Shape
  (`.claude/shapes/registry-entry.md`).
- **Evidence Precondition** — a structural condition checked but never
  put under attack, whose silent breaking voids the evidence
  (`.claude/shapes/registry-entry.md`).
- **Enemy Collision Kill Shape** — the Output Shape for an Enemy
  Collision Kill (`.claude/shapes/kill.md`).
- **Evidence Test Shape** — the Output Shape for an Evidence Test
  (`.claude/shapes/evidence-test.md`).
- **Invariant Slice Record Shape** — the Output Shape for an Invariant
  Slice Record (`.claude/shapes/slice-record.md`).
- **Invariant Slice Entry Shape** — the Output Shape for an Invariant
  Slice Entry (`.claude/shapes/registry-entry.md`).
