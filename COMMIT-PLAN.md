# Commit plan: gate shapes

## Summary — the state after all commits

A shape is read at a step's closing gate and nowhere else. In a run,
every shape lives in `.claude/shapes/`, nothing loads it, and what
must hold while work is written belongs to the skill or rule that
runs the work. Shapes travel like any copy, with the group of what
they shape, at birth and at every delivery; nothing is staged in
`temp/` for a gate. Before a shape is written its examples are read
for where they differ and what they all lack; a difference at the
gate ends one of four ways; a shape that names work is asked for by
its skill too.

The method ships four shapes in `delivery/method/.claude/shapes/`,
offered by run 3 and taken reshaped: run 3's skeletons, full-word
tags, and illustrations rewritten from the worked example's order
service, so run 4, which rebuilds never-oversold, meets no answer of
run 3's. ADR-0052 records it, from run 3's RETRO.md, D12, D13, D18
and D29. Run 4's first evidence test, written without its shape in
view and read against it at the gate, is the measurement TODO held
the shape back for.

## Commits

**1. `docs(agent): add commit plan for gate shapes`**
This plan, agreed.

**2. `docs(adr): 0052, shapes read at the gate only`**
The decision, opened Proposed: one place, read at the gate; shapes
travel as copies with their group; no staging in `temp/`; the look,
the fourth ending, work named by the skill; run 3's four taken
reshaped. Rejected: holding them back; shipping them as rules that
load; run 3's illustrations as they are. Amends ADR-0035 and
ADR-0037.

**3. `docs: a shape is read at the gate, nowhere else`**
The shapes manual, rewritten where it held two places and a staging
act: the seats, §3, §4 and §5, and what it is made usable as. The
shipped `shapes-lifecycle.md` as run 3 wrote it. The pointers that
named the old places with it: `delivery/README.md`,
`docs/conventions/agent-arrangement/`, `ARCHITECTURE.md`.

**4. `docs: shapes travel with their group`**
The exchange's §3.2 and §3.5, and the shipped `delivered-copies.md`:
the copies that travel after birth include `.claude/shapes/`; a
shape carries `foundation` as a skill or rule does; one pin covers
them.

**5. `chore(agent): deliveries stage the shapes too`**
`exchange-deliver`'s staging copies each group's `.claude/shapes/`
beside its skills and rules. The agent's files, a commit of their
own.

**6. `docs: the method ships the slice-record shape`**
**7. `docs: the method ships the evidence-test shape`**
**8. `docs: the method ships the kill shape`**
**9. `docs: the method ships the registry-entry shape`**
One commit per shape, each read on its own: run 3's skeleton, kept;
the tags in full words; the illustration rewritten from the worked
example. *Provisional:* where the worked example lacks the material
an illustration needs, each says so at its boundary, and the commit
either adds it to the worked example, both copies, or keeps the
illustration to the skeleton's own placeholders.

**10. `docs: the playbook reads shapes at the gate`**
The run playbook's "`temp/` looked in for shapes staged for this
step", at every step, becomes the gate's reading against
`.claude/shapes/`.

**10b. `docs: the manuals stop calling rules shapes`**
Agent-arrangement, the conventions manual and the exchange manual
call our two form rules "the shape of a reading" and "the shape of
a manual"; the conventions manual's §3.3 is titled "The shape".
Each now calls them rules that state a form, as commit 3 left the
deliverer holding no shape in use; §3.3 keeps its number.

**11. `chore(agent): our form rules are rules`**
`exchange-reading.md`, `convention-manual.md` and
`working-a-reading.md` call the two rules shapes, one of them
exposed, in their comments and a footer; they stop saying so.

**12. `docs: records carry gate shapes`**
ADR-0052 Accepted. TODO: the evidence-test measurement item says the
measurement is now run 4's own first gate; "our own side of shapes"
closes; the `temp/` item drops shapes from its context. CHANGELOG's
[Unreleased] entry on the method names the shapes it ships.

**13. `docs(agent): close commit plan for gate shapes`**
Deletes this file; the body says what diverged.

## Decisions taken inside this plan

- **The four shapes are the method's.** They shape framing's records,
  slice records and evidence tests, and a shape travels with the
  group of what it shapes (the shapes manual, §4).
- **A shape carries `foundation`**, as a shipped skill or rule does:
  a run can then tell which manual it stands on. Run 3's carry none.
- **At the deliverer, no shape is in use.** It has no steps and no
  gates, so it reads nothing at one; its two rules with a Governs
  line are rules. Commit 11 follows from it.
- **Run 3's own `.claude/shapes/` sits at the paths the method now
  ships.** Its next take lands ours over them, as the exchange lands
  any taken edit; its illustrations stay in its history. The note
  says so before the staging goes, which is also the moment TODO's
  item on checking a delivery's paths against the run's own files
  fires.
- **What run 4 must judge is group C's.** RETRO D22's rows for shapes
  (gate-only judged at the second slice; the two new shapes' first
  reading) become playbook gate items there, not here.
- **F8's files are not in this set**: the writing and one-home
  rules, the check script and the two skills are their own decision.
