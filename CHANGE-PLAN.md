# Change-plan: harvest the archived run's template lessons

## Summary — the state after all commits

Two shape improvements, lived in safe-reservations — the run that
predates this repo, read read-only from its archive snapshot — land
in the template masters (ADR-0007). The verification suite prints
section banners and decodes default-privilege object types to
readable names, so an on-demand run reads without the file open
beside it. The runtime password key is named for whose password it
is — `<PROJECT>_RUNTIME_PASSWORD` — consistently across the `.env`
shape that declares it and the `application.yaml` that reads it.
Each touched master's header carries a dated harvest line; pins
untouched, no concept version moves.

## Commits

**1. `docs(executions): harvest verify-suite legibility`**
`verify-database-model.sql` alone: `\echo` banners before the five
sections, and readable object-type names (table/sequence) in the
default-privileges query. Queries and expectations otherwise
unchanged.

**2. `docs(executions): rename runtime password key`**
One step across two skills, deliberately: `.env.example`
(infra-establish) declares the key and `application.yaml`
(cbc-bootstrap) reads it — renamed apart, either commit reverts
incoherent. `<PROJECT>_DB_PASSWORD` → `<PROJECT>_RUNTIME_PASSWORD`,
from the run's lived `SAFE_RESERVATIONS_RUNTIME_PASSWORD`.

## Decisions taken inside this plan

- **Partial harvest, declared.** The archived verify suite also
  diverges in its role query (an explicit `IN` list) and its
  schema-privilege matrix (a row per privilege). Not adopted: the
  master's prefix `LIKE` also surfaces stray roles, and the boolean
  matrix is more compact. The harvest line says so.
- **`<PROJECT>_DB_PORT` stays.** Not a password, and the
  two-keys-for-one-fact question is already TODO'd (fix in the run
  first, then harvest); renaming it here would widen the harvest
  past what was lived.
- **The masters now diverge from checkout-system's lived key, by
  intent.** That is the authoritative-vs-pinned rule working: the
  run's copy changes only by copying anew from here (bundle doc);
  nothing edits the run.
- **Source citation.** The harvest lines name the run's lived files;
  no log-entry citation — the old run's maintenance records are its
  own system, deliberately not adopted here.
