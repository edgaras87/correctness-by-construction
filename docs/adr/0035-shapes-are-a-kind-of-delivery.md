# 0035. What a shape is belongs to the container; each rides its group

Date: 2026-09-23
Status: Accepted (2026-09-23, at the set's final records commit;
opened Proposed and revised at a boundary before acceptance —
decision 4 promised a shipped `.claude/shapes/` stub, and the stub
was written, staged and dropped as duplication); **amended
2026-09-24 by ADR-0047** — decision 2's vocabulary entry is gone with
`artifact-kinds`, which was discarded whole. What a shape is now
lives only in the rule, which is where decision 3 had already put
how it lives. Nothing else changed that day.
Changed in part by ADR-0037 (2026-09-27): decision 9's model becomes a
manual.

## Context

never-oversold asked this repo to become **the collector**: to hold
unexposed shapes from every project in one place, to stage them into
a run's `temp/` with a note when that run reaches a gate — a note
saying we hold none being a real delivery that closes its item — and
afterwards to read the run's kept version against what was sent.

A **shape** says what a kind of a project's output looks like: its
form, never its content. It is **exposed** when it sits where the
writer loads it, **unexposed** when it sits where nothing loads it
and is opened at a gate. The directory is the mechanism, and that is
the part worth having.

Weighed as a role, the ask invites a yes-or-no. Read against our own
tree, it is not new. `docs/baselines/` has held artifacts on exactly
this mechanism since 2026-09-06, in our own words:

> Blind… never shown to a newborn — a future derivation that has
> seen this one measures imitation, not the concept's legibility.
> — `cbc-derived-claude-walk1.md`

> the paid-for warnings handed to the run only after each derivation
> is recorded, never as silent playbook text.
> — `cbc-run-pure-playbook-v2.md`

The second is a delivery at a gate, after the work, written a
fortnight before the ask arrived. What is missing is not a role. It
is a name and a rule for something this repo has been doing unnamed,
decided case by case in each artifact's own header.

Two things surfaced while placing it, and both changed the answer.

**The drawer holds two kinds whose blindness runs opposite ways.** A
shape is blind until a gate, after which being in front of the next
writer is the whole point. Trial evidence is blind for as long as
the trial runs, because a derivation that has seen it measures
imitation. One is withheld in order to be delivered; the other is
withheld in order to stay undelivered. Under one word and one rule,
the second gets shipped eventually by someone correctly applying the
first's rule.

**A shape is not a CbC idea.** Nothing in it is about slices,
invariants or evidence. Every project has kinds of output and a
house form for them. That places the vocabulary and the rule in the
container, which
is what any repo is born into and which this repo intends to hand
back to the handbook — while the shapes we actually hold are about
CbC outputs and are not the container's business at all.

## Options considered

1. **Take the role as asked.** Rejected: it writes a protocol for
   many projects from one project's experience, which is the fault
   that withdrew ADR-0021 three days ago; and it names as new a
   mechanism we already run, leaving the existing practice unruled
   beside a new rule for the same thing.
2. **Hold it with a trigger and decline for now.** The standing
   recommendation until the tree was read. Rejected on that reading:
   declining to *start* something we have done since 2026-09-06
   leaves the real defect untouched, and nothing would ever fire the
   trigger, because a second project is not what is missing.
3. **A fourth kind of delivery at `delivery/shapes/`.** The first
   draft of this ADR. Rejected once the general/particular split was
   named: it puts the universal part and the CbC part in one place,
   so handing the container to the handbook would need CbC filtered
   out of it, and a shape of a Spring artifact would travel to runs
   that get no Spring group.
4. **What a shape is in the container, each shape in the group of
   the thing it shapes.** Chosen.

## Decision

1. **What a shape is, and how it lives, belongs to the container.**
   Universal, with nothing of this concept in it, so the container
   can go to the handbook with no filtering. Three parts, and none
   of them is a model: a **vocabulary entry**, `artifact-kinds`'
   **shape** word; a **rule**, `shapes-lifecycle`, which binds; and
   **stubs** for the two directories a project is born with. The
   container ships no models and this decision adds none — a model
   demands nothing, and what has to reach every project is a rule.

2. **Each shape rides the group of the thing it shapes.** This is
   ADR-0029 applied, not a new rule — a skill belongs to exactly one
   group and travels whole, and a shape belongs to whichever group
   owns the output it describes. A slice record's shape is
   `method`, beside `cbc-slice`. A Spring harness file's is
   `spring-postgres`. A devlog entry's or a commit plan's is
   `container`. A run on another stack then gets the slice-record
   shape and never a Spring one, and that falls out rather than
   being enforced.

3. **An exposed shape ships as a pinned copy** into the run's
   `.claude/rules/`, carrying its own `paths:`, re-copied at a new
   pin and never edited in place except under `convention-lifecycle`
   §3. It takes a row in the pinned-copies table like any other
   delivered path.

4. **The container ships no shapes directory, and a project makes
   one when it writes its first shape.** *Revised at this step's own
   boundary.* The rule and `agent-arrangement` §3 both say what the
   directory is for, so a stub in it was a third statement of one
   fact, and most of what remained was making an empty directory
   trackable. What must never happen still holds and is the reason
   nothing is shipped into it: an unexposed shape in a birth copy
   spends the only independence there is, since the first output of
   a kind is the only one nothing here has influenced.

   **The gap this leaves is named rather than hidden.** The rule
   loads only when a file under `.claude/shapes/` is read, so a
   project holding it with no shape never meets it. Two other homes
   were weighed and rejected — a stub in the directory, and a clause
   in `artifact-kinds`, which has no moment and waits to be stumbled
   on. The answer is a default gate item at a step's close, which is
   run 3's step form and is not in this set. **This set ships a rule
   a project can hold and not find**, and that is the cost of
   dropping the stub rather than an oversight.

5. **Unexposed stock is held apart from the groups, and each piece
   names the group it belongs to.** It is not part of any birth copy,
   so it cannot sit inside a group without breaking "copied whole";
   and the group tag is what decides who may be staged it. **This
   repo holds no unexposed shape today**, so no directory is created
   by this decision — the rule is stated and the place is made when
   there is a first occupant.

6. **Trial evidence stays in `docs/baselines/` and never ships.**
   Its blindness is the measurement, not a stage before delivery.
   Sorting that drawer is its own change set; this one only says
   which kind stays in it.

7. **ADR-0033's "nothing is handed mid-run" is narrowed to trial
   evidence, and the narrowing is stated rather than assumed.** That
   decision withdrew a protocol handing a reference at every slice
   close for a shape-by-shape comparison, because the first
   comparison ends the independence of every later one. That holds
   for what it was written about: a document claiming to be about
   slices in general, moving after every firing, weighed against one
   slice at a time. It does not reach a shape delivered once at a
   named gate, after the output it is read against already exists.
   `spring-slice-reference.md` stays what decision 7 of that ADR
   makes it — material in a drawer until the Release reading, handed
   to nobody. **If this narrowing turns out to be ADR-0021 returning
   under another name, this decision is where that is visible, and
   it should be withdrawn.**

8. **No new procedure is written.** Knowing which gate a run stands
   at means reading the run, which is the inbound harvest whose
   manual does not yet exist. Staging shapes is a step of that
   manual when it is written, not a third procedure beside two.

9. **A model is written here, for us, and does not ship.** The rule
   says what a project must do; it does not say how shapes relate to
   outputs, gates, groups and the conventions beside them, and that
   is what makes the rule recallable a month from now. It goes to
   `docs/models/`, which is this repo's and is delivered to nobody
   (ADR-0026). It describes and demands nothing, so it cannot
   contradict the rule — and if the two ever disagree, the rule is
   what binds and the model is what is wrong.

10. **"Collector" is not adopted, and the reply says why.** It names
   a new function where there is an existing one. What goes back to
   never-oversold is what we do, not a role accepted and then half
   declined — together with one finding: its `shapes-lifecycle` §2
   says unexposed shapes are held by "the repository this project
   takes its **method** from". Under this decision that should be
   the repository it takes its **container** from. The two are the
   same repo today and this project's own plan separates them.

## Consequences

Good: a practice running for a fortnight gets a name, a place and a
rule, written from four artifacts that already exist rather than
from one project's proposal. The universal half can leave for the
handbook without carrying anything of this concept. And the
shape-versus-evidence distinction is caught before it costs
anything, which it would have the first time someone applied a
shipping rule to the whole drawer.

Bad: **most of this is machinery for one shape that is not ours
yet.** The only shape in existence is never-oversold's
`slice-record.md`, offered as a finding and not yet evaluated. The
container half is defensible alone — the rule is what any project
needs and two thirds of it is already written — but decisions 3 and
5 describe traffic that has never moved. Decision 5 answers this by
creating nothing; decision 3 does not, and if the slice-record shape
is declined, the pinned-copies row it adds has no occupant.

Also: we adopt another project's vocabulary — shape, exposed,
unexposed — into our own container. It is theirs, it is better than
what we had, which was nothing, and the alternative was inventing a
second word for one mechanism.

Also: this is the second time in four days that a run's argument has
changed a rule here, and the first time one has named something we
were already doing. ADR-0034 was a clause dropped; this is a
practice recognised. Worth naming, because the reading that found it
was looking for something else entirely.
