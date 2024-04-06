'''
A나라가 B나라 공격
운용 비용 최소화
2차원

미사일

끝나는 지점 + 시작 지점(탐색 중단 목적)
'''
from collections import deque
def solution(targets):
    targets = sorted(targets, key = lambda x:(x[1], x[0]))
    # print('after sorting', targets)

    targets = deque(targets)
    count = 0
    currentLocation = -1
    while targets:
        start, end = targets.popleft()
        # print(start, end, currentLocation)
        if currentLocation == -1:
            currentLocation = end-0.1
            count += 1
            # print('init', currentLocation)
            continue
        if currentLocation < start:
            currentLocation = end-0.1
            count += 1
            # print('renewal', currentLocation)


    return count


# (3,5)(2,5) 끝점이 같으면, 시작점의 위치정렬 필요 없음


print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))