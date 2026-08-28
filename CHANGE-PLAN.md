# Change-plan: executions land (PLAN Step 3)

## Summary — the state after all commits

The executions layer exists: cbc-framing (SKILL.md + three
references), cbc-slice (SKILL.md + three references), and the
startup snippet live under `executions/` at the repo root, each file
under a header stating "derives from concept v1" plus provenance
(source path, archive commit `fe0075d`, changes on import).
ADR-0004 records why they live there and how run repos consume them;
`executions/README.md` is the bundle doc — what a run repo copies at
birth and where each piece installs. ARCHITECTURE gains the
executions component, a codemap row, and the version-pinning
invariant. Step 3 is closed and Step 4 detailed. From this point a
run can be born from this repo's copies, not the archive's.

## Commits

**1. `docs(agent): add change-plan for executions import`**
The approved plan, committed before work.

**2. `docs(adr): decide executions home and delivery`**
ADR-0004 alone, committed before the placement it governs — the
same decision-before-work pattern as the change-plan itself.
Decides: `executions/` at the repo root as content (this repo never
runs cbc-framing on itself), flat layout, per-file pin headers, and
delivery to run repos by copy per a bundle doc. Rejected options in
the ADR (see Decisions below).

**3. `docs(executions): import executions from archive`**
The nine files: `executions/cbc-framing/` (SKILL.md,
references/cbc-framing-workflow.md, worked-example.md,
the-whole-system-in-plain.md), `executions/cbc-slice/` (SKILL.md,
references/cbc-slice-workflow.md, worked-example.md,
system-readiness.md), `executions/cbc-startup-snippet.md`. Verbatim
below headers unless the close read finds a defect — any fix named
in the header, never silently absorbed. Same discipline and header
shape as Step 2, plus the pin line.

**4. `docs(executions): add bundle doc for run births`**
`executions/README.md`, adapted from the archive birth-materials
README (with its own provenance header naming the adaptation): what
a run repo copies at birth — `concept/`, the two skills into
`.claude/skills/`, the snippet merged into the run's CLAUDE.md then
deleted — and the standing rule stated once: this repo's copies are
authoritative; a run's copies are pinned. Separate from commit 3 so
the import stays a pure copy; reverting this commit alone leaves a
coherent repo.

**5. `docs: add executions layer to architecture`**
Components gains the executions layer (`executions/`); the
"arrives Steps 3–4" note narrows to Step 4's practice executions.
Codemap gains the `executions/` row. Invariants gains: an execution
never lands without stating its concept version — enforced in each
file's pin header, which travels with every copy.

**6. `docs: close Step 3 in PLAN, detail Step 4`**
Gate items checked with the facts that make them true; Step 4
detailed per rolling wave (infra-establish + infra-serve,
cbc-bootstrap, problem-framer/ stays out); Decision index gains
ADR-0004; TODO's Step 3 line triaged out.

**7. `docs(agent): close change-plan for executions import`**
Deletes this file; body is the retrospective.

## Decisions taken inside this plan

- **Home: `executions/` at the repo root, flat** —
  `cbc-framing/`, `cbc-slice/`, `cbc-startup-snippet.md`. Rejected:
  `.claude/skills/` (would install them into *this* repo's working
  arrangement — this repo never frames or slices itself, the
  ambient skill descriptions could misfire here, and the
  agent/project commit split would misclassify content commits as
  agent-scoped); a mirrored `executions/.claude/skills/` bundle
  layout (hidden dotdir inside content; install paths are the
  bundle doc's job, not the tree's).
- **Pin + provenance is one header per file.** In SKILL.md files it
  sits *below* the YAML frontmatter, so a verbatim copy into a run
  repo still parses as a skill; reference files carry it at the
  top as usual. The pin line ("derives from concept v1") is phrased
  to stay true inside a run-repo copy; the authoritative-vs-pinned
  rule lives once in the bundle doc, not in every header.
- **The bundle doc is `executions/README.md`** — a run birth starts
  by reading the executions it is about to copy, so the doc sits
  where that look lands (agent model P2: placement decides firing).
  It replaces the archive birth-materials README, which is not
  imported as-is.
- **Verbatim-unless-defect, same as Step 2.** Noted from the close
  read so far: the skills' backend-oriented trigger wording is the
  executions' own scoping, not a defect — imported as-is.
