# Tiers Model

A structured description of how the workspace's repos relate: three
tiers, the top one empty today, each answering a different question,
with delivery flowing down and learning flowing up. Its job is to
answer, for any lesson or file, *which repo does this belong
to* — instead of each session re-deriving the picture.

A draft: revised when the Concept Garden earns machinery (§2.2, *Concept Repos*).

This is an Idea Model: the top Canonical Description of its chain. It binds
what stands on it. When the two disagree, either side may be
the wrong one (`docs/models/idea-to-output.md` §3.3, *Settling a disagreement*).

---

## 1. A drawing of the tiers

The drawing is judged not needed: the layers document in keeping
knowledge draws the repos and their layers
(`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
§2, *The picture*).

## 2. The tiers

### 2.1 The empty top tier

What a second Concept Repo does, and when a kit for them is weighed,
is the layers document's in keeping knowledge, its open question 1
(`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
§5, *Open questions*).

### 2.2 Concept Repos

A **Concept Repo** is one repo per concept. It keeps the full records
any project keeps, derived from the manuals (ADR-0042). It holds two
layers:

1. Its Canonical Descriptions: the plain-words statement of the idea,
   its rationale, its open questions, and the log of what changed it
   and why.
2. What is made usable from them: Agent Skills, checklists,
   templates, birth materials for projects that follow the concept.

Each states which concept version it derives from. No Run Repo's
work is done here.

The **Concept Garden** is whatever holds the Concept Repos together.
It is a plain folder with no records, no arrangement, and no agent of
its own, until something exists that belongs to no single concept. The
trigger is concrete: the second Concept Repo, and the first rule
written twice. This Idea Model, which maps the Concept Garden, moves there then.

### 2.3 Run Repos

A **Run Repo** is where a concept meets reality: a project or experiment that
took what a Concept Repo made usable and a Container Group copy, pinned to the versions it
took. A Run Repo's records are its own. What it learns about *the
concept* does not stay in the Run Repo: it is harvested.

## 3. The flows

What moves between tiers, and in which direction. Five facts hold
on every flow (§3.5, *What holds on every flow*). How it moves is
each repo's own convention:
here, for example, the Exchange Convention (`docs/conventions/exchange/`).

### 3.1 Downward delivery

Down is delivery, in two forms:

1. a copy, always pinned at a commit of the tier above. The copy also
   names the concept version it derives from, which the Concept Repo's
   own log sets;
2. a Delivery Fill: text written at birth into a file the Run Repo
   owns from then on. It is never re-copied. At the Run Repo's
   retrospective it is merged back by name into the playbook it came
   from. Here, for example, a playbook's Plan
Steps are written into a CBC Run's plan (`delivery/README.md` §2,
*Three ways a file lands*).

At a Run Repo's birth the two meet. Both are input to the Run Repo's
first decisions, which choose what to keep of them. Neither binds
it.

### 3.2 The Told Channel

The Told Channel is not delivery, and is unpinned by design
(`knowledge/backbone-ideas/how-an-agent-works.md` §3.4, *The Told Channel*). A tier above may hand a
Run Repo a warning as session input, after the Run Repo's own work
has missed it and is on record. The Run Repo's records say it was
told. A Run Repo that leans on it has the Told Channel's diagnostic.
A copy the Run Repo has edited between two Delivery Pins is not a
form of delivery either (§3.5, *What holds on every flow*, fact 4):
delivery comes down, and an edit is read from above.

### 3.3 Upward harvest

Up is the Record Harvest, and only through what the Run Repo committed:
its records, and the diff of its copies. The tier above reads them,
read-only, and the Run Repo sends nothing. A Run Repo's
surprise about the concept becomes a concept change, and what is
made usable is re-derived from it. A method lesson stops at the
Concept Repo while it holds the method. Work in one repo never edits
another as a side effect, up or down.

### 3.4 The Delivery Pin and documents

That the repo below cannot see the one above, and that each take
records the version it brings, is Change, in keeping knowledge's
(`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md`
§3.5, *Deliver the Kit Update*, and §3.6, *Take the Kit Update*,
item 4).

### 3.5 What holds on every flow

Each fact has its home in the layers:

1. **The tier below is blind:** Change, in keeping knowledge
   (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md`
   §3.5, *Deliver the Kit Update*).
2. **Nothing arrives by itself:** the same section, its *Staging*.
3. **Below holds copies; above holds Master Copies:** the layers
   document in keeping knowledge
   (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
   §1, *Its Defined Terms*, the Backend Kit).
4. **A copy is edited when it fails:** Change, in CBC backend design
   (`knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md`
   §2, *Changing a Kit Copy*).
5. **Nothing moves up as files:** Change, in keeping knowledge
   (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md`
   §3, *How a change travels*, its picture).

The one number, the Delivery Pin: Change, in keeping knowledge, §3.5,
*Deliver the Kit Update*, its *What a Kit Update is*.

## 4. What the Idea Model answers

### 4.1 Where a lesson lands

Where a lesson lands is Change's
(`knowledge/backbone-ideas/change.md` §3, *How the layers fill*)
and the layers of knowledge's
(`knowledge/backbone-ideas/layers-of-knowledge.md` §3.4, *The layer of work*).

### 4.2 The dependency rule

What crosses between the repos is Change, in keeping knowledge's
(`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md`
§2, *The arrows*). That each repo is one kind is the layers
document's in keeping knowledge
(`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
§3, *The layers*).
