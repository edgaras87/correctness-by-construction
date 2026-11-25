---
name: take-the-kit-update
description: Take a Backend Kit Update waiting in temp/ into this repo's Kit Copies, on a branch with a gate last. Use when the human says to take the Kit Update, or when the next Plan Step is about to open with a Kit Update waiting in temp/.
---

<!-- One of the Backend Kit's files: the Instruction Text of its Adapted Case for taking a Kit Update, an Agent Skill. Why it is as it is: .claude/understanding/take-the-kit-update.md. -->

# Take the Kit Update

Takes a Kit Update waiting in `temp/` into this repo's Kit Copies. Each Defined Term here is defined in the Backend Kit's Defined Terms.

## When

- Between two of this repo's Plan Steps, when the next is about to open. Never in the middle of one: a Plan Step still open finishes on the old Kit Copies first.
- Propose it; the human decides.

## Stage 1. The check

1. Read the Update Note in `temp/`, and the *settled snapshot* it names.
2. If this repo's main is that commit, go on to Stage 2.
3. If it is anything else, there is no Update Take. Say so to the human, and stop. The human names this repo to update again, and a new Kit Update replaces the waiting one.

A Backend Kit that moved on after the Kit Update was made is no reason to stop: the Kit Update is correct, if not the latest, and the next brings the rest.

## Stage 2. The Update Take

Cut a branch from main. Its first commit is the Kit Update as it arrived, in `temp/`, not yet in force. Then, in order, each item a commit of its own but item 2:

1. Take the Adapted Case for taking a Kit Update first, on its own: this Agent Skill and its Adapted Understanding Text. Read the new Agent Skill, and go on by it from item 2.
2. Check the files against the Update Note: what changed, and how many. On a mismatch, say it before anything moves, and stop.
3. Take every Kit Copy whole, at the new Kit Version: each file to the path the Kit Update gives it. Remove each path gone, and move each renamed. Their Change Records go with them.
4. Write `.claude/kit-version.md`: the new Kit Version, and item 3's commit, the *version snapshot*.
5. Remove the Kit Update and its Update Note from `temp/`.
6. The gate: check that the files matched the Update Note, every Kit Copy is at the new Kit Version, `.claude/kit-version.md` says both, and `temp/` holds no Kit Update. At the gate's close, move main to the branch's last commit by fast-forward.
