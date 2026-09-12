# Change-plan: harvest run 3's bootstrap into cbc-bootstrap

## Summary — the state after all commits

Eight findings from run 3's Step 4 (read 2026-09-12, TODO Now) land
in the cbc-bootstrap masters, in the run's own wording, one dated
harvest line per change per file (CBC ADR-0007), the pins untouched
— runs re-pin on their own act. After the set: the Ryuk trap and the
properties template are true for Testcontainers 2.x; Stage 2 names
no directory for the requirements document; the walkthrough's stage
5 says when the machinery proof must cross the process boundary and
the harness reference carries the plural-instance shape as a
variation point; stage 3 and the README template say what a missing
secret looks like; the reference states the Boot 4 Flyway split;
the application template reads the port key the env template
names; stage 2's rename trap says when it bites; and Stage 5 names
the entry file's opening line beside the README projection, so the
next run makes it true unprompted. Nothing in `concept/` moves: no
CHANGELOG entry, no concept version.

## Commits

**1. `docs(agent): add change-plan for the run 3 bootstrap harvest`**
This plan.

**2. `docs(starter): the Ryuk trap is true for Testcontainers 2.x`**
templates/testcontainers.properties loses its `ryuk.disabled=true`
line — checked here against the 2.0.5 jar the build manages: the
properties file reads only `ryuk.container.image`, `.privileged`,
`.timeout`; the disable switch is the environment variable
`TESTCONTAINERS_RYUK_DISABLED`. The walkthrough's stage 4 trap 2
and recall item 6 rewritten from run 3's manual: Ryuk ran unmodified
under rootless podman 5.8, reaping the throwaways within seconds of
the JVM's exit; if it fails on a host, the variable in the
environment, never a properties line; a hard-killed JVM's stranded
throwaway is found by image and removed by name. Harvest lines in
the template and the walkthrough.

**3. `docs(starter): Stage 2 names no directory of its own`**
SKILL.md Stage 2: the requirements document lands "at the path the
project's records choose"; `internal/construction/` goes. Both
lived runs put it at `docs/construction/` beside the builder's
manuals, and the sentence says so as the lived default. Harvest
line in SKILL.md.

**4. `docs(starter): the machinery proof across processes`**
The definition's runtime ground decides how many instances the
proof needs. SKILL.md Stage 1, the proven-adversity bullet: read
the instance count from the definition's L1 beside the adversity
class. The walkthrough's stage 5 gains the condition — when L1 says
plural instances, the in-process burst is the cheap first check
and the proof is N ≥ 2 instances as separate processes against one
store, each through its own door, released at one instant across
them, the witness read from the store from outside — and the lived
realization: forked from the build's own output, `target/classes`
plus the runtime classpath the dependency plugin writes at
`process-test-classes`, because the test phase runs before
packaging and an image would need a second command; the three
environment facts a real instance gets and nothing else; free
ports from the socket; the harness owning the processes' lifecycle.
The harness reference: its header's "two bases, not three" line
qualified, and a variation point 8 describing the shape in prose —
the store lifted out of the database base into its own holder, the
base keeping only the datasource override; a process helper; the
probe answering its pid beside the identity; the race asserting the
pids served are exactly the instances started. Harvest lines in
SKILL.md (second, same set), the walkthrough (second, same set),
the reference.

**5. `docs(starter): a missing secret does not stop the app`**
The walkthrough's stage 3 "Fact:" paragraph gains run 3's lived
trap: Boot's binding leaves an unresolvable placeholder as the
literal, the app starts with it as the password, and only health
(`db` DOWN) tells; the store logs the failed authentication.
Whether the app should refuse to start is a *what* — decided, never
absorbed; run 3 decided it at release. A recall-list item.
templates/readme-run-test.md's Run section gains the symptom line
run 3 wrote. Harvest lines in the walkthrough (third, same set)
and the template.

**6. `docs(starter): the reference states the Boot 4 Flyway split`**
Harness reference §1, a bound fact: on Boot 4 the Flyway
auto-configuration lives in its own module; with only the engine
and the postgresql module on the test classpath, no auto-
configuration runs in the application context, and the harness's
own call is the only migration path in tests. The walkthrough's
stage 4 harness bullet gains the clause: the engine enters, not
Boot's Flyway module. Harvest lines in the reference (second, same
set) and the walkthrough (fourth, same set).

**7. `docs(starter): application.yaml reads POSTGRES_PORT`**
templates/application.yaml's datasource URL reads
`${POSTGRES_PORT:5432}`, the key the env template names, instead
of a project-prefixed key the env template never carried; the
header line says the two templates now share the key. Harvest line
in the template.

**8. `docs(starter): the rename trap says when it bites`**
The walkthrough's stage 2 trap: Initializr on Boot 4 already emits
the web-MVC starter and the `-test` companions; the trap bites when
a pom is written or translated by hand. One clause. Harvest line
in the walkthrough (fifth, same set).

**9. `docs(starter): Stage 5 names the entry file's opening line`**
SKILL.md Stage 5's exit-records paragraph: beside the README
projection, the entry file's orientation — a line that states the
system's state is made true at this close; "no code yet" is false
now. Run 3 left the line standing after the bootstrap. Harvest
line in SKILL.md (third, same set).

**10. `docs: records for the run 3 bootstrap harvest`**
TODO's harvest item DONE, with what each fix became; the checkout
two-keys item in Later closed by fix 7; devlog entry and resume
line. No ADR: every change is a harvest under CBC ADR-0007's flow.

**11. `docs(agent): close change-plan for the run 3 bootstrap harvest`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **The plural-instance shape enters as prose, not code.** The
  reference's code is a confirmed pass, lived three times; the
  forked shape is lived once. A variation point names the shape
  and its why; code joins after a second run lives it.
- **The Ryuk claim is verified here, not taken from the report.**
  The run's finding was checked against the Testcontainers 2.0.5
  jar in the local repository; the commit body names the keys
  found.
- **Stage 2 names no directory, and states the lived one.** "The
  path the project's records choose" is the rule; "both lived runs:
  `docs/construction/`" is the default a run gets when it has no
  reason to differ — the same move as the records shape harvested
  for infra-establish.
- **The entry-file clause stays on our side.** The kit owns the
  file's shape; the truth of a line the run wrote about its own
  state, at the moment this skill closes, is the skill's to name —
  the README projection's shape (CBC ADR-0013). Noted for the
  sixth handoff. infra-establish's close does not get the clause
  in this set: run 3 updated the line at Step 3 unprompted; the
  miss was the bootstrap's.
- **Fix 5 changes no requirement.** Whether the app refuses to
  start without its secret stays a *what* for the run's Stage 1;
  the trap says decide, never absorb.
- **The walkthrough takes five harvest lines from one set**, one
  per change, as the verify template took three last set —
  ADR-0007's line is per change, and each reverts alone.
- **Wording is the run's.** Each fix quotes or closely follows run
  3's manual, ADRs, devlog and delivered files; nothing is
  re-derived from the finding alone.
