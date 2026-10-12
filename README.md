# entirius-py-int-enum-choices

A helper that turns an `IntEnum` into `(value, label)` choices with reverse lookups, part of
Entirius, the open-source modular ecommerce platform. It fits Django-style choice fields backed by integer enums and
has no runtime dependencies.

[![PyPI](https://img.shields.io/pypi/v/entirius-py-int-enum-choices.svg)](https://pypi.org/project/entirius-py-int-enum-choices/)
[![Python](https://img.shields.io/pypi/pyversions/entirius-py-int-enum-choices.svg)](https://pypi.org/project/entirius-py-int-enum-choices/)
[![License: MPL-2.0](https://img.shields.io/badge/license-MPL--2.0-blue.svg)](https://github.com/entirius/entirius-py-int-enum-choices/blob/develop/LICENSE)

## What it does

- Lists `(value, label)` pairs for a choice field (`choices()`).
- Lists the enum values (`keys()`).
- Returns the label of a value (`label()`, `labelFromId()`).
- Finds the enum member for a label, case-insensitively, with a default (`idFromText()`).

## Installation

```shell
uv add entirius-py-int-enum-choices
pip install entirius-py-int-enum-choices
```

The import name is `int_enum_choices`.

## Quick start

```python
from enum import IntEnum
from int_enum_choices import IntEnumChoices

class Color(IntEnum):
    RED = 1
    GREEN = 2

class ColorChoices(IntEnumChoices):
    enumClass = Color
    labels = {Color.RED: "Red", Color.GREEN: "Green"}

ColorChoices.choices()          # [(1, "Red"), (2, "Green")]
ColorChoices.label(1)           # "Red"
ColorChoices.idFromText("red")  # Color.RED
ColorChoices.keys()             # [1, 2]
```

## Requirements

- Python 3.11 or newer.
- No runtime dependencies.

## Documentation

- Entirius documentation: https://docs.entirius.com/
- Changelog: https://github.com/entirius/entirius-py-int-enum-choices/blob/develop/CHANGELOG.md

## Part of Entirius

This helper backs integer choice fields in the Entirius backend service (Volkanos) and its modules.

- Backend service: https://github.com/entirius/entirius-service-volkanos
- Docker harness: https://github.com/entirius/entirius-zeno
- Consumer modules: https://github.com/entirius/entirius-django-pim, https://github.com/entirius/entirius-django-accounts, https://github.com/entirius/entirius-django-pricemanager

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest)
```

Development and agent instructions: https://github.com/entirius/entirius-py-int-enum-choices/blob/develop/AGENTS.md

## License

Mozilla Public License 2.0 (MPL-2.0) — see https://github.com/entirius/entirius-py-int-enum-choices/blob/develop/LICENSE.
