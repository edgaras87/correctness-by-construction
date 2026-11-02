---
name: infra-serve
description: Add, change, or remove an Infrastructure Service or capability on an ALREADY-ESTABLISHED Runtime Ground. A new dependency found during the project's build (a cache, a queue, a second datastore, a broker, an extension, a new port or capability on an existing service) re-enters the original evaluation from need, as one logged decision, with the manuals grown from the setup as done. Use whenever the user wants to add infrastructure to a project whose Runtime Ground already stands, such as "we need Redis now", "add a message queue", "the new slice needs X", "open another port", "bump the postgres version", even if it sounds like a small compose edit. An Infrastructure Service Re-entry is the normal case, never a failure of the first pass. Do NOT use for the first Infrastructure Establishment (the infra-establish Agent Skill), or for application or schema work: that is building, not the Runtime Ground.
foundation: practice, checked against concept v1
---

# Infrastructure Service Re-entry — keeping an established Runtime Ground

The Runtime Ground stays governed after it stands: **every new
dependency re-enters the evaluation.** It is the same question from
need that Infrastructure Establishment asked, one logged decision, and
the manuals grown. Nothing joins the Runtime Ground because it was
easy to add.

## Stage 0 — the Runtime Ground stands?

Check:

1. **The Runtime Ground's record exists,** with the original
   evaluation of Infrastructure Services and its Infrastructure
   Service Exclusions: the Infrastructure Establishment Log, or, in a
   repo with records, the ADR that holds the evaluation
   (`.claude/skills/infra-establish/SKILL.md`, *Records and outputs*).
2. **The Infrastructure Contract and the Operator Manual exist.**
3. **The Runtime Ground comes up now:** `podman compose ps`, or the
   project's equivalent. Read the actual output.

Any missing: this is not an Infrastructure Service Re-entry. Run the
infra-establish Agent Skill, or repair the record first.

Check the original evaluation. If the wanted service is an
Infrastructure Service Exclusion, the new need must answer the old
Infrastructure Service Exclusion's why: name what changed. If it is not answered, the
Infrastructure Service Exclusion stands, and the request is refused with that reasoning.

## The Infrastructure Service Re-entry, one pass

1. **Need.** What Invariant Slice, invariant, or environment fact
   demands this? Concretely: what must the evidence or the system now
   be able to *do* that the current Runtime Ground refuses? "We'll
   probably need it" is not a need. Refuse anticipation, even when it
   is cheap. Removals and version changes take the same question in
   reverse: what need does the current shape no longer serve?
2. **Decision.** One entry in the Runtime Ground's record: an
   Infrastructure Establishment Log entry, or an ADR in a repo with records. It holds:
   - the need;
   - the service, or change, that answers it;
   - what was considered and excluded, each with its why.

   The reviewer's confirmation is the verdict.
3. **Constraints.** The new service gets its Infrastructure Service
   Constraints named, with their enforcement mechanisms. Where a
   reference exists, it is the default, unless a project fact defeats
   it: for a datastore, the Database Role Split,
   `.claude/skills/infra-establish/references/postgres-role-split.md`.
   A changed service gets its existing Infrastructure Service
   Constraints checked again against the change.
4. **Stand up, and verify both ways.**
   - The Runtime Ground's files are written as complete files, never
     fragments.
   - Secrets are split out.
   - Then the Catalog Check *and* the Behavioral Check for the new
     capability: the expected result stated before running, the
     outcome read from actual output.

   A service family used before may have a walkthrough among
   `.claude/skills/infra-establish/references/`. Consult it. Never
   force its shape on a different service.
5. **Grow the manuals.**
   - The Infrastructure Contract gains or amends the service's
     section, in the form
     `.claude/skills/infra-establish/SKILL.md`, *Records and outputs*,
     gives it.
   - The Operator Manual gains the setup as done, and any new reset
     path.
   - If the project keeps a public setup guide, derive it again from
     the Operator Manual. The manual stays its only home.

## Hard lines

1. Never frame the problem again.
2. Never build the system: the Runtime Ground ends where application
   code and schema content begin.
3. Destructive acts need explicit confirmation
   (`.claude/skills/infra-establish/SKILL.md`, *The rule for results…*).
4. Installs on the host are the reviewer's own acts
   (`.claude/skills/infra-establish/SKILL.md`, *The rule for results…*).
5. Project files are written in the language the project's records are written in.
6. One logical change per commit, with a commit message drafted for
   each.
