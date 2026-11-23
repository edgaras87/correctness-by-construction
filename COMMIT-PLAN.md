# Commit plan: System Repo and System Kit become Backend Repo and Backend Kit

## Summary — the state after all commits

The two names carry their Problem Domain, CBC backend design. A second Problem Domain no longer makes them ambiguous. Every Living Text says Backend Repo and Backend Kit: the Maintainer Repo's layers document, which defines them, three of the four drafts in `temp/common-ground/`, and `TODO.md`. The frozen `between-repos-simulation.md` keeps the old names: there they mean a repo and a kit for any kind of system, and one line of its header says so. The 9 Defined Terms built on them change with them, each keeping its length: Backend Kit Copy, Backend Kit Update Take, Backend Repo Reading. The two drafts named `system-repo-…` are named `backend-repo-…`.

What stays:
- Maintainer Repo, Maintainer Repo Register, and the 10 short forms, such as Kit Copy and Repo Reading;
- history: the devlog, the ADRs, and the parts of `TODO-CONVERSATION-MEMORY.md`.

ADR-0086 records the four decisions and the options rejected. The TODO item "Rename System Repo and System Kit" leaves TODO. The Change idea's split loses half of its trigger.

Measured on 2026-11-23, by `git grep` over the text unwrapped: 685 uses in 6 living files. The layers document has 269, `between-repos-simulation.md` 141, `common-ground-problem.md` 104, the simulation 80, the flow 65 and `TODO.md` 26. Two of them are broken across lines.

## Commits

**1. `docs(agent): add commit plan for Backend Repo`**
This plan, agreed before any of the work.

**2. `docs: ADR-0086, Backend Repo and Backend Kit`**
ADR-0086, Proposed. It holds the four decisions taken in the chat on 2026-11-23:
1. the names, with CBC Backend Repo and CBC Backend Kit rejected, since 5 of the 11 Defined Terms would pass 4 words;
2. Maintainer Repo stays, since it keeps every Problem Domain's kit;
3. the 10 short forms stay, since a collision is caught by the search before a new Defined Term;
4. the two drafts renamed.

It goes first because the decisions were settled in the chat.

**3. `docs: rename the two system-repo drafts`**
`git mv` of `temp/common-ground/system-repo-change-flow.md` and `system-repo-change-simulation.md` to `backend-repo-…`. The 11 living pointers to the simulation follow: 8 in the layers document, and 1 each in `TODO.md`, the problem file and the flow. Nothing points at the flow from Living Text. Kept apart from the word sweep, so git shows a pure move with 11 changed pointer lines.

**4. `docs: Maintainer layers doc says Backend Repo`**
The 269 uses in `layers-of-knowledge-in-keeping-knowledge.md`, the home of the definitions. §1's 11 definitions are re-read for what each now claims. Backend Repo's definition gains its Problem Domain (below). Kept apart from the drafts because the definitions are the one part to read closely.

**5. `docs: 3 drafts say Backend Repo and Backend Kit`**
The 249 uses in the problem file, the simulation and the flow. Their own titles change with them, such as *What the Backend Kit holds*; every living pointer to them is in the same files. The problem file's list of Defined Terms is sorted again, as it says it is. In the pictures, a column's rule under "Backend Repo" grows by one. The frozen `between-repos-simulation.md` is not swept: its header gains one line saying it keeps the old names, and the simulation's 2 pointers to its titles keep them too.

**6. `docs: TODO follows Backend Repo and Backend Kit`**
The 26 uses in `TODO.md`. The rename item leaves TODO. The Change idea's split keeps one trigger: the layers model out of `temp/`.

**7. `docs: ADR-0086 accepted`**
The final records commit. Its status names anything changed since it was proposed: the frozen draft kept out of the sweep.

**8. `docs(agent): close commit plan for Backend Repo`**
Deletes this file. The body records what diverged. Before it, the sweep: every old name, `system-repo-change-` and each changed title, grepped unwrapped over Living Text. The frozen draft, and pointers to its titles, keep the old names.

## Decisions taken inside this plan

- **Backend Repo's definition gains its Problem Domain.** Today: "a repo where a real system is built by the concept, working from copies of the System Kit". Proposed: "a repo of CBC backend design, where a real system is built by the concept, working from copies of the Backend Kit". The TODO item already says it: "Until the rename, a System Repo is a repo of CBC backend design". The other 10 definitions change only their words.
- **The frozen simulation is not swept.** Revised at commit 5: it was written when a System Repo could be of any kind of system, and it says so throughout, such as "what each System Kit is for. Today there is one, for backends". Renamed, it reads wrong. Its TODO item reworks it when it resumes.
- **The definitions and the drafts are two commits, not one.** Between commits 4 and 5 the drafts still say System Repo. The problem file then names Defined Terms the layers document no longer defines. A revert of commit 5 leaves the same. The gain is a diff of 269 lines whose definitions the reviewer reads closely, apart from 249 mechanical ones. Merging them is the other way.
- **No Plan Step, on main.** As the commit plan for `knowledge/` ran.
- **The Foundation Check finds nothing to read.** No staged file has a Foundation Line, and none is a Canonical Description. Its *A moved section* part runs at commits 3 and 5, and the close sweep repeats it.
- **The glossary is untouched.** It lists neither name. Writing rule 9 does not apply under `knowledge/` (ADR-0085).
- **The sweep is one perl script.** It replaces `System(\s+)(Repo|Kit)` with `Backend$1$2` over whole files, so a wrapped name is caught. Headings, references and code fences are counted before and after, and a second run changes nothing.
