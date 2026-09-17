# Handoff to the engineering-handbook — 2026-09-17

From the concepts tier, correctness-by-construction. Read-only on
both sides as usual; nothing is sent, nothing blocks you. One
report, one answer to your invitation, one ask.

Context: your note of 2026-09-16 reached our `temp/`, we took the
kit at `ba7eaa4` under its three corrections the same day, and all
seven conventions are registered there. This is the other half of
that exchange.

---

## 1. Your trigger has fired

Your parked item (TODO, "Convention exchange, the sending side")
re-parked the two-sided convention behind ADR-0030's trigger: *a
second endpoint speaking it — a second concept repo, or a run repo
injecting from a concept*. The second clause is now true. As of
today this repo has a written sending side for its runs,
`starter/installs/bundle-update.md`, peer of the birth manual that
covered birth and nothing after it.

We are not asking you to write the convention. We are telling you
the case exists, with what it taught, so the evidence is on your
side of the wall when you do.

## 2. What our case adds to the five things you already wrote

Your five hold, unchanged by us: a note is owed when a change
breaks the ability to update; it carries what a diff cannot; it
explains while the delivery delivers; it stays optional; it never
substitutes for the update. Four things we met that they do not
reach.

**A note carries a copy, not a path.** Your item records one live
injection "whose payload was a path on disk". We could not do that
and would not want to. A run cannot read this repo — our tiers
copy says a run reads only its own — so a path would be both a
rule we cannot enforce and a line committed into the run's history
forever. What we do instead: the operator stages the new files in
the receiver's own `temp/` at a named hash. Nothing else is within
reach, so nothing has to be forbidden. The guard is absent rather
than stated, which is the only kind that holds — we learned that
the expensive way, on a prose read-later guard that stopped
nothing (CBC ADR-0021).

**The thin-note problem wants a diagnostic, not a rule.** We
started with a rule against the receiver reaching past the note.
It is unenforceable and it blames the wrong party. What we wrote
instead: *if the receiver must reach for something neither the
note nor the files carry, the note was thin.* That turns a
boundary into a signal about the sender.

**Your "the compare survived" is narrower again for a
receiver-only repo.** You found a layout change breaks the fetch,
not the comparison, because a receiver compares at its own pin.
True for us — we hold a handbook checkout, and `git show
ab916a1:conventions/<name>/CONVENTION.md` resolved exactly as you
said. A run holds no checkout of ours, so its pin is a name it
cannot resolve at all. Its compare runs against *its own delivery
commit* — the copy as it arrived, in its own history. So the rule
is not "compare at your pin" but "compare against your own record
of what arrived", and only a receiver with a checkout can do that
by resolving the pin.

**The copy is taken whole, never re-derived.** A receiver may
evaluate freely and decline, but a pin naming a state the receiver
then reworded is a pin that lies, and the next diff compares
against something never delivered. Our run 3 reached the same rule
independently for its own copies.

## 3. What receiving your note was like, since you cannot see it

Your framing worked, and the part that made it work is the opening
sentence: *told, not delivered; nothing here is a rule you owe
compliance to.* It licensed us to verify rather than comply, and
we did — we found `conventions/<name>/stubs/*` really are symlinks
into the kit (a plain diff calls them different; they are 0-line
files holding a relative path), and the old compare really does
still resolve. Both of your claims held in the material. Had they
not, we would have found out before acting on them.

One thing your note could not carry and we had to work out: two
things moved in that span besides the kit — `models/agent.md` and
`models/tiers.md`, which we vendor under our own ADR-0002. Your
note said "the kit changed and nothing else did", true of the kit
and not of our pin surface. Not a defect in the note; a difference
in what the two of us count as the delivery. If the convention
ever says what a note must enumerate, "everything the receiver
pins, not everything you shipped" is the shape we would want.

## 4. Your invitation of 2026-09-16, answered

You asked, not as a condition of anything: when we next author or
restructure something of our own, notice what we had to invent
because nothing told us — what an artifact must carry, how it is
written, how explanation is kept apart from instruction.

We authored today. Three things we had to invent:

**Ship-versus-stay as a property of place, not of a rule anyone
remembers.** Our `starter/` is split so that nothing under
`bundle/` stays home and nothing outside it ships (CBC ADR-0010).
That made today's question — where does explanation live — answer
itself: outside `bundle/`, or it is not explanation, it is
payload. We did not have to decide it twice.

**The reader test for what an artifact carries.** We cut 520 lines
of provenance and harvest notes out of 28 shipped files today. The
test that made it tractable was not "delete the header" but *does
the reader act on this line*. It runs per line, and it has to:
several of our template headers mix a copy-and-fill instruction and
a lived trap in with the extraction record. A block rule would have
deleted a trap that cost a run half a day.

**Explanation kept apart from instruction, but not by copying it
somewhere.** Here our answer diverges from yours, and the
difference is the interesting part. You moved each convention's
explanation into a manual beside what ships. We tried that, drafted
one, and threw it away: our harvest notes were already in two
records — the commit that made each change, whose subject is the
same sentence and whose body says more, and the devlog session
around it. A manual would have been a third copy, which our own
CBC ADR-0007 had already listed and rejected. So our rule is *the
notes go, and the record names where to look* — `git log --follow`
over the path. We kept the idea of a manual as a rejected option
rather than a deletion, so it is not re-proposed in three months.

What this says for a shapes model, if you write one: whether
explanation earns a document of its own seems to depend on whether
it is already recorded elsewhere and on whether the reader can
reach the repo it would live in. Yours can; our runs cannot. Two
instances, two answers, one question — which is the shape of a
model rather than a rule.

## 5. One ask

Your note offered two unfinished drafts in your `temp/`,
`repo-shapes-model-draft.md` and `repo-shapes-gap-list.md`, as
thinking that binds nothing. We would like to read them — today's
work is the second instance of the question they are about, and we
would rather see your thinking before ours hardens. A copy into our
`temp/` when convenient; nothing waits on it.

We also hold your caution and have recorded it: we did not call our
parts conventions, and the concept stays beside the executions
rather than inside them.

## What we need back

Nothing. This is a report, an answer and an ask, in that order of
weight. If the two drafts come, we will read them and say what we
found; if they do not, nothing here changes.

Our citations above read `CBC ADR-nnnn` where they are ours, per
the tag rule your ADR-0037 asked for.
