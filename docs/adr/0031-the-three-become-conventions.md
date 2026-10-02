# 0031. decide-first and the comparisons become conventions

Date: 2026-09-19
Status: Accepted; **superseded in part 2026-09-24 by ADR-0047** —
two of the three are discarded. `visual-comparison` remains a
convention of this container on exactly these terms; `decide-first` and
`option-comparison` are gone, and a run is born with eight
conventions rather than ten.

## Context

Three skills written in this repo — `decide-first`,
`option-comparison`, `visual-comparison` — sit in `.claude/skills/`
beside four convention copies, and do not ship. Two accepted
decisions put them there, and both are superseded here.

**ADR-0028 decision 5** parked shipping `format-comparison` on two
arguments: two uses by one author in one week is thin evidence, and
whether a method *about* the work belongs in the delivery was PLAN
Step 9's question. **ADR-0029 decision 6** answered the second —
container group, held for maturity — and added a third: the
container's skills directory holds pinned *convention* copies, so a
playbook is ineligible on its kind whatever the group says.

All three arguments rest on a distinction that no longer exists.

**The borrowed/native split is gone, and it went in stages.**
ADR-0025 made the kit and the manuals this repo's, with the
handbook as provenance and nothing tracking it. That was ownership
on paper; the files still spoke from the handbook's seat. On
2026-09-19 they stopped: 66 bare `ADR-nnnn` citations that read as
this repo's decisions were prefixed `HANDBOOK`, nine paths were
repointed, four outward links were written from the repo root, and
nine sentences that put the handbook where we now stand were
rewritten. `docs/conventions/README.md` was adopted as ours and
`docs/conventions.md` was folded into it.

So `docs/conventions/` holds seven manuals that are ours, and
`.claude/skills/` holds four copies of rules that are ours, pinned
to a container that is ours. "Pinned convention copies" describes
where a file came from, not a different kind of thing. The
ineligibility argument was reading a historical accident as a
category.

**And the maturity argument is answered by a different route than
the one it named.** ADR-0028's trigger was *the first run that
meets a format question of its own, seen through the harvest loop*
— wait for evidence to arrive. The user's call is to deliver and
watch instead, testing them in runs directly. That is not the
trigger firing; it is a different method of getting the same
evidence, and a faster one.

## Decision

1. **The three become conventions of the container.** A manual
   each under `docs/conventions/`, a row in its table, a registry
   entry, a pin, and a place in what a run is born with. Ten
   conventions where there were seven.

2. **The container's skills directory means one thing again**, and
   this time positively rather than by absence: it holds the rules
   a run is born with, all of them this repo's. ADR-0028 worried
   that a native skill beside four copies made the directory mean
   two things, and ADR-0029 called the distinction "carried by
   absence — no pin header, no manual, no registry row". The answer
   is not to mark the difference better but to remove it.

3. **The claim being made is that these are rules, not methods**,
   and it should be stated plainly because it is what a convention
   asserts: *you may ignore this, with a reason you can give*.
   `artifact-kinds`' own test. For `commit-messages` that is
   obvious. For `decide-first` it is a claim about a method that
   has run zero times.

   **What falsifies it:** a run that ignores one of the three,
   gives no reason, and comes to no harm. That is a convention
   nobody owes anything to, which is a method filed in the wrong
   place. The three manuals are where that would be recorded, and
   the first delivery is when it could first be seen.

4. **The first manual is the set's own test.** A manual is the why
   behind a rule, written for a maintainer. If `decide-first`'s
   says nothing a reader could not get from the skill, the premise
   here is wrong — these are playbooks, copied to be used rather
   than rules owed an explanation — and this ADR is revised rather
   than accepted. It is written first, alone, and with the
   thinnest-evidenced of the three, because testing with the
   strongest would prove the least.

5. **The by-name loops are widened, not fixed.**
   `bundle-update.md` names four conventions in two loops; they
   become ten. Deriving the set from the run's pin instead of a
   list is the better answer, is already filed in TODO with the
   user's reasoning — neither side's directory names can be
   trusted, both sides have a hash — and is left there. A set with
   one decision should not acquire a second on the way past.

6. **The map is not part of this.** A document stating how the ten
   relate — what fires when, what is standalone, that
   `visual-comparison` specialises `option-comparison`, where the
   domain skills supply sequences — is the next set, and it holds
   relations only, never a rule that lives in a manual or a skill.
   That scope rule is what `docs/conventions.md` never had, and why
   it grew to 126 lines of restatement before it was deleted.

## Consequences

Good: no second kind in the container's skills directory, no
exception in the update loops, and a manual for every rule a run
holds — which matters more once a run holds them, because a run
cannot read this repo's ADRs and the manual is the only *why* that
travels within reach.

Bad: three rules reach three runs having been used, between them,
three times — all by their author, all in this repo. That is the
thin evidence ADR-0028 named, shipped rather than waited out. The
trade is deliberate: evidence from a run arrives faster than
evidence from us, and the cost of a bad convention is that a run
ignores it, which decision 3 makes the falsification rather than a
failure.

Also: `bundle-update.md`'s by-name loops get longer at exactly the
moment the case for deriving them got stronger. Ten names in two
places is not worse than four, but it is more to be wrong about,
and the filed item should be read before an eleventh arrives.
