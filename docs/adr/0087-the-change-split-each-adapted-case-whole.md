# 0087. The Change split, each Adapted Case whole

Date: 2026-11-24
Status: Proposed, opened under the commit plan for the Change split

## Context

The Maintainer Repo's layers document says how a Copy Change travels, in six parts (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §4.2, *How a change travels*). Its §4.2.1 to §4.2.6 run to about 200 lines, mostly steps that one part uses. Left at layer 2, a change to one step reads as a change to the Problem Domain Idea, and sets off a survey of every Adapted Case built on it (`TODO.md`, the item "Split the Change idea").

Four of the six parts are the Maintainer Repo's: Read Copy Changes, Judge Copy Changes, Act on the verdicts, Deliver the Kit Update. Its own Adapted Cases are layer 4, kept whole in `.claude/` (the layers document's §3.4; ADR-0084). The other two, Change a Kit Copy and Take the Kit Update, are the Backend Repo's, at layer 3. They are written from a Problem Domain Idea of CBC backend design not yet written (the layers document's §3.2.2 and §3.3.1), and the Backend Kit's Defined Terms are decided with the first of them (ADR-0085, decision 4).

The why of each rule sits only in the simulation, in each step's *Chosen* field. Each part's section points there: "How each rule was chosen is the simulation's". The simulation is a draft in `temp/`, deleted once what it holds has landed. It used nothing of backends: its steps were written for a repo of any kind that works from Kit Copies, and only renamed by ADR-0086.

Layer 3 holds one set of Adapted Cases for each Problem Domain, never shared (ADR-0084, decision 5). One Problem Domain has a kit so far.

## Options considered

- **Two Change Sets, the Maintainer Repo's side first.** Rejected: layer 2 holds only what is shared once both sides are cut, and depth c walks all six parts.
- **Understanding only, the Instruction Texts left to the rewrite.** Rejected: it reads today's repo into the new texts, through the exchange-read and exchange-deliver Agent Skills. The new texts are written from the simulation alone; the rewrite compares the two.
- **An Instruction Text for Judge alone.** Rejected for the same reason. An Adapted Case is understanding with the instructions built on it (`knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms*).
- **The steps moved as the understanding.** Rejected: steps are what the agent acts on, so they are Instruction Text. The understanding says why.
- **The whys left in the simulation, the layers pointing at it.** Rejected: the layers would point at a draft that is deleted.
- **A base kit for any repo that works from Kit Copies, which the Backend Kit extends.** Rejected: it shares a set across Problem Domains, against ADR-0084, decision 5, for a second kind of project that does not exist. How a second kit reuses the group is a TODO item, its trigger that kit.
- **Four Adapted Cases for the Maintainer Repo,** making and staging a Kit Update apart. Rejected: staging is one step of the same work, after the human's word. One Agent Skill holds both, in two stages.

## Decision

1. **Each of the six parts gets its Adapted Case, whole:** its Adapted Understanding Text and its Instruction Text. Each is written from the simulation alone; today's repo is compared with it in the rewrite.
2. **The Maintainer Repo's parts go to its own Adapted Cases, at layer 4,** kept whole in `.claude/`, the understanding in `.claude/understanding/` and the Agent Skill in `.claude/skills/`. Three: Read Copy Changes; Judge Copy Changes with Act on the verdicts; Deliver the Kit Update, making and staging.
3. **The Backend Repo's parts go to the Backend Kit, at layer 3,** in its group for keeping knowledge, under `knowledge/adapted-cases/cbc-backend-design/`. Nothing in them names backends.
4. **Each line goes to one of three places:**
   - **layer 2:** what more than one part relies on, and its why; a line goes here when changing it would change more than one Adapted Case;
   - **the Adapted Understanding Text:** why the part's own steps are as they are, what was rejected, and the open points with their triggers; the agent does not need it to do the work;
   - **the Instruction Text:** when it starts, the steps in order, the checks, what it writes, and where it stops for the human; the agent acts on it in the work.
5. **The whys leave the simulation.** Layer 2 no longer points at it for how a rule was chosen. The simulation keeps its steps, which depth c walks, and its *Today* lines, which the rewrite reads.
6. **One Change Set, the Maintainer Repo's side first.**
7. **Depth c changes what it must in both halves** of every Adapted Case the split writes; Judge's before CBC Runs 4, 5 and 6 are judged.

## Consequences

- Until the simulation goes, each why sits in it and in the layers. The layers are its home.
- The new Agent Skills name Backend Repos and the Look for Lessons, and the exchange Agent Skills name CBC Runs. The item on CBC Runs 4, 5 and 6 says which it uses.
- Three questions wait for their commits: what the layers of knowledge in CBC backend design hold that the Maintainer Repo's document does not; the Backend Kit's Defined Terms; the Backend Kit's folder layout and each Instruction Text's form.
- A second kit copies the group for keeping knowledge, unless its TODO item decides one shared group.
