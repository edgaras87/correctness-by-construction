# Commit plan: a take is two commits

## Summary — the state after all commits

A run takes a delivery in two commits, and no rule it holds is
broken by doing so. `commit-messages` already keeps the concept
chapters and the `.claude/` copies apart; what the take adds is
the order. The chapters' commit comes first, and the decisions
entry carrying the pin and the read-through lands in the last,
where every copy equals the pin — so that commit stays the diff
base `exchange-read` already names.

`docs/conventions/exchange/` §4 says the order for us, and the
shipped `delivered-copies.md` rule 5 says it for the run. Both
point at `commit-messages` for how each commit is made and restate
none of it (`docs/conventions/conventions/` §3.1). ADR-0046 records
why the take splits rather than the rule bending. This is W2 of
the reading of 2026-10-01, D1 settled; run 3 asked it (F11), and
the next note answers it.

## Commits

**1. `docs(agent): add commit plan for the take's two commits`**
This plan.

**2. `docs(adr): 0046, a take is two commits`**
Proposed. Context: run 3's take @ `0000855` put `.claude/` and
`docs/concept/` in one `chore(agent)` commit, following rule 5's
"one act" and breaking `commit-messages`. Options: an exception in
`commit-messages` for a take, rejected — a rule with an exception
cannot be applied without first classifying the commit; the take
split. Decision: two commits, concept first, the entry in the
second.

**3. `docs(conventions): a take is two commits`**
The exchange's §4: step 3, *Place*, and step 5, *Register*, say
which commit each lands in. The deliverer's text first, so the
shipped rule follows its manual.

**4. `docs(conventions): the take points at commit-messages`**
Step 3 restated `commit-messages` — the commit types, which part
goes in which — where §3.1 asks for a pointer. §4 keeps only the
order and points for the rest. ADR-0046, still Proposed, is
corrected with it: its decision says the take follows
`commit-messages`, chapters first, and names no type.

**5. `fix(delivery): delivered-copies takes in two commits`**
The container's `.claude/rules/delivered-copies.md` rule 5 says
the order in the run's words and points at `commit-messages`, and
its Decisions footer cites `CBC ADR-0046`.

**6. `docs: records carry the take's two commits`**
ADR-0046 Accepted. CHANGELOG gains a Changed line under
Unreleased: what a run does at a take. The reading marks W1 done
at `9d4370f` and W2 done with this set's commits, with the pass
over its open items.

**7. `docs(agent): close commit plan for the take's two commits`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **The take says the order, and points for the rest.** Which
  part goes in which commit, and each commit's type, are
  `commit-messages`'; which paths are the arrangement's is
  `docs/conventions/agent-arrangement/`'s. Only the order serves
  the pin, and the pin is the exchange's. Added at the revision,
  after step 3 had restated `commit-messages`.
- **Concept first.** The other order puts the decisions entry in
  a commit where the concept chapters are still at the old pin.
  Concept first means the entry's commit is the one where every
  copy equals the pin — what `exchange-read` diffs against when no
  receipt branch was cut — so that skill needs no change. A birth
  already gives the concept a commit of its own
  (`delivery/installs/pure-seed.md`).
- **A deleted path goes in the commit of its kind.** A copy under
  `.claude/` the note names as gone is removed in the second
  commit, a chapter in the first. No delivery has removed a chapter
  yet; the rule says it once rather than leaving it to be guessed.
- **The manual and the rule in two commits**, as group 1 did: the
  deliverer's text, then what ships. Each reverts to a state the
  other can be read against.
- **No devlog in this set.** The session's entry carries it, with
  W3 to W6, at the session's end.
- **Nothing in `commit-messages`.** Its *The agent's own files*
  stands as it is; the open TODO decision on that section's commit
  types is separate and stays where it is.
