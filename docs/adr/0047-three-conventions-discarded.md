# 0047. Three conventions discarded, 2026-09-24

Date: 2026-09-24, recorded 2026-10-02
Status: Proposed (2026-10-02, under the commit plan for the eval's
group 6)

## Context

On 2026-09-24 three conventions went in one day. Each was recorded
in `.claude/decisions.md` and in a Status line of the ADR it
reversed, and in no ADR of its own — the gap ADR-0001 rules out,
which this record closes.

- **`decide-first`**, a skill of this repo's by ADR-0030 decision 2
  and a convention of the container by ADR-0031 decision 1. Three
  firings, one win, and in the win one line did the work — *can you
  say roughly how many commits this takes?* The two misfires
  produced a draft covering queued work rather than one unsettled
  shape, and seven ordered questions written and discarded. What
  settled the same question instead was a proposed ADR corrected
  while building, which `commit-plan` already carries.
- **`option-comparison`**, split out by ADR-0030 and made a
  convention by ADR-0031. One firing, in the set that created it.
  The method it carried is `visual-comparison`'s spine, which had
  three firings; what was discarded is a second copy of that spine,
  kept for choices not about showing something, of which one had
  come.
- **`artifact-kinds`**, the container's vocabulary, where ADR-0035
  decision 2 had entered *shape*. Its purpose was that one word
  mean the same to both parties, and the reviewer could not use its
  definitions: one definition fitting all, and no telling what it
  meant. A header rule written to replace it was discarded the same
  day — eight of ten documents already said what they were,
  unprompted, and a rule describing a practice that holds itself up
  changes nothing.

Counted again on 2026-10-02: run 3 had used `decide-first` and
`option-comparison` in its writing pass, which the count missed.
Both discards stand on it (`.claude/decisions.md`, 2026-10-01).

## Options considered

- **Keep all three on trial a few weeks more.** Rejected: each had
  been kept on exactly that reasoning, and a trial never ends by
  itself.
- **Move `decide-first`'s one line into `commit-plan`.** Rejected:
  moving a sentence so a discard feels less wasteful is how the
  discarded thing grows back. If the question is missed in real
  work, that is the trigger to put it somewhere.
- **Merge `option-comparison` into `visual-comparison` and rename
  it.** Rejected: it keeps every line and changes the sign on the
  door; nothing had asked for the general scope in five weeks.
- **Keep `artifact-kinds` here and stop shipping it**, or **fix it**
  — drop its unused axis, cut it to 84 lines. Rejected: one keeps a
  vocabulary one of its two readers cannot use, the other makes an
  unusable thing smaller.
- **Discard all three** — chosen.

## Decision

1. **`decide-first`, `option-comparison` and `artifact-kinds` are
   discarded**: each skill, its manual and the master shipped.
2. **This supersedes in part** ADR-0030 decisions 2 and 9; ADR-0031
   decision 1 for two of its three conventions — `visual-comparison`
   stays on its terms; and ADR-0035 decision 2's vocabulary entry.
   Everything else in them stands.
3. **Nothing replaces them.** A choice not about showing something
   is decided and corrected while building, inside a commit plan; a
   document says what it is in its own opening, as most already did.

## Consequences

- The container went from ten conventions to seven that day; shapes
  and conventions have since made it nine.
- `decide-first`'s one line lives here and in the decisions log. If
  the question it asked is missed in real work, that is the trigger
  to give it a home.
- ADR-0030, 0031 and 0035 name this record in their Status lines.
