# Commit plan: numbered parts

## Summary — the state after all commits

A manual's structure follows its form, and not the accidents of
citation. A section divided into labelled parts numbers them,
`### N.M`, and so does every section of the same form in the same
document. A pointer to a part names the number, so it lands on the
part and one grep finds it. Bold emphasis inside running prose is
not a part. The rule sits in the conventions manual's §3.2 and in
the shape rule for a manual. The walk first wrote it only in the
devlog, and this set first wrote it as "a part other text points
at", which numbered one section of a manual and left its siblings
as they were.

Applied:
- agent-arrangement §2 and §3.
- project-recording §2 to §10.
- The agent model's §4, §10 and §12. Its §10 is divided into its
  facts, because three pointers name different ones.

No existing section number changes. One broken pointer is fixed:
the commit-plan sweep lives in the skill's §4. The concept waits
for its first pointer into a chapter's section.

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

**6. `docs(conventions): number parts by form`**
The reviewer's reading at step 6's boundary. Numbering only the part
that is pointed at gave project-recording §3 subsections while §2
and §4 to §9, which are built the same way, kept bold paragraphs,
and gave agent-arrangement a numbered §2 beside an unnumbered §3.
§3.2's sentence becomes structural: a section divided into labelled
parts numbers them, every section of the same form in the document
does too, and a pointer names the number. Emphasis in running prose
is not a part.

**7. `chore(agent): the shape rule numbers by form`**
The shape rule's body item says the same, in its own agent commit.

**8. `docs(conventions): agent-arrangement §3 numbered`**
§3's seven parts, one per path, become `### 3.1` `skills/` to
`### 3.7` `CLAUDE.local.md`. §1's two bold lead-ins follow an
unlabelled opening. They are emphasis, not parts, and stay.

**9. `docs(conventions): project-recording numbered`**
§2 to §9, the records, each What, Why, Where, How, When and
Anti-patterns, and §10's four supporting records are numbered in
order. §3's tag rule becomes a part of its own, §3.5, and pointers
name §3.3 for the index and §3.5 for the tag. §13's bold lead
sentence is emphasis and stays.

**10. `docs(models): agent model §4, §10 and §12 numbered`**
§4's channels and §12's claim groups, already `###`, get numbers.
§10 is divided into its facts: the table, hooks, memory files and
comments, permission rules, skills, rules files. The pointers in
agent-arrangement and the tiers model name the number they mean.

**11. `docs: devlog carries numbered parts`**
The session's entry. TODO gains the concept's item: its chapters
get numbered headings when a pointer first needs a section of one.
Nothing points into a chapter's section today, and the chapters are
the canonical text every run holds a copy of.

**12. `docs(agent): close commit plan for numbered parts`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **By form, not by citation** — revised at step 6's boundary. The
  plan first numbered a section when one of its parts was pointed
  at, and all of that section's parts, since a `###` heading runs
  until the next one. Every section of the same form in the document
  is numbered too, so a reader meets one structure throughout.
- **No section number moves.** Subsections sit inside, so every
  existing "§N" pointer still resolves, and only pointers to a named
  part change.
- **The skill is not restructured.** The sweep's pointer goes to the
  skill's §4 as it stands. A shipped skill that changes shape is a
  delivery, and nothing here needs one.
- **The concept waits for its first pointer.** Numbering the
  canonical text would put a change in every run's copy for no
  reader.
