# Install: the pure seed — material only, the agent finishes

The birth procedure of record (ADR-0016). One idea: the seed
delivers everything and decides nothing. Every delivery is a commit
on a receipt branch, `birth-seed`, so that branch is the manifest —
what arrived, from where, at which pin — while main stays at the
hygiene commit with the same files in its worktree, untracked: the
newborn's agent finishes the birth itself by reading what is there
and committing it under its own sequence and split (ADR-0018). The
container comes from `delivery/container/`, this repo's (ADR-0024,
ADR-0025), and the seed fills only what is mechanical: the birth
entry's pin and date, two other birth dates, the working name in the
two entry files, and the playbook's steps into PLAN with its "Steps
from:" line. Beyond those, no field is filled: not the other stubs,
no bundle birth entry. What the agent cannot derive rides in the
seed commits' subjects; everything else it can.

Deliberately not delivered: nothing that encodes a prior run's
conclusions, and no playbook file — its steps ride in PLAN. The
agent meets the container and the method raw. One exception: the
two entry files arrive composed, in the kit itself, because runs
that derived their own produced neither the pre-framing guard nor
the pin stance (ADR-0019, ADR-0024).

**1. Set the paths and capture the pin.**

```bash
new_project_dir=~/IdeaProjects/<placeholder-name>
bundle_dir=~/PycharmProjects/engineering/concept-garden/correctness-by-construction

bundle_pin=$(git -C "$bundle_dir" rev-parse --short HEAD)
```

One pin, ours, and one directory: everything the seed copies is
under `$bundle_dir`, and a run is born from this repo alone.

The name is a placeholder — everything before the briefing is
problem-agnostic, and the briefing brings the real name.

**2. Copy the kit.**

```bash
mkdir -p "$new_project_dir"
cp -r "$bundle_dir"/delivery/container/. "$new_project_dir"/
sed -i -e "s/<bundle-commit>/$bundle_pin/" \
    -e "s/<YYYY-MM-DD> Born/$(date +%F) Born/" \
    "$new_project_dir"/.claude/decisions.md
sed -i "s/^Date: <YYYY-MM-DD>/Date: $(date +%F)/" \
    "$new_project_dir"/docs/adr/0001-record-architecture-decisions.md
sed -i "s/^## <YYYY-MM-DD>/## $(date +%F)/" \
    "$new_project_dir"/devlog/devlog.md
name=$(basename "$new_project_dir")
sed -i "s/<working-name>/$name/g" \
    "$new_project_dir"/.claude/CLAUDE.md "$new_project_dir"/README.md
```

The trailing `/.` matters: `delivery/container/*` silently skips the
dotfiles — `.gitignore`, `.gitattributes`, `.editorconfig` — and
the whole `.claude/` directory.

The birth entry takes two placeholders: the pin, for what was
delivered, and the date. Its read-through is written as *none* in
the template — nothing has been read before the first note — and
the seed leaves it. One pin, because the run holds one delivery
(ADR-0025, ADR-0036). The next two `sed`s fill the
other birth dates the kit carries, the first ADR's and the devlog's
first heading: three records, one moment. The last fills the working
name into the two entry files, which arrive inside the kit rather
than being written over stubs. Every `sed` targets a placeholder and
not a line number, so re-running the block is harmless. Installing
by hand, fill the five placeholders yourself before the agent's
first session.

**3. Create the repo and land the hygiene commit** — verbatim, the
same in every project, because the hygiene base carries no
per-project content:

```bash
cd "$new_project_dir"
git init
git branch -M main
git add .gitignore .gitattributes .editorconfig
git commit -m "chore: add repo hygiene base"
```

**4. Cut the receipt branch and commit the deliveries there, the
pin in the subjects.** One commit per delivery; the subject is where
the agent later reads the pin. Main is left at the hygiene commit.

```bash
git switch -c birth-seed

git add -A
git commit -m "chore: seed — kit remainder, pin @ $bundle_pin"

mkdir -p docs/concept
cp "$bundle_dir"/concept/*.md docs/concept/
git add docs/concept
git commit -m "chore: seed — concept/ from the bundle, pin @ $bundle_pin"

# The groups this run takes, on top of the container that step 2
# copied. Each group is a piece of the run's tree, so copying it in
# place is the whole of the mapping (ADR-0036). This run is
# Spring and PostgreSQL; a run on another stack names method alone
# and is born with two skills, not five (ADR-0029).
for g in method spring-postgres; do
  cp -r "$bundle_dir"/delivery/$g/. .
done
git add .claude/skills
git commit -m "chore: seed — the method and stack groups, pin @ $bundle_pin"

sed -i -e "/<!-- STEPS-BEGIN/r "<(echo; sed -n '/^## Step/,$p' \
    "$bundle_dir"/delivery/fills/cbc-run-pure-playbook.md; echo) \
    -e '/<!-- STEPS-BEGIN/,/<!-- STEPS-END/{/STEPS-BEGIN/b;/STEPS-END/b;d}' \
    PLAN.md
sed -i "s|<playbook> v<N> at <concept commit>|cbc-run-pure v7 at $bundle_pin|" \
    PLAN.md
git add PLAN.md
git commit -m "chore: seed — steps into PLAN, cbc-run-pure v7 @ $bundle_pin"
```

One pin in every subject, ours: the container arrives inside the
delivery rather than beside it, and where it began is ADR-0025's,
not a number the newborn holds.

The first sed is the kit's marker-keeping swap — the steps land
between the STEPS markers and the markers stay; the second fills
the "Steps from:" comment's placeholder in place, as its own text
sanctions. Both are re-runnable.

The source is `delivery/fills/cbc-run-pure-playbook.md`, read
verbatim — no filter rides the insert; this manual delivers what the
master holds, like every other seed step. Framing's (CbC) comment
rides in with the steps: where the briefing lands, no conclusions.

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
--cached --stat birth-seed; git reset -q` lists every file that
differs from the branch tip, so it lists nothing when the worktree
equals it, and it empties the index either way.

**6. Fire the agent** — a fresh session in the newborn, never the
concept repo's, with this prompt and nothing more:

```text
This repo was seeded, not born whole — the branch birth-seed
shows it: one delivery from the correctness-by-construction
bundle, its container half first (the records, the conventions,
the two entry files) and its method half after (docs/concept/,
five skills, the steps in PLAN), every seed commit naming that
one pin. Main holds the same files, untracked, on top of the
hygiene commit; the branch is a receipt, never merged. Your
task is to finish the birth: assemble what was delivered into a
working project — your own arrangement, the records, PLAN's
Step 0 closed on its gates. Read the whole repository first,
every file and every seed commit. Then plan the work as the
conventions you were given direct — your own commit sequence,
your own order of artifacts, split by the commit scopes the
skills define, each choice one you can justify in the plan.
I am the reviewer the commit-plan convention names, and the
work moves at my pace: stage the plan and ask for my approval
before committing it; then one step at a time — stage a step,
show me what changed, and commit only on my word, staging the
next step after each approval.
Work only within this repository — the repo the delivery came
from is not yours to read. The problem arrives later, as a
briefing that opens Framing; nothing before it names the
problem.
```

What the agent does with the delivered entry files stays its own
choice, and that choice is the reading's object.

The prompt is the session channel — it carries what is true only of
this moment: the situation (one delivery in two halves, the branch
that holds them — deletable, never merged, session-shaped truth),
the task, the read-everything instruction, the expectation of a
plan, and the review protocol. That last is session truth like the
rest — a reviewer is present *this run* — and a stop written only in
a file loses to the harness's pressure to finish when no voice above
the file says anyone is watching (devlog 2026-09-06, "the pure seed
runs"). Pacing is not a measured object, so the lines leak nothing.
PLAN carries only what stays true of the project. What the prompt
deliberately never says: any order, any answer to which records to
touch or how far to adapt them, whether skills land as one commit or
split by source — the sequence the agent chooses and justifies is
the run's central data. The commit-scope rule is not restated; it
rides in the delivered skills, and the prompt only points at them.
The stay-inside line guards the blindness: this repo holds the
answer sheet, `docs/baselines/`, and the permission prompt on any
outside read is the human's hard backstop behind it.

Anything said to the newborn after this prompt, at a review stop or
in an answer, is told text, held to the note's rules
(`docs/conventions/exchange/` §3.7). One case is the birth's own: a
newborn holds no earlier state, so it cannot check "this changed
since" — the claim has nothing to land on. Such a claim says so, in
a clause.

**A correct seed is checkable** — before the agent starts, every
item is a verifiable fact:

- Four commits on birth-seed above the hygiene commit: the kit
  remainder, the concept chapters, the method and stack groups,
  the steps into PLAN. Main at the hygiene commit, its log
  holding nothing else; main's worktree byte-identical to the
  branch tip, every delivered file listed untracked by
  `git status` (the check in step 5 lists nothing).
- Every bundle copy byte-identical to its master at the subject's
  pin: the concept chapters, the five skills.
- PLAN's STEPS region holds the pure playbook's sequence —
  identical to cbc-run-pure-playbook.md from its first step down
  at the subject's pin — both markers in place, and the "Steps
  from:" comment names cbc-run-pure v7 at the bundle pin. No
  playbook file exists, and no line of the region states an
  assembly conclusion.
- The five birth placeholders are filled and no more: the birth
  entry's pin and date, ADR-0001's date, the devlog heading,
  and the working name in the two entry files. Every other stub
  still reads as a stub, and no bundle birth entry exists.
  `.claude/CLAUDE.md` and `README.md` are byte-identical to the
  kit's with the name filled, neither carries a provenance
  header, and no `CLAUDE.md` sits at the root.
- No provenance header from this repo anywhere in the newborn.

What the agent is left to do — the reader's checklist for the
reading afterwards, not instructions delivered to it: every
delivered file committed on main by the agent, under its own
sequence and the commit split the skills define (an add-all in
one commit is an outcome the reading records, not one the seed
prevents); a commit plan whose sequence is chosen and
justified (the entrance doc's place in it, when records enter
history and how far they adapt to the method, whether skills land
whole or split by source); the record stubs filled; Step 0 closed
clean on its container gates — no briefing gate exists to block
it, the briefing opens Framing; the agent/project commit split
held throughout, from the skills, unprompted.

The reading is the concept repo's act, read-only, recorded there:
the derived arrangement against the walk-1 baseline and the
shipped template, the order chosen, the misses.
