# int-enum-choices

Helper turning an `IntEnum` into `(value, label)` choices with reverse lookups —
handy for Django-style choice fields backed by integer enums.

## Installation

```shell
pip install entirius-py-int-enum-choices
```

## Usage

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

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest)
```

Development and agent instructions: [AGENTS.md](AGENTS.md).

## License

Mozilla Public License 2.0 — see [LICENSE](LICENSE).
