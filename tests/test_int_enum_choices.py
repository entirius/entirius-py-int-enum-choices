# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from enum import IntEnum

from int_enum_choices import IntEnumChoices


class Color(IntEnum):
    RED = 1
    GREEN = 2


class ColorChoices(IntEnumChoices):
    enumClass = Color
    labels = {Color.RED: "Red", Color.GREEN: "Green"}


def test_choices():
    assert ColorChoices.choices() == [(1, "Red"), (2, "Green")]


def test_keys():
    assert ColorChoices.keys() == [1, 2]


def test_label():
    assert ColorChoices.label(1) == "Red"
    assert ColorChoices.label(None) == ""
    assert ColorChoices.label(99).startswith("unknown key")


def test_id_from_text():
    assert ColorChoices.idFromText("red") == Color.RED
    assert ColorChoices.idFromText(None) is None
    assert ColorChoices.idFromText("nope", default=-1) == -1
