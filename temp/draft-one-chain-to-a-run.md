# Draft — one chain to a run: this repo integrates the kit

Thinking, not a decision. Staged here to be argued with before it
becomes an ADR here and a hand-off up. It binds nothing.

Raised 2026-09-17 by the user, at the close of the set that wrote
`starter/installs/bundle-update.md` — writing that manual is what
made the problem visible, because it is only half a manual: it
delivers our half to a run and is silent about the other half the
run also holds.

---

## The problem

A run has two parents. never-oversold holds `kit @ 9e28143` from
the handbook and `bundle @ 7bbf49a` from here, in one decisions
log, updated by two procedures on two schedules. Nobody owns the
pair. When the handbook's kit restructured at `ba7eaa4`, the break
had to be absorbed here *and* will have to be absorbed again in
every run, separately, because each run took the kit itself.

And our independence from the handbook is already a fiction.
`pure-seed.md` step 2 defers to their `installs/pure.md` **by
pointer**: change it and our birth procedure changes silently, with
no pin between us. We have half-noticed this before — our fills
carry the kit's entry-file text verbatim at the pin and re-verify
it at every re-pin, which the contract already calls "a harvest
duty here, not a surface the kit must hold still". That is
vendoring, done once, informally, for one file.

So the handbook cannot be the general-purpose kit it wants to be
while our install depends on the exact shape of its install.

## The proposal

One chain. The handbook sends to us; we integrate; we send to runs.

    handbook  →  this repo  →  run

- This repo **vendors the kit** at a pin, the way it already
  vendors the two models (CBC ADR-0002).
- What a run receives is **one composed delivery** with **one pin**:
  the kit as we adapted it, plus the bundle on top, tested together
  before a run sees it.
- A kit change reaches a run only after it has landed here. The
  handbook writes us a note; we evaluate, adapt our composition,
  and pass on what survives.
- A run's lesson reaches the handbook only through here. We read
  the run; if the lesson is method rather than ours, we hand it up
  with our own reading attached.

## Why it is probably right

**The handbook has already written this role down.** Its TODO,
since their ADR-0041:

> every maintainer repo is both sides — the handbook receives its
> own kit and sends to CbC, CbC receives and sends to its runs.
> Only a run is receiver-only.

That is this proposal, in their words. The kit half is the part
that was never made true.

**It matches the tiers model's own shape.** Delivery comes down one
step at a time and learning goes up one step at a time. A run with
two upstreams is the anomaly, not the fix.

**It gives the handbook back its independence.** Today it ships a
kit that must behave in the particular way our seed assumes.
Vendored, it ships a kit for anyone, and adapting it is our job.

**It halves a run's bookkeeping.** One pin, one procedure, one
note. `bundle-update.md` becomes a whole manual instead of half of
one.

## The kit is not neutral, and here is the evidence

Raised by the user 2026-09-17: the kit cannot be the same thing for
everyone, because a handbook, this repo and a run are different
kinds of repo. Checked, and the strongest instance is the kit's
`ARCHITECTURE.md` stub:

```
## Invariants
<!-- What must NEVER happen to the data / system, and where each rule
     is enforced (DB constraint, module boundary, ...). -->
- <invariant> — enforced in <where>.

## Codemap
| `src/...` | |
```

Two leaks in one stub. "What must NEVER happen", "invariant",
"where enforced" is this concept's own vocabulary sitting in a
generic kit — a kit that says "list your invariants" has already
decided the project does correctness-by-construction. And
`src/...`, `DB constraint` assume an application repo, which
neither the handbook nor this repo is.

We are carrying it: our own `ARCHITECTURE.md` has an `## Invariants`
section with that comment verbatim, because the kit handed us the
slot.

**The sweep, so the size is not guessed.** Every file in the kit at
`ba7eaa4`, against this concept's vocabulary and app-shape markers:

| file | hits |
|---|---|
| `ARCHITECTURE.md` | 4 — the Invariants section and `src/...` |
| `.claude/skills/commit-messages/SKILL.md` | 1 — an example commit body about a unique index |
| everything else | 0 |

The four conventions are clean apart from that one example line.
So the flavour is one section of one stub, not rot through the kit.
That matters for what follows.

**What the sweep does not test** is shape rather than words. Our
CHANGELOG stub "had to be replaced, not filled — app-repo
assumptions" (2026-08-28), and a grep for vocabulary would not have
caught it. A real pass asks of each kit artifact: does this assume
what kind of thing is being built? That is a report the handbook
can act on without conceding anything about who owns method — a
defect list, not a preference.

## Two derivations, not one

If the kit is purified upstream, one update becomes two here:

    handbook's pure kit
          │
          ├──→ the kit for this repo's agent  (a maintainer repo:
          │    documents, no src/, no invariants section)
          └──→ the kit inside the bundle      (a CbC project: the
               invariants slot, the walls, the slice records)

Different targets, different adaptations, one source. When the pure
kit moves, the note from the handbook is evaluated twice, once per
derivation, and both are re-derived.

**Half of this exists already and is not named as such.** Our
`.claude/skills/` is the first derivation — four convention copies
adapted to us by being held, registered and pinned. Our
`starter/fills/` is the second — the playbook's steps into PLAN,
the CLAUDE.md fill, the README fill, all shaped for a run. They are
the same kind of thing and have never been called that. Naming them
is most of the design.

## Rebuild the handbook, or fix it?

Asked by the user: would a new pure repo, with the current one
archived and used as reference, be simpler than updating what
exists?

**Recommend against, on the evidence above.** Four lines in one
stub plus one example is a defect, not rot, and a rebuild is the
largest available tool.

Four reasons, in order of weight:

1. **It is not ours to decide.** The handbook is another repo with
   its own ADRs and its own owner. We can report a defect; we
   cannot retire their repository.
2. **A new repo discards the record we just decided to rely on.**
   This repo's own ADR-0022 concluded, days ago, that git history
   is where a change's account lives — that is why the harvest
   notes could leave the bundle. Starting fresh throws away forty
   ADRs of accumulated why, or copies them across, which is the
   update again at higher cost.
3. **Every pin downstream stops resolving.** Our registry names
   handbook hashes in roughly ten entries; run 3 holds kit pins on
   receipt branches. This whole session turned on `git show
   ab916a1:...` still resolving. A new repo makes all of that
   dead reference.
4. **It does not solve the thing it is aimed at.** The purification
   still has to be decided artifact by artifact. A new repo starts
   with the same questions and no history of how the old answers
   were reached.

**The case where it would be right** is a structural one — if the
kit's shape, not its words, assumed an application repo throughout.
The sweep does not show that, and the handbook itself now consumes
its own kit (their ADR-0041), which is the strongest ongoing
pressure toward neutrality there could be.

**The lighter path that gets the same result**: a defect report
listing what each kit artifact assumes, ours to write and theirs to
act on; the CbC-flavoured slots move here into the bundle's
derivation, where they shape a run's records and nothing else. No
repo is retired and no pin dies.

## What it costs — the honest list

- **We own the kit's correctness in runs.** The handbook fixes
  something; runs wait for us to pass it on. Today they could take
  it directly.
- **A vendored copy drifts.** We would need, at repo scale, the
  same discipline we just wrote for a skill copy: pinned, adapted
  only for stated reasons, the adaptations logged and re-applied or
  dropped at each re-pin.
- **Our adaptation layer is new work with no precedent here.** "The
  kit at hash X, adapted by us in ways Y" needs a home and a
  format. That is the piece we have not designed.
- **Run 3 has two pins today.** Migrating it is real work and a
  one-off procedure.
- **Several decisions get superseded**, not amended: the overlay
  design runs through CBC ADR-0009, 0015, 0016, 0017 and 0019.

## The back door, and why not

The idea as raised kept "special cases when we need direct contact
to the handbook from a run". Recommend against. A back door that
exists is used, and then there are two chains again *plus* a rule
about which applies — worse than two chains. If a run needs the
handbook, it comes through here, slower and traceable.

## What is not settled

- **How much of the kit do we actually adapt?** If the answer is
  "almost none", a lighter version of this proposal does most of
  the work: vendor the *install procedure* only, so `pure-seed.md`
  stops pointing at their `pure.md`, and leave kit updates flowing
  directly. That removes the silent coupling without taking on the
  kit's correctness. Worth costing before the full version.
- **Where the adaptation layer lives**, and whether it is diffs, a
  fork, or a composed output committed here.
- **What the handbook loses.** They may want direct reach to a run
  for their own evidence; their conventions bind a run's
  arrangement, and they have never read one through an intermediary.
- **Whether one pin is honestly one thing.** A composed delivery
  named by our hash hides which kit hash is inside it. Our registry
  would have to name both, which is two pins wearing one coat —
  acceptable if we say so, dishonest if we do not.

## Order of work, if it goes ahead

1. **Decide here first.** We have the problem, the evidence and the
   friction; the handbook has neither. Asking them to move for an
   unvalidated design is backwards.
2. **Hand it up**, paired with the exchange hand-off already in
   `temp/` — that one says we now have a sending side; this one
   says we would like to be the only sender to runs.
3. **Migrate run 3** at its next re-pin, once both have agreed.

Not before the lighter version above has been costed and rejected
on its merits.
