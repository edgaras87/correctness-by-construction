# 0020. This repo's decisions are cited from other repos as CBC ADR-nnnn

Date: 2026-09-11
Status: Accepted (2026-09-11, at the set's final records commit;
opened Proposed per change-plans §4. The sweep boundary held the
claim as stated: 102 citations, six numbers all ours, zero bare
after, none doubled, the twins still differing only in their
provenance path)

## Context

The handbook's reply of 2026-09-10 answered our citation ask with
a rule wider than the one we asked for (HANDBOOK ADR-0037): a bare
`ADR-nnnn` is the reading repo's own; a reference to another repo's
decision carries that repo's tag before the number, a short
upper-case name each repo declares once in its README's decisions
row; a document written for another repo's seat carries the tag on
every citation; records that never leave a repo stay bare. The
handbook applied it to itself — every convention and model now
reads `HANDBOOK ADR-nnnn` — and asked two things of us: declare
our tag, and tag any citation of our own decisions in a document
that reaches a run. Which documents those are was left to us.

The collision the rule prevents is already lived here. The pure
seed copies `starter/bundle/` verbatim into a run's
`.claude/skills/` (`starter/installs/pure-seed.md`), and the
bundle's headers cite this repo's decisions bare — 102 citations
across the five skills, of ADR-0003, 0005, 0006, 0007, 0008 and
0013. Run 3's own ADR-0003 names its project; cbc-framing's header
in the same checkout says "derives from concept v1 (ADR-0003)". A
reader there resolves the number against the run's `docs/adr/` and
lands on the wrong decision. The registry entry of 2026-09-09 gave
a reading rule for the same trap in the other direction — a
citation in a pinned copy resolves at its source — and queued the
fix as the master's; the handbook has now made it the master's.

This repo also has a rule for text that leaves for a run as
session input, in `temp/README.md`: no ADR numbers, paths or
vocabulary of this repo in it, because the run cannot see this
repo and a citation it cannot follow reads as its own. The reply
names that rule as one reading of the same fact and the tag as the
other, and leaves the choice to the bundle.

## Options considered

1. **Declare the tag and sweep the bundle; keep the temp rule for
   told text.** The tag is `CBC` — the reply's own example for this
   repo, and the name the prose already uses. Every citation of this
   repo's decisions under `starter/bundle/` reads `CBC ADR-nnnn`;
   the README's decisions row declares it. What stays bare: the
   records (`docs/adr/`, PLAN, the devlog, this file's neighbours),
   the bundle doc, the seed procedure, and the fills' headers —
   none leaves this repo; the seed inserts a fill's body and drops
   its header. The temp rule stays as written for told text: a
   session line reaches a run with no repo behind it, so a citation
   there is unfollowable whether tagged or not — the tag makes a
   copied citation resolvable, it does not make a told one so.
   Chosen.
2. **Keep the temp rule alone, no tag.** Leaves the bundle's 102
   bare citations leaking into every run — the lived collision
   untouched. Rejected.
3. **Tag everything, records included.** Contradicts the handbook's
   rule for records that never leave a repo, and would make this
   repo's own records read as if written for another seat.
   Rejected.
4. **Drop the temp rule and tag told text instead.** A told line
   carrying `CBC ADR-0012` is still a citation the run cannot open;
   the rule's reason is the run's blindness, not the number's
   ambiguity. Rejected.

For the sweep's record: one dated harvest line per touched header
(ADR-0007's discipline) — 30 identical lines beside the real
harvest lines, for a change that alters no execution's content;
ADR-0007's line is for lessons lived in runs, and the sweep is not
one. Rejected in favour of logging the sweep once, here and in the
bundle doc's Harvest section, with git history carrying it per
file.

## Decision

Option 1. This repo's tag is `CBC`. README's decisions row reads
"cited from other repos as `CBC ADR-nnnn`". Every citation of this
repo's decisions inside `starter/bundle/` carries the tag; the
sweep lands as one commit in the absorption change-plan, verified
by grep — the distinct numbers listed before, zero bare citations
after, no double tag. Text that stays in this repo cites bare. The
`temp/` rule for told text stands unchanged.

From here on: a new bundle file, or a harvest line added to one,
cites this repo's decisions with the tag; the fills and the seed
keep citing bare until the day one of them ships a header into a
run, which is the trigger to revisit.

## Consequences

Good: a run's copy of a skill resolves every citation at its
source without a reading rule; a re-pin carries the tagged text
into runs 1 to 3, whose copies collide today. Bad: two forms live
side by side in this repo — bare in the records, tagged in the
bundle — and an author must know which side a file is on; the
bundle doc's Harvest section says it at the moment of writing a
harvest line. Runs pinned before this commit keep the bare form
until they re-pin; nothing here edits a run.
