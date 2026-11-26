# Repo hygiene

<!--
What it is: one of the Backend Kit's files, the Adapted Understanding Text of its Adapted Case for repo hygiene. It says why its Instruction Text is as it is, where only this Adapted Case relies on the reason.
What it stands on: knowledge/problem-domain-ideas/cbc-backend-design/repo-hygiene-in-cbc-backend-design.md, kept in the Maintainer Repo. The rules this Adapted Case shares with every repo, and why each is so, are there and in the Backbone Idea it adapts.
What stands on it: its Instruction Text, beside it: the Hygiene Base, .gitignore, .gitattributes and .editorconfig, copied to a Backend Repo's root at birth; and the Stack Overlay for Java and Spring, java-spring/.
Its first source, input and not rules: the repo-hygiene manual, docs/conventions/repo-hygiene/README.md, Why it arrives this way and §2.
It never loads; it is read when its Instruction Text changes.
-->

This text says why repo hygiene reaches this repo as three files, and not as a text the agent reads. Each Defined Term here is defined in the Backend Kit's Defined Terms.

## 1. Why files

The three files act by being there. Nobody follows a `.gitignore`: git leaves out what it names. So the Hygiene Base is its own Instruction Text, with nothing beside it for the agent to read. A rule that cannot be a line in one of the three files cannot reach this repo this way.

## 2. Why a marked line

A Stack Overlay is appended to the end of each file, as it is. So each file of the Hygiene Base ends at its marked line, and each part of a Stack Overlay starts with its stack's name. All three formats take an appended block without change.

## 3. Open

- **How a Stack Overlay reaches this repo:** nothing gives one to it at the Plan Step that first builds the application on its stack, so this repo writes its stack's lines itself. The Maintainer Repo holds this question open.
