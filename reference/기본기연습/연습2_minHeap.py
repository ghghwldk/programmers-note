from heapq import heappush, heapify, heappop

l = [1, 4, 3, 2]
print(heapify(l))
print(l)
heappop(l)
print('after heappop from the heapq')
print(l)
heappush(l, 1)
print('after item pushed')
print(l)