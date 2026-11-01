# Commit plan: the last read's round 1, layer 1

## Summary — the state after all commits

The conventions manual, `docs/conventions/conventions/README.md`, meets the last read's round 1 findings: FINDING-1411 to 1418 (`temp/refinement-2026-10-18.md`, *The last read*, *The read's list*).

- **Its list of what derives** gives each entry its mark and its moment. The index entry says what the index holds, which is not a list of manuals.
- **Its references** use the one form: the path inside the parentheses, and root paths in *Where to look*.
- **Where the Foundation Line sits** is said once, in §1.3. The template and *Why it arrives this way* defer to it.
- **A convention's Work Approaches** are the Idea-to-Output Model's three: an Agent Skill, an Agent Rule, an Output Form. A CBC Run receives Work Approaches, not conventions.

The refinement file's *The work* names each finding's commit.

## Commits

**1. `docs(agent): add commit plan, round 1, layer 1`**
This file.

**2. `docs: conventions manual's list names its moments`**
FINDING-1413, 1414, 1415, 1418, all Wiring. *What this is made usable as* gives the index entry its mark and each entry its moment. The index entry stops claiming the index points at each manual. Two references take the path inside the parentheses: this manual's line 35, and the index's line 8, which has the same defect. *Where to look* splits its joined bullet into two lines, each a root path.

**3. `docs: Foundation Line's places as §1.3 gives`**
FINDING-1411, 1417, both stale. §1.2's frontmatter template points at §1.3 for the value, instead of giving the one value for a convention's Agent Skill. *Why it arrives this way* says the line sits in every file §1.3 names, not only in shipped Agent Skills and Agent Rules.

**4. `docs: a convention's Work Approaches, the model's`**
FINDING-1416 (Agreement) and 1412 (stale). §1's third kind becomes the Output Form, a record's form in its header comment, shipped in a Record Stub. An Agent Skill Template travels inside its Agent Skill. §3's steps 3 and 6 say a CBC Run receives Work Approaches, not conventions (DECISION-32). The Foundation Check runs here: §1 is a Canonical Description's part, so what retells it is walked.

**5. `docs(temp): round 1, layer 1's endings`**
*The last read* gains *The work (§2.7)*: each finding of this layer and its commit.

**6. `docs(agent): close commit plan, round 1, layer 1`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **The index's line 8 is fixed in commit 2,** though the index is layer 3. It is the same defect as FINDING-1415's line 35, and fixing a follower beside its source is what the Foundation Check asks.
- **The wording for FINDING-1412,** "the Work Approaches it received", is the one left B3, left G3 and FINDING-1539 take in layers 3 and 6, by the agent's call on 1539.
- **FINDING-1416's words** follow ADR-0078 decision 1, which took the model's words. The Agent Model's line 239 retells the old list. It is FINDING-1466 and left D5, in layer 3, and takes these words there.
- **The moments in commit 2:** the Foundation Line is read whenever its file is opened; the convention-manual Agent Rule loads when a manual is opened; the index is opened when a reader looks for the order the conventions act in.
