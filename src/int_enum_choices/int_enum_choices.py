# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.


class IntEnumChoices:
    @classmethod
    def choices(self):
        rv = []
        for k in self.enumClass:
            x = (k.value, self.labels[k])
            rv.append(x)
        return rv

    @classmethod
    def idFromText(self, txt, default=None):
        if txt is None:
            return None
        txt = txt.lower()
        for k, name in self.labels.items():
            if name.lower() == txt:
                return k
        return default

    @classmethod
    def label(self, key):
        if key is None:
            return ""
        key = int(key)
        if key in self.labels:
            return self.labels[key]
        return f"unknown key: {key}"

    @classmethod
    def labelFromId(self, key):
        return self.label(key)

    @classmethod
    def keys(self):
        rv = []
        for k in self.enumClass:
            rv.append(k.value)
        return rv
