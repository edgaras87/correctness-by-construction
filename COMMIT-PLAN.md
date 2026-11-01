# Commit plan: the last read's work

## Summary — the state after all commits

Every finding of the last read has its ending: FINDING-1411 to 1795, 385 findings of all eight Finding Kinds (`temp/refinement-2026-10-18.md`, *The last read*, *The read's list*). Each fix follows its proposal, read with the decisions DECISION-41 to 54, the agent's calls and DECISION-49's pass. FINDING-1433, 1444 and 1487 end as the reviewer decides them.

The Change Set is written from the list (DECISION-54; `.claude/approaches-on-trial/refinement.md` §2.7, *Working the findings*):
- **pass 1, the shared facts:** each rule line a decision changes, and each fact told in more than one file, lands with its home and every copy in one commit, so no commit leaves the repo disagreeing with itself;
- **pass 2, each area once:** every other finding, all three Refinement Rounds together, one area of files a commit. Where findings of two Refinement Rounds touch the same lines, the edit takes them in Refinement Round order.

Every commit body names its findings. *The work*, written once from `git log` at the end, names each finding's commit. Then the last read is read again (§2.9).

## Commits

**1. `docs(agent): add commit plan, round 1, layer 1`**
Landed, `f92d6b7`, as one layer's plan.

**1b. `docs(agent): revise commit plan — the Change Set`**
This revision, by DECISION-54. It replaces the plan of `f92d6b7`, whose commits 2 to 6 never landed.

**1c. `chore(agent): the refinement's Change Set from its list`**
Landed, `00c0b07`, before this revision, on the reviewer's word: refinement.md §2.7 and §2.9 say what DECISION-54 chose. Its subject is 55 characters, past the limit of 50; so is `cf3ca66`'s, 53, before the plan. Both were not counted when written.

**1d. `docs: glossary's Refinement Layer, listed together`**
Landed, `39fbf9e`: the glossary entry follows 1c.

### Pass 1: the shared facts

A family that reaches an agent file or a shipped file lands as two or three commits in a row, one per scope: `docs`, `chore(agent)`, `fix(delivery)`. Each is coherent alone and the next lands at once.

**2. `docs: facts-in-sync's rules take the decisions`**
Facts-in-sync §3.1: a shipped reference opens with "the Concept Deliverer's" (DECISION-41, FINDING-1447); a numbered rule is cited by its number and its lead, cut at 30 characters (FINDING-1553). §3.2 gains DECISION-45's lines. §3.4 names the Output Shape (FINDING-1517). The Foundation Check runs here.

**2b. `chore(agent): our rules follow facts-in-sync`**
The convention-manual Agent Rule's retelling of §3.2; our one-home Agent Rule, rule 7.

**2c. `fix(delivery): shipped lines follow facts-in-sync`**
The container's one-home comment, lines 12–13 (FINDING-1447); the 17 shipped references to a rule's lead (FINDING-1553).

**3. `docs: writing manual takes the decisions`**
Rule 9's "a bold lead" (DECISION-46); rule 6 (FINDING-1456); rule 10 names a record's fixed headings for the CBC Run's seat (FINDING-1535); *What this is made usable as* names the container's glossary (FINDING-1453); the kind word in rule examples (FINDING-1728).

**3b. `chore(agent): our writing rule follows its manual`**
Rules 6 and 9, *Where it applies* names the delivered glossaries (FINDING-1520), rule 6's example takes the kind word (FINDING-1755).

**3c. `fix(delivery): container's writing rule follows`**
Rules 6, 9 and 10; its rule 9 example takes the kind word (FINDING-1763).

**4. `docs: a CBC Run receives Work Approaches`**
FINDING-1412, 1416, 1591 in the conventions manual; 1437, 1596 in agent-arrangement; 1466 in the Agent Model; 1729 in the Idea-to-Output Model: a convention's Work Approaches are an Agent Skill, an Agent Rule and an Output Form, and a CBC Run holds Work Approaches, not conventions.

**4b. `fix(delivery): the container holds Work Approaches`**
FINDING-1527, 1539: the container's Decisions Log, its `CLAUDE.md` line 54, its glossary, and the Pure Seed's prompt and commit subjects.

**5. `docs: Agent Skill Stages from Stage 0, by §1.4`**
FINDING-1525, the conventions manual's half: §1.4 says a first stage is Stage 0 only when it checks readiness, and gives the heading's case.

**5b. `chore(agent): exchange Agent Skills' headings`**
FINDING-1525, our half: the exchange-read and exchange-deliver headings follow §1.4.

**6. `chore(agent): our rules name delivered glossaries`**
FINDING-1516, 1518: the Foundation Check's step 1 names the delivered Glossary Names files and the playbook; our one-home Agent Rule's example of what goes names the Glossary Names.

**6b. `fix(delivery): delivered-copies covers glossaries`**
FINDING-1529: its `paths:` gains `docs/glossary/**`. With 6c, the glossary's place is in every list that names what goes.

**6c. `docs: records name the delivered glossaries`**
FINDING-1436 in agent-arrangement, 1478 in `ARCHITECTURE.md`.

**7. `docs: trials point at their TODO items`**
DECISION-48: FINDING-1425, 1431 in project-recording, 1451 in the retrospective manual; the TODO item "Run this repo's retrospective" takes its new trigger, the refinement Plan Step's close.

**7b. `chore(agent): auto-run's rejection says when`**
FINDING-1513.

**8. `docs: CBC Run Birth, the event`**
FINDING-1458: the glossary entry widens to the event, as DECISION-36 reads it.

**8b. `fix(delivery): the Pure Seed's CBC Run Birth`**
FINDING-1542.

**9. `fix(delivery): a Name's home in the CBC Run's seat`**
DECISION-47: FINDING-1650, 1651, 1652, 1758, 1765. The container's glossary entries point at their homes; the bold stays at the home.

**10. `chore(agent): held Agent Skills take references`**
DECISION-42 and the Layout and One home findings in the three copies held identical: FINDING-1633, 1634, 1635, 1636, 1639, 1640, our side.

**10b. `fix(delivery): the container's held copies follow`**
The same, the container's side: FINDING-1643, 1644, 1645, 1647, 1648, 1649. After it, the pairs differ only as ADR-0069 allows.

**11. `docs: exchange and delivered-copies agree`**
FINDING-1531, 1530, the manual's side: the Decisions Log entry's contents, one list; the Receipt Branch step. FINDING-1444 joins once the reviewer decides it.

**11b. `fix(delivery): delivered-copies and its glossary`**
The same, the container's side: rule 5's step 6, the Receipt Branch step and its glossary entry.

**12. `docs: the rules-in-force list's place`**
FINDING-1537, the manual's side: agent-arrangement §3.4 names it as the one part of the log not appended.

**12b. `fix(delivery): retrospective and the Record Stub`**
FINDING-1537, 1538, the container's side.

**13. `docs: the devlog in short sentences`**
FINDING-1705, 1731: project-recording §4.4 and `devlog/README.md`, by ADR-0079's doubt 8.

**13b. `fix(delivery): the devlog Record Stub follows`**
FINDING-1766.

**14. `docs: a fact the agent misses by not noticing`**
FINDING-1714, agent-arrangement §2.4, in the words FINDING-1751 then takes.

**14b. `chore(agent): our Entry File's three tests`**
FINDING-1751, 1752.

**15. `docs: "Real question" in plain words`**
FINDING-1740, TODO's side.

**15b. `chore(agent): auto-run's "Real question", plain`**
FINDING-1748.

### Pass 2: each area once — provisional

Each commit takes every remaining finding of its files, of all three Refinement Rounds. Split at its boundary when it passes about 15 findings or a diff too long to review.

**16. The conventions manual and the index.** FINDING-1411, 1413 to 1415, 1417, 1418, 1588 to 1590, 1703, 1704, 1724.

**17. Project-recording.** FINDING-1419 to 1424, 1426 to 1430, 1432, 1592, 1593, 1706 to 1709: DECISION-51's dated counts among them.

**18. Agent-arrangement, commit-messages and commit-plan.** FINDING-1434, 1435, 1438 to 1443, 1595, 1597 to 1600, 1715 to 1717.

**19. Exchange and facts-in-sync.** FINDING-1445, 1446, 1601 to 1603, 1718 to 1723.

**20. Repo-hygiene and its template, retrospective, shapes, visual-comparison, writing.** FINDING-1448 to 1450, 1452, 1454, 1455, 1457, 1604 to 1615, 1725.

**21. The glossary and the Idea Models.** FINDING-1459 to 1465, 1467 to 1473, 1616 to 1618, 1726, 1727, 1730.

**22. The concept chapters.** FINDING-1594, 1710 to 1713, each editorial; FINDING-1433 once the reviewer decides it, a concept change with its CHANGELOG line.

**23. `ARCHITECTURE.md` and `README.md`.** FINDING-1474 to 1477, 1479, 1485, 1486, 1619 to 1622, 1735: the archive's fact gets its home.

**24. `PLAN.md`.** FINDING-1480 to 1484, 1732 to 1734.

**25. `TODO.md`.** FINDING-1490 to 1511, 1623 to 1626, 1738, 1739, 1741 to 1747, with DECISION-49's pass. Likely two commits: the pass, then the rest.

**26. `temp/README.md` and the Conversation Memory.** FINDING-1487 once decided, 1488, 1489, 1736, 1737.

**27. Our Agent Rules, `CLAUDE.md` and the Decisions Log, `chore(agent)`.** FINDING-1514 declined, 1515, 1519, 1628 to 1632, 1753, 1754; an entry in `.claude/decisions.md` where how this repo's agent works changes.

**28. Our Agent Skills and Approaches on Trial, `chore(agent)`.** FINDING-1512, 1521 to 1524, 1627, 1637, 1638, 1749, 1750.

**29. The container's Agent Rules and Agent Skills.** FINDING-1526, 1528, 1532 to 1536, 1641, 1642, 1646, 1759 to 1762, 1764.

**30. The container's Record Stubs and glossary.** FINDING-1540, 1541, 1756, 1757, 1767, 1768.

**31. The Pure Seed, the playbook and `delivery/README.md`.** FINDING-1543 to 1546, 1570, 1571, 1653 to 1659, 1668 to 1671, 1769, 1770.

**32. The Method Group's Output Shapes.** FINDING-1547 to 1552, 1660 to 1663, 1771, 1772: DECISION-52 lands here.

**33. The cbc-framing Agent Skill.** FINDING-1553 to 1562, 1664 to 1666, 1773 to 1782, the worked example in both copies.

**34. The cbc-slice Agent Skill and the method's glossary.** FINDING-1563 to 1569, 1667, 1783, 1784.

**35. The cbc-bootstrap Agent Skill.** FINDING-1572 to 1579, 1672 to 1694, 1785 to 1789: DECISION-44's counts.

**36. The infra-establish and infra-serve Agent Skills and the stack's glossary.** FINDING-1580 to 1587, 1695 to 1702, 1790 to 1795.

### The close

**37. `docs(temp): the last read's work`**
*The work (§2.7)*: each finding and its commit, from `git log`; the count of endings.

**38. `docs(agent): close commit plan, the last read`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **A family opens a file pass 2 opens again.** Pass 1 commits touch only the lines of their fact, so a revert stays coherent. Pass 2 then takes the file's other findings. About 20 files are opened twice this way, against most of 61 under DECISION-53.
- **The Method Group's and the Stack Group's own shared facts** go in pass 2, in their area's commits, since each stays inside one area. Pass 1 holds facts that cross areas.
- **The finding lists above are the agent's first sort.** Each commit checks its list against *The read's list* when it opens; a finding found to belong elsewhere moves, and the close says so.
- **The three findings left to the reviewer,** FINDING-1433, 1444 and 1487, are asked when their commit opens; that commit waits for the answer.
- **About 52 commits, not 33.** Laid out, the scope splits (agent files apart, shipped files apart) add 17 follower commits the estimate left out. Under DECISION-53 it would have been about 70.
