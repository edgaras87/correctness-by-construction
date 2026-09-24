<!-- DRAFT, 2026-09-24. Two sections so far. It lives in temp/ and
     is edited in place until it is worth placing; where it finally
     sits, and what kind of document it is, are decided from what it
     ends up containing rather than before.

     The name is provisional, chosen the same day from these two
     sections: everything here is a master, and everywhere else
     holds copies. Revisit it when there is more to read.

     Written under one rule: state only what is checkable in this
     repo and in run 3 today, and mark anything that is merely
     intended as intended. Where we contradict ourselves, say so
     rather than pick a side. -->

# Master

## 1. What this repo is

**One concept, everything derived from it, and the machinery that
puts both into projects that build real things.**

Nothing is built here. No application, no service, no run — the
repo holds documents and a delivery.

Three things live here, and the order matters because each is
derived from the one above it:

- **The concept** — `concept/`, five chapters. The plain-words
  statement of correctness by construction. Authoritative: this is
  where it is true, and every copy elsewhere is a copy. Versioned
  as a whole; it is at **v1**.

- **The method derived from it** — `delivery/method/`, two skills
  (`cbc-framing`, `cbc-slice`) that turn the concept into work a
  project can do. Each states which concept version it derives
  from.

- **The practice that one stack taught** — `delivery/spring-postgres/`,
  three skills built from a real Spring and Postgres project. These
  do not derive from the concept; they were **checked against** it.

And beside those, the thing a project is born into rather than
derived from:

- **The container** — `delivery/container/`. The records, the
  entry file, the conventions, the hygiene files. Not CbC. It is
  how a project is *kept*, not how it is *thought*.

## 2. Who we are to a project, and what a project is to us

We are **the deliverer**. We hold the master of every file a project
receives. Nothing a project holds originates in the project.

A project — a **run** — is a separate repository that builds a real
system using what we gave it. Run 3, `never-oversold`, is the live
one.

**A run is blind to us.** It holds no address for this repo, no
checkout, no remote. It cannot fetch, and nothing here reaches it by
itself. Every delivery is a person copying files into the run's
`temp/` and the run's own agent taking them from there.

```
          this repo                              a run
   ┌────────────────────────┐            ┌────────────────────────┐
   │ concept/               │            │ docs/concept/   copy   │
   │ delivery/method/       │  ── a  ──▶ │ .claude/skills/ copies │
   │ delivery/spring-…/     │   person   │ .claude/rules/  copies │
   │ delivery/container/    │   copies   │ PLAN, TODO, devlog     │
   │                        │            │ src/  ← the only thing │
   │  masters               │            │        that is its own │
   └────────────────────────┘            └────────────────────────┘
              ▲                                       │
              └───────── we read its repo ────────────┘
                         and take what it learned
```

Two flows, and they are not symmetrical:

**Down — delivery.** Files, copied whole. The run records one hash
for the whole delivery in its own decisions log. That hash is a
commit of ours; the run stores it without being able to resolve it.

**Up — harvest.** No files move. We read the run's repository
directly and write what we learned into our own masters. A run
never pushes anything here.

*Intended, not yet true: that this asymmetry is written down
anywhere but here. Today it is spread across `delivery/README.md`,
`delivery/installs/bundle-update.md`, the `convention-lifecycle`
skill, and a rules file run 3 wrote for itself because ours did not
reach that far.*
