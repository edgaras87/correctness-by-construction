# 0086. Backend Repo and Backend Kit

Date: 2026-11-23
Status: Proposed, opened under the commit plan for Backend Repo

## Context

Layer 3 is grouped by Problem Domain, a kind of project (ADR-0084, decisions 5 and 7). The System Kit is the set of Adapted Cases of one Problem Domain, CBC backend design, and a System Repo is a project of it. "System Repo" and "System Kit" name no Problem Domain, so a second one would make them ambiguous (`TODO.md`, the item "Rename System Repo and System Kit").

On 2026-11-23, `git grep` over the text unwrapped found 685 uses in 6 living files: the Maintainer Repo's layers document, the four drafts in `temp/common-ground/`, and `TODO.md`. 9 more Defined Terms are built on the two, such as System Kit Copy Change Record. The Change idea's split and depth c would add more.

## Options considered

- **CBC Backend Repo and CBC Backend Kit.** Rejected: every Defined Term built on them grows one word, and 5 of the 11 pass 4 words, a trigger to look for a shorter one. "CBC" does not tell this Problem Domain from another CBC one; "Backend" does.
- **Maintainer Repo renamed too.** Rejected: it keeps the texts of every Problem Domain, its own and the Backend Repos' (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2, *The Problem Domain layer*). A second Problem Domain adds a kit to it, not a second kind of Maintainer Repo.
- **The short forms dropped, or given the Problem Domain word.** Rejected: they do most of the work, about 730 uses in living text, and the full terms keep their length. A second kit's short form that collides is caught by the search run before any new Defined Term (`knowledge/problem-domain-ideas/keeping-knowledge/defined-terms-in-keeping-knowledge.md` §5, *Finding a definition*).
- **The two drafts named `system-repo-…` left as they are.** Rejected: the name is retired, and a search for the new one misses them. The simulation lives on through depth c, and the move costs 11 pointers.

## Decision

1. **System Repo becomes Backend Repo, and System Kit becomes Backend Kit.** The 9 Defined Terms built on them change with them, each keeping its length: Backend Kit Copy, Backend Kit Update Take, Backend Repo Reading. Backend Repo's definition names its Problem Domain, CBC backend design.
2. **Maintainer Repo and Maintainer Repo Register stay.**
3. **The 10 short forms stay,** Kit Copy, Repo Reading and the rest.
4. **`temp/common-ground/system-repo-change-flow.md` and `system-repo-change-simulation.md` become `backend-repo-change-flow.md` and `backend-repo-change-simulation.md`.**

## Consequences

- Every Living Text says the new names. History keeps the old: the devlog, the ADRs before this one, and the parts of `TODO-CONVERSATION-MEMORY.md`.
- The glossary's CBC Run, the twin of Backend Repo, is untouched; it goes in the rewrite.
- A second Problem Domain's kit needs short forms of its own that share no words with these.
