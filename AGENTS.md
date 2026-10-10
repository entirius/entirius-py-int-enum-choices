# AGENTS.md

Integer enum choices helper — distribution `entirius-py-int-enum-choices`, import `int_enum_choices`.

## Commands

| Command | Meaning |
|---|---|
| `make install` | sync dependencies (uv, incl. extras) |
| `make check` | lint + format-check (ruff) |
| `make fix` | auto-fix lint + format |
| `make test` | test suite (pytest) |

## Conventions

- English only: code, docs, commits, branches, PRs.
- MPL-2.0: every non-trivial source file carries the license header (pre-commit inserts it).
- Toolchain: uv + ruff + hatchling + pytest; all config in `pyproject.toml`; `uv.lock` committed.
- Git flow: `master` (production) + `develop` (integration); changes land via PR; semver tag on `master`.
- Never rename the import package `int_enum_choices` — it is a public API contract.
- Default: do not commit — git is the user's call.
- No AI attribution in commits or PR descriptions.

## Architecture

Single class `IntEnumChoices` in `int_enum_choices/`: subclass it with `enumClass` (an `IntEnum`)
and `labels` (member → label). Provides `choices()`, `keys()`, `label()`, `idFromText()`.
No runtime dependencies.
