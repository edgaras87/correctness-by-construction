# 0006. Practice executions as skills, without agent seats

Date: 2026-08-28
Status: Accepted

## Context

The archive packages the practice executions as skills driven by
agent definitions (groundskeeper over infra-establish + infra-serve,
system-bootstrap over cbc-bootstrap). At import review the whole
form came into question: the run's human drives the pipeline phase
by phase through plan steps, so how much delivery machinery do
these phases actually need? Three forms were on the table.

## Options considered

1. Import the packaging as-is (skills + agents) — faithful, but the
   agent layer is untested by its own admission (the archive STATUS:
   "first lived use owed... expect corrections from its first real
   run") and ~80% of the agent text restates the skill bodies. A
   subagent seat adds a layer the human-gated flow never uses.
2. Guides + references, pointed at from the run's plan steps — the
   simplest form, and right for the planned phases: establishment
   and bootstrap happen once, at a known step, and a pointer at the
   moment of need fires (agent model P2). It fails at re-entry:
   "we need Redis now" arrives months later with no plan step
   waiting, and a guide then depends on human memory — P1 is
   precisely the claim that this fails.
3. Skills without agents — chosen.

## Decision

infra-establish, infra-serve, and cbc-bootstrap land as skills, the
same mechanism as cbc-framing and cbc-slice: one delivery form for
everything a run installs, one bundle mapping, and each skill still
invokable explicitly from the plan step that owns its phase. The
trigger earns its keep exactly once — infra-serve fires on the
unplanned utterances that make re-entry the moment the method is
most needed and least remembered.

The agent definitions stay behind in the archive. Their one piece
of content the skills lack — the record-path defaults — is absorbed
into the infra-establish skill as a recorded import change. If a
lived run later shows the seat boundaries are needed, that arrives
as a harvest with evidence, not as an import of untested packaging.

## Consequences

Good: one mechanism throughout the executions layer; re-entry is
protected by its trigger; two never-lived files stay out of the
authoritative tree; the run flow the author actually works —
plan-driven, human-gated — matches the delivery form.
Bad: the skills' seat-discipline text loses its standing enforcer —
accepted: the human is the gate in this flow, and the disciplines
remain stated inside the skill bodies where the agent reads them at
the moment they apply.
