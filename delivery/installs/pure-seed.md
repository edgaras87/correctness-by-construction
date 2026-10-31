# Install: the Pure Seed — material only, the agent finishes

The birth procedure of record (ADR-0016). One idea: the Pure Seed
delivers everything and decides nothing. Every delivery is a commit
on a receipt branch, `birth-seed`, so that branch is the manifest —
what arrived, from where, at which Delivery Pin — while main stays at the
hygiene commit with the same files in its worktree, untracked: the
newborn's agent finishes the birth itself by reading what is there
and committing it under its own sequence and split (ADR-0018). The
container comes from `delivery/container/`, this repo's (ADR-0024,
ADR-0025), and the Pure Seed fills only what is mechanical: the birth
entry's Delivery Pin and date, two other birth dates, the working name in the
two entry files, and the playbook's Plan Steps into PLAN with its "Steps
from:" line. Beyond those, no field is filled: not the other Record Stubs,
no bundle birth entry. What the agent cannot derive rides in the
seed commits' subjects; everything else it can.

Deliberately not delivered: nothing that encodes a prior CBC Run's
conclusions, and no playbook file — its Plan Steps ride in PLAN. The
agent meets the container and the method raw. One exception: the
two entry files arrive composed, in the container itself, because
they hold two stances a CBC Run can only receive, the pre-framing guard
and the pin stance: nothing it does before the Run Briefing produces
them (ADR-0019, ADR-0024).

**1. Set the paths and capture the Delivery Pin.**

```bash
new_project_dir=~/IdeaProjects/<placeholder-name>
bundle_dir=~/PycharmProjects/engineering/concept-garden/correctness-by-construction

bundle_pin=$(git -C "$bundle_dir" rev-parse --short HEAD)
```

One Delivery Pin, ours, and one directory: everything the Pure Seed copies is
under `$bundle_dir`, and a CBC Run is born from this repo alone.

The name is a placeholder — everything before the Run Briefing is
problem-agnostic, and the Run Briefing brings the real name.

**2. Copy the container.**

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
(cd "$new_project_dir" && find .claude/skills .claude/rules .claude/shapes .claude/approaches-on-trial \
  -name '*.md' -exec python3 -c '
import re, sys
for p in sys.argv[1:]:
    t = open(p, encoding="utf-8").read()
    n = re.sub(r"\n+---\n+## Decisions\n.*\Z", "\n", t, flags=re.S)
    if n != t: open(p, "w", encoding="utf-8").write(n)
' {} + 2>/dev/null)
```

The trailing `/.` matters: `delivery/container/*` silently skips the
dotfiles — `.gitignore`, `.gitattributes`, `.editorconfig` — and
the whole `.claude/` directory.

The birth entry takes two placeholders: the Delivery Pin, for what was
delivered, and the date. Its Read-Through Commit is written as *none* in
the Record Stub — nothing has been read before the first Delivery Note — and
the Pure Seed leaves it. One Delivery Pin, because the CBC Run holds one delivery
(ADR-0025, ADR-0036). The next two `sed`s fill the other birth
dates the container carries, the first ADR's and the devlog's
first heading: three records, one moment. The last fills the
working name into the two entry files, which arrive inside the
container rather than being written over Record Stubs. Every `sed`
targets a placeholder and not a line number, so re-running the
block is harmless. The last command strips every copy's *Decisions*
footer, which cites decisions the CBC Run cannot open; it cuts the
`---` line and the section below it, and nothing else
(`docs/conventions/exchange/` §3.8, *The footer at delivery*). Installing by hand, fill the five placeholders
yourself before the agent's first session.

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
Delivery Pin in the subjects.** One commit per delivery; the subject is where
the agent later reads the Delivery Pin. Main is left at the hygiene commit.

```bash
git switch -c birth-seed

git add -A
git commit -m "chore: seed — records and conventions, pin @ $bundle_pin"

# concept/ lands at docs/concept/, the mapping's one exception
# (docs/conventions/exchange/ §3.3).
mkdir -p docs/concept
cp "$bundle_dir"/concept/*.md docs/concept/
git add docs/concept
git commit -m "chore: seed — the concept, pin @ $bundle_pin"

# The groups this CBC Run takes, on top of the container that step 2
# copied. Each group is a piece of the CBC Run's tree, so copying it in
# place is the whole of the mapping (docs/conventions/exchange/
# §3.3). This CBC Run is
# Spring and PostgreSQL; a CBC Run on another stack names method alone
# and is born with two method skills, not five (ADR-0029).
for g in method spring-postgres; do
  cp -r "$bundle_dir"/delivery/$g/. .
done
# Their footers stay home, as the container's did in step 2.
find .claude/skills .claude/rules .claude/shapes .claude/approaches-on-trial \
  -name '*.md' -exec python3 -c '
import re, sys
for p in sys.argv[1:]:
    t = open(p, encoding="utf-8").read()
    n = re.sub(r"\n+---\n+## Decisions\n.*\Z", "\n", t, flags=re.S)
    if n != t: open(p, "w", encoding="utf-8").write(n)
' {} + 2>/dev/null
git add .claude/skills .claude/shapes docs/glossary
git commit -m "chore: seed — method and stack skills, shapes, pin @ $bundle_pin"

sed -i -e "/<!-- STEPS-BEGIN/r "<(echo; sed -n '/^## The Plan Step Form/,$p' \
    "$bundle_dir"/delivery/fills/cbc-run-pure-playbook.md; echo) \
    -e '/<!-- STEPS-BEGIN/,/<!-- STEPS-END/{/STEPS-BEGIN/b;/STEPS-END/b;d}' \
    PLAN.md
playbook_version=$(sed -n 's/^Playbook version: \(v[0-9]*\).*/\1/p' \
    "$bundle_dir"/delivery/fills/cbc-run-pure-playbook.md)
sed -i "s|<playbook> v<N> at <concept commit>|cbc-run-pure $playbook_version at $bundle_pin|" \
    PLAN.md
git add PLAN.md
git commit -m "chore: seed — steps into PLAN, cbc-run-pure $playbook_version @ $bundle_pin"
```

One Delivery Pin in every subject, ours: the container arrives inside the
delivery rather than beside it, and where it began is ADR-0025's,
not a number the newborn holds.

The first sed is the swap the container's markers ask for — the
Plan Steps land between the STEPS markers and the markers stay; the
second fills the "Steps from:" comment's placeholder in place, as
its own text sanctions. Both are re-runnable.

The source is `delivery/fills/cbc-run-pure-playbook.md`, read
verbatim — no filter rides the insert; this manual delivers what the
Master Copy holds, like every other seed step. Framing's (CbC) comment
rides in with the Plan Steps: where the Run Briefing lands, no conclusions.

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
Concept Deliverer's, with this prompt and nothing more:

```text
This repo was seeded, not born whole — the branch birth-seed
shows it: one delivery from correctness-by-construction, in two
halves — first the records, the conventions and the two entry
files, then docs/concept/, five method and stack skills, the
method's four Output Shapes and the Plan Steps in PLAN — every seed commit
naming that one Delivery Pin. Main
holds the same files, untracked, on top of the hygiene commit;
the branch is a receipt, never merged. Your
task is to finish the birth: assemble what was delivered into a
working project — your own arrangement, the records, PLAN's
Step 0 closed on its gates. Read the whole repository first,
every file and every seed commit, but for .claude/shapes/: an
Output Shape is read at a Plan Step's closing gate, never before the work it
judges. Then plan the work as the
conventions you were given direct — your own commit sequence,
your own order of artifacts, split by the commit scopes the
skills define, each choice one you can justify in the plan.
I am the reviewer the commit-plan convention names, and the
work moves at my pace: stage the plan and ask for my approval
before committing it; then one commit at a time — stage it,
show me what changed, and commit only on my word, staging the
next after each approval.
Work only within this repository — the repo the delivery came
from is not yours to read. The problem arrives later, as a
Run Briefing that opens Framing; nothing before it names the
problem.
```

What the agent does with the delivered entry files stays its own
choice, and that choice is the Run Reading's object.

The prompt is the session channel — it carries what is true only of
this moment: the situation (one delivery in two halves, the branch
that holds them — deletable, never merged, session-shaped truth),
the task, the read-everything instruction, the expectation of a
plan, and the review protocol. That last is session truth like the
rest — a reviewer is present *this CBC Run* — and a stop written only in
a file loses to the harness's pressure to finish when no voice above
the file says anyone is watching (devlog 2026-09-06, "the pure seed
runs"). Pacing is not a measured object, so the lines leak nothing.
PLAN carries only what stays true of the project. What the prompt
deliberately never says: any order, any answer to which records to
touch or how far to adapt them, whether skills land as one commit or
split by source — the sequence the agent chooses and justifies is
the CBC Run's central data. The commit-scope rule is not restated; it
rides in the delivered skills, and the prompt only points at them.
The stay-inside line guards the blindness: this repo holds the
answer sheet, `docs/baselines/`, and the permission prompt on any
outside read is the human's hard backstop behind it.

Anything said to the newborn after this prompt, at a review stop or
in an answer, is told text, held to the Delivery Note's rules
(`docs/conventions/exchange/` §3.7, *The Delivery Note*). One case is the birth's own: a
newborn holds no earlier state, so it cannot check "this changed
since" — the claim has nothing to land on. Such a claim says so, in
a clause.

**A correct Pure Seed is checkable** — before the agent starts, every
item is a verifiable fact:

- Four commits on birth-seed above the hygiene commit: the
  records and conventions, the concept, the method and stack
  skills with the method's Output Shapes, the Plan Steps into PLAN. Main at
  the hygiene commit, its log holding nothing else; main's
  worktree byte-identical to the branch tip, every delivered file
  listed untracked by `git status` (the check in step 5 lists
  nothing).
- Every pinned copy (`docs/conventions/exchange/` §3.2, *What goes*)
  byte-identical to its Master Copy at the subject's Delivery Pin, and as many
  method and stack skills and Output Shapes as step 6's prompt counts.
- PLAN's STEPS region holds the pure playbook's sequence —
  identical to `delivery/fills/cbc-run-pure-playbook.md` from the Plan Step Form down
  at the subject's Delivery Pin — both markers in place, and the "Steps
  from:" comment names cbc-run-pure at the version the playbook's
  version line gives, at the Delivery Pin. No
  playbook file exists, and no line of the region states an
  assembly conclusion.
- The five birth placeholders are filled and no more: the birth
  entry's Delivery Pin and date, ADR-0001's date, the devlog heading,
  and the working name in the two entry files. Every other Record Stub
  still reads as one, and no bundle birth entry exists.
  `.claude/CLAUDE.md` and `README.md` are byte-identical to the
  container's with the name filled, neither carries a provenance
  header, and no `CLAUDE.md` sits at the root.
- No provenance header from this repo anywhere in the newborn.

What the agent is left to do — the reader's checklist for the
Run Reading afterwards, not instructions delivered to it: every
delivered file committed on main by the agent, under its own
sequence and the commit split the skills define (an add-all in
one commit is an outcome the Run Reading records, not one the Pure Seed
prevents); a commit plan whose sequence is chosen and
justified (the entrance doc's place in it, when records enter
history and how far they adapt to the method, whether skills land
whole or split by source); the Record Stubs filled; Step 0 closed
clean on its container gates — no briefing gate exists to block
it, the Run Briefing opens Framing; the agent/project commit split
held throughout, from the skills, unprompted.

The Run Reading is the Concept Deliverer's act, read-only, recorded there:
the derived arrangement against the walk-1 baseline and the
shipped template, the order chosen, the misses.
