# Commit plan: the Names-and-labels pass

## Summary — the state after all commits

Every living text writes a defined thing by its Glossary Name, and
every numbered section's title is a label of 30 characters or fewer
that stands alone, in both Convention Seats. The 92 living Markdown
files were read whole, by Refinement Layer, in the refinement's order:
the conventions manual, project-recording, the other manuals with the
models, the concept and the glossary, the root records, our agent
setup, what ships. Each line that carried a bare word of ours now
carries the Name or stands as English; about 230 titles are labels,
and every Fact Reference to them carries the label whole, none cut to
30 characters and "…". The six places that told a lesson's case
inline point at the devlog entry that now holds the case word for
word. TODO's two items leave; `PLAN.md`'s Now line says round 3
reads. Round 3's read then meets text already in Names and labels,
and its Writing findings are what the pass missed, not the pass.

Measured at the opening, 2026-10-29, over the 92 files: 15,214 lines
of text; 5,131 carry a bare word that ends some Name, one line in
three, so the hand reads every file; 171 spell a Name in lowercase,
which a script capitalizes once the hand confirms each; 360 numbered
titles, 174 past 30 characters, one word or with a gloss, and the
statements among the rest found by reading, about 230 in all.

## Commits

**1. `docs(agent): add commit plan for the Names pass`**
This file.

**2. `docs: five manuals point at their stories`**
TODO's history item, first, so the layers below read text already
in the form. The cases told inline in the shapes manual's reshape
note, facts-in-sync's "Where it has already happened", two CBC Run
3 cases under the retrospective manual's lessons, writing rule 2's why
and one clause in the exchange manual's *Why it arrives this way*
move word for word into one devlog entry, *the lessons' own stories:
six places*; each section keeps "*Its story:*" and is read again,
keeping a short plain example where the lesson no longer reads
without one (ADR-0073). The visual-comparison skill's §4 and footer,
the sixth place, go with commits 10 and 11, their files being agent
and shipped files.

**3. `docs: the conventions manual, Names and labels`**
Layer 1, one file: 132 lines read, 9 confirmed for the script, 16
titles, one past 30. References to its retitled sections fixed in
every file of the docs scope in this commit; those in agent and
shipped files follow in their scope's commit (the decision below).

**4. `docs: project-recording, Names and labels`**
Layer 2, one file: 211 lines read; 69 titles, 60 breaking rule 10,
the ten records' *What*, *Why*, *Where*, *How*, *When* and
*Anti-patterns* among them, which take the decided pattern: *What a
plan is*, *Why a plan*, *Where a plan lives*, *How a plan is
written*, *When a plan changes*, *A plan's anti-patterns*.

**5. `docs: five manuals, Names and labels`**
Layer 3, first part: exchange, facts-in-sync, agent-arrangement,
commit-plan and commit-messages, the five that define most Names and
hold most references. Commit-plan §2's thirteen titles take the
labels judged on 2026-10-29. The sample paragraph, exchange §3.1
*Delivery Staging*, lands here as judged.

**6. `docs: five manuals and the index, Names and labels`**
Layer 3, second part: shapes, writing, retrospective,
visual-comparison, repo-hygiene and `docs/conventions/README.md`.

**7. `docs: models, concept, glossary, Names and labels`**
Layer 3, third part: the three models, the five concept chapters and
the glossary, whose references to retitled sections are fixed as
each docs commit retitles, so it is read last for its own words.
Revised 2026-10-29, at 5: the glossary gains three Names for things
found defined without one, Delivery Fill, Run Ask and Foundation
Check, and the lines in layers 1 to 3 that carry the bare words take
them in this commit.

**8. `docs: the root records, Names and labels`**
Layer 4: `ARCHITECTURE.md`, whose six area titles keep their paths;
`README.md`; `PLAN.md`; `TODO.md`, every open item; `devlog/README.md`;
`temp/README.md`; and the living header comments of `CHANGELOG.md`
and `TODO-CONVERSATION-MEMORY.md`, their entries and parts being
history.

**9. `chore(agent): our rules, Names and labels`**
Layer 5, first part: the six files under `.claude/rules/`,
`CLAUDE.md`, and the header comment of `.claude/decisions.md`. With
them, every reference in these files to a section retitled in
commits 3 to 8.

**10. `chore(agent): our skills and approaches, Names`**
Layer 5, second part: the five skills and five Approaches on Trial
under `.claude/`, their titles too. The visual-comparison skill's §4
lessons state the general and its footer entries become pointers,
the case having gone to the devlog in commit 2.

**11. `fix(delivery): the container, Names and labels`**
Layer 6, first part: `delivery/container/`, 22 files: the shipped
Agent Rules, skills, Approach on Trial, entry file and Record Stubs,
whose 9 references to one-word titles take the labels. The shipped
visual-comparison skill follows ours from commit 10.

**12. `fix(delivery): the method, Names and labels`**
Layer 6, second part: `delivery/method/`, 14 files: the two skills
with their references and Skill Templates, the four Output Shapes. The worked
example's two copies stay byte-identical.

**13. `fix(delivery): stack, seed, fill, Names and labels`**
Layer 6, third part: `delivery/spring-postgres/` (12 files), where the
stack references' "§1 · …" titles become `N.M` numbers with labels
(`docs/conventions/facts-in-sync/` §3.2, *A section's parts are numbered*);
`delivery/installs/pure-seed.md`, `delivery/fills/cbc-run-pure-playbook.md`,
whose version line moves, and `delivery/README.md`.

**14. `docs: the pass's items leave, round 3 reads next`**
TODO: the pass item and the history item leave. `PLAN.md`'s Now line:
round 3 reads, *Met in round 2, of other kinds* first.

**15. `docs(temp): the pass, how it ran`**
The refinement's file, under *Round 3: how it reads*: the pass's
counts at the opening and the close, what the hand changed beyond
the script, and what it leaves to the read.

**16. `docs(agent): close commit plan for the Names pass`**
Deletes this file; the body says what diverged. Before it, the sweep:
every old title and its cut form with "…", every lowercase Name
phrase, grepped over the living text unwrapped.

**17. `docs: devlog for the Names pass`**
The entry for the set, with the session-end lines.

## Decisions taken inside this plan

- **The sample first.** Exchange §3.1 was rewritten with only its
  words and title changed and shown before this plan was written:
  nine Names in five sentences. The reviewer, 2026-10-29: "they read
  right". Commit 5 lands it as shown.
- **The hand reads every file whole; the script changes three
  things.** One line in three carries a word that ends some Name, so
  no list of lines is shorter than the file. The script, run from the
  scratchpad and never committed, capitalizes the lowercase Name
  phrases the hand confirmed, replaces the italic title in every
  reference to a retitled section, wrapped across lines or not and
  cut with "…" or not, and counts headings, references, front matter
  and code fences before and after; it changes nothing on a second
  run (writing rule 11). The hand decides every other line in place.
- **A bare word becomes its Name or stays English; a repeated Name
  may become "it".** Where a sentence names the same thing twice,
  ordinary English carries the second mention, never a lowercase word
  of ours. The verb "stage" takes its object, "stage a delivery".
- **Labels are shown at the boundary.** Each commit's retitles, old
  and new, are shown to the reviewer in chat with the diff; the body
  names their count. Statements are found by the hand reading, not by
  the script, which flags only length, one word and a gloss.
- **References cross scopes one commit late.** A retitle's references
  in files of the same commit scope are fixed in that commit, as the
  rename grep asks. Those in agent files and shipped files are fixed
  in the next commit of their scope, as the foundation check allows
  when one side is an agent file
  (`.claude/rules/foundation-check.md`, step 5), so that no commit
  mixes `docs`, `chore(agent)` and `fix(delivery)`. The sweep before
  the close greps every old title once more.
- **The history item rides first,** as commit 2, so layers 3, 5 and
  6 read text already in the manual form. The six cases go to one
  devlog entry word for word, as the lesson stories of 2026-10-29
  did; a devlog entry is never edited, so a new one holds them.
- **Left out:** `CLAUDE.local.md`, the reviewer's own words; the
  refinement's file, its own record, whose new lines follow the rule;
  `docs/baselines/`, as rounds 1 and 2 left them; the history
  records' entries, which keep their words, their header comments
  being read; `docs/conventions/repo-hygiene/templates/`, which holds
  no Markdown.
- **Three judgments from commit 3, held for every layer** (revision
  of 2026-10-29, after commit 3). The manual form's fixed headings
  keep their words, *The seats*, *What this is made usable as*; in
  prose a seat is a Convention Seat. A convention is never the bare
  word: a hyphenated name is a label in backticks,
  "`project-recording`'s rule"; a single word takes its Name, "the
  Exchange Convention's"; its manual is "the facts-in-sync manual".
  "Form" stays lowercase where an owner names it or English means it,
  "`PLAN.md`'s step form"; Output Form is the kind. Verbs stay
  English: "a change here walks it". "Rule" is an Agent Rule only
  where it means a file under `.claude/rules/`.
- **A thing found defined without a Name gets one in the pass**
  (revision of 2026-10-29, after commit 5). The hand meets them while
  reading: fill, hand-off and the foundation check in the exchange
  and facts-in-sync manuals. The reviewer names each at the boundary
  where it is found; the glossary takes it in commit 7, and the sweep
  at the close greps every layer for the bare word.
- **The models speak in Names, the concept keeps its words**
  (revision of 2026-10-30, after commit 7). The Tiers Model's
  generic repos took Concept Repo, Run Repo and Concept Garden, CBC
  Run and Concept Deliverer staying this repo's instances; the
  Idea-to-Output Model's kinds take their Names, output staying
  English; the Agent Model's channel names stay italic labels. The
  five concept chapters leave the pass untouched: their words are the
  method's, their headings unnumbered, and renaming them would be a
  concept edit. A particular model is the Agent Model or the Tiers
  Model, as the glossary already said, and a particular form the Plan
  Step Form.
- **No commit is provisional.** The layers and their files are known;
  a file that turns out to need no change still counts as read, and
  the commit body says so.
