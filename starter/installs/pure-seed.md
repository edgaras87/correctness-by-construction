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
     pacing. Run 1's straight-through walk stands as data.
     Seventh revision, 2026-09-07 (ADR-0018): the seed commits on
     a receipt branch, birth-seed, and main holds the same files
     untracked — the agent's first commit on main is its own, so
     the sequence and split the experiment measures are the
     agent's to choose for every delivered file, not only its
     additions; run 2's straddling-seed known issue never enters
     main. The prompt gains the one line that names the branch.
     Runs 1 and 2 were seeded on main; readings against them say
     so.
     Eighth revision, 2026-09-07 (ADR-0019): one optional step,
     the semi-pure delivery — the two fills written over the
     kit's entry stubs, headless, name filled, one more commit on
     the branch. ADR-0016's parking condition fired at run 2's
     Step 0 reading: two runs derived the entry files unaided and
     neither produced the pre-framing guard or the skills' pin
     stance. Run 3 runs with the step on; the prompt's situation
     sentence names the delivery. The manual's name stays —
     "pure" is the seed's nature, delivers and decides nothing;
     the switch delivers two more texts. -->

# Install: the pure seed — material only, the agent finishes

One idea: the seed delivers everything and decides nothing. Every
delivery is a commit on a receipt branch, `birth-seed`, so that
branch is the manifest — what arrived, from where, at which pin —
while main stays at the kit's hygiene commit with the same files
in its worktree, untracked: the newborn's agent finishes the birth
itself by reading what is there and committing it under its own
sequence and split (ADR-0018). The kit is
born per the handbook's pure install, which fills its own
mechanical birth fields; the seed also maps the playbook's steps
into PLAN and fills its "Steps from:" line — mechanical, from
the pins, matching the no-copy model (the newborn holds no
playbook file). Beyond those, no field is filled: not the other
stubs, not CLAUDE.md, no bundle birth entry. What the agent
cannot derive (the bundle pin) rides in the seed commits'
subjects; everything else it can.

Deliberately not delivered — nothing that encodes a prior run's
conclusions: the birth scenario, the birth fills, the pre-written
birth entries, and no playbook file — its steps ride in PLAN. The
agent meets the kit and the method raw. One exception, switched
on per run (step 4, ADR-0019): the two entry files written from
the fills — the harvest of the readings so far, delivered because
two runs showed it cannot be derived.

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

**3. Cut the receipt branch and commit the deliveries there, pins
in the subjects.** One commit per delivery; the subject is where
the agent later reads the pin. Main is left at the hygiene commit.

```bash
git switch -c birth-seed

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
git commit -m "chore: seed — the five CbC skills, pin @ $bundle_pin"

sed -i -e "/<!-- STEPS-BEGIN/r "<(echo; sed -n '/^## Step/,$p' \
    "$bundle_dir"/starter/fills/cbc-run-pure-playbook.md; echo) \
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

**4. Semi-pure, optional: write the two entry files from the
fills.** Each fill is cut from its title line down — the
provenance header stays in the concept repo — with
`<working-name>` filled by the placeholder directory name, and
written over the kit's stub. One commit, both files: the branch
is a receipt, never merged, so the newborn's commit split does not
govern it (ADR-0019). Skip this step for a pure run.

```bash
name=$(basename "$new_project_dir")
for f in claude-md-template:CLAUDE.md readme-md-template:README.md; do
  src=${f%%:*}; dst=${f##*:}
  sed -n '/^# <working-name>/,$p' "$bundle_dir"/starter/fills/"$src".md \
    | sed "s/<working-name>/$name/g" > "$dst"
done
git add CLAUDE.md README.md
git commit -m "chore: seed — entry files from the fills, pin @ $bundle_pin"
```

No other placeholder exists in either fill; nothing else is
filled. From this commit the two files are the newborn's own
(ADR-0017's fill rule): edited in place, never re-copied.

**5. Return to main and restore the branch tip into its worktree,
untracked.** The branch is never merged.

```bash
git switch main
git restore --source=birth-seed --worktree --staged -- .
git reset -q
```

The restore writes every file of the branch tip into main's
worktree and index; the reset empties the index again, so the
files stand untracked and main's log holds nothing but the
hygiene commit. Check it before firing: `git add -A && git diff
--cached --quiet birth-seed && git reset -q` prints nothing when
the worktree equals the branch tip.

**6. Fire the agent** — a fresh session in the newborn, never the
concept repo's, with this prompt and nothing more:

```text
This repo was seeded, not born whole — the branch birth-seed
shows it: the handbook's starter kit first (the container —
records, conventions, the entry file), then the
correctness-by-construction bundle (the method — docs/concept/,
five skills, the steps in PLAN), each seed commit naming its
source's pin. Main holds the same files, untracked, on top of the
kit's hygiene commit; the branch is a receipt, never merged. The
kit knows nothing of the method; the bundle presumes the
container. Your
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

With the semi-pure step on, the parenthetical naming the bundle
reads instead: "(the method — docs/concept/, five skills, the
steps in PLAN, and the two entry files, CLAUDE.md and README.md,
written filled from the bundle's fills)". Nothing else in the
prompt changes: what the agent does with delivered entry files is
its own choice, and that choice is the reading's object.

The prompt is the session channel — it carries what is true only
of this moment: the situation (two sources, why split, the branch
that holds them — deletable, never merged, session-shaped truth),
the task, the read-everything instruction, the expectation of a
plan, and the review protocol. That last is session truth like the rest —
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

- Five commits on birth-seed above the hygiene commit — six with
  the semi-pure step on; main at the hygiene commit, its log
  holding nothing else; main's worktree byte-identical to the
  branch tip, every delivered file listed untracked by
  `git status` (the check in step 5 prints nothing).
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
  stub still reads as a stub, and no bundle birth entry exists.
  CLAUDE.md carries no content beyond the kit's — unless the
  semi-pure step ran, in which case CLAUDE.md and README.md are
  byte-identical to their fills from the title line down with
  the name filled, and neither carries a provenance header.
- Nothing from the excluded list present: no birth-scenario.md,
  no birth-fill content, no bundle birth entry; no fill's header
  in the newborn.

What the agent is left to do — the reader's checklist for the
reading afterwards, not instructions delivered to it: every
delivered file committed on main by the agent, under its own
sequence and the commit split the skills define (an add-all in
one commit is an outcome the reading records, not one the seed
prevents); a change-plan whose commit sequence is chosen and
justified (the entrance doc's place in it, when records enter
history and how far they adapt to the method, whether skills land
whole or split by source); its own CLAUDE.md; the record stubs filled; the
bundle's birth entry reconstructed from the seed subjects (the
kit's is filled at birth); Step 0 closed clean on its container
gates — no briefing gate exists to block it, the briefing opens
Framing; the agent/project commit split held throughout, from
the skills, unprompted.

The reading is the concept repo's act, read-only, recorded there:
the derived arrangement against the walk-1 baseline and the
shipped template, the order chosen, the misses.
