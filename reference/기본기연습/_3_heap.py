'''
알고리즘 종류라기 보단 자료구조다.
완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조이다.

여러 개의 값들 중에서 최댓값이나 최솟값을 빠르게 찾아내도록 만들어진 자료구조이다.

insert 하는 순간에 대소비교를 하며 노드추가를 하니 최악은 O(logN) 이다.
그래서 P.Q를 for loop 하나와 쓰는 경우 O(NlogN) 이며 중첩 for loop 대신 최적화를 한다고 생각하자.
python P.Q는 기본라이브러리 heapq를 활용

PriorityQueue는 thread-safe하다,
heapq는 not thread-safe하다.
>> 코딩테스트에서는 thread-safe가 필요 없다. 더 빠른 heapq를 사용
'''
import heapq

heap = []

# 아래 for문을 실행하고 나면 heap은 [1,2,3,5,4]로 힙 정렬이 되게 된다.
for i in range(1,6):
    heapq.heappush(heap, i)

# 작은 숫자 순서대로 1,2,3,4,5가 출력된다.
for i in range(5):
    print(heapq.heappop(heap))