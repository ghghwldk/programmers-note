# 현재 누적되어 있는 데이터 중 가장 큰 값, 혹은 작은 값의 제거가 필요한 경우 사용할 수 있는 자료구조는 힙이다.
from heapq import heappop, heappush
'''
n: 준호가 처음 가지고 있는 병사의 수
k: 사용가능한 무적권의 횟수
enemy: 매 라운드마다 공격해오는 적의 수가 담긴 정수배열

# 참고 heap sorting은 첫번째 원소로 진행가능
for item in heap_items:
  heapq.heappush(max_heap, (-item, item))
'''

def solution(n, k, enemy):
    maxRound, sumEnemy = 0, 0
    heap = []

    for e in enemy:
        heappush(heap, (-e, e))
        sumEnemy += e
        # use 무적권
        if sumEnemy > n:
            # 무적권은 가장 큰 e에다가 사용
            if k == 0:
                break
            else:
                k -= 1
                maxE = list(heappop(heap))[1]
                sumEnemy -= maxE
        maxRound += 1
    return maxRound