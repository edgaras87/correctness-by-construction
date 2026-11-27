# One home

<!--
What it is: a Backbone Idea, bound to no Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.1, The Backbone Idea layer).
Its place in the repo: knowledge/backbone-ideas/ (ADR-0084).
Why it is an idea of its own: both Problem Domains work by it, settling a disagreement with it (temp/rewrite-map.md §10, Shared questions, QUESTION-7).
Its first sources, input and not rules:
- the facts-in-sync manual, docs/conventions/facts-in-sync/README.md: its opening; What it is for; §1; §2; §3.1, but how a Fact Reference is written; §3.3; §3.4; §4, but its greps and the Foundation Line; §5, but where a disagreement is raised;
- the Idea-to-Output Model, docs/models/idea-to-output.md: §3.3, Settling a disagreement;
- three earlier drafts, read for ideas: temp/model-example/idea/one-home.md, its limits, the ways rejected and the three ways out; temp/model-example/this-repo/one-home.md; temp/model-example/approaches/change-a-home.md (PLAN.md, the facts-in-sync manual's Plan Step).
The decisions behind them: ADR-0039; ADR-0059; ADR-0065; ADR-0070; ADR-0072; ADR-0078.
What stands on it: its Problem Domain Ideas, one for each Problem Domain. Each points here, and never retells it.
How it is edited:
- It gives no example from one Problem Domain's work.
- It names no file that carries its rules to the agent: that is each Adapted Case's.
- A trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document says where a fact is written, and how every text that relies on it stays in agreement with it. It names no Problem Domain: each Problem Domain Idea adapted from it says how its own texts point, and how a change finds them.

Its neighbours: which text may point at which is the layers of knowledge's (`knowledge/backbone-ideas/layers-of-knowledge.md` §3, *The layers*); how a change moves between the layers is Change's (`knowledge/backbone-ideas/change.md`); which record holds which kind of fact, and what a decision record is, are records' (`knowledge/backbone-ideas/records.md`); how a Defined Term is shared is Defined Terms' (`knowledge/backbone-ideas/defined-terms.md` §4, *Where it is defined*).

## 1. Its Defined Terms

- **Fact Reference:** what a line carries when it relies on a fact written elsewhere: the address of the fact's home.
- **Living Text:** every text but history: text kept true as things change.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Defined Term | `knowledge/backbone-ideas/defined-terms.md` §1, *Its Defined Terms* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Pulled Channel | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Repo Tag | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. Why one home

A fact written in several places drifts. One copy changes, and the others do not. A reader meets two truths, and cannot tell which holds. Records that have drifted apart stop being trusted.

With one home, a fact read anywhere is the fact as its home states it today. A change is made once, in one place, and reaches every line that relies on it. Two copies cannot quietly disagree, and a reader knows where the truth is.

Two other ways were weighed:

- **Copies kept in step by hand:** every copy must be known and found, and nothing says where they are.
- **A fact widened until it fits every place that uses it:** it fits all, and helps none.

## 3. A fact and its home

Each fact has one home. Other texts point at it, and copy it only as a follower.

A copy is a follower when one text owns the fact and the other follows it, checked against it. There are two cases. The first is a copy that cannot be avoided, where two texts must each state the fact. The second is a retelling beside its Fact Reference, where the reader acts on the fact in place and a lookup would cost more than the retelling. A copy without a Fact Reference to its owner is a second home.

History is the records that say what was true then. They are never updated, so they cannot drift, and they are not a second home. They are not a first home either. Nothing changes at a history entry, so nothing would re-read what retells it. Each history file's header comment is Living Text.

**Rules:**

- Each fact has one home. Elsewhere, a text points at it.
- A summary says it is one. It names its owner, and nobody reads it in the owner's place.
- A fact changes at its home. What points at it does not change, unless the home moves (§5). Each retelling whose Fact Reference names it is found and re-read, with the paragraph around it.
- A copy is a follower, and carries a Fact Reference to its owner.
- A fact stated only in history gets a home in Living Text before anything retells it.
- Comments and configuration count too, not only records.

## 4. Pointing at a home

A text relies on a fact in one of two ways. It may touch the fact: then it points at the home, and does not restate it. It may make the fact usable, as an Instruction Text does: then it stands on the text that holds the fact, and names it (§7). A reader who finds a fact stated twice, with no Fact Reference between them, has found a defect.

A Fact Reference has two readers. The agent may follow it to read the fact whole, with no guarantee that it will (`knowledge/backbone-ideas/how-an-agent-works.md` §10.2, *On the Pulled Channel*, claim P1). A change to the home re-reads the line that carries it (§7). Any text that sends an agent to a file is a pointer. A Fact Reference is the kind written where a line relies on a fact.

A fact has one home, so a Fact Reference has one target: the home of the fact its line relies on. A line that relies on a claim about agents points at where agents are understood, not at a text that applies the claim. Which layer the target may sit in is the layers of knowledge's (`knowledge/backbone-ideas/layers-of-knowledge.md` §3, *The layers*).

**Rules:**

- A line that relies on a fact written elsewhere carries a Fact Reference to its home.
- A Fact Reference has one target: the home of the fact the line relies on.
- It is written in one form, so one search finds every line that points at a text. The form is each Problem Domain's.
- It is never a relative path: a relative path means another thing once the text is read from another root, as every copy is.
- A Fact Reference beside a retelling names the part of the home it retells, so a change re-reads only the retellings of the part that changed.
- A name in prose is not a Fact Reference.

## 5. When a home moves

A home moves when its text is renamed, or a part of it is renumbered or retitled, or a fact goes to a new home. Every Fact Reference to the old address then points at nothing, or at the wrong thing.

A word can be replaced across many texts at once. A search finds every place the word stood. Only a read finds a sentence the new word has made false.

**Rules:**

- A change that moves a home searches all Living Text for each old address, and fixes what points at it, in the same change.
- A change that replaces a word across texts re-reads each sentence it changes, for what it now claims.

## 6. Where a decision is cited

A text that rests on a decision cites the decision record that took it. The record is the home of the why, so a citation is a kind of Fact Reference. Where it goes depends on who reads the text.

**Rules:**

- An Understanding Text cites a decision inside its sentences. Its reader asks why, and the citation stands beside the claim it backs.
- A record does the same. Its reader follows the citation where it stands.
- An Instruction Text lists the decisions it rests on once, in a footer, and never inside a sentence. Its reader acts on the rule at the moment of work, and a citation gives nothing to act on. The footer keeps the why one look away for whoever changes the text. Each footer line names the part it backs, unless it backs the whole text.
- A repo cites a decision it holds. A decision inherited from another repo is adopted before it is cited. How another repo's decision is named, by its Repo Tag, is records' (`knowledge/backbone-ideas/records.md` §5, *The decisions*).
- A text sent to work in a repo that cannot open the decisions loses its footer there: its reader could not follow it. A form another repo fills cites nothing, since the citation would become a line of that repo's own record, pointing at nothing it can open.

## 7. What stands on a text

Some texts are how a thing is understood today, written down, and other texts stand on them: an Instruction Text on its Understanding Text, a lower idea on the higher one it adapts. Such a text states what is true now. How it came to be is history's. It may be wrong, or incomplete. It counts regardless: everything that stands on it agrees with it until it changes. It changes only for a reason that is recorded, and practice is the evidence. What stands on it applies it, and does not explain it.

A text that stands on another names it once, for the whole, and a line that uses one part of it carries a Fact Reference to that part. The two do different jobs. The name says which text to re-read whole when the text above changes. That finds what no single line shows: a fact gone missing, or a text that no longer holds together. The Fact Reference says which line to re-read when its part changes.

**Rules:**

- A text others stand on lists what stands on it. Where it cannot know them all, as with an idea other repos adapt, a search finds them.
- A text that stands on another names it once. A line that uses a part of it carries a Fact Reference to that part. Where every line of a section uses one part, the section carries it once.
- A change to a text finds, in the same change, what points at it and what stands on it, and re-reads each retelling whose Fact Reference names a changed part, with the paragraph around it. The change and its fixes share a change, or follow one after the other where the two may not share one (`knowledge/backbone-ideas/commit-messages.md` §4, *What shares a commit*).
- A change forced in a text below is checked back against the text above.
- A text that changes for it has its own re-reads in turn. They end when one finds nothing new.

## 8. A disagreement

A disagreement is a text that says other than the text it stands on or points at: a line beside its Fact Reference, a text below its text above, or practice beside the text it was done by. Either side may be the wrong one. The upper binds the lower, but being upper does not make it right, nor does being newer.

It is settled, never left standing. It ends when the two agree again, by changing the lower, the upper, or both. Practice is the evidence. A text that contradicts the one above it may have found the upper text's flaw rather than its own. So when practice and a statement disagree, the statement is a candidate for change, not the judge, and this text with it.

Where the lower side is wrong, there are three ways out:

- that place changes;
- the fact splits, and each place points at the part it needs;
- that place takes a fact of its own, and stops pointing.

**Rules:**

- A disagreement is raised where it is found, and decided, never defaulted.
- Neither side is right for being upper, nor for being newer.
- A fact is never widened until it fits every place: that place changes, the fact splits, or the place takes its own.
- When the upper text changes, its re-reads run again (§7).
- The decision is recorded where the repo records decisions.

## 9. Its limits

One home has a cost. Every place that points at a fact is judged when the fact changes, and a search can find a place but cannot judge it.

**Rules:**

- A fact with many places pointing at it is costly to change. Such facts are kept few, and stable.
- Small, settled facts, such as a definition, are pointed at. Reasoning changes often, and pointing at it carries every change to each place that points.
- Two places that need different things each hold a fact of their own, and neither points at the other.
