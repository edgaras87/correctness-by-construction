# Commit plan: the agent's two texts checked against outside sources

## Summary — the state after all commits

The agent model and agent-arrangement agree with Claude Code's
documentation as of 2.1.310, and say where community practice and
measured studies support or doubt them.

- The model's §10 says when each file loads as the docs say it now:
  a path rule on Read, Write, Edit and a shell read of one file;
  `ask` still prompting in auto and bypass modes; a `Read` deny
  stopping simple shell reads. It adds what it lacked: nested
  `CLAUDE.md`, `AGENTS.md`, what compaction restores, what a
  subagent receives, skills' `paths:`, and that the tool ignores
  our `foundation` and `requires` fields.
- The model's §12 carries the outside evidence on A2, P1, P2 and G1.
- agent-arrangement §2 says what the entry file holds in the docs'
  terms, what every session needs, instead of "a map".
- TODO's item for the outside check closes.

## Commits

**0. `docs(agent): add commit plan for outside check`**
Opens the set.

**1. `docs: the agent model's §10 matches 2.1.310`**
The model's mechanism section, at its home, with each retelling of
when a path rule loads: agent-arrangement §3.2, conventions'
*Why it arrives this way*, writing's channel list. A new file's
first draft is still written without its rule, since the rule can
load only once the file is touched; those lines keep that effect.
One fact and its retellings, so one commit.

**2. `docs: agent model claims gain outside evidence`**
§12: A2, P1, P2 and G1 gain the docs and the studies, each marked
measured or reported; A2, P1 and P2 stay assumed for this repo,
since none was measured here. Its own commit: evidence, not
mechanism.

**3. `docs: the entry file holds what each session needs`**
agent-arrangement §2.1 and §2.2: "a map, not a rulebook" goes; what
the three tests of §2.4 already leave is said in the docs' terms.
§2.6 names the docs' 200 lines beside "a screen". §3.7 says outside
practice ignores the file, and why ours is tracked. A change of
stance, so its own commit.

**4. `chore(agent): the check and auto-run on loads`**
`.claude/rules/foundation-check.md`'s comment: a path rule loads on
the file tools and simple shell reads, never on a script's edit.
`.claude/approaches-on-trial/auto-run.md`: a `Read` deny stops
simple shell reads, not `grep -r` or a script. The agent's own
files, so a commit of their own.

**5. `docs: TODO's outside check of the agent closes`**
The item goes from `TODO.md`. The final records commit.

**6. `docs(agent): close commit plan for outside check`**
Deletes this file; the body says what diverged.

## Decisions taken inside this plan

- **Lines that state an effect stay.** "Loads when one is read, not
  while a new one is written", in shapes, conventions §3.3 and the
  two form rules, stays true: the first draft is written before any
  call can load the rule. Only lines that name the Read tool alone
  as the trigger change.
- **Docs and practice may differ, and both are said.** Bug reports
  show path rules failing to load as documented; this repo observed
  Read alone on 2.1.284, and a shell read loading one on 2.1.310.
  The model states the documented trigger and that it is
  unreliable.
- **No ADR.** No ADR decided "a map, not a rulebook"; the change of
  stance is recorded in commit 3's body, as commit-messages allows
  for a decision too small for one.
- **History stays:** the devlog, closed ADRs and
  `.claude/decisions.md`'s entries keep their words.
- **The devlog** is written at the session's end, with one line for
  each of the two readers sent out.
