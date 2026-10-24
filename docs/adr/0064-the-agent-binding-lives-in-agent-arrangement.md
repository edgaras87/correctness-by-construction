# 0064. The agent binding lives in agent-arrangement

Date: 2026-10-25
Status: Proposed (2026-10-25, under the commit plan for the agent
binding).

## Context

`docs/models/agent.md` held two kinds of text. Its §2 to §8 and §12
fit any tool: the parts, the channels, the context window, the
gate, claims that can be proven wrong. Its §10, the binding, held
one tool's mechanisms, checked against Claude Code 2.1.310.

agent-arrangement, which stands on the model, retold §10.6 in its
§3.2. On 2026-10-24 one fact, when a path rule loads, changed in
both (`36eb0c1`). That met the trigger of an item open since
2026-09-29: fold the whole model into the manual (ADR-0043 had
deferred it).

ADR-0063 then made a model the top description of its chain, with
every link pointing up. Two things in the agent model broke that:

- §9, and §8's second sentence, said where a manual records its
  channel. That is a rule about manuals, held by conventions §3.3.
- `auto-run.md`, an approach on trial, cited the model's §10.4, a
  reference that jumps a level (TODO, the fact-reference item).

The talk is `TODO-CONVERSATION-MEMORY.md` §14.

## Options considered

- **Leave both as they are.** Rejected: the double edit repeats at
  every release of the tool, and §9 and §8 keep pointing down.
- **Fold the whole model into agent-arrangement.** Rejected: the
  idea any tool fits would sit inside a Claude Code page, and the
  manual would more than double.
- **The binding as a page of its own.** Not now: a new kind of
  text, to try only if the section fails.
- **The agent model as a concept.** Rejected: a concept is copied
  whole and built by, with a version and a CHANGELOG. The agent
  model is never copied; a repo adapts it in its arrangement.
- **The model written more general.** Rejected: §2 to §8 are
  vendor-neutral already. What was not general is §10.
- **The binding spread over the sections that use it,** §2.3, §2.6,
  §3.1, §3.2 and §3.5. Rejected: a tool's facts change together, by
  release, and are checked together against its documentation.
- **Renumber the model once §10 empties.** Rejected: every
  reference to §11 and §12, in the manuals and in the claims, would
  move for no change of meaning.

## Decision

1. **The binding lives in agent-arrangement,** as its §5, *The
   binding: Claude Code*. The model is the interface; the
   arrangement is this repo's implementation for one tool.
2. **§5.n holds what the model's §10.n held,** so each reference
   moves by one rule.
3. **The model's §10 says what a binding is:** the mechanisms one
   tool gives each capability, written by the repo that uses the
   tool. One mechanism may serve two channels, and a tool may
   reshape what it loads. No section of the model is renumbered.
4. **The model points down at nothing:** §9 keeps that the model
   lists no channel choices; §8 no longer says where a manual
   records its channel.

## Consequences

- agent-arrangement grows by about 115 lines; its §3.2 points at
  §5.6 instead of retelling it.
- `auto-run.md` cites agent-arrangement §5.4, and its level jump
  closes.
- A change to Claude Code is one edit, in one convention, and the
  foundation check reaches the model only when an idea changes.
- The binding item and conversation-memory §14 go.
