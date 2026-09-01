# 0004. Executions live as content under executions/

Date: 2026-08-28
Status: Accepted (amended by ADR-0010, 2026-09-01: the executions'
home moved to `starter/bundle/`; all else stands)

## Context

The executions — two skills and a startup snippet, later the
practice executions — are what this repo delivers to run repos,
each pinned to a concept version. In the archive they shipped
inside a copy-me bundle laid out as a run repo expects them
(`.claude/skills/...`). Here they need a home, and the home decides
two things: whether this repo's own agent treats them as *its*
arrangement, and what a run birth copies.

## Options considered

1. Install them in this repo's `.claude/skills/` — the archive
   bundle's layout, kept. Rejected three ways: this repo never
   frames or slices itself, so the skills would be installed where
   they can only misfire (their ambient descriptions trigger on
   "design a backend"); content changes would land as agent-scoped
   commits, breaking the agent/project split's meaning; and the
   executions' lifecycle (re-derived on a concept bump) is content
   work, not arrangement work.
2. Mirror the bundle under `executions/.claude/skills/...` —
   verbatim-copy convenience, but a hidden dotdir inside content
   that no one browses, and it hard-codes one consumer layout into
   the tree. Install paths are documentation, not structure.
3. Flat content directory `executions/` at the repo root — chosen.

## Decision

Executions live under `executions/` at the repo root, flat:
`cbc-framing/` and `cbc-slice/` (each SKILL.md + references/), and
`cbc-startup-snippet.md`, alongside the mental layer they derive
from. They are content — the agent model's terms: in this repo they
are nothing but files; they become *installed* delivery only inside
a run repo.

Every execution file carries one header: the pin ("derives from
concept v1", ADR-0003) plus provenance. In SKILL.md files the
header sits below the YAML frontmatter so a verbatim copy into a
run repo's `.claude/skills/` still parses as a skill; the pin line
is phrased to stay true inside that copy.

Delivery to run repos is by copy at birth, directed by a bundle doc
(`executions/README.md`): what to copy, where each piece installs,
and the standing rule — this repo's copies are authoritative, a
run's copies are pinned. The doc sits with the executions because a
run birth starts by reading what it is about to copy (agent model
P2: placement decides firing).

## Consequences

Good: the repo's two layers are visible as two root directories;
this repo's sessions cannot invoke the executions by accident;
execution commits are project-scoped as they should be; the pin
travels with every copy.
Bad: a run birth is a mapping (executions/cbc-framing →
.claude/skills/cbc-framing), not a bare recursive copy — accepted,
the bundle doc states the mapping and a birth is deliberate work
anyway.
