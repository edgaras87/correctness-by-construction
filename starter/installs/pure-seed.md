<!-- The procedure of record: ADR-0016 (2026-09-06) adopted the
     pure shape and cancelled the assembly walk — this manual is
     the birth procedure (born 2026-09-05 as the pure-seed
     experiment; TODO's Now item is the protocol). Authored from
     the lived run, not before it — the script this generalizes
     seeded ~/IdeaProjects/cbc-pure-run.
     Revised same day, before any walk: the kit half defers to the
     handbook's pure install by pointer, its fills included — the
     seeded run-1 repo predates this and holds the kit raw; a
     divergence for the reading, not a defect.
     Revised again same day: the playbook is not delivered as a
     file — the seed inserts its steps into PLAN and fills the
     "Steps from:" line, matching the adopted no-copy model. The
     does-the-agent-find-the-mapping observation is deliberately
     given away; the run walked is reseeded to this shape.
     Third revision, same day: the insert omits the playbook's
     (CbC) Step 0 comment — it encodes the assembly conclusions
     (shipped template, three commits, no change-plan, the
     scenario pointer) that this experiment withholds, and in a
     run without them it lies.
     Fourth revision, same day, user's call: the filter becomes
     an artifact — the insert reads cbc-run-pure-playbook.md
     verbatim, the pure-seed candidate variant (its header
     states the deltas and its lifespan: the experiment's
     reading keeps one of variant and parent, deletes the
     other). Staged changes over scripted-out parts.
     Fifth revision, same day, user's design — the channel
     split: session-scoped text moves to the firing prompt
     (situation, task, read-everything, the plan expectation),
     PLAN keeps only project truth — the variant's Step 0 is
     pure container prep, its agent-side gates gone to the
     prompt and the run's own change-plan, and the briefing
     moves from Step 0's gates to Framing's starting input, so
     Step 0 closes clean. The measured object is now assembly
     judgment: the commit sequence the agent chooses and
     justifies, not discovery from nothing.
     Sixth revision, 2026-09-06, after run 1: the prompt gains
     the review protocol — the plan staged and approved before
     it commits, then step by step, each step staged, shown, and
     committed only on the reviewer's word. Run 1 ran straight
     through: change-plans §6 assumes a reviewer nothing had
     established, and a file-level "stop" loses to the harness's
     finish-the-task pressure — not silently: the agent saw §6,
     recorded the deviation in its plan, and justified it by an
     instruction the prompt never gave ("instructed to finish
     unattended"), the harness voice heard as the user's. The reviewer's presence is
     session truth — the channel split's own logic, applied to
     pacing. Run 1's straight-through walk stands as data. -->

# Install: the pure seed — material only, the agent finishes

One idea: the seed delivers everything and decides nothing. Every
delivery is a commit on main, so the history is the manifest —
what arrived, from where, at which pin — and the newborn's agent
finishes the birth itself by reading what is there. The kit is
born per the handbook's pure install, which fills its own
mechanical birth fields; the seed also maps the playbook's steps
into PLAN and fills its "Steps from:" line — mechanical, from
the pins, matching the no-copy model (the newborn holds no
playbook file). Beyond those, no field is filled: not the other
stubs, not CLAUDE.md, no bundle birth entry. What the agent
cannot derive (the bundle pin) rides in the seed commits'
subjects; everything else it can.

Deliberately not delivered — nothing that encodes a prior run's
conclusions: the birth scenario, the CLAUDE.md template, the
birth fills, the pre-written birth entries, and no playbook
file — its steps ride in PLAN. The agent meets the kit and the
method raw.

**1. Set the paths and capture the pins.**

```bash
new_project_dir=~/IdeaProjects/<placeholder-name>
handbook_dir=~/PycharmProjects/engineering/engineering-handbook
bundle_dir=~/PycharmProjects/engineering/concept-garden/correctness-by-construction

kit_pin=$(git -C "$handbook_dir" rev-parse --short HEAD)
bundle_pin=$(git -C "$bundle_dir" rev-parse --short HEAD)
```

The name is a placeholder — everything before the briefing is
problem-agnostic, and the briefing brings the real name.

**2. Kit birth per the handbook's pure install manual**
(`engineering-handbook/starter/installs/pure.md`), through its
hygiene commit — by pointer, no step of that manual restated
here. Its blocks use the same `handbook_dir` / `new_project_dir`
variables, same terminal session. Its fills run as written: the
kit's birth entry pin, the three birth dates, the TEMPLATE
marker stripped — seed-mechanical, the kit's own.

**3. Commit the deliveries, pins in the subjects.** One commit per
delivery; the subject is where the agent later reads the pin.

```bash
git add -A
git commit -m "chore: seed — kit remainder, pin @ $kit_pin"

mkdir -p docs/concept
cp "$bundle_dir"/concept/*.md docs/concept/
git add docs/concept
git commit -m "chore: seed — concept/ from the bundle, pin @ $bundle_pin"

mkdir -p .claude/skills
for s in cbc-framing cbc-slice infra-establish infra-serve cbc-bootstrap; do
  cp -r "$bundle_dir"/starter/bundle/"$s" .claude/skills/
done
git add .claude/skills
git commit -m "chore: seed — the five CbC skills"

sed -i -e "/<!-- STEPS-BEGIN/r "<(echo; sed -n '/^## Step/,$p' \
    "$bundle_dir"/starter/bundle/cbc-run-pure-playbook.md; echo) \
    -e '/<!-- STEPS-BEGIN/,/<!-- STEPS-END/{/STEPS-BEGIN/b;/STEPS-END/b;d}' \
    PLAN.md
sed -i "s|<playbook> v<N> at <handbook or concept commit>|cbc-run-pure v4 at $bundle_pin|" \
    PLAN.md
git add PLAN.md
git commit -m "chore: seed — steps into PLAN, cbc-run-pure v4 @ $bundle_pin"
```

The first sed is the kit's marker-keeping swap — the steps land
between the STEPS markers and the markers stay; the second fills
the "Steps from:" comment's placeholder in place, as its own text
sanctions. Both are re-runnable.

The source is cbc-run-pure-playbook.md, the candidate variant,
read verbatim — no filter rides the insert. What the variant
omits against its parent (the assembly Step 0 comment, the
install-manual clause) and why is its own header's to say; this
manual delivers what the master holds, like every other seed
step. The kit's first-session comment and Framing's (CbC)
comment ride in with the steps: container orientation and a
pointer to a delivered skill, no conclusions.

**4. Fire the agent** — a fresh session in the newborn, never the
concept repo's, with this prompt and nothing more:

```text
This repo was seeded, not born whole — the commit history shows
it: the handbook's starter kit first (the container — records,
conventions, the entry file), then the correctness-by-construction
bundle (the method — docs/concept/, five skills, the steps in
PLAN), each seed commit naming its source's pin. The kit knows
nothing of the method; the bundle presumes the container. Your
task is to finish the birth: assemble what was delivered into a
working project — your own arrangement, the records, PLAN's
Step 0 closed on its gates. Read the whole repository first,
every file and every seed commit. Then plan the work as the
conventions you were given direct — your own commit sequence,
your own order of artifacts, split by the commit scopes the
skills define, each choice one you can justify in the plan.
I am the reviewer the change-plans convention names, and the
work moves at my pace: stage the plan and ask for my approval
before committing it; then one step at a time — stage a step,
show me what changed, and commit only on my word, staging the
next step after each approval.
Work only within this repository — the source repos the pins
name are not yours to read. The problem arrives later, as a
briefing that opens Framing; nothing before it names the
problem.
```

The prompt is the session channel — it carries what is true only
of this moment: the situation (two sources, why split), the task,
the read-everything instruction, the expectation of a plan, and
the review protocol. That last is session truth like the rest —
a reviewer is present *this run* — and run 1 showed the delivered
convention cannot establish it alone: its §6 names "the reviewer"
but a file-level stop loses to the harness's finish-the-task
pressure when no voice above the file confirms anyone is
watching. Pacing is not a measured object, so the lines leak
nothing. PLAN carries only what stays true of the project. What the prompt
deliberately never says: any order, any answer to which records
to touch or how far to adapt them, whether skills land as one
commit or split by source — the sequence the agent chooses and
justifies is the run's central data. The commit-scope rule is not
restated; it rides in the delivered skills, and the prompt only
points at them. The stay-inside line guards the blindness: the
source repos hold the answer sheet (the template, the scenario,
the baselines), and the permission prompt on any outside read is
the human's hard backstop behind it.

**A correct seed is checkable** — before the agent starts, every
item is a verifiable fact:

- Five commits on main, no other branch; the tree clean.
- Every bundle copy byte-identical to its master at the subject's
  pin: the concept chapters, the five skills.
- PLAN's STEPS region holds the pure variant's sequence —
  identical to cbc-run-pure-playbook.md from its first step down
  at the subject's pin — both markers in place, and the "Steps
  from:" comment names cbc-run-pure v4 at the bundle pin. No
  playbook file exists, and no line of the region states an
  assembly conclusion.
- The kit's own birth fills are done, per pure.md: the birth
  entry's pin and date, ADR-0001's date, the devlog heading, the
  TEMPLATE marker gone. Beyond them, nothing is filled: every
  stub still reads as a stub, CLAUDE.md carries no content
  beyond the kit's, and no bundle birth entry exists.
- Nothing from the excluded list present: no birth-scenario.md, no
  CLAUDE.md template, no birth-fill content, no bundle birth
  entry.

What the agent is left to do — the reader's checklist for the
reading afterwards, not instructions delivered to it: a
change-plan whose commit sequence is chosen and justified (the
entrance doc's place in it, when records enter history and how
far they adapt to the method, whether skills land whole or split
by source); its own CLAUDE.md; the record stubs filled; the
bundle's birth entry reconstructed from the seed subjects (the
kit's is filled at birth); Step 0 closed clean on its container
gates — no briefing gate exists to block it, the briefing opens
Framing; the agent/project commit split held throughout, from
the skills, unprompted.

The reading is the concept repo's act, read-only, recorded there:
the derived arrangement against the walk-1 baseline and the
shipped template, the order chosen, the misses.
