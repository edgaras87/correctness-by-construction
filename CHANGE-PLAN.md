# Change-plan: harvest run 3's bootstrap into cbc-bootstrap

## Summary — the state after all commits

Nine findings from run 3's Step 4 (read 2026-09-12, TODO Now; the
run's own re-read of the skill the same day, four hand-offs) land in
the cbc-bootstrap masters and one fill, in the run's own wording, one
dated harvest line per change per file (CBC ADR-0007), the pins
untouched — runs re-pin on their own act. After the set: the Ryuk trap
and the properties template are true for Testcontainers 2.x; Stage 2
names no directory for the requirements document; the walkthrough's
stage 5 says when the machinery proof must cross the process boundary
and the harness reference carries the plural-instance shape as a
variation point; stage 3 and the README template say what a missing
secret looks like and Stage 1's exclusions say when fail-fast is
decided; the reference states the Boot 4 Flyway split and carries the
refusal test that witnesses the split in the miniature; the
application template reads the port key the env template names; stage
2's rename trap says when it bites; and the entry-file fill states no
current state, so the next run inherits no line that stales. Nothing
in `concept/` moves: no CHANGELOG entry, no concept version.

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
absorbed. A recall-list item. SKILL.md Stage 1's exclusions gain
the entry by name, with run 3's why: fail fast on a missing secret
— not at bootstrap, decided at release, where a stranger's clean
machine makes a forgotten export a real need; the harness already
accepts an instance only on health with the store UP. So the next
run does not re-decide it mid-set. templates/readme-run-test.md's
Run section gains the symptom line run 3 wrote. Harvest lines in
the walkthrough (third, same set), SKILL.md (third, same set) and
the template.

**6. `docs(starter): the reference states the Boot 4 Flyway split`**
Harness reference §1, a bound fact: on Boot 4 the Flyway
auto-configuration lives in its own module; with only the engine
and the postgresql module on the test classpath, no auto-
configuration runs in the application context, and the harness's
own call is the only migration path in tests. The walkthrough's
stage 4 harness bullet gains the clause: the engine enters, not
Boot's Flyway module. Harvest lines in the reference (second, same
set) and the walkthrough (fourth, same set).

**7. `docs(starter): the miniature witnesses the refusal`**
Harness reference §3: the migration-path test gains a third test,
lived once (run 3) — `runtime` attempting `CREATE TABLE` in the
miniature, refused with the ground's own message; three lines that
catch a miniature quietly wired without the split, where
`current_user` alone witnesses the identity, not the authority.
Its trap in the code's shape: Spring wraps the driver's error, so
the assertion goes on the root cause. The file's one-line table
and bound facts say so. Harvest line in the reference (third,
same set).

**8. `docs(starter): application.yaml reads POSTGRES_PORT`**
templates/application.yaml's datasource URL reads
`${POSTGRES_PORT:5432}`, the key the env template and the compose
template both name, instead of a project-prefixed key neither
carries — a run copying the templates as shipped gets an
application that never reads the port the ground publishes, silent
on 5432 and wrong on any other. The header line says the templates
now share the key. Harvest line in the template.

**9. `docs(starter): the rename trap says when it bites`**
The walkthrough's stage 2 trap: Initializr on Boot 4 already emits
the web-MVC starter and the `-test` companions; the trap bites when
a pom is written or translated by hand. One clause. Harvest line
in the walkthrough (fifth, same set).

**10. `docs(starter): the entry-file fill states no current state`**
starter/fills/claude-md-template.md's orientation paragraph loses
its state clause — "nothing to build, no tests, no runtime" — and
says only what never changes before the briefing. Run 3's answer,
lived on its main 2026-09-12: a line about current state has a
moment and stales at every step; current state is PLAN's by the
records table (agent-arrangement's test 2). The fill's header
records the cut and its source. Harvest line in the fill.

**11. `docs: records for the run 3 bootstrap harvest`**
TODO's harvest item DONE, with what each fix became — its fix 8,
the entry file, retargeted from the skill's Stage 5 to the fill,
the user's call on the run's answer; the watch item under Later
updated the same way; the checkout two-keys item in Later closed
by the port-key fix (commit 8); the sixth handoff gains the kit stub's state clause and
agent-arrangement's test 2 as fold-back targets; devlog entry and
resume line. No ADR: every change is a harvest under CBC
ADR-0007's flow.

**12. `docs(agent): close change-plan for the run 3 bootstrap harvest`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **The plural-instance shape enters as prose; the refusal test
  as code.** The reference's code is a confirmed pass, lived three
  times; both of these are lived once. The forked shape is a shape
  — a holder, a helper, a race — and a variation point names it
  and its why; code joins after a second run lives it. The refusal
  test is three lines whose trap is in their shape (the root-cause
  assertion), so prose would lose the lesson; it enters as code,
  marked lived once.
- **The Ryuk claim is verified here, not taken from the report.**
  The run's finding was checked against the Testcontainers 2.0.5
  jar in the local repository; the commit body names the keys
  found.
- **Stage 2 names no directory, and states the lived one.** "The
  path the project's records choose" is the rule; "both lived runs:
  `docs/construction/`" is the default a run gets when it has no
  reason to differ — the same move as the records shape harvested
  for infra-establish.
- **The entry-file fix is the fill's, not the skill's.** The
  first draft had Stage 5 make the line true at the close; run 3's
  own fix is stronger — no state line, nothing to stale — and the
  user took it. The fill is ours, so the cut lands here; the kit's
  stub carries the same clause and goes to the handbook through
  the sixth handoff. No skill names the entry file.
- **Fix 5 adds an exclusion, not a requirement.** Whether the app
  refuses to start without its secret stays a *what*; Stage 1's
  exclusions now say when it is decided, with the run's why, as
  every exclusion there carries one. A run may decide otherwise
  by name.
- **The walkthrough takes five harvest lines from one set, the
  reference and SKILL.md three each**, one per change, as the
  verify template took three last set — ADR-0007's line is per
  change, and each reverts alone.
- **Wording is the run's.** Each fix quotes or closely follows run
  3's manual, ADRs, devlog and delivered files; nothing is
  re-derived from the finding alone.
