# Commit plan: round 2's work on layer 4, ARCHITECTURE, README and the records

## Summary — the state after all commits

Round 2's fixes for layer 4 have landed, on the four decisions taken
for TODO's "Decide what kind of text our ARCHITECTURE is, and its
size" (2026-10-27). ADR-0068 records them.

- **Our ARCHITECTURE is a record, not a description.** Facts-in-sync
  §4, the foundation check's step 1 and the glossary's
  "description" no longer list it. It stays checked as a record
  whose header carries a `foundation` line (FINDING-179's
  "description").
- **The glossary is a file of its own,** `docs/glossary.md`, the
  path a run's has. Its header comment holds the form of an entry
  and `foundation: the writing convention`. Writing rule 6, in both
  our rule and the writing manual, names it. Project-recording §1
  lists it as a record both seats keep. Its entries point at their
  homes: "take" at exchange §4, "note" at §3.7, "pin" at §2.2
  (FINDING-184's part).
- **ARCHITECTURE is a map of about two pages,** down from 3,765
  words to about 1,200. It keeps what it owns or what someone reads
  it for:
  - its header comment, its form, naming project-recording by path
    (FINDING-186);
  - an overview: what is stated, what ships, how runs are born and
    read back, what must hold, where things are; pointing at the
    README for what this repo is;
  - §1, the pairing, with the models added. §1.1 points at the
    CHANGELOG's comment for the version rule (FINDING-176). §1.2
    gives a phrase and a path for each convention;
  - §2, the delivery and the runs: one line a group, pointing at
    `delivery/README.md`; the table of runs; the exchange in one
    sentence with its sections (FINDING-184);
  - §3, what must stay true, as a table: rule, home, how it is
    held;
  - §4, the codemap, its records pointing at project-recording's
    map (FINDING-145's last part).

  Gone: *How to read it*, the list of what it knows is wrong, whose
  entries are TODO known issues, the old §3 and §4 (FINDING-185 with
  them), §2.3's list of which convention owns each container file,
  the counts, and §2.5's diagram and retellings.
- **Project-recording's deliverer seat** lists our map's parts,
  each with what it holds and who reads it, in place of ADR-0044's
  paragraph.
- **The concept's version rule is told once,** in `CHANGELOG.md`'s
  comment (DECISION-14). Three manuals' *What this does not cover*
  and facts-in-sync §4 point there, keeping ADR-0003 as the why.
- **The README is the home of what this repo is.** It says the
  deliverer, and that a reading changes our masters, not only the
  concept. `CLAUDE.md`'s opening follows it with a fact reference.
  It points at the tiers model for the tiers' triggers
  (FINDING-187).
- **TODO** names sections by root path (FINDING-188), and holds the
  worked example's two copies as one item (FINDING-190).
- The refinement's file names each finding's ending. TODO's
  ARCHITECTURE item goes, each Idea weighed, and conversation-memory
  §17 with it.

## Commits

**0. `docs(agent): add commit plan for layer 4's work`**
Opens the set.

**1. `docs: ADR-0068 our ARCHITECTURE is a map`**
Proposed. The four decisions of 2026-10-27, each with its rejected
options: a record, not a description; the glossary its own file; a
map of about two pages, parts listed, not run-only; the README the
home of what this repo is, the others following. It reverses
ADR-0044's words and length.

### Decision 1: a record

**2. `docs: ARCHITECTURE is a record, not a description`**
Facts-in-sync §4's list of descriptions drops `ARCHITECTURE.md`.
*The words*' "description" drops "this page" (FINDING-179). The
walk reads what stands on facts-in-sync.

**3. `chore(agent): foundation check drops ARCHITECTURE`**
Step 1's descriptions list drops it. It stays under "records whose
header comment carries a `foundation:` line". Agent file, next
after 2.

### Decision 2: the glossary

**4. `docs: the glossary is a file of its own`**
`docs/glossary.md`: a header comment with the form *The words*
follows today and `foundation: the writing convention`; the 30
entries moved word for word, their bare "§" given
`ARCHITECTURE.md`'s path. ARCHITECTURE keeps one line pointing at
it. The pointers move: the writing manual §2, project-recording
§1's item 11, now both seats, and its *The seats*, and TODO's.

**5. `chore(agent): our rules name the glossary`**
`.claude/rules/writing.md` rule 6, and
`.claude/approaches-on-trial/refinement.md` §3's "stage" line.

**6. `docs: the glossary's entries point at their homes`**
FINDING-184's part. "Take" points at exchange §4, "note" at §3.7.
"Pin" keeps its definition with exchange §2.2, and ARCHITECTURE's
second telling goes in commit 9. Moved first and fixed second, so
each commit reverts alone. "Delivery" pointed at exchange §6.7,
which layer 3's commit 7 merged away and its sweep missed; it names
§6.6.

**6b. `docs: the glossary groups its words`**
Inserted at commit 4's boundary, on the reviewer's question. The 30
entries sit in five groups by what they name: the repositories,
between them, kinds of text, how texts tie, the work. Inside a
group a word follows the words it uses. Plain `##` headings, as
TODO's are; a word is found by its name. The header comment gains
the rule: a new word goes in its group.

### Decision 3: a map of two pages, part by part

**6c. `docs: ADR-0068 sends the known-wrong list to TODO`**
Inserted at commit 7's boundary. The reviewer asked why the map
says what is wrong instead of telling the architecture. Of the
page's 104 versions, 102 had the list empty, and TODO's *Known
issues* already holds what is known and deferred. Decision 3 and
the Consequences change: the list goes, and a line known wrong is a
known issue. ADR-0044's list is superseded with its length.

**7. `docs: ARCHITECTURE opens with an overview`**
Reworked at its boundary, on the reviewer's questions. The header
comment says what the map holds, naming project-recording by root
path (FINDING-186), and that a line known wrong is a TODO known
issue. The opening is an overview of the repo, as a run's map opens
(project-recording §8.4): what is stated, what ships, how runs are
born and read back, what must hold, where things are, each with its
section; it points at `README.md` for what this repo is, and
argues nothing. *What this is*, *How to read it* and the list of
what it knows is wrong go.

**8. `docs: ARCHITECTURE §1 is the pairing`**
The models join the table. §1.1: canonical here, versioned as a
whole, its rule in `CHANGELOG.md`'s comment (FINDING-176's home
end). §1.2: a phrase and a path for each convention, which the
index and `one-home.md` rule 3 point at.

**9. `docs: ARCHITECTURE §2 maps the delivery and runs`**
One line a group, pointing at `delivery/README.md`. §2.3's list of
which convention owns each file goes, and the counts. §2.5 keeps the
table of runs and says the exchange in one sentence, with sections
(FINDING-184). The tiers model's pointer at §2.5 for the note and
the pin goes; it keeps the exchange's. `delivery/README.md`'s
pointer at §2.2 is read at the boundary.

**10. `docs: ARCHITECTURE drops its retold sections`**
§3 and §4 go: facts-in-sync, the exchange and agent-arrangement say
them (FINDING-185 goes with §3). §5 and §6 become §3 and §4. Nothing
outside points at §3 to §6; the codemap's own "(§4)" moves.

**11. `docs: what must stay true is a table`**
§3's eleven bullets become rows: the rule, its home, how it is
held. A run's invariants are a table the same way (project-recording
§8.4).

**12. `docs: the codemap points at the records map`**
FINDING-145's last part. The codemap's lines for records point at
`docs/conventions/project-recording/` §1 and stop describing them.

**13. `docs: project-recording lists our map's parts`**
The deliverer seat's ARCHITECTURE paragraph, ADR-0044's, becomes
the parts of commits 7 to 12, each with what it holds and who reads
it. A part no one reads goes.

**14. `docs: the concept's version rule is told once`**
FINDING-176, DECISION-14 (b). The conventions, exchange and
project-recording manuals' *What this does not cover*, and
facts-in-sync §4, point at `CHANGELOG.md`'s comment, each keeping
ADR-0003 as the why.

### Decision 4: the README

**15. `docs: the README says what this repo is`**
It gains what only `CLAUDE.md` and ARCHITECTURE's old opening
said: the deliverer, runs read back here, documents only and nothing
built. "Harvested concept changes" becomes changes to our
masters.

**16. `chore(agent): the entry file follows the README`**
`CLAUDE.md`'s opening keeps its words for the agent and carries a
fact reference to `README.md`.

**17. `docs: the README points at the tiers model`**
FINDING-187. Its retold triggers, "anything general waits on three"
and the garden rule, gain `docs/models/tiers.md` §2.1 and §2.2.

### TODO

**18. `docs: TODO names sections by root path`**
FINDING-188, the seven Context lines.

**19. `docs: TODO holds the worked example once`**
FINDING-190. "Decide whether a check compares the worked example's
two copies" and "Deduplicate the worked example" become one item
with both triggers.

### Records and close

**20. `docs: round 2's layer 4 is worked`**
The records commit. ADR-0068 Accepted. The refinement's file: each
of FINDING-184 to 192, and 145's last part, 176 and 179's
"description", names its ending; 189 names `4eb8a57`. TODO's
ARCHITECTURE item goes, each Idea's verdict in the body, and
conversation-memory §17 with it. ADR-0044's status names ADR-0068,
as the ADR form asks of a superseded record.

**21. `docs(agent): close commit plan for layer 4's work`**
Deletes this file; the body says what diverged.

**Provisional, after any commit: the walk's inserts.** A commit that
changes a manual walks what stands on it; a derived file that then
disagrees gets a lettered commit after it, the shipped master first.
Two are likely:

- **8b. `chore(agent): one-home rule 3's example`**, if §1.2's new
  form no longer fits the rule's example.
- **9b**, if `delivery/README.md`'s pointer at §2.2 loses its fact.

## Decisions for you to object to

- **One ADR for the four decisions.** They answer one item, and
  three of them change what ADR-0044 decided.
- **§1 and §2 keep their numbers;** §5 and §6 become §3 and §4.
  Eleven living pointers land in §1 and §2; none in §3 to §6.
- **§1.2 keeps a phrase and a path for each convention.** The index
  points there, and a local map holds no list the map holds
  (project-recording §8.6). The paths make `one-home.md` rule 3's
  example true, a met item.
- **The glossary moves word for word, then is fixed.** Two commits,
  so each reverts alone.
- **The tiers model keeps its instance for now.** Only its pointer at
  §2.5 goes, since §2.5 no longer holds that fact. The rest waits for
  "Decide which way a fact reference may point".
- **Nothing ships.** A run's glossary is already `docs/glossary.md`,
  and its stubs do not change.
- **FINDING-191 is TODO's** (DECISION-10), 192 is declined
  (DECISION-13), and 189 was fixed in layer 3.
- **Conversation-memory §17 goes in the records commit,** where its
  item closes (its header).
