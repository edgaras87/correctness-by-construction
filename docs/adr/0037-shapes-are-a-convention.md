# 0037. Shapes are a convention, and the model is its manual

Date: 2026-09-27
Status: Proposed (opened under the commit plan for the shapes
convention; flips Accepted in that set's records commit)

## Context

What a shape is, and how one lives, was said in three documents and
none of them was a manual. The rule, `shapes-lifecycle.md`, ships in
the container and binds a run. ADR-0035 records why the rule exists
and where a shape sits between repositories. `docs/models/shapes.md`,
249 lines, says what a shape is and is not and why the exposed and
unexposed split exists — calling itself a model because on 09-23
that was the word the vocabulary offered, and the vocabulary was
discarded the next day. `master.md` §2.3 named the result as its
first erratum: sixteen of the container's seventeen files were the
artifact of one of seven manuals, and the rule was the seventeenth.

On 2026-09-26 the reviewer spent an hour reading the rule to learn
what a shape is, and named three things. The rule is written from
the run's seat: its §4 is what a step's gate does with shapes staged
in `temp/`, and this repo has no steps, no gates, and nothing staged
to it. Our one shape, the reading's, loads by `paths:` while a file
is written — the exposed case of §2 and nothing else — and nothing
says so: the one-file-two-seats asymmetry the exchange had before
ADR-0036. And the manual may already exist, as the model.

The same day the reading's shape was found restating the reading's
lifecycle — revised as items close, deleted when the work does —
which the exchange's manual already says; the reviewer asked what
lifecycle has to do with form, and the sentences were removed rather
than added to. Run 3's `slice-record.md`, the only other shape in
existence, opens with a section on how it is used that restates the
same rule from its side. Two firings of one lesson: a shape says
what an output looks like while it exists, and when the output opens
and closes is the owning convention's. A shape that restates it is a
copy, and a copy that repeats is what drifts.

## Options considered

1. **Keep the three documents as they are.** Rejected: the erratum
   stands, the seat asymmetry stays unstated, and the next reader
   pays the hour again. A description that is not a manual is not
   found by anyone looking for the why behind a rule.

2. **Write a manual and keep the model beside it.** Rejected: two
   descriptions of one thing, and the last two sets closed exactly
   that drift — a copy thirteen lines behind its master, a rule
   saying one pin where its prose said two. The model's own header
   says what a manual says: it describes and demands nothing, and
   the rule binds.

3. **Rewrite the rule for both seats.** Rejected on the exchange's
   finding: the two arrangements hold different things because they
   do different jobs (`master.md` §4.3). A rule with a section for a
   seat that has no gate would ship a run text about a repo it
   cannot see.

4. **A convention, `shapes`: the model reshaped into its manual, the
   rule its shipped artifact, our seat stated in the manual.**
   Chosen.

## Decision

1. **Shapes are a convention of the container.** Its manual is
   `docs/conventions/shapes/README.md` and never ships. It is the
   model moved and reshaped, not rewritten: the facts were measured
   against the implementation on 2026-09-23 and hold; what changes
   is posture, ownership, and two additions.

2. **The run's rule stays whole, and is derived.** `shapes-lifecycle.md`
   keeps its definition of a shape, because a run cannot open the
   manual and the rule is its only source. It gains a `foundation`
   line naming the convention, cites this decision, and gains one
   sentence: a shape says its form and nothing of its own lifecycle,
   which is the rule's, and a shape that restates it drifts.

3. **This repo's seat is a section of the manual, not an artifact.**
   Here a shape is exposed only: a rule under `.claude/rules/` with
   its own `paths:`, marked as a shape by the Governs line. There is
   no `.claude/shapes/`, no gate, and nothing staged to this repo;
   the reviewer moves a shape as the rule says. A file saying only
   that would be the stub ADR-0035 decision 4 dropped.

4. **Placement is the manual's.** That a shape rides the group of the
   thing it shapes, and that only an exposed one travels, was stated
   in the model and in `delivery/README.md` both. The manual owns it;
   the README keeps two sentences and a pointer.

5. **One gap is named and not closed.** An unexposed shape staged for
   a gate is not a pinned copy: it becomes the run's own after the
   gate reads it. `delivered-copies.md` loads on `temp/` and says to
   take what is there whole. No unexposed shape exists on either
   side, so nothing fires wrongly today. What closes it — the note
   naming a staged shape as one, and the take excluding it — is
   written from the first staging, not before.

6. **ADR-0035 decision 9 is superseded in part.** The description of
   shapes is a manual, not a model; `docs/models/` holds two. The
   rest of ADR-0035 stands: what a shape is belongs to the container,
   each rides its group, an exposed one ships as a pinned copy,
   unexposed stock is held apart, trial evidence never ships.

## Consequences

Good: every shipped file is the artifact of a manual — the erratum
closes; a reader looking for the why finds it where every other why
is; the seat asymmetry is written down where the exchange's is; and
the lesson that a shape says form reaches the one run that holds a
shape, in the next delivery, as a sentence in a rule it already
follows rather than as a note it must interpret.

Cost: run 3's shape has the section the sentence argues against,
and the next note has to say so — the third time in a week a run is
told to change something it wrote and that worked. And a convention
whose only artifact of ours is an instance, not a copy of the rule,
is a second shape the conventions index has not described; the
exchange was the first.

Held: the gap in decision 5, with its trigger; whether the manual's
two pictures earn their place, a `visual-comparison` question no one
has asked.
