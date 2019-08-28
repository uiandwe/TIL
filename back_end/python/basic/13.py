# -*- coding: utf-8 -*-
# dictionary
# get all keys

a = {"1":1, "2":2, "3":3}
b = {"2":2, "3":3, "4":4}

print(a.keys())

# get key and value

print(a.items())

# find keys

print([_ for _ in a.keys() if _ in b.keys()])

c = set(a).intersection(set(b))
print(list(c))


# set default value

d = {}
key = "foo"
if key not in d:
    d[key] = []

print(d)

d = {}
d.setdefault(key, 'bar')

print(d)


from collections import defaultdict

d = defaultdict()


#update
a.update(b)
print(a)

# merge two dict

a = {"x": 55, "y": 66}
b = {"a": "foo", "b": "bar"}

print({**a, **b})

# emulating dict

class EmuDict(object):
    def __init__(self, dict_):
        self._dict = dict_

    def __repr__(self):
        return "emuDict:" + repr(self._dict)

    def __getitem__(self, item):
        return self._dict[item]

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __delitem__(self, key):
        del self._dict[key]

    def __contains__(self, item):
        return item in self._dict

    def __iter__(self):
        return iter(self._dict.keys())


_ = {"1": 1, "2": 2, "3": 3}

emud = EmuDict(_)
print(emud)

print(emud['1'])

emud['5'] = 5
print(emud)


del emud['2']
print(emud)

for _ in emud:
    print(emud[_])
else:
    print()


print('1' in emud)
