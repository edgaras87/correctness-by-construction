<!-- Draft — provisional, run once (2026-09-05, the pure-seed
     experiment; TODO's Now item is the protocol). Not the
     procedure of record: starter/installs/cbc.md holds that until
     a trial-closing ADR decides between the assembly birth
     (docs/birth-scenario.md) and this shape. Authored from the
     lived run, not before it — the script this generalizes seeded
     ~/IdeaProjects/cbc-pure-run.
     Revised same day, before any walk: the kit half defers to the
     handbook's pure install by pointer, its fills included — the
     seeded run-1 repo predates this and holds the kit raw; a
     divergence for the reading, not a defect. -->

# Install: the pure seed — material only, the agent finishes

One idea: the seed delivers everything and decides nothing. Every
delivery is a commit on main, so the history is the manifest —
what arrived, from where, at which pin — and the newborn's agent
finishes the birth itself by reading what is there. The kit is
born per the handbook's pure install, which fills its own
mechanical birth fields; beyond that no field is filled: not the
stubs, not CLAUDE.md, no bundle birth entry. What the agent
cannot derive (the bundle pin) rides in its seed commit's
subject; everything else it can.

Deliberately not delivered — nothing that encodes a prior run's
conclusions: the birth scenario, the CLAUDE.md template, the
birth fills, the pre-written birth entries. The agent meets the
kit and the method raw.

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

mkdir -p docs/playbooks
cp "$bundle_dir"/starter/bundle/cbc-run-playbook.md docs/playbooks/cbc-run.md
git add docs/playbooks
git commit -m "chore: seed — the CbC run playbook"
```

**4. Fire the agent** — a fresh session in the newborn, never the
concept repo's, with this prompt and nothing more:

> The container and the method are delivered — the commit history
> shows what arrived and from where. Finish the birth: set up what
> is left — your own arrangement, the records, the plan. PLAN's
> Step 0 gates are the exit.
>
> The problem arrives later as a briefing; nothing before it names
> the problem.

The first line is scope; the second is a fact about the world the
agent cannot know and the one guard that must precede every skill.
No order hints — the order the agent chooses is the run's data.

**A correct seed is checkable** — before the agent starts, every
item is a verifiable fact:

- Five commits on main, no other branch; the tree clean.
- Every bundle copy byte-identical to its master at the subject's
  pin: the concept chapters, the playbook, the five skills.
- The kit's own birth fills are done, per pure.md: the birth
  entry's pin and date, ADR-0001's date, the devlog heading, the
  TEMPLATE marker gone. Beyond them, nothing is filled: every
  stub still reads as a stub, CLAUDE.md carries no content
  beyond the kit's, and no bundle birth entry exists.
- Nothing from the excluded list present: no birth-scenario.md, no
  CLAUDE.md template, no birth-fill content, no bundle birth
  entry.

What the agent is left to do — the reader's checklist for the
reading afterwards, not instructions delivered to it: its own
CLAUDE.md; the playbook mapped into PLAN between the STEPS markers
with the "Steps from:" line; the record stubs filled; the bundle's
birth entry reconstructed from its seed subject (the kit's is
filled at birth); Step 0 closed on its gates; the agent/project
commit split held throughout.

The reading is the concept repo's act, read-only, recorded there:
the derived arrangement against the walk-1 baseline and the
shipped template, the order chosen, the misses.
