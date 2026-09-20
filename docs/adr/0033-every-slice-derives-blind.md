# 0033. Every slice derives blind; the reading happens once, at the end

Date: 2026-09-20
Status: Accepted (2026-09-20, at the set's final records commit;
opened Proposed and revised at a boundary before acceptance —
decision 2 had kept the withdrawn protocol's deadline and asked for
a write-up per slice close, which nothing any longer needed)

## Context

ADR-0021 decision 5 set a protocol and it has never run. The Spring
reference is held here, and at each slice close — after the build is
on record, before the fast-forward to main — it is handed to the run
as session input. The run compares its shapes against it section by
section, and per shape keeps its own, adopts the reference's as a
recorded revision, or marks a variation point. Each verdict the
reading here confirms lands in the reference as a harvest line.

Run 3 closed SL-1 on 2026-09-14; the reference was written from that
slice as lived; SL-2's close was to be the protocol's first firing.
Read again before it fires, three things about it:

1. **It generalises from one instance.** The reference is one
   slice's shapes called a baseline. The standing answer everywhere
   else in this repo is that one instance is not a shape — it is
   what we told run 3 about the facility paragraph on 2026-09-17,
   and it is why we are waiting to read SL-2 as the second instance
   that would make it one. ADR-0021 does not apply that rule to
   itself.

2. **The first comparison ends the independence of every later
   one.** A verdict of "the reference's is stronger" is adopted as a
   recorded revision. From that moment the run holds the reference's
   shape, and the slice after it does not derive that shape — it
   inherits it. What the protocol produces is one independent sample
   followed by refinements of a converging baseline, which is not
   what its "second measured category" was meant to measure.

3. **What it schedules is per slice; what it compares is per
   stack.** Each firing weighs one slice against a document claiming
   to be about slices in general, and the document moves after every
   firing.

## Decision

1. **Nothing is handed mid-run.** ADR-0021's moment — the slice
   close, before the fast-forward — is withdrawn. A run derives
   every slice with no reference in hand, not only its first.

2. **Nothing is written up per slice.** One line here when a slice
   closes — which slice, when, and what caught the eye — and no
   more. Writing SL-1 up at its close was urgent only because the
   write-up had to exist in time to be handed back at SL-2's;
   decision 1 removes that deadline. The source it was written from
   is the run's own `docs/construction/` record, which sits in the
   run's repo and is not going anywhere. Making our copy early does
   the work twice, ahead of a reading that has not happened.

3. **The reading happens once, over the whole set**, at the moment
   decision 4 names. Its material is the run's own slice records
   read read-only, plus `spring-slice-reference.md`, which holds
   SL-1 and is already paid for. Its question is not "is this
   slice's shape stronger than that one's" but what recurs across
   slices each derived without sight of our reading of the others —
   and what a recurrence is evidence of. A shipped reference, if
   there is to be one, is written *from* that reading. Until it
   runs, nothing here is a lived best.

4. **The moment is the run's Release step opening** — the first
   point at which "all the slices" is a closed set rather than a
   count that may still grow. Named here because a reading with no
   trigger never fires.

5. **The blindness is partial, and the limit is named rather than
   wished away.** Slices inside one run are not blind to each other:
   run 3's `docs/construction/sl-1-no-over-admission.md` is in run
   3's own repo, SL-2's agent reads it, and should — the tier rule
   says a run reads its own records. What is withheld is our
   *write-up* and our generalisation of it, not the slice. So the
   set is independent of this repo's reading, not of itself, and
   what recurs across it is evidence about how a slice is **shaped**
   — not evidence that two slices invented the same mechanism
   twice. Independence of the second kind needs a second run, not a
   second slice.

6. **ADR-0021 keeps everything else.** The reference is held here
   and not in the bundle; it is blind to newborns; `cbc-slice` stays
   stack-free and names nothing. Only decision 5's protocol changes,
   and ADR-0021's status line says so.

7. **`spring-slice-reference.md` stays where it is and does not
   grow.** It holds SL-1 and will hold SL-1 only. It is material in
   a drawer until decision 3's reading — not a document kept
   current, not a baseline, not something a later slice is measured
   against — and its header says that instead of the protocol it
   was opened with. Deleting it was considered and rejected: six
   shapes that cost a run real time, one of them through a dead
   end, and the next Spring project would re-invent or re-derive
   every one.

## Consequences

Good: the set the generalisation is drawn from has more than one
member in it, which is the rule this repo applies to everything
else. What the reading weighs is what a run derived without sight
of our reading, rather than refinements of a baseline it had
already adopted. And it is nearly free until it fires — a line at
each slice close, and one reading — where ADR-0021 spent a
write-up and a reviewer session per slice.

Bad: **a weaker design is now found after it has shipped.**
ADR-0021's timing was chosen exactly so a build the comparison found
weaker could be redone on a fresh branch from the same main, instead
of refined on top of a merge; that is given up, and a weak shape in
SL-2 stays in SL-2. This is the whole of what the change costs and
it is a real cost, paid in the run's code to buy cleaner evidence.

Also: there is nothing to hand a different Spring run that starts
before run 3 reaches Release. Under ADR-0021 the reference was a
lived best from SL-1's close; it is now material until the reading.
If a second Spring run is born in the meantime, this decision is
what stands between it and the only Spring slice write-up we have,
and that is the trade being made knowingly.

Also: the reading at Release is one large piece of work at a run's
busiest gate, and decision 2 makes it larger — it reads the run's
records cold rather than write-ups made while the work was close.
Foreseen, not discovered, and the price of not paying per slice.

Also, and it limits what the reading can conclude: every slice in
the set comes from one run. What recurs may recur because it is the
same project and the same agent, not because it is the right shape.
Decision 5 says the set is independent of our reading and not of
itself; this says the rest of it — a shipped reference wants a
second Spring run, and the reading at Release can only say what is
worth carrying to one.
