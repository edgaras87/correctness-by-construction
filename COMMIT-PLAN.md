# Commit plan: read to becomes the settled snapshot

## Summary — the state after all commits

The snapshot the Maintainer Repo has already taken into account is called the *settled snapshot*, not *read to*. *Read to* read as an instruction, "read to …". The new name says what the snapshot is: the point up to which the Maintainer Repo has read, judged and acted on, and the files there, which hold the last Version it saw. That Version may be behind the newest.

The *settled snapshot* is a label inside the Maintainer Repo Register, as *read to* was (`temp/common-ground-problem.md`, *Defined Terms*). The stop keeps its name: main as written down when a Reading starts. Main's latest snapshot keeps its name.

No Living Text says *read to* any more. History keeps its words.

## Commits

**1. `docs(agent): add commit plan for snapshot rename`**
This plan.

**2. `docs: temp's problem names the settled snapshot`**
`temp/common-ground-problem.md`, 8 uses. The problem file is the label's home: the Register's Defined Term and its entry list it. Its definition changes from "the commit the next System Repo Reading starts from" to what the snapshot is: read, judged and acted on up to there, holding the System Kit Version the System Repo had then, which may be behind the newest. "Starts from" goes, since a Reading compares two snapshots and walks no commits. First, so that the files after it follow a name already defined.

**2b. `docs: TODO sweeps the drafts for commit walks`**
A TODO item: words that read as walking commits, such as "runs from … to main" and "across that span", where a Reading compares two snapshots. A sweep of its own, not part of this rename.

**3. `docs: temp's simulation says settled snapshot`**
`temp/system-repo-change-simulation.md`, 15 uses, the *Snapshots* paragraph among them. That paragraph keeps its sentences and points at the label's home with a Fact Reference (`temp/common-ground-problem.md`, *Defined Terms*), so the settled snapshot has one home. Each changed sentence re-read for what it now claims.

**4. `docs: temp's flow says settled snapshot`**
`temp/system-repo-change-flow.md`, 21 uses, most inside the box-drawing pictures and the Mermaid chart. The pictures are realigned by script; their line counts and the columns of `●` and `│` are counted before and after. The chart is rendered again and looked at.

**5. `docs: TODO says settled snapshot`**
`TODO.md`, 1 use, line 139.

**6. `docs(agent): close commit plan for snapshot rename`**
Deletes this file. Before it, the rename sweep: "read to" grepped across Living Text, unwrapped and case-insensitive. The body records what diverged.

## Decisions taken inside this plan

- **One commit per file,** though a rename is one change and fails the revert test split this way: reverting commit 3 alone leaves the simulation on the old name. Chosen so that each diff is small enough to review, the pictures above all.
- **A label, written *settled snapshot*,** italic and lowercase, as the problem file writes a label inside a Defined Term. Not a Defined Term of its own, "Settled Snapshot", since it belongs to the Register as *read to* did.
- **Left alone:** `temp/reading-run-5-2026-10-22.md`'s "Where we read to", which is plain English; `TODO-CONVERSATION-MEMORY.md`'s 13 uses and the devlog's, which are history.
