# The Backend Kit's Defined Terms

<!--
What it is: one of the Backend Kit's files, its Defined Terms: an Instruction Text with no Adapted Understanding Text. Every Defined Term a Kit Copy uses is defined here.
What it stands on: knowledge/problem-domain-ideas/cbc-backend-design/defined-terms-in-cbc-backend-design.md, kept in the Maintainer Repo (ADR-0088, decision 9).
How each entry is written: adapted from its Defined Term's one home in the Maintainer Repo, named at its end, and narrowed to what this repo reads: what only the Maintainer Repo does is left out. In the Maintainer Repo, an entry changes only when its home does.
Its Change Records: in a footer of this text, since it has no Adapted Understanding Text.
-->

Each Defined Term is written with capitals at every use, and bold only here. Search this text for it in bold.

- **Adapted Case:** a part of the Backend Kit, written for one piece of work or for what all the work uses: an Adapted Understanding Text, with the Instruction Texts built on it. Its home: `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms*.
- **Adapted Understanding Text:** the text of an Adapted Case that says why its Instruction Texts are as they are. It never loads, and is read when they change. Its home: `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms*.
- **Agent Skill:** a file under `.claude/skills/<name>/`, its `SKILL.md`, read when its moment comes. Its home: `docs/conventions/agent-arrangement/` §3.1, *`.claude/skills/`*.
- **Backend Kit:** the set of Adapted Cases this repo was born with copies of. It is kept in the Maintainer Repo, and its changes reach this repo by a Backend Kit Update. Its home: `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms*.
- **Backend Kit Copy:** a copy of a Backend Kit file, as it lives in this repo. Short form: **Kit Copy**. Its home: `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms*.
- **Backend Kit Copy Change:** this repo's change to a Backend Kit Copy. Short form: **Copy Change**. Its home: `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms*.
- **Backend Kit Copy Change Record:** what this repo writes with each Backend Kit Copy Change, saying what changed and why. Short form: **Change Record**. Its home: `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms*.
- **Backend Kit Update:** what the Maintainer Repo sends this repo: a copy of every Backend Kit file at a newer Backend Kit Version, with its Backend Kit Update Note. Short form: **Kit Update**. Its home: `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms*.
- **Backend Kit Update Note:** what the Maintainer Repo writes with a Backend Kit Update, for this repo to take it by. It names the *settled snapshot*: this repo's commit up to which the Maintainer Repo has read and judged its work. Short form: **Update Note**. Its home: `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms*.
- **Backend Kit Update Take:** this repo taking a Backend Kit Update into its Backend Kit Copies. Its *version snapshot* is this repo's commit where the Backend Kit Update Take put every Backend Kit Copy at the new Backend Kit Version. Short form: **Update Take**. Its home: `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms*.
- **Backend Kit Version:** the Backend Kit as it stood at one Maintainer Repo commit. This repo records the one its Backend Kit Copies came from. Short form: **Kit Version**. Its home: `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms*.
- **Defined Term:** a word, or words, given an exact meaning plain English does not give them, and written so it is told apart from plain words at every use. Its home: `knowledge/backbone-ideas/defined-terms.md` §1, *Its Defined Terms*.
- **Hygiene Base:** the three files `.gitignore`, `.gitattributes` and `.editorconfig` as this repo was born with them, true for any repo. Each ends at a marked line, for its Stack Overlay. Its home: `knowledge/backbone-ideas/repo-hygiene.md` §1, *Its Defined Terms*.
- **Instruction Text:** a text of an Adapted Case that the agent acts on in its work. Its home: `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms*.
- **Maintainer Repo:** the repo that keeps the Backend Kit, and reads back what this repo learns. Its home: `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms*.
- **Paths Rule:** a rule file with a `paths:` list, loaded when a file it names is touched. Its home: `docs/conventions/agent-arrangement/` §5.6, *Rules files*.
- **Plan Step:** one piece of this repo's plan, closed at its gate. Its home: `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms*.
- **Record Stub:** a record as this repo was born with it: the Backend Kit's file, its form in its header, its content still to be filled. Its home: `knowledge/problem-domain-ideas/cbc-backend-design/records-in-cbc-backend-design.md` §1, *Its Defined Terms*.
- **Stack Overlay:** the lines this repo's stack adds to each file of the Hygiene Base, appended below its marked line. Its home: `knowledge/backbone-ideas/repo-hygiene.md` §1, *Its Defined Terms*.
