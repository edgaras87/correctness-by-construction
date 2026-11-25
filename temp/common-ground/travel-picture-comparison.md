# How a change's travel between the repos is shown: a visual comparison

<!-- A visual comparison's draft (.claude/skills/visual-comparison/SKILL.md), commit 8i of the commit plan for the Change split. It settles how Change, in keeping knowledge, knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md, shows a change travelling between the Maintainer Repo and the Backend Repos, now that the layers picture draws only what is where (ADR-0088, decision 8), and whether the simulation's picture The whole flow moves there or goes. It goes once the outcome is recorded, in the commit that places the winner. -->

## 1. The defect

Since the keeping-knowledge layers picture lost its arrows, nothing in Change, in keeping knowledge draws how a change travels between the two repos. It says it in a list of arrows (§2) and two tables (§3: the six parts, and the arrows each depth travels). The simulation's picture *The whole flow* draws the six parts across the two repos, with a chart of how high each depth goes, but it sits in a draft that goes once depth c is done. A form that answers no better than today's text loses to it.

## 2. What the reader must get

Each is stated so a candidate can fail it.

1. **The two repos, and which part each does:** the Backend Repo changes a Kit Copy and takes the Kit Update; the Maintainer Repo reads, judges, acts and delivers.
2. **The six parts in order,** one round: Change a Kit Copy, Read Copy Changes, Judge Copy Changes, Act on the verdicts, Deliver the Kit Update, Take the Kit Update.
3. **What crosses between the repos, and which way:** the Maintainer Repo reads the Backend Repo and writes nothing there; a Kit Update comes back only into the Backend Repo's `temp/`.
4. **The arrows between the repos by layer:** *Copy Change, read back*, layer 4 to layer 3; *Kit Update* and *birth*, layer 3 to layer 4 (§2).
5. **The two jobs:** a Look for Lessons is Read, Judge and Act; bringing a Backend Repo up to date adds Deliver and Take, and needs the first (§3).
6. **Nothing redrawn from the layers picture:** what each layer holds, and where each is kept, is not drawn again.

## 3. The candidates

Each is built whole. A is today's form, where "nothing wins" lands.

### Candidate A: today's text

Change, in keeping knowledge §2 and §3's opening, as they stand:

**§2, The arrows**

- **adapt,** **lesson** and **set apart,** between layers 1, 2 and 3: as Change has them (`knowledge/backbone-ideas/change.md` §4, *The arrows*). A lesson, or a part set apart, can come from the Backend Kit's Adapted Cases or from the Maintainer Repo's own.
- **birth,** layer 3 to layer 4: a new Backend Repo receives Kit Copies of the Backend Kit, at one Backend Kit Version.
- **Kit Update,** layer 3 to layer 4: a Backend Kit Update (the layers document's §3) brings a Backend Repo's Kit Copies to a newer Backend Kit Version. The Backend Repo takes it by its own Kit Copy of the Adapted Case for taking a Kit Update.
- **Copy Change, read back,** layer 4 to layer 3: a Backend Repo changes a Kit Copy and records why. The Maintainer Repo reads it back and judges it against the Adapted Case the Kit Copy came from.
- **adapt,** **lesson** and **set apart,** between layer 2 and layer 4, for the Maintainer Repo's own Adapted Cases: they are written from its Problem Domain Ideas, and its lessons, and the parts it sets apart, go up to them (`knowledge/backbone-ideas/change.md` §4, *The arrows*).

**§3, How a change travels**

A Copy Change travels through six parts, each done by one repo. Each part sits at a layer, or on an arrow of §2:

| Part | Who | Where |
|---|---|---|
| Change a Kit Copy | Backend Repo | layer 4, in a Kit Copy |
| Read Copy Changes | Maintainer Repo | the arrow *Copy Change, read back* |
| Judge Copy Changes | Maintainer Repo | layer 3: which layer the Copy Change holds for |
| Act on the verdicts | Maintainer Repo | the layer the verdict names; the arrows *lesson* and *adapt* |
| Deliver the Kit Update | Maintainer Repo | the arrow *Kit Update* |
| Take the Kit Update | Backend Repo | layer 4, its Kit Copies |

So the six parts are one movement: up from layer 4, as high as the Copy Change holds, and back down.

**The Look for Lessons.** Read Copy Changes, Judge Copy Changes and Act on the verdicts make one pass over one Backend Repo, the Look for Lessons. It starts when the human names a Backend Repo, for its lessons or to update it. It ends once Act on the verdicts is done, which sets the *settled snapshot* to the stop (§3.2). It falls into one of three cases (§3.2). Deliver the Kit Update and Take the Kit Update are outside it.

**Bringing a Backend Repo up to date.** It is a second job, which needs the first. It runs only when the human names the Backend Repo to update, and starts with a Look for Lessons. Its check, whether a Kit Update is due, belongs to Deliver the Kit Update. It comes after Act on the verdicts, since the Backend Kit moves for a Copy Change only once it is judged and acted on (§3.5).

Each of the simulation's depths names the highest layer a Copy Change reaches (§3.7). The arrows each travels:

| Depth | Arrows it travels |
|---|---|
| a. it stays in the Backend Repo | *Copy Change, read back*; nothing comes down |
| b. the Backend Kit's Adapted Case changes | *Copy Change, read back*; *Kit Update* |
| c, at layer 2. the idea above changes: its Problem Domain Idea | *Copy Change, read back*; *lesson*; *adapt*, to every text built on that idea, the Maintainer Repo's own when they stand on it; *Kit Update* |
| c, at layer 1. the idea above changes: its Backbone Idea | *Copy Change, read back*; *lesson*, twice; *adapt*, to every text built on that idea, the Maintainer Repo's own when they stand on it; *Kit Update* |
| d. the idea above already holds it | *Copy Change, read back*; *adapt*; *Kit Update* |
| e. it asks to narrow the idea above | *Copy Change, read back*; *Kit Update* |
| f. several Adapted Cases need it, but not all | *Copy Change, read back*; *Kit Update* |

Depth f's gap, text shared by several Adapted Cases of one Problem Domain but not all, is §3.7's, its row f.

### Candidate B: The whole flow's top half

```
 Backend Repo              ┆ Maintainer Repo
 ────────────              ┆ ───────────────
                           ┆
 1. Change a Kit Copy ─────┼── reads; writes nothing there ──▶ 2. Read Copy Changes ──▶ 3. Judge Copy Changes ──▶ 4. Act on the verdicts
    §3.1                   ┆                                   §3.2                     §3.3                      §3.4
                           ┆                                                                                      │
 6. Take the Kit Update ◀──┼── writes only into its temp/ ──── 5. Deliver the Kit Update ◀────────────────────────┘
    §3.6                   ┆                                   §3.5
```

Key: each § is a section of this document. A Look for Lessons is 2 to 4; bringing a Backend Repo up to date adds 5 and 6, and needs the first.

### Candidate C: The whole flow whole

```
 Backend Repo              ┆ Maintainer Repo
 ────────────              ┆ ───────────────
                           ┆
 1. Change a Kit Copy ─────┼── reads; writes nothing there ──▶ 2. Read Copy Changes ──▶ 3. Judge Copy Changes ──▶ 4. Act on the verdicts
    §3.1                   ┆                                   §3.2                     §3.3                      §3.4
                           ┆                                                                                      │
 6. Take the Kit Update ◀──┼── writes only into its temp/ ──── 5. Deliver the Kit Update ◀────────────────────────┘
    §3.6                   ┆                                   §3.5

 How high each depth goes: 3. Judge Copy Changes sets it, 4. Act on the verdicts changes it

 depth                          b        c, at 2   c, at 1   d         e         f
                                         └─────────── not yet checked ────────────┘
 layer 1  Backbone Idea                            ●
 layer 2  Problem Domain Idea            ●         ●         ○         ○
 layer 3  Adapted Case          ●        ●         ●         ●         ●
 layer 4  a Backend Repo's work ●        ●         ●         ●         ●         ●
 ───────────────────────────────────────────────────────────────────────────────────────────
 highest layer                  3        2         1         3, or 2   3, or 2   none, open
```

Key: as B's. ● is a Copy Change's path, from its Kit Copy up to the highest layer it changes; ○ is "or up to here", when the case asks it (§3.7, its rows d and e). At every depth, 5. Deliver the Kit Update brings a Kit Update down.

### Candidate D: a new box drawing

```
              the Maintainer Repo                     ┆               a Backend Repo
              ───────────────────                     ┆               ──────────────
                                                      ┆
            ┌─────────────────────────────────┐       ┆
 Layer 3    │ the Backend Kit                 │       ┆
            │ 3. Judge Copy Changes           │       ┆
            │ 4. Act on the verdicts          │       ┆
            └─────────────────────────────────┘       ┆
                    │                 ▲               ┆
                    │                 │               ┆
                    │                 └───────────────┼─── 2. Read Copy Changes, reading only ────┐
                    │                                 ┆                                           │
                    │                                 ┆                                           │
                    └── 5. Deliver the Kit Update ────┼───────────────▶ temp/                     │
                                                      ┆                   │ 6. Take the Kit Update│
                                                      ┆                   ▼                       │
                                                      ┆     ┌───────────────────────────────────────────────┐
 Layer 4                                              ┆     │ its work, by its Kit Copies                   │
                                                      ┆     │ 1. Change a Kit Copy                          │
                                                      ┆     └───────────────────────────────────────────────┘
```

Key: a box names a layer's texts in one repo, never what they hold, which is the layers document's picture. *Birth*, a new Backend Repo's first Kit Copies, takes 5's path once. A Look for Lessons is 2 to 4; bringing a Backend Repo up to date adds 5 and 6, and needs the first.

## 4. The verdicts

Each turns on a requirement of §2. Every verdict on how a candidate looks is a prediction until the reviewer has rendered it.

| Requirement | A, text | B, flow's top | C, flow whole | D, new drawing |
|---|---|---|---|---|
| 1. which repo does which part | holds, a table column | holds, by side | holds, by side | holds, by side |
| 2. the six parts in order | holds, numbered rows | holds, numbered on one loop | holds, as B | holds, numbered, the loop read by the numbers |
| 3. what crosses, which way | holds, in words across §3 | holds, both crossings labelled | holds, as B | holds in part: "reading only" and "temp/" drawn, "writes nothing there" in its label's words only |
| 4. the arrows by layer, *birth* among them | holds, §2's list | fails: no layers | fails, as B; its chart shows depths, not these arrows | holds: layer 3 to 4 and back; *birth* by the key |
| 5. the two jobs | holds, two paragraphs | holds, by the key | holds, by the key | holds, by the key |
| 6. nothing redrawn | holds | holds | holds | holds: names only |

Prediction: B shows the loop most plainly, and fails 4. C adds a chart §3.7's table already holds, so it says one thing twice, in two forms. D holds every requirement; prediction: it reads busier than B, its two paths crossing to reach the Backend Repo's box. A holds every requirement in words, and shows no loop.
