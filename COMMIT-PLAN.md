# Commit plan: group E, text we would write

## Summary — the state after all commits

A run framed from this bundle (the reading's W16, decisions 1 to 4):

- commits its briefing unchanged when framing opens, at
  `docs/system/framing/briefing.md`, and never edits it after;
- starts `docs/glossary.md` at framing, from a template in
  `cbc-framing`, and its records table names it;
- tags its layers in full words, from chapter 01's names:
  LAYER-1-ENVIRONMENT, LAYER-2-SYSTEM, LAYER-3-AREAS,
  LAYER-4-PROBLEMS, LAYER-5-INTERACTION, in the concept and every
  text derived from it;
- reads a worked example whose kills each show the failure with
  numbers, and no "costume".

What else in the method is not yet plain is one TODO item, a step of
its own.

## Commits

**1. `docs: framing commits the briefing first`**
Decision 1. `cbc-framing`'s record section opens on the briefing:
committed unchanged when framing opens, private parts removed and
named in its first line, history after. The playbook's Step 1
comment and the devlog stub's "Briefing:" line point at the file.

**2. `docs: framing starts the glossary`**
Decision 2. A new `cbc-framing/templates/glossary.md`, its header
saying what goes in and that a word is defined once; the skill names
it beside the registry template. The container's records table gains
the glossary's row, and its writing rule drops "where it keeps one".

**3. `docs: layers are tagged in full words`**
Decision 3. Chapter 01 and every text that uses its tags, in one
commit so no text cites a tag the concept no longer has: `cbc-framing`
(skill, workflow, the plain page, the registry template),
`cbc-slice` (skill, workflow, readiness), both worked examples alike,
`infra-establish` (skill, walk). CHANGELOG's Unreleased gains one
editorial line.

**4. `docs: the worked example's kills show numbers`**
Decision 4, now. Both copies of the worked example, kept identical:
each kill gains a worked example with numbers, as the kill shape
asks, and "three costumes" goes. The registry-entry shape's
illustration loses its "costume". `cbc-framing`'s "derive your own
shape" for the registry's layout says layout.

**5. `docs: TODO holds the method's plain rewrite`**
Decision 4, later. One item: the method's texts not yet plain, about
35,000 words, a step of its own. Its story in today's devlog entry.

**6. `docs(temp): the reading closes W16`**
W16 marked done with its commits. The pass over every open item, by
`working-a-reading.md` step 5.

## Decisions taken inside this plan

- **The rename is editorial; the concept stays where it is.** No
  layer changes its meaning, only its tag, and every derived text
  changes in the same commit. Unreleased already holds v2 for the
  walls chapter; this rides with it.
- **No ADR.** Run 3's full-word tags for every other kind were taken
  in F1 without one (`b7d3448`). The rejected options, holding for
  run 4's reading and run 3's names, are in the reading and go in
  commit 3's body.
- **The glossary arrives as a template in `cbc-framing`,** as the
  registry does, not as a container stub: it is born at framing,
  and nothing before the briefing names the problem.
- **No CHANGELOG line for commits 1, 2 and 4.** F1 and F2 changed
  what framing and a slice write and added none. Commit 3 has one,
  because it changes a chapter.
- **History keeps its tags:** ADRs, the devlog, CHANGELOG's `[v1]`,
  the baselines, `temp/`.
