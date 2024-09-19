# Ordered Dictionary
"""
Dictionary which maintains the insertion order
"""
from collections import OrderedDict, defaultdict

d = OrderedDict()

d['name'] = "Yashodhar"
d['Age'] = 30
d['Place'] = "Kundapura"
d['Gen'] = "Male"

dd = defaultdict(int)
dd['test'] += 0
print(dd['test'])

print(dd)

d1 = OrderedDict()