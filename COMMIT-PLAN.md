# Commit plan: the agent binding moves into agent-arrangement

## Summary — the state after all commits

The agent model holds only what any tool fits. Claude Code's
mechanisms, the binding, live in the convention that adapts the
model to this repo's tool.

- ADR-0064 records the move and the options weighed
  (`TODO-CONVERSATION-MEMORY.md` §14, last whole at this plan's
  opening commit).
- agent-arrangement gains §5, *The binding: Claude Code*: §5.1 to
  §5.7 hold what the model's §10.1 to §10.7 held, each number kept,
  so a reference moves by one rule. §3.2 points at §5.6 instead of
  retelling it; §2.3 and §2.6 point at §5.1 and §5.3.
- The agent model's §10 says what a binding is, and that the repo
  using a tool writes it. §9 says the model keeps no list of where
  conventions land; §8 no longer says where a manual records its
  channel. No section is renumbered.
- `auto-run.md`'s reference to the model's §10.4 points at
  agent-arrangement §5.4: the level jump closes.
- Both models drop their provenance comments.
- `ARCHITECTURE.md`'s codemap names the three models.
- The binding item and conversation-memory §14 go.

## Commits

**0. `docs(agent): add commit plan for the agent binding`**
Opens the set.

**1. `docs: ADR-0064 the agent binding lives in agent-arrangement`**
The ADR, Proposed: the options of conversation-memory §14, and the
numbering kept.

**2. `docs: the agent binding moves into agent-arrangement`**
agent-arrangement's §5, from the model's §10.1 to §10.7, its
references to the model's §10 now its own §5; §1 names §5; §3.2
keeps what goes in `rules/` and points at §5.6 for how a rule
loads. The model's §10 shrinks to what a binding is: one mechanism
may serve two channels, and a tool may reshape what it loads. §4.1
and claim P2's evidence stop pointing at §10. The conventions
manual's reference to §10.6 moves to agent-arrangement §5.6. One
move: neither side may hold the binding alone for a commit.

**3. `chore(agent): auto-run points at the binding's new home`**
`.claude/approaches-on-trial/auto-run.md`: the model's §10.4
becomes agent-arrangement §5.4. The agent file, next after 2.

**4. `docs: the agent model stops pointing down`**
§9 keeps that a convention's channel is chosen per convention by
§8, and that the model lists none of the choices. §8 drops "until
now made implicitly" and "Recorded per convention, in its manual's
*why it arrives this way*". The rule it pointed at is conventions
§3.3's.

**5. `docs: the models drop their provenance comments`**
`docs/models/agent.md` and `docs/models/tiers.md` open with a
comment citing ADR-0026, ADR-0038 and ADR-0043: provenance, and a
model pointing at records. ADR-0043 still says the models are ours
to edit. As was cut from the idea-to-output model.

**6. `docs: the codemap names three models`**
`ARCHITECTURE.md` §6 says "the agent model and the tiers model";
the idea-to-output model landed in `55078bc` and was missed.

**7. `docs: the binding item closes`**
The records commit. ADR-0064 Accepted. TODO: the binding item goes.
The fact-reference item's level-jump idea says the one case closed.
The item's idea on the tiers model is declined: round 2's Layout
kind reads it. `TODO-CONVERSATION-MEMORY.md` §14 goes.

**8. `docs(agent): close commit plan for the agent binding`**
Deletes this file; the body says what diverged.

## Decisions for you to object to

- **One section, not spread.** The binding sits whole in §5, not
  split into §2.3, §2.6, §3.1, §3.2 and §3.5 where each fact is
  used. A tool's facts change together, by release, and are checked
  together against its documentation; those sections point in.
- **§5.n mirrors §10.n.** Every reference to the model's §10.n
  becomes agent-arrangement §5.n.
- **No renumbering in the model.** §9 and §10 stay, each a short
  statement, so every reference to §11 and §12, in the manuals and
  in the claims, holds.
- **A page of its own for the binding** is tried only if §5 fails.
- **The provenance comments go,** in both models.
- **The tiers pass is declined,** since round 2's Layout kind reads
  every model.
