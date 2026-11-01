<!-- Agent Skill Template — the Master Copy is in correctness-by-construction.
     Merge into the CBC Run's README at the cbc-bootstrap Agent Skill's Stage 5, when the Adversity
     Harness is real, and fill from the certified commands. The filled
     sections are the CBC Run's own (.claude/rules/delivered-copies.md, rule 8, An Agent Skill Template is…).
     Only the material below is merged; this header stays with the
     Master Copy. The stack line joins the Prerequisites section that
     Infrastructure Establishment opened. The command bodies are the
     Spring and Maven shape CBC Runs used. A different stack writes its
     own, keeping the shape:
     - Run stands the Runtime Ground up, and ends in a check that the
       system answers;
     - Test is the one standard test command, with what it really
       drives stated beside it. -->

<!-- Into the existing Prerequisites section: -->

- JDK <version> (Maven comes with the committed wrapper)

## Run

```bash
# stand the Runtime Ground up (first time: creates roles/schema; see
# the Operator Manual for the Catalog Check and the Behavioral Check)
cp .env.example .env
podman compose up -d

# run the system against it, as the runtime role
set -a; . ./.env; set +a
./mvnw spring-boot:run
# check it answers: curl localhost:8080/actuator/health → status UP, db UP
```

If health answers with `db` DOWN, the environment was not exported:
the system starts anyway and only health tells. Export `.env` in the
same shell and start again.

## Test

```bash
# the one standard test command — unit and integration tests together;
# integration tests drive a real throwaway PostgreSQL (Testcontainers,
# rootless podman), so the Runtime Ground does not need to be up
./mvnw test
```
