<!-- Split from the bundle doc 2026-09-01 (ADR-0010): the Birth
     section, now the install manual — peer of the handbook's
     starter/installs/default.md. The describing side is
     starter/README.md. -->

# Install: correctness by construction

**In trial:** the next birth walks `starter/bundle/birth-scenario.md` —
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
2. Copy this bundle per the starter README's table (`starter/README.md`).
3. Replace the plan's STEPS region with the playbook's sequence —
   the handbook's mechanism (their ADR-0028), run against our
   playbook. The manual carrying their block
   (their `starter/installs/default.md`) is the one this file replaces, so the
   block lives here too; the paths are pure.md's, same terminal
   session:

   ```bash
   sed -i -e "/<!-- STEPS-BEGIN/r "<(sed -n '/^## Step/,$p' \
       "$new_project_dir"/playbooks/cbc-run.md) \
       -e '/<!-- STEPS-BEGIN/,/STEPS-END -->/d' \
       "$new_project_dir"/PLAN.md
   ```

   The inner sed keeps everything from the first step down; the
   outer swaps the marker region for it. Markers, not line
   numbers — re-running is harmless. Then fill the plan's "Steps
   from:" line from the playbook's own version line. The copy
   source is the newborn's `playbooks/cbc-run.md`, landed at
   step 2; the kit's own playbooks stay in `playbooks/`,
   uncopied — a CbC birth chooses cbc-run.md (ADR-0011).
4. Append the bundle's birth entry to `.claude/decisions.md`,
   beside the kit's: the date, this repo's commit at copy time,
   "pinned to concept v1". Mechanical, done at copy time like the
   kit's own pin fill — never left for the born agent to remember.
5. Run the plan's Step 0 (bootstrap) as it directs. CLAUDE.md's
   CbC section is the newborn's own writing at this step — derived
   from `concept/`, no text supplied by the bundle (ADR-0012). The
   bundle files need no Step 0 decisions of their own: the kit's
   commit-messages rule already scopes them — the skills and every
   CLAUDE.md edit are arrangement (agent commits); `concept/` and
   `playbooks/cbc-run.md` are project content and land with the
   records. State this in the Step 0 change-plan; do not re-derive
   it per birth.
6. At Framing, the step's gates are met *via* cbc-framing — the
   intent, definition, and registry are the problem statement,
   success criteria, and out-of-scope in the method's richer form —
   and the middle-steps gate item is confirmation, not authoring:
   the steps came whole into PLAN.md at step 3; confirm them
   against the framed problem.

A correct birth is checkable, not judged — after Step 0 closes,
every item below is a verifiable fact:

- `concept/`, the five skills, and `playbooks/cbc-run.md` present
  and byte-identical to this repo's masters at the pinned commit.
- PLAN.md's STEPS region holds the playbook's full sequence
  (Step 0 through Step N, no marker left), and the "Steps from:"
  line names `playbooks/cbc-run.md` at the copied version.
- CLAUDE.md's CbC section is the newborn's own — derived at
  Step 0 from `concept/`, no text merged in at copy time
  (ADR-0012).
- `.claude/decisions.md` carries both birth entries: the kit's
  (handbook commit) and the bundle's (this repo's commit, concept
  v1).
- No commit mixes bundle arrangement files with project records
  (the kit's split, held for bundle files too).
- No bundle file was edited at copy — a run's copies change only
  by re-copy from here, or by a fix its own records state
  (ADR-0007).
