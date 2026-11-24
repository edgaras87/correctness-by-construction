# 0087. The Maintainer Repo's side of the Change split

Date: 2026-11-24
Status: Proposed, opened under the commit plan for the Maintainer split

## Context

The Maintainer Repo's layers document says how a Copy Change travels, in six parts (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §4.2, *How a change travels*). Its §4.2.1 to §4.2.6 run to about 200 lines, mostly steps that one part uses. Left at layer 2, a change to one step reads as a change to the Problem Domain Idea, and sets off a survey of every Adapted Case built on it (`TODO.md`, the item "Split the Change idea").

Each part's own steps go to its Adapted Cases. Four of the six parts are the Maintainer Repo's: Read Copy Changes, Judge Copy Changes, Act on the verdicts, Deliver the Kit Update. Its own Adapted Cases are layer 4, kept whole in `.claude/` (the layers document's §3.4; ADR-0084). The other two are the Backend Repo's, at layer 3. They are written from a Problem Domain Idea of CBC backend design not yet written (the layers document's §3.2.2 and §3.3.1), and that Problem Domain's Defined Terms come with it (ADR-0085, decision 4).

Today, reading a CBC Run and delivering to it are done by the exchange-read and exchange-deliver Agent Skills, written before the layers model. The TODO item on CBC Runs 4, 5 and 6 judges their findings by Judge Copy Changes. Depth c, the item before it, works on how Judge's question 4 is answered.

## Options considered

- **One Change Set for both sides.** Rejected: the Backend Repo's side first needs two layer-2 texts, each with its own decisions. The Maintainer Repo's side needs none, and neither side needs the other.
- **Instruction Texts for all three of the Maintainer Repo's Adapted Cases.** Rejected: Read and Deliver have no user before the rewrite. A CBC Run holds no Change Record and no *settled snapshot*, and no Kit Update is sent until the rewrite (ADR-0082, decision 4). Each new Agent Skill would also sit beside its exchange Agent Skill, both answering the same moment.
- **No Instruction Text for any.** Rejected: Judge has a user soon, the judging of CBC Runs 4, 5 and 6.
- **Four understanding texts, one for each Adapted Case the parts name.** Rejected: §4.2.5 names two, making and staging a Kit Update, and staging is one paragraph. One understanding text may stand under two Instruction Texts (the layers document's §5, question 8).

## Decision

1. **The Maintainer Repo's own steps go to its own Adapted Cases, at layer 4,** their Adapted Understanding Texts in `.claude/understanding/`. What one part hands the next, and the rules every part keeps, stay in §4.2.
2. **Two Change Sets.** The Maintainer Repo's side first; the Backend Repo's after, beginning with its layer-2 texts.
3. **One Adapted Understanding Text per part:** Read Copy Changes; Judge Copy Changes with Act on the verdicts; Deliver the Kit Update, making and staging both.
4. **Judge Copy Changes gets its Instruction Text now,** an Agent Skill. Depth c rewrites it if it must, before CBC Runs 4, 5 and 6 are judged.
5. **Read Copy Changes and Deliver the Kit Update get understanding only.** Each header names the exchange Agent Skill that does the work until the rewrite writes its Instruction Text.

## Consequences

- For a while, two of the Maintainer Repo's own Adapted Cases have no Instruction Text: the case the layers document's §5, question 6, names for the Backend Kit, met here in layer 4.
- Two ways of judging stand side by side: the new Agent Skill, by the layers model, and the working-a-reading Agent Rule, for a CBC Run Reading's list. The item that judges says which it uses.
- The Backend Repo's parts, §4.2.1 and §4.2.6, stay whole at layer 2 until the second Change Set.
