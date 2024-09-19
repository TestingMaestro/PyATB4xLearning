# deque --->
"""
--> List like sequence
---> Double ended queue --> we insert elements from left and right
"""

from collections import deque

d = deque([1, 2, 3])
print(d)

d.append(4)  # ed of the deque
print(d)

d.appendleft(0)  # insert from left
print(d)

d.extend([5, 6, 7, 8])
print(d)

d.extendleft([-1, -2, -3])
print(d)

d.reverse()
print(d)

d.remove(4)
print(d)

d.index(1, 4)
print(d)

m = [1, 3, 4, 5]
print(m.index(1))
