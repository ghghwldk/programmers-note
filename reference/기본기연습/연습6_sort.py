# len로 sort 시
l1 = [[1 , 2, 3], [1], [1, 2]]
l1 = sorted(l1, key = len)
print(l1)

l2 = [[1 , 2, 3], [1], [1, 2]]
l2 = sorted(l2, key = lambda x: ( - len(x)))
print(l2)

# 여러개의 키로 sort 시
l3 = [(1, 3), (1, 2), (2, 1), (2, 3), (3, 5), (3, 1)]
l3 = sorted(l3, key= lambda x: (-x[0] , x[1]))
print(l3)