# Conventions

A convention is a rule you may break only with a reason. Here each
one is two things, kept apart:

- **A manual**, `conventions/<name>/README.md`. What this is, how it
  works, why, with pointers to the decisions. Written for a person
  and for the maintainer. Never shipped, never loaded into an agent
  by default.
- **Its artifacts**: what a project actually holds. A skill file for
  a rule bound to a moment; stubs and templates for rules that ride
  in the files a project is born with. The rules live here, one
  sentence each. The artifacts are real files in the starter kit,
  `starter/kit/`, and each convention's directory links to its own
  beside the manual.

The kit is the master. Edit an artifact there and the links under
`conventions/` follow; this repo's own `.claude/skills/` holds
copies at a pin and takes the change at its next update, like any
project's (ADR-0041). The kit is copied whole into a new project,
as real files, which is why it has to be the origin (ADR-0040).

## The seven

| Convention | Manual | Artifacts |
|---|---|---|
| project-recording | [project-recording/](project-recording/) | the record stubs |
| commit-messages | [commit-messages/](commit-messages/) | a skill |
| repo-hygiene | [repo-hygiene/](repo-hygiene/) | the hygiene base; stack overlays stay here |
| artifact-kinds | [artifact-kinds/](artifact-kinds/) | a skill |
| change-plans | [change-plans/](change-plans/) | a skill |
| convention-lifecycle | [convention-lifecycle/](convention-lifecycle/) | a skill: the kit's protocol, receiver side |
| agent-arrangement | [agent-arrangement/](agent-arrangement/) | the entry-file and decisions-log stubs |

## A skill file

Opens with YAML frontmatter, which is what a skill loader reads:

```yaml
---
name: <the convention's name>
description: <when to read this file — the trigger>
requires: <conventions this one delegates to; omit if none>
---
```

- `description` says when to read the file, never what the rule is.
- `name` equals the directory name; registry entries and `requires`
  lines refer to the convention by it.
- `requires` names the conventions this one delegates rules to; a
  receiver lands a convention together with its chain.

## Writing an artifact

The reader is an agent in a project, holding a pinned copy and
opening it at the moment of use.

- A rule is one sentence in the imperative. Its why is the manual's
  or the ADR's.
- Cite no decision mid-sentence. A skill lists the decisions it
  rests on once, in a footer headed *Decisions*, each as
  `HANDBOOK ADR-nnnn`. A stub cites nothing.
- Say what a rule is not only when a consumer lived the misreading,
  and then name the run.
- A worked example in a code block is exempt from all of this.

The manual is free prose. It explains, points at the artifact and
the ADRs, and states no rule the artifact does not (ADR-0039).

## The kit's rules

- A convention entering or leaving the kit updates the file table
  and the shipped-conventions table in `starter/README.md`, and the
  birth entry in the kit's decisions-log stub, in the same commit.
- A citation in any shipped file is written `HANDBOOK ADR-nnnn`,
  since a bare number names the reading repo's own decision.
- Only `starter/kit/` is copied. Everything else under `starter/`
  is about the kit.

## Adding a convention

1. A directory `conventions/<name>/` with its `README.md`.
2. Its artifacts in the kit, and links to them from the directory.
3. An ADR for the decisions behind it.
4. A row in the table above and in the handbook README; the kit's
   tables and birth entry per the rules above.
5. A changelog entry prefixed with the convention name; a PLAN
   step, numbered by creation.
6. For a skill, this repo's own copy under `.claude/skills/` and a
   registry entry, landed as a first injection by
   convention-lifecycle §3, in its own agent-scoped commit
   (ADR-0041).
