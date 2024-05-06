'''
알고리즘 종류라기 보단 자료구조다.
중복 제거, 최적화,
완주하지 못한 선수
'''

from collections import defaultdict

dd = defaultdict(int)
dd[0] = 1
dd[1] = 2
print(dd[2])

d = dict()
d[0] = 1
d[1] = 2
# print(d[2])

# 원소 존재 확인