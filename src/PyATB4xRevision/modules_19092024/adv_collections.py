from collections import deque, defaultdict, OrderedDict

# deque

d = deque([1, 2, 3])
print(d)

d.append(4)
d.appendleft(0)
d.extend([5, 6, 7])
d.extendleft([-1, -2, -3])
print(d)
d.remove(-3)
d.reverse()
d.pop()
d.popleft()
print(d)
print(d[1])
print(d.index(3))

# ordered dict
od = OrderedDict({'name': "Yash",
                  'Age': 30,
                  'Address': {'Place': "Kuda",
                              'State': "KA"}})
print(od)
print(od['Address']['Place'])
print(od['Address'].keys())
print(od['Address'].values())
for items in od:
    print(items)
