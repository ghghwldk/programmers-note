'''
선택, 삽입, 버블, 합병(병합), 힙(tree), 퀵 까지는 기본 소양이다.
n^2 / nlogn / 메모리 복잡도에 대한 개념은 있어야 한다.
sorting 자체의 문제보다는 PS에 데이터 정렬이 필요한가?
정도를 알아차리는게 또 중요한 것 같다.

>> 하지만, 나는 파이썬의 기본정렬만 사용한다.
기본 정렬 라이브러리는 O(NlogN)이다.
알고리즘은 병합 정렬과 삽입 정렬의 아이디어로 만들었다고 한다.
'''

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