# Commit plan: the eval's group 3, our seat against its manuals

## Summary — the state after all commits

What this repo holds for its own agent says what its manuals say.

- **A new agent skill is a chore, in both seats.** `commit-messages`
  says `chore(agent)` to add, install or update a skill — the
  container's master and ours, byte-identical — which is what we
  already do (F21, D1).
- **Our convention skills are derivations.** The three manuals that
  call ours "a copy of the container's" say what ADR-0042 decided:
  each derived from its manual, identical today (F22, D1).
- **The exchange's skills say what the exchange says.** `exchange-read`
  writes the reading's first line before it reads, diffs against the
  run's receipt branch or its last delivery entry's commit, and asks
  what the run teaches the worked example; `exchange-deliver` sends a
  one-line note when nothing is addressed to us, not when nothing is
  taken (F23–F26).
- **The manual's shape counts its nine sections** (F27).
- **The decisions log's header says what earns an entry**: a decision,
  not every fix that brings a skill to its manual (F28).
- **Pointers are root paths** in `exchange-deliver` and the entry
  file's guard comment (F29).

Our own arrangement changes; one shipped skill does, and reaches
run 3 with group 2's delivery after SL-3.

## Commits

**1. `docs(agent): add commit plan for the eval's group 3`**
This plan.

**2. `fix(delivery): a new agent skill is a chore`**
The container's `commit-messages`, *The agent's own files*:
`chore(agent)` to add, install or update.

**3. `chore(agent): commit-messages follows the container's`**
Ours, byte-identical again, and a `.claude/decisions.md` entry: the
rule changed, why, the two options rejected.

**4. `docs(conventions): our skills are derivations`**
The commit-messages, commit-plan and visual-comparison manuals'
*What this is made usable as*: the deliverer's skill derived from
the manual, identical to the container's today (CBC ADR-0042) —
not a copy.

**5. `chore(agent): the exchange skills say what the exchange says`**
`exchange-read`: the first line written at step 2, before anything
is read; the diff base named in this repo's words — the receipt
branch, or the commit of the last delivery entry; step 4 asks what
the run teaches the worked example (exchange §6.3).
`exchange-deliver` §3: a note alone when nothing is addressed to us
(exchange §6.6), since a declined item still owes its verdict.

**6. `chore(agent): the manual's shape counts nine`**
`.claude/rules/convention-manual.md`: "the seven" where the list
holds nine.

**7. `chore(agent): the decisions log says what earns an entry`**
Its header: an entry per arrangement decision — a skill or rule
added, a rule's meaning changed, a workflow adopted; a fix that
brings a skill to its manual is no decision, and its commit body
says why.

**8. `chore(agent): pointers are paths`**
`exchange-deliver` §5's `pure-seed.md` and `CLAUDE.md`'s guard
comment, "(agent-arrangement)", as root paths.

**9. `docs: records carry the eval's group 3`**
The eval marks F21 to F29 fixed with their commits. TODO's item on
the commit type for a new agent skill closes. CHANGELOG gains a
Changed line: what a run commits a new skill as.

**10. `docs(agent): close commit plan for the eval's group 3`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **No ADR for the commit type.** ADR-0038 1c decided that the
  agent's files never share a commit, not which type each takes;
  the mapping is the skill's own text. The decision is small, so
  its record is the commit body of step 2, the decisions entry of
  step 3, and the eval's D1 until the eval goes.
- **Two seats, two commits**, where a skill both seats hold changes
  (steps 2 and 3) — the counting lesson of the last reading.
- **F28 narrows the header rather than back-filling entries.** Of
  nine skill and rule commits since 2026-09-29, two have an entry;
  the other seven are fixes that bring a skill to its manual, and an
  entry for each would retell its commit body. Proposed here; the
  reviewer may prefer back-filling.
- **`commit-messages` §3 stays.** The deliverer's habit names
  `chore(agent)` for its own skills; after step 2 the shipped rule
  says the same, and §3 still explains the rest of the habit.
