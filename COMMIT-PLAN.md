# Commit plan: numbered parts

## Summary — the state after all commits

The walk's rule is written down: a part of a document that other
text points at gets a numbered subsection, `### N.M`, so the
pointer lands on it and one grep finds everything pointing there.
It sits in the conventions manual's §3.2 and in the shape rule for
a manual, where the next writer meets it. Until now it was in the
devlog alone.

It is applied wherever a pointer lands on a named part today:
- agent-arrangement §2, "§2's tests" and "§2, *Size*".
- project-recording §3, the tag rule and "§3's index".
- The agent model's §4, where "model §4" means ambient, told or
  ownership.
- The agent model's §10, where "model §10" means three different
  facts.

Every such pointer names its number. No existing section number
changes, because subsections go inside their sections.

One pointer was broken and is fixed: "`docs/conventions/commit-plan/`
§4's sweep" names a section that manual does not have. The sweep
lives in the commit-plan skill's §4. The concept is left as it is,
with a TODO item naming the trigger that would number it.

## Commits

**1. `docs(agent): add commit plan for numbered parts`**
This plan.

**2. `docs(conventions): a pointed-at part is numbered`**
The rule goes into the conventions manual's §3.2: a part other text
points at gets `### N.M`, and once one part of a section is
numbered, every part of it is, in order, so that no part falls
under another's heading. Decision first, since it was agreed in
the walk and again here.

**3. `chore(agent): the shape of a manual numbers parts`**
The same line goes into `.claude/rules/convention-manual.md`'s body
item, where a writer meets it while writing a manual. It is an
agent file, so it gets a commit of its own.

**4. `docs: the sweep pointer finds its rule`**
The conventions manual's §3.2 and the TODO item on the grep lesson
point at the commit-plan skill's §4, where the sweep is. The
manual's §4 does not exist.

**5. `docs(conventions): agent-arrangement §2 numbered`**
§2's six parts become `### 2.1` What to `### 2.6` Size, in their
order. "§2's tests" and "§2, *Size*" name their numbers.

**6. `docs(conventions): project-recording §3 numbered`**
*Provisional in its cut.* The tag rule is a bullet inside §3's How,
and the index is a sentence in its Where, and both are pointed at.
How §3 divides, so that each gets its own number and nothing falls
under another heading, is decided on the material. Its pointers name the numbers: the
conventions manual's "project-recording's rule, §3" and the seat's
"§3's index".

**7. `docs(models): agent model §4 and §10 numbered`**
§4's six channels become `### 4.1` ambient to `### 4.6` installed,
already headed, now numbered. §10's facts become subsections. The
pointers in agent-arrangement and the tiers model name the number
they mean.

**8. `docs: devlog carries numbered parts`**
The session's entry. TODO gains the concept's item: its chapters
get numbered headings when a pointer first needs a section of one.
Nothing points into a chapter's section today, and the chapters are
the canonical text every run holds a copy of.

**9. `docs(agent): close commit plan for numbered parts`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **The whole section, once one part is numbered.** A `###` heading
  runs until the next heading, so a single numbered part among bold
  paragraphs would take in the parts after it. Numbering all of them
  in order keeps each part under its own heading.
- **No section number moves.** Subsections sit inside, so every
  existing "§N" pointer still resolves, and only pointers to a named
  part change.
- **The skill is not restructured.** The sweep's pointer goes to the
  skill's §4 as it stands. A shipped skill that changes shape is a
  delivery, and nothing here needs one.
- **The concept waits for its first pointer.** Numbering the
  canonical text would put a change in every run's copy for no
  reader.
