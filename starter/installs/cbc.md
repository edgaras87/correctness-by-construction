<!-- Split from the bundle doc 2026-09-01 (ADR-0010): the Birth
     section, now the install manual — peer of the handbook's
     starter/installs/default.md. The describing side is
     ../README.md. -->

# Install: correctness by construction

**In trial:** the next birth walks `../bundle/birth-scenario.md` —
a draft reordering this procedure (seed, a newborn-walked
introduction, briefing last). This manual stays the procedure of
record until the trial closes in adoption; divergences land in the
devlog.

A run repo is born in two copies: the handbook's starter kit
(`engineering-handbook/starter/kit/`) supplies the container, this
bundle overlays the method (ADR-0009). The sequence:

1. Copy the kit per the handbook's pure install manual
   (`engineering-handbook/starter/installs/pure.md`) — repo,
   hygiene, records, the PLAN stub.
2. Copy this bundle per the starter README's table (`../README.md`).
3. Merge `cbc-startup-snippet.md` into the run's CLAUDE.md and
   delete the copy — the stub agent is now the CbC project agent.
4. Append the bundle's birth entry to `.claude/decisions.md`,
   beside the kit's: the date, this repo's commit at copy time,
   "pinned to concept v1". Mechanical, done at copy time like the
   kit's own pin fill — never left for the born agent to remember.
5. Run the stub's Step 0 (bootstrap) as the kit directs. The
   bundle files need no Step 0 decisions of their own: the kit's
   commit-messages rule already scopes them — the skills and
   CLAUDE.md's merged section are arrangement (agent commits);
   `concept/` and `playbooks/cbc-run.md` are project content and
   land with the records. State this in the Step 0 change-plan;
   do not re-derive it per birth.
6. At Framing, the step's gates are met *via* cbc-framing — the
   intent, definition, and registry are the problem statement,
   success criteria, and out-of-scope in the method's richer form —
   and the middle-steps gate item is where the playbook's steps are
   copied into PLAN.md and renumbered.

A correct birth is checkable, not judged — after Step 0 closes,
every item below is a verifiable fact:

- `concept/`, the five skills, and `playbooks/cbc-run.md` present
  and byte-identical to this repo's masters at the pinned commit.
- CLAUDE.md carries the snippet's content with its pin comment;
  the snippet copy is deleted.
- `.claude/decisions.md` carries both birth entries: the kit's
  (handbook commit) and the bundle's (this repo's commit, concept
  v1).
- No commit mixes bundle arrangement files with project records
  (the kit's split, held for bundle files too).
- No bundle file was edited at copy — a run's copies change only
  by re-copy from here, or by a fix its own records state
  (ADR-0007).
