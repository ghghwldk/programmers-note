'''
A나라가 B나라 공격
운용 비용 최소화
2차원

미사일

끝나는 지점 + 시작 지점(탐색 중단 목적)
'''
from collections import deque
def solution(targets):
    targets = sorted(targets, key = lambda x:(x[0], x[1]))
    print('after sorting', targets)

    targets = deque(targets)
    count = 0
    currentLocation = -1
    isFired = True
    while targets:
        start, end = targets.popleft()
        print(isFired, currentLocation, start, end)
        # 발사 전이라면, 시작점과 비교한다
        if not isFired:
            # 이전 location이 현재 target도 수용할 수 있는 경우

            if currentLocation > start:
                continue
            # 불가능한 경우
            else:
                isFired = True
                count += 1
                print('발사', currentLocation)
                currentLocation = end - 0.1
        else :
            # 발사 후라면, 현재 target의 끝점을 기준으로 currentLocation을 갱신한다.
            isFired = False
            currentLocation = end - 0.1
            # print('신규', currentLocation,start, end)
        if len(targets) == 0:
            count+= 1
            print('발사', currentLocation)
    return count


# (3,5)(2,5) 끝점이 같으면, 시작점의 위치정렬 필요 없음


print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))