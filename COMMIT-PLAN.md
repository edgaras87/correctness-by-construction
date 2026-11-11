# Commit plan: the terms in use

## Summary — the state after all commits

`temp/system-repo-change-simulation.md` and `temp/common-ground-problem.md` write each thing the Common Ground Problem now defines by its Defined Term, and keep the old word only where it is plain English.

- **"moment"** of the System Kit is System Kit Version.
- **"register"** is Maintainer Repo Register, and "read to" is its label, *read to*.
- **"reading"**, where it means the Maintainer Repo's read of one System Repo and its draft, is System Repo Reading.
- **"note"** is System Kit Attention Note where a System Repo writes it, and System Kit Update Note where it goes with an update.
- **"update"**, where it means what the Maintainer Repo sends, is System Kit Update.
- **"change"**, where it means a System Repo's change to a System Kit Copy, is System Kit Copy Change.
- **"entry"** is System Kit Copy Change Record.

A reader meets no word in a narrow sense the Defined Terms do not give it.

## Commits

**1. `docs(agent): add commit plan, the terms in use`**
This file.

**2. `docs: temp's "moment" is System Kit Version`**
29 uses. Nearly all are narrow; the plain one in the definition of *text*, "as it stood at one moment", stays.

**3. `docs: temp's register is Maintainer Repo Register`**
18 uses of "register" and 19 of "read to". The label is written in italics, as the problem file writes its other labels.

**4. `docs: temp's reading is System Repo Reading`**
122 uses, many plain: "reading back", the movement; *reading*, a Text Life Phase label; "reading the copy". Only the narrow ones change.

**5. `docs: temp's notes take their two Defined Terms`**
71 uses of "note" and "notes", each sorted into its two meanings. The rule *A note* under Change is retitled, and every Fact Reference to its title fixed in this commit.

**6. `docs: temp's update is System Kit Update`**
110 uses. Narrow where it names what is sent; plain where it is the act, "to update", or the movement in the table of what passes between the repos.

**7. `docs: temp's change is System Kit Copy Change`**
275 uses of "change" and "changes", the most mixed: "the System Kit's changes", "a change read back", "changes nothing" stay plain. Only a System Repo's change to a copy changes.

**8. `docs: temp's entries take their Defined Term`**
98 uses of "entry" and "entries". A sentence that names both the change and its record is reworded here, so the two five-word terms do not stand side by side more than it needs.

**9. `docs(agent): close commit plan, the terms in use`**
Deletes this file. Before it, the sweep: each old word grepped, unwrapped, in both files, each hit plain English or a quote.

## How each commit is made

- **Every use is read, never replaced blind.** A script lists each use with its line; the agent decides narrow or plain for each, and a narrow one is changed by hand or by an exact-match script that asserts its count. The diff is checked against the list.
- **A Defined Term is written whole,** by writing rule 9. Where a sentence would repeat a long term, it names the term once and refers back with "it" or "they", plain English. No shortened form, such as "the record", stands for a term.
- **A step title or a rule's bold lead that changes** is grepped for every Fact Reference to it, fixed in the same commit (`docs/conventions/facts-in-sync/` §3.3, *The rename grep*).
- **Only the lines the change needs change** (writing rule 11).

## Decisions taken inside this plan

- **One term per commit,** in the order the terms were defined, but for the record: "entry" goes last, after "change", since the sentences that hold both are reworded once, at commit 8.
- **Only the two temp files.** `TODO.md`'s item on resuming the simulation says "read to"; it quotes the simulation, and stays. The frozen `temp/between-repos-simulation.md` is left as frozen.
- **Today's sections stay in today's words.** A *Today* field, or §2.2, that names what exists today keeps today's names, such as the Delivery Note; only the words of the intent change.
- **The counts above are of the word, not of the narrow uses.** Each commit's body gives how many changed and how many stayed plain.
