# 0043. The models are ours to edit

Date: 2026-09-29
Status: Accepted (2026-09-29, at the set's records commit; opened
Proposed under the commit plan for the agent model, and amended
before acceptance at the reviewer's question — folding the agent
model into agent-arrangement moved from rejected to deferred)

## Context

ADR-0026 made both models this repo's, and its decision 4 took their
bodies verbatim: "editing is permitted, not owed", and the refutation
conditions "stay as written until something lived here contradicts
them". The reason was the re-sync: "A rewrite on the day of taking
would spend the only thing that keeps a re-sync cheap."

ADR-0038 ended the re-sync. The handbook is history, and no
coordinates are kept for a compare. ADR-0038 also removed the
`HANDBOOK ADR-nnnn` citations from the manuals, because "a why that
points past the manual at a record the reader cannot open is not a
why". It spared the models only because ADR-0026 decision 4 had
already frozen their bodies.

So the freeze outlived its reason, and `docs/models/agent.md` shows
the cost. Its header says the body is "as taken". Its §1 names the
delivering repo as an instance of a project receiving pinned copies,
which ADR-0042 contradicts. It cites twelve handbook decisions that
nobody here can open. And its claims invite "a repo that vendors
this model" to add its own evidence, which this repo never did,
though it has plenty.

The model is live. agent-arrangement explains against it in nine
places, commit-messages cites its claim A1, the tiers model cites
its §4, and the shapes rule works through the channel it calls
pushed.

## Options considered

- **Keep the freeze.** Rejected: its only reason is gone, and a
  frozen text that is false misleads every manual that cites it.
- **Fold the agent model into agent-arrangement,** as the shapes
  model became the shapes manual (ADR-0037). Deferred to the reading
  of `tiers.md`. Whether `docs/models/` stays a kind of thing needs
  both files, and the fold would grow agent-arrangement by about 200
  lines before that is known. The first reason given here, that the
  model serves four readers, was weak: manuals cite one another.
- **Rewrite it from scratch as ours.** Rejected: its structure and
  most of its claims hold, and its handbook evidence was lived.
  Correcting it keeps what is true.

## Decision

1. **Both models are edited as ours.** A model is corrected when it
   is false, the same as any record here. ADR-0026 decision 4's
   verbatim rule ends. Its decisions 1 to 3 stand.
2. **A model cites what its reader can open.** A handbook decision
   is replaced by its reason, written in place, or by what this repo
   adopted in ADR-0038.
3. **The handbook's evidence stays, as attribution.** Evidence lived
   there is still evidence. This repo's is added beside it, not in
   its place.
4. **Section and claim numbers do not move.** Other files cite them,
   and a renumbering would break every one of those citations.

## Consequences

- `docs/models/agent.md` is corrected, cited and evidenced in this
  set. `docs/models/tiers.md` falls under the same decision, and
  waits for its own reading.
- `agent.md`'s header stops saying "as taken" in this set;
  `tiers.md`'s, which says the same, changes at its own reading.
- A later change to a model is an ordinary edit, and needs no ADR
  unless it changes what the model claims.
