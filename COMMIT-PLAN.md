# Commit plan: the agent model becomes ours

## Summary — the state after all commits

`docs/models/agent.md` is this repo's model, edited as ours. It is
no longer a frozen copy of the handbook's draft. ADR-0026 froze its
body verbatim to keep a re-sync cheap, and ADR-0038 ended the
re-sync, so that reason is spent and a new ADR says so.

Nothing in it is false today. Its subject is a project that
receives conventions, and the deliverer, which derives its own
since ADR-0042, is named as a different case. It cites only what a
reader here can open, or gives the reason in place. Its claims
carry this repo's evidence beside the handbook's: O1's missed
divergence is observed now, A1 has run 3's subjects and our own,
and P2 names a test that can still run. Its Claude Code binding is
checked against the version in use, and says which version that
was.

It stays a model, shared theory, and is not folded into
agent-arrangement, because several manuals and the tiers model lean
on it. No section or claim is renumbered: agent-arrangement cites
§4, §10, §12, A2 and M1, commit-messages cites A1, and the tiers
model cites §4. The TODO item "Check `docs/models/`" narrows to
`tiers.md`.

## Commits

**1. `docs(agent): add commit plan for the agent model`**
This plan.

**2. `docs(adr): ADR-0043 — the models are ours to edit`**
Decision first, since it was agreed in conversation. It opens as
Proposed and amends ADR-0026 decision 4. The body stayed verbatim
"to keep a re-sync cheap", and there is no re-sync since ADR-0038.
So a model is edited like any record of ours: corrected when false,
and cited so its reader can follow it. The handbook's evidence stays
as attribution, as ADR-0038 said of the models.

**3. `docs(models): the agent model says what is true`**
The parts that are false today. The header's "as taken" and the
draft line naming the handbook's Step 14. §1's subject, whose
"delivering repo maintaining itself is one instance of it" ADR-0042
contradicts. §9's "what its directory lists". §10's "starter kit".

**4. `docs(models): the agent model's citations open`**
Twelve `HANDBOOK ADR-nnnn` citations, handled as ADR-0038 handled
the manuals' citations. Where the text already gives the reason,
the citation goes. Where it does not, the reason is written in
place, or the citation points at what this repo adopted in ADR-0038.

**5. `docs(models): the claims carry our evidence`**
O1 becomes evidenced: a missed divergence is observed here, in
ADR-0024 decision 4 (wrong for 11 days), the decision index (stale
twice) and PLAN's "same stubs". Each was found only by a comparison
run for another reason. A1 gains run 3's subjects and our own
drafts. P2's resolving test, "the handbook's field test", will never
run, and is replaced by one that can. The scorecard follows.

**6. `docs(models): the Claude Code binding rechecked`**
*Provisional.* §10's tool facts were observed on Claude Code
2.1.260 to 2.1.263 and never re-checked, and agent-arrangement
relies on one of them, that HTML comments are dropped on load. They
are checked against the version in use, through the Claude Code
guide agent and by observation where that is possible here, and
the version is recorded. What changes depends on what the check
finds.

**7. `docs: devlog carries the agent model`**
The session's entry. ADR-0043 flips to Accepted here. The TODO item
"Check `docs/models/` against today's repo" narrows to `tiers.md`.

**8. `docs(agent): close commit plan for the agent model`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **A model, not part of a manual.** The shapes model became the
  shapes manual because the two covered one convention. This model
  serves four readers, so it stays shared theory.
- **No renumbering.** Sections and claims keep their numbers, so
  every live citation of them still resolves.
- **The handbook's evidence stays.** It is attribution, and it was
  lived, even if not here. Ours is added beside it, not in its
  place.
- **`tiers.md` is out of scope.** It is the other half of the TODO
  item, and it waits for its own reading.
