from collections import defaultdict
from heapq import heappush, heapify, heappop

dd = defaultdict(int)
dd[0] = 1
dd[1] = 2
print(dd[2])

d = dict()
d[0] = 1
d[1] = 2
# print(d[2])

l = [1, 4, 3, 2]
print(heapify(l))
print(l)
heappop(l)
print('after heappop from the heapq')
print(l)
heappush(l, 1)
print('after item pushed')
print(l)