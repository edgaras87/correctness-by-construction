# Other patterns for the same problem

<!-- A draft: patterns from shared code and technical writing that
     answer the problem the sockets answer, keeping texts that rely on
     each other cheap to change. What each would mean here, what it
     gives, what it costs, and a mix. The sockets:
     temp/model-example/sideways-pointers.md §5, Sockets and plugs. -->

None of these rules out sockets. The best answer is likely a mix.

## 1. Single-sourcing

From technical writing; the best-known standard is DITA, used for
large product manuals.

- **How it works:** small typed pieces, each written once: a concept
  says what and why, a task gives steps, a reference holds facts. A
  map for each product names the pieces its manual takes. Lines marked
  for one audience or product are kept or dropped when the manual is
  built.
- **Here:** the concept pieces are ideas, the task pieces Work
  Approaches, a map a project text, and lines marked by audience the
  seats.
- **Gives:** the shipped Work Approach is built from its idea and its
  project text. The agent reads one finished text, with no pointer
  left in it. This answers how a Work Approach ships.
- **Costs:** a build step and its tooling. Text stitched from pieces
  can read unevenly.

## 2. Versions and pinning

How a package manager keeps shared code.

- **How it works:** each idea carries a version. A project text pins
  the version it was written against. A change that breaks its users
  raises the version's first number, and each project moves when it
  chooses.
- **Gives:** a change does not hit everything at once. Upkeep runs
  when the project is ready.
- **Costs:** two versions alive at once, for a while.
- **Here already, in part:** the project text's *Draws on* line, "as
  of 2026-11-02", is a pin; so is the Delivery Pin a CBC Run is born at.

## 3. A public part and a private part

How a library keeps what others rely on small.

- **How it works:** each idea marks the parts others may rely on, its
  public part. The rest is private, and changes freely.
- **Gives:** a change to a private part needs no check. Only the
  public part is checked.
- **Costs:** deciding what is public, and keeping it so.

## 4. Checks written by the user

In shared code: consumer-driven contracts.

- **How it works:** each place that relies on an idea writes a small
  check of what it needs. Before the idea changes, its owner runs every
  check.
- **Here:** the sockets turned round. The user owns the check, not the
  idea. Each check can be run by an agent, one for each place.
- **Gives:** what breaks is known before the change lands.
- **Costs:** the checks are texts to keep too.

## 5. Copy and own, with drift found

- **How it works:** each place keeps its own copy and owns it. A tool,
  or an agent, finds where a copy has drifted from its source, and a
  person decides: bring it back, or let it differ.
- **Gives:** the cheapest reading; places differ freely.
- **Costs:** bringing copies back by hand.
- **Here already, in part:** the shipped copies are kept this way,
  without the finding of drift.

## 6. A pattern language

Christopher Alexander's way.

- **How it works:** ideas link on purpose, to larger and smaller ones;
  the network is the point.
- **Works when** ideas are stable and change rarely.
- **Fails when** they change often, as ours do. It is the opposite of
  sockets, and near today's design.

## 7. A mix

| Problem | Pattern |
|---|---|
| Ideas relying on each other | Sockets |
| A change hitting everything at once | Versions and pinning |
| Which changes need a check | A public part and a private part |
| How the changes that do are checked | Checks written by the user, one agent for each place |
| Shipping, and what the agent reads | Single-sourcing: each Work Approach built from its idea and project text |

Single-sourcing is the one to weigh most. It settles how a Work
Approach ships, and the agent never reads the layers above. Its cost
is a build step: new machinery, to be built only when a need shows.
