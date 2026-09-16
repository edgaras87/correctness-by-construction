# Handoff from never-oversold (run 3 of the pure seed) — 2026-09-17

<!-- Staging copy, untracked in temp/; deleted once the bundle's
     reply is absorbed. Substance is on record in this repo: TODO
     Later (the line "Hand-off to the CbC bundle (CBC ADR-0007, the
     harvest section)"), .claude/decisions.md (2026-09-14 through
     2026-09-16), and .claude/rules/skills-changed-in-place.md.
     Read the repo; this document says where to look and what we
     need back. -->

From the runs tier. Context: this run closed SL-1 on 2026-09-14 and
re-pinned to the bundle @ 7bbf49a on 2026-09-15 — every one of your
five method skills byte-identical to that pin today. One ask. It
does not block us; Step 6 (SL-2) opens on the copies as they stand.

## The ask: may a run edit its copy of a method skill between two pins?

**Where, on your side:** CBC ADR-0007 (harvest discipline) and the
bundle doc's Harvest section. **On record here:**
`.claude/rules/skills-changed-in-place.md` (seven rules, scoped to
your five skills), `.claude/decisions.md` 2026-09-14 through
2026-09-16, TODO Later's line for you.

**What happened.** SL-1 closed with twenty prose hand-offs in TODO
that no repo would read before the retrospective, while the slice
skill was about to run three more times known thin. The pinned-copy
rule as this run was born with it cost twice: behind the source, and
behind the run's own lessons.

**What the handbook did with the same ask.** It took it for its own
four conventions, reshaped, at kit `9e28143` — convention-lifecycle
§8 step 4 now carries "A project may edit its copy between two
pins", HANDBOOK ADR-0038, provisional until one such edit has gone
through an update. Its tiers model §3 gained two sentences: an
edited copy is not a third form of delivery — delivery comes down,
an edit goes up — and an edited copy's diff against its pin is one
of the records the tier above reads. It explicitly left your five
method skills to you and decided nothing for them. You will receive
the convention yourself at your next kit re-pin.

**What we ask.** That CBC ADR-0007 say whether the same holds for
the bundle's skills, and if so, that its harvest section say it from
the harvester's seat. The mechanics you already have: your first
lived case was a run editing its local walkthrough copy, you read a
run's records read-only, you update the master in the run's own
wording, you add a dated harvest line, the pin is untouched. What it
does not say is that the change may arrive already made, in the copy,
with its own dated header line — so the harvest is a diff against
the pin rather than a reading of prose, and the run's provenance
carries into your harvest line as it does today.

**The rules this run holds, for your judgment** (the handbook's text
is the same shape, in its words): a skill is a copy pinned at a
source commit; edited in place only from lived work, as a question
or outcome any project would want, never project-specific — what
this project alone needs goes into its own records; each edit
carries a dated line in the copy's header and an entry in the
decisions log; at a step's close one TODO line per edited copy asks
you to evaluate since the pin, and you read it when you read the run,
not at every close; a step opening before your reply runs on the
edited copy; at the re-pin your version overwrites the copy whole,
each edit taken, reshaped or declined in your own text, a declined
edit gone and never edited back, a need it served going to the
project's records. Scope here: your five skills with their
references and templates. Outside it: `docs/concept/` — theory the
skills derive from upstream, no step here runs a chapter, its
lessons stay prose hand-offs.

**Rejected here, named so you can weigh them:** an overlay file per
skill beside the pinned copy (holds project-specific behaviour and
survives a slow source; a second file per skill and a prune at every
re-pin — machinery for a need no step has met, kept as the
fallback); keeping declined edits with a logged reason (compounds at
every re-pin and makes the copy project-specific in fact).

**Honest state:** no edit of any copy has gone through a re-pin yet,
here or anywhere. The handbook's text is provisional on that, and
yours would be too. If you would rather wait for that evidence, say
so — we keep writing prose hand-offs for your skills meanwhile, and
the rules file says it stands only until you answer.

## What we need back

A reply into this repo's `temp/`, or your verdict readable in your
own records at your next commit — either way we read, nothing is
sent:

- Taken, declined, reshaped, or held for evidence, and the hash.
  Taken or reshaped: our rules file goes redundant at the next
  bundle re-pin, or follows your text. Declined or held: it stands
  as a logged local layer until the retrospective, and we go back to
  prose for your skills.
- Nothing else is owed. The SL-1 harvest (`7bbf49a`) is absorbed
  here and its TODO lines are closed.
