# Commit plan: the eval's group 6, the ADRs

## Summary — the state after all commits

The ADRs tell their own story: every reversal has an ADR, and every
ADR's Status says what later changed it.

- **ADR-0047 records 2026-09-24**: `decide-first`, `option-comparison`
  and `artifact-kinds` discarded — what went, why, what was
  rejected — superseding the parts of ADR-0030, 0031 and 0035 that
  day reversed, as ADR-0001 asks. Its reasons are the decisions
  log's entries of that day, stated in the ADR (D2, F62).
- **Every Status names what changed it**: the fourteen pairs F60
  found, and 0030, 0031 and 0035 pointing at 0047.
- **The ADRs keep their form**: 0039's Status covers its body's
  2026-09-29 amendment; 0031 and 0033 record the options their own
  Context weighed; 0039's options run in order; 0024's Status notes
  its body's 2026-09-29 amendment; 0025's Status reads whole (F61,
  F65).
- **The playbook's version line cites ADR-0035 decision 4**, the gap
  its shapes line answers (F63).
- **The eval is gone**: every finding fixed, or held where it is
  weighed — F64 under TODO's baselines item.

## Commits

**1. `docs(agent): add commit plan for the eval's group 6`**
This plan.

**2. `docs(adr): 0047, the discards of 2026-09-24`**
Proposed. Context from 0030, 0031 and 0035 and the decisions log of
that day; options as that log weighed them; the decision; what each
earlier ADR keeps. Decision-first: settled in conversation.

**3. `docs(adr): every Status names what changed it`**
The fourteen Status lines F60 lists, each gaining "changed in part
by ADR-nnnn (date)" and what changed; 0030, 0031 and 0035 point
their 2026-09-24 notes at 0047. Status lines only — no body moves.

**4. `docs(adr): the ADRs keep their form`**
0039's Status names the 2026-09-29 amendment and its options run
1 to 5; 0031 and 0033 gain *Options considered*, from what their
own Context already weighed — nothing invented after the fact;
0024's Status notes its body's amendment; 0025's parenthetical
closed.

**5. `fix(delivery): the playbook cites the gap it answers`**
`delivery/fills/cbc-run-pure-playbook.md`'s version line: ADR-0035
decision 4, not 8 (F63).

**6. `docs: records carry the eval's group 6`**
ADR-0047 Accepted. The eval marks F60 to F65 fixed or held. TODO's
item on the partial reversals closes.

**7. `docs(temp): the eval goes`**
Every finding has ended; the eval's own header says it goes then.
Git keeps it.

**8. `docs(agent): close commit plan for the eval's group 6`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **Status lines, not bodies.** ADR-0001 keeps an ADR immutable; its
  Status is the one line that tracks what happened to it after.
  F60's fixes touch Status alone.
- **0039's options are renumbered in place** only if nothing cites
  them by number; otherwise they are reordered under their numbers
  and the close says so.
- **No options invented for 0031 and 0033.** If either Context
  weighed none, its *Options considered* says so in a line, rather
  than writing alternatives nobody weighed.
- **The eval goes in its own commit**, after the records that mark
  it, as the readings did.
- **No CHANGELOG line.** Nothing here is the concept or an execution.
