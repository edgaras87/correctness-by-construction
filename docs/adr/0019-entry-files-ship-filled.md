# 0019. The entry files ship filled — the semi-pure delivery

Date: 2026-09-07
Status: Accepted (2026-09-07, at the set's final records commit;
opened Proposed per change-plans §4. The manual's boundary proved
the cut-and-fill against the real fills on a scratch repo — both
outputs byte-identical to their fill from the title line down, no
header or placeholder leaking — before it was written; the
contract boundary held the "no surface enters" claim as stated.
No boundary contradicted the shape)

## Context

ADR-0016 adopted the pure shape: the seed delivers material and
decides nothing, and the newborn's agent derives its own CLAUDE.md
from the kit's stub. It parked the CLAUDE.md template rather than
deleting it, with the condition on record: "its content may
re-enter delivery if the pure runs show derivation inadequate."
A README template was composed beside it the next day
(2026-09-06) from run 1's own derivation, and the TODO item that
holds the semi-pure idea set the test: if derivation keeps
producing what the templates hold, the shape is never needed; if
it keeps missing something, that gap is the install's
justification.

Two pure runs have now derived their entry files unaided, under
the same skills. The Step 0 reading of both (devlog 2026-09-06)
found the same gaps twice:

- Neither run produced the pre-framing guard — never invent the
  framing artifacts to fill the gap — the one line in the CLAUDE
  template that is a stance rather than a fact.
- Neither produced the pin stance for the skills; run 2 held it
  for the concept only, run 1 for both.
- Run 2's README lacked the start-here pointer and the note that
  its own paragraph is rewritten at Step 1; its devlog called the
  paragraph badly written.
- What both derived unaided — the nothing-to-build-yet line, the
  working-name line, the records table untouched — the templates
  already hold; run 2's opening line was harvested into the README
  template (166bc7e) under the rule that a birth template is
  judged at the Step 0 reading.

The test is answered on the justify side. The gap is specific
and stable: a stance line and a pin rule, both of which a run can
only receive, not re-derive, because nothing in the run's
experience before the briefing produces them.

Two other decisions make the delivery cheap. ADR-0015 chose
whole-copy over merge, so writing a fill over the stub assumes
nothing of the stub's shape — the same reason CLAUDE.md never
re-entered the assumed-surface contract. ADR-0018 put the seed on
a receipt branch, so one more delivery is one more commit there,
and main's first commit is still the agent's.

## Options considered

1. **Keep deriving; hand the guard back at the Framing
   boundary.** The hand-back protocol exists for playbook
   warnings. Rejected: the guard governs the whole pre-framing
   window, and handing it back after Step 0 delivers it late by
   exactly the period it protects.
2. **Deliver the CLAUDE body only; README stays derived.** The
   guard and the pin stance live in CLAUDE.md. Rejected: the
   README gap is smaller but the same kind (a self-retiring note
   and a pointer no run produced), and one fill delivered with the
   other left derived makes two shapes where one commit makes one.
3. **Deliver both fills, one commit on the receipt branch** —
   chosen.

## Decision

The seed manual gains one optional step, the semi-pure delivery,
between the material deliveries and the return to main: each fill
in `starter/fills/` is cut from its title line down (headless —
the provenance header stays here), `<working-name>` is filled with
the placeholder directory name, and the result is written over the
kit's stub — `claude-md-template.md` over CLAUDE.md,
`readme-md-template.md` over README.md — in one commit on
`birth-seed`, the bundle pin in its subject. Nothing else is
filled; no other placeholder exists in either fill.

Both files in one commit: the commit split governs the newborn's
own line, and the receipt branch is never merged into it — the
kit-remainder commit straddles there already. On main the agent
commits the two files under whatever split it chooses, like every
other delivered file.

The firing prompt's situation sentence names the delivered entry
files in a clause; it says nothing about what to do with them.
They are the newborn's own from delivery (ADR-0017's fill rule):
edited in place, never re-copied.

Run 3 runs with the step on. The reading's object changes with
it: not whether the agent derives the guard, but what it changes
in delivered entry files at Step 0 and whether the guard holds
through Framing. The does-it-invent-protections measurement the
three-way reading item assigned to pure runs ends with run 2.

ADR-0016 is amended in one clause: the pure-born newborn no longer
derives its CLAUDE.md when the step is on; its parking condition
fired and the content re-entered. The rest of ADR-0016 stands.
The overlay's contract statement (starter/README.md) changes from
"no non-additive act" to the true statement: one act, replacing
two stubs whole with fills that carry the kit's half verbatim at
the pin and assume nothing of the stub — no surface enters the
contract, nothing to widen handbook-side.

## Consequences

Good: the guard and the pin stance arrive before the window they
protect; the README is true for a stranger from the first commit;
the two shapes differ by one commit, so a pure run remains one
switch away if a reading ever wants it; both templates carry
every line's source in their headers, so the reading can attribute
any edit the agent makes.
Bad: the kit's stub text for the two entry files is discarded at
delivery — the fills carry it verbatim at the pin, and each kit
re-pin owes a re-verification of that half (the headers say so);
the agent meets an arrangement it did not write, and whether it
reads it as its own or as vendor text is now something to watch;
shipped text encodes prior runs' conclusions, which the pure seed
excluded on purpose — accepted, because those conclusions are the
harvest the readings exist to produce.
