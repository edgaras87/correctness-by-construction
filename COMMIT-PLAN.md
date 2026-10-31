# Commit plan: the design of DECISION-19, 29 and 32

## Summary — the state after all commits

ADR-0078 is built and Accepted. The Idea-to-Output Model has a
convention as its manual's level, with the Work Approaches made from
it one level down, and the conventions manual follows: Agent Skill is
a Glossary Name, with Agent Skill Stage and Agent Skill Template, an
agent part is always named with its kind, and a new name never
repeats an old one. One rule for citing a decision stands in
facts-in-sync §3, carried by both one-home Agent Rules: a Work
Approach cites in its *Decisions* footer only, our Master Copies keep
their footers, and every delivery strips them, in the Pure Seed and
in `exchange-deliver`, whose list of changed copies leaves out a
footer-only change. Every
citation in living text follows the rule. The glossary is grouped by
who uses a Name; the shared, the concept's and method's, and the
stack's Names ship as three pinned copies under `docs/glossary/`, and
a CBC Run's `docs/glossary.md` holds only its own. Every candidate
word has been judged in one table, and each judged Name has its
entry.

Not here: giving old text its new Names. Round 3's work does that
file by file, with each file's findings (ADR-0078, decision 11).

## Commits

**1. `docs(agent): add commit plan for the design`**
This plan, once agreed.

**2. `docs: the Now line names the design`**
`PLAN.md`'s Now line moves from the endings to this plan. A records
commit of its own, since the agent's files and the records never share
one.

**3. `docs: a convention is its manual, in the model`**
`docs/models/idea-to-output.md` §6: a convention is the Canonical
Description of a way of working, its Work Approaches one level down
as for any Canonical Description (§2); §6 then gives only what differs
from the concept: where the manual lives, what reaches a CBC Run, what
it asserts, its having no version. "Artifacts" leaves the model. The
model is a Canonical Description, so the Foundation Check walks what
stands on it, and what the walk finds rides here or in commit 4.

**4. `docs: conventions manual takes Agent Skill`**
The conventions manual follows the model: §1 retitled *A convention's
Work Approaches*; §1.4 retitled *Agent Skill Stages*; the kind word
always; a new name never repeats a manual's, an Agent Skill's or an
Agent Rule's, checked by grep, and a new Agent Skill takes a verb.
The glossary gains Agent Skill, and Skill Stage and Skill Template
become Agent Skill Stage and Agent Skill Template, their entries and
homes changed in this commit, the exchange's §5.8 retitled with them.
The rename grep fixes every Fact Reference to the three retitled
sections.

**5. `docs: facts-in-sync holds the citation rule`**
facts-in-sync §3 gains a part for a decision citation, with ADR-0078's
six points; the conventions manual §1.1 points at it instead of
holding its own footer rule.

**6. `docs: the exchange strips footers at delivery`**
The exchange manual: a copy equals its Master Copy at the Delivery Pin
without its *Decisions* footer; the strip runs at Delivery Staging and
in the Pure Seed, and the Delivery Note's list leaves out a footer-only
change.

**7. `chore(agent): our files follow the design`**
Our side's Work Approaches: the one-home Agent Rule takes the citation
rule; `exchange-deliver` strips at staging and leaves a footer-only
change out of its list; `exchange-read` stays as it is, since a read
compares two stripped copies; `writing.md`'s rule 9 names Agent Skill Template;
`.claude/rules/convention-manual.md` follows the
manual's wording. An `agent` commit, apart from the records.

**8. `fix(delivery): the seed and shipped rules strip`**
The Pure Seed strips every copy's footer as it copies the container
and the groups; the container's one-home Agent Rule takes the citation
rule, from the CBC Run's side; the delivered-copies Agent Rule's rule 1
says a copy arrives without our footer. The shipped renames to Agent
Skill Template, rule 8's bold lead among them, quoted in 17 places, are
round 3's work, with each file's findings (ADR-0078, decision 11).

**9. `chore(agent): citations move to footers`**
The citation script, run over living text, lists every citation
breaking the rule; ours move: 5 in our Agent Skills, 8 in our
Approaches on Trial.

**10. `fix(delivery): shipped citations move to footers`**
The 20 in the Method Group's and Stack Group's files move to footers
of their own, stripped at delivery. ADR-0013 then stands in
cbc-bootstrap's footer.

**11. `fix(delivery): delivered Names as pinned copies`**
The shared Names leave the container's glossary record for
`delivery/container/docs/glossary/container.md`; the record keeps
*This project's own*, and its header points at the delivered files.
`delivery/method/docs/glossary/method.md` and
`delivery/spring-postgres/docs/glossary/stack.md` are created with
their headers, their entries to come. The exchange's §3.2, *What
goes*, names the three among the pinned copies, and the container's
`writing.md` names them in its rule 9, now that they exist.

**12. `docs: the glossary grouped by who uses a Name`**
Our `docs/glossary.md`: the Names only we use, the shared Names, and
one line per delivered group pointing at its file; the writing manual's
*What this is made usable as* and rule 9 name the files.

**12b. `chore(agent): our writing rule names the files`**
Our `writing.md`'s rule 9 names the glossary files, after the manual
it follows; `exchange-deliver` copies `docs/glossary/` with the other
pinned copies after birth, and lists it among the paths whose changes
the Delivery Note carries.

**13. `docs(temp): the Names table, <group> judged`** *(provisional)*
One commit per group, in this order: the concept's ten, the method's,
the stack's, the Agent Model's with the Names the decisions gave. The
table stands in the refinement's file under DECISION-19; each row a
two-word Name with its reason and compounds, or "English" with why.
Judged by the reviewer one group at a time; the exact split follows
the table.

**14. `docs: <group>'s Names enter the glossary`** *(provisional)*
After each group of 13 is judged: its Names into their file, the
delivered ones under `delivery/` as `fix(delivery)`, ours as `docs`;
the Agent Model's six channel titles take their Names, with the
rename grep. One commit per group, after its judging.

**15. `docs: ADR-0078 accepted`**
The final records commit: ADR-0078 Accepted, with what changed since
it was proposed.

**16. `docs(agent): close commit plan for the design`**
Deletes this file; the body records what diverged.

**17. `docs: devlog for the design`**
The session's entry, after the close.

## Decisions taken inside this plan

- **The renames of old text are not here.** Only the Names' homes,
  their glossary entries and the references to retitled sections
  change in this plan; every other use takes its new Name in round 3's
  work, file by file (ADR-0078, decision 11).
- **Three retitles,** each with its rename grep in its commit:
  conventions §1 *A convention's artifacts* to *A convention's Work
  Approaches*, 30 characters; conventions §1.4 *Skill Stages* to
  *Agent Skill Stages*; exchange §5.8 *Filling a Skill Template*, its
  new title chosen at commit 4 within 30 characters.
- **The citation script stays in the session's scratchpad,** as the
  sweep's scripts do; nothing commits a script.
- **The Names table stands in the refinement's file,** beside the
  decisions it carries out, and goes with that file at the
  refinement's close; the glossary keeps its outcome.
- **The agent's files and the shipped files land after the manuals
  they follow,** in commits of their own: a source before what
  derives from it.
- **The delivered glossary files are created empty in 11** and filled
  in 14, so the structure lands before the Names, and a judged group
  never waits on another. A text names them only once they exist.
