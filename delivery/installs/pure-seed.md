# Install: the Pure Seed — material only, the agent finishes

The birth procedure of record (ADR-0016). One idea: the Pure Seed
delivers everything and decides nothing.

The delivery is committed on a Receipt Branch, `birth-seed`, in four
commits. That branch is the manifest: what arrived, from where, at which Delivery
Pin. Main stays at the hygiene commit, with the same files in its
worktree, untracked. The Newborn CBC Run's agent finishes the CBC
Run Birth itself. It reads what is there and commits it under its
own sequence and split (ADR-0018).

The container comes from `delivery/container/`, this repo's
(ADR-0024, ADR-0025). The Pure Seed fills only what is mechanical:

- the birth entry's Delivery Pin and date;
- two other birth dates;
- the working name in the two composed files, the Entry File and
  `README.md`;
- the playbook's Plan Steps into PLAN, with its "Steps from:" line.

No other field is filled. The other Record Stubs stay as they are,
and no entry from this repo's own birth is copied. What the agent
cannot derive is in the seed commits' subjects. Everything else it
can derive.

Deliberately not delivered:

- anything that encodes an earlier CBC Run's conclusions;
- a playbook file.

The agent meets the container and the method with nothing added.
One exception: the two composed files arrive written, in the
container itself, for the two stances a CBC Run can only receive
(`delivery/README.md` §4, *What the tree does not show*).

**1. Set the paths and capture the Delivery Pin.**

```bash
new_project_dir=~/IdeaProjects/<placeholder-name>
deliverer_dir=~/PycharmProjects/engineering/concept-garden/correctness-by-construction

deliverer_pin=$(git -C "$deliverer_dir" rev-parse --short HEAD)
```

Everything the Pure Seed copies is under `$deliverer_dir`. A CBC Run
is born from this repo alone.

The name is a placeholder. Everything before the CBC Run Briefing is
the same for every problem, and the CBC Run Briefing brings the real
name.

**2. Copy the container.**

```bash
mkdir -p "$new_project_dir"
cp -r "$deliverer_dir"/delivery/container/. "$new_project_dir"/
hygiene_dir="$deliverer_dir"/knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/repo-hygiene
cp "$hygiene_dir"/.gitignore "$hygiene_dir"/.gitattributes \
   "$hygiene_dir"/.editorconfig "$new_project_dir"/
records_dir="$deliverer_dir"/knowledge/adapted-cases/cbc-backend-design/keeping-knowledge
mkdir -p "$new_project_dir"/devlog "$new_project_dir"/docs/adr "$new_project_dir"/temp
cp "$records_dir"/readme/README.md "$records_dir"/architecture/ARCHITECTURE.md \
   "$records_dir"/changelog/CHANGELOG.md "$records_dir"/backlog/TODO.md "$new_project_dir"/
cp "$records_dir"/devlog/devlog.md "$new_project_dir"/devlog/
cp "$records_dir"/decisions/0001-record-architecture-decisions.md "$new_project_dir"/docs/adr/
cp "$records_dir"/scratch-space/README.md "$new_project_dir"/temp/
cp "$records_dir"/entry-file/CLAUDE.md "$records_dir"/decisions-log/decisions.md \
   "$new_project_dir"/.claude/
sed -i -e "s/<delivery-pin>/$deliverer_pin/" \
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

The trailing `/.` matters. `delivery/container/*` silently skips the
whole `.claude/` directory. The three hygiene files, `.gitignore`,
`.gitattributes` and `.editorconfig`, are copied from
`knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/repo-hygiene/`.
Six Record Stubs and the scratch space's README are copied from their
folders beside it, each to the path it lands at, and so are the Entry
File and the Decisions Log's Record Stub, to `.claude/`. The plan's Record
Stub and the glossary's still come with the container.

The birth entry takes two placeholders:

- the Delivery Pin, for what was delivered;
- the date.

Its Read-Through Commit is written as *none* in the Record Stub,
because nothing has been read before the first Delivery Note. The
Pure Seed leaves it. One Delivery Pin, because the CBC Run holds one
delivery (ADR-0025, ADR-0036).

The next two `sed`s fill the other birth dates the container
carries: the first ADR's, and the devlog's first heading. Three
records, one moment. The next fills the working name into the two
composed files. They arrive inside the container, not written over
Record Stubs. Every `sed` targets a placeholder, not a line number,
so running the block again is harmless.

The last command strips every copy's *Decisions* footer, which cites
decisions the CBC Run cannot open. It cuts the `---` line and the
section below it, and nothing else
(`docs/conventions/exchange/` §3.8, *The footer at delivery*). Installing by hand, fill the five placeholders
yourself before the agent's first session.

**3. Create the repo and make the hygiene commit.** Run it as it
stands. It is the same in every project, because the Hygiene Base
carries nothing of one project:

```bash
cd "$new_project_dir"
git init
git branch -M main
git add .gitignore .gitattributes .editorconfig
git commit -m "chore: add repo hygiene base"
```

**4. Cut the Receipt Branch and commit the delivery there, the
Delivery Pin in every subject.** One commit per part of the delivery. The subject
is where the agent later reads the Delivery Pin. Main is left at the
hygiene commit.

```bash
git switch -c birth-seed

git add -A
git commit -m "chore: seed — records and Work Approaches, pin @ $deliverer_pin"

# concept/ lands at docs/concept/, the mapping's one exception
# (docs/conventions/exchange/ §3.3, A group's place in the tree).
mkdir -p docs/concept
cp "$deliverer_dir"/concept/*.md docs/concept/
git add docs/concept
git commit -m "chore: seed — the concept, pin @ $deliverer_pin"

# The groups this CBC Run takes, on top of the container that step 2
# copied. Each group is a piece of the CBC Run's tree, so copying it in
# place is the whole of the mapping (docs/conventions/exchange/
# §3.3, A group's place in the tree). This CBC Run is
# Spring and PostgreSQL; a CBC Run on another stack names `method` alone,
# and is born with the Method Group's two Agent Skills, not the five of both groups
# (docs/conventions/exchange/ §3.4, One group per file; ADR-0029).
for g in method spring-postgres; do
  cp -r "$deliverer_dir"/delivery/$g/. .
done
# Their footers are stripped, as the container's were in step 2.
find .claude/skills .claude/rules .claude/shapes .claude/approaches-on-trial \
  -name '*.md' -exec python3 -c '
import re, sys
for p in sys.argv[1:]:
    t = open(p, encoding="utf-8").read()
    n = re.sub(r"\n+---\n+## Decisions\n.*\Z", "\n", t, flags=re.S)
    if n != t: open(p, "w", encoding="utf-8").write(n)
' {} + 2>/dev/null
git add .claude/skills .claude/rules .claude/shapes docs/glossary
git commit -m "chore: seed — method and stack Agent Skills, Output Shapes, pin @ $deliverer_pin"

sed -i -e "/<!-- STEPS-BEGIN/r "<(echo; sed -n '/^## The Plan Step Form/,$p' \
    "$deliverer_dir"/delivery/fills/cbc-run-pure-playbook.md; echo) \
    -e '/<!-- STEPS-BEGIN/,/<!-- STEPS-END/{/STEPS-BEGIN/b;/STEPS-END/b;d}' \
    PLAN.md
playbook_version=$(sed -n 's/^Playbook version: \(v[0-9]*\).*/\1/p' \
    "$deliverer_dir"/delivery/fills/cbc-run-pure-playbook.md)
sed -i "s|<playbook> v<N> at <concept commit>|cbc-run-pure $playbook_version at $deliverer_pin|" \
    PLAN.md
git add PLAN.md
git commit -m "chore: seed — Plan Steps into PLAN, cbc-run-pure $playbook_version @ $deliverer_pin"
```

The container's commit carries our Delivery Pin too. The container
arrives inside the delivery, not beside it. Where the container came from is told in
ADR-0025. The Newborn CBC Run holds no number for it.

The first `sed` is the swap the container's markers ask for. The
Plan Steps land between the STEPS markers, and the markers stay. The
second fills the "Steps from:" comment's placeholder in place, as
the comment's own text allows. Both can be run again.

The source is `delivery/fills/cbc-run-pure-playbook.md`, read as it
stands. No filter changes the insert. The Pure Seed delivers what the
Master Copy holds, like every other seed step. The comment under the playbook's Step 1, CBC Framing,
goes in with the Plan Steps. It says where the CBC Run Briefing
lands, and holds no conclusions.

**5. Return to main and restore the branch tip into its worktree,
untracked.** The branch is never merged.

```bash
git switch main
git restore --source=birth-seed --worktree --staged -- .
git reset -q
```

The restore writes every file of the branch tip into main's worktree
and index. The reset empties the index again. The files stand
untracked, and main's log holds nothing but the hygiene commit.

**6. Check the seed.** Before the agent starts, every item is a fact
that can be checked. First, main's worktree against the branch tip:
`git add -A && git diff --cached --stat birth-seed; git reset -q`.
It lists every file that differs from the branch tip, so it lists
nothing when the worktree equals it. It empties the index either
way. Then:

- Four commits on birth-seed above the hygiene commit: the
  records and Work Approaches, the concept, the method and stack
  Agent Skills with the method's Output Shapes and their Glossary
  Names, the Plan Steps into PLAN. Main at
  the hygiene commit, its log holding nothing else; main's
  worktree byte-identical to the branch tip, every delivered file
  listed untracked by `git status` (the check above lists
  nothing).
- Every pinned copy (`docs/conventions/exchange/` §3.2, *What goes*)
  byte-identical to its Master Copy at the subject's Delivery Pin, and as many
  method and stack Agent Skills and Output Shapes as step 7's prompt counts.
- PLAN's STEPS region holds the pure playbook's sequence,
  identical to `delivery/fills/cbc-run-pure-playbook.md` from the Plan Step Form down
  at the subject's Delivery Pin. Both markers are in place, and the "Steps
  from:" comment names cbc-run-pure at the version the playbook's
  version line gives, at the Delivery Pin. No
  playbook file exists, and no line of the region states how an
  earlier CBC Run was assembled.
- The five birth placeholders are filled and no more: the birth
  entry's Delivery Pin and date, ADR-0001's date, the devlog heading,
  and the working name in the two composed files. Every other Record Stub
  still reads as one, and no entry from this repo's own birth exists.
  `.claude/CLAUDE.md` and `README.md` are byte-identical to the
  Backend Kit's files with the name filled, neither carries a provenance
  header, and no `CLAUDE.md` sits at the root.
- No provenance header from this repo anywhere in the Newborn CBC Run.

**7. Start the agent.** Open a fresh session in the Newborn CBC Run,
never the Concept Deliverer's. Give it this prompt and nothing more:

```text
This repo was seeded, not born whole. The branch birth-seed
shows it. It holds one delivery from correctness-by-construction,
in two halves:
- first, the records, the container's Work Approaches and the two composed files,
  the Entry File and README.md;
- then docs/concept/, five method and stack Agent Skills, the
  method's four Output Shapes, their Glossary Names, and the Plan
  Steps in PLAN.
Every seed commit names that one Delivery Pin. Main holds the
same files, untracked, on top of the hygiene commit. The branch
is a receipt, never merged.

Your task is to finish the birth. Assemble what was delivered
into a working project: your own arrangement, the records, and
PLAN's Step 0 closed on its Plan Step Gate. Read the whole
repository first, every file and every seed commit, except
.claude/shapes/. An Output Shape is read at a Plan Step Gate,
never before the work it judges.

Then plan the work the way the delivered Agent Skills and Agent Rules say:
your own commit sequence and your own order of files, split by
the commit scopes the Agent Skills define. Each choice is one you
can justify in the plan.

I am the reviewer the commit-plan Agent Skill names, and the
work moves at my pace. Stage the plan and ask for my approval
before committing it. Then go one commit at a time: stage it,
show me what changed, and commit only on my word. Stage the next
after each approval.

Work only within this repository. The repo the delivery came
from is not yours to read. The problem arrives later, as a
CBC Run Briefing that opens CBC Framing. Nothing before it names
the problem.
```

What the agent does with the two composed files stays its own
choice. That choice is what the CBC Run Reading looks at.

The prompt holds what is true of this session only:

- the situation: one delivery in two halves, and the branch that
  holds them, which can be deleted and is never merged;
- the task;
- the instruction to read everything;
- the expectation of a plan;
- the review protocol.

The review protocol is true of this session too: a reviewer is
present *in this session*. An agent pressed to finish skips a stop written only in a file,
when nothing outside the file says a
reviewer is present (`knowledge/backbone-ideas/how-an-agent-works.md` §4, *The context window*;
its story: devlog 2026-09-06, "the pure seed runs").
Pacing is not what a CBC Run Reading measures, so these lines give
nothing away. PLAN carries only what stays true of the project.

What the prompt deliberately never says:

- any order;
- which records to touch, or how far to adapt them;
- whether Agent Skills land as one commit or split by source.

The sequence the agent chooses and justifies is the CBC Run's
central data. The commit-scope rule is not restated. It is the
commit-messages Agent Skill's
(`delivery/container/.claude/skills/commit-messages/SKILL.md`, *The agent's own files*),
and the prompt only points at it.

The line that keeps the agent inside the repo keeps it from seeing
answers. This repo holds the baselines a CBC Run must not read,
`docs/baselines/`. The permission prompt on any read outside is the
reviewer's last check behind that line.

Anything said to the Newborn CBC Run after this prompt, at a review
stop or in an answer, is Told Channel text. It is held to the
Delivery Note's rules
(`docs/conventions/exchange/` §3.7, *The Delivery Note*). One case is the CBC Run Birth's own. A
Newborn CBC Run holds no earlier state, so it cannot check "this
changed since": the claim has nothing to compare against. Such a
claim says so, in a clause.

**After the birth.** What the agent is left to do is the reader's
checklist for the CBC Run Reading afterwards. It is not delivered to the agent as
instructions:

- Every delivered file committed on main by the agent, under its
  own sequence and the commit split the Agent Skills define. An
  add-all in one commit is an outcome the CBC Run Reading records,
  not one the Pure Seed prevents.
- A Commit Plan whose sequence is chosen and justified: the Entry
  File's place in it, when records enter history and how far they
  adapt to the method, whether Agent Skills land whole or split by
  source.
- The Record Stubs filled.
- Step 0 closed clean on the Plan Step Gate the agent wrote when it
  opened. No Plan Step Gate waits on the CBC Run Briefing: it opens
  CBC Framing.
- The split between agent commits and project commits held
  throughout, from the Agent Skills, unprompted.

The CBC Run Reading is the Concept Deliverer's act, read only, and
recorded there. It compares the arrangement the agent derived
against `docs/baselines/cbc-derived-claude-walk1.md` and the
container's Record Stubs, the order chosen, and the misses.
