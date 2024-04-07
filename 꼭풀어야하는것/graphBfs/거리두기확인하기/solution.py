def bfs(start, place):
    visited = [[False] * cCount for i in range(rCount)]
    startR, startC = start
    q = deque()
    # 3번째는 사람으로부터의 거리이다.
    q.append((startR, startC, 0))
    visited[startR][startC] = True

    while q:
        r, c, d = q.popleft()
        for i in range(4):
            nr, nc, nextDistance = r+ dr[i], c+ dc[i], d+1
            # 가지 못하는 조건 확인
            if nr < 0 or nc < 0 or nr >= rCount or nc >= cCount:
                continue
            if visited[nr][nc]:
                continue
            if nextDistance > 2:
                continue
            if place[nr][nc] == 'X':
                continue
            # player인지 확인
            if place[nr][nc] == 'P':
                return True
            # 다음으로 가기
            q.append((nr, nc, nextDistance))
            visited[nr][nc] = True
    return False

from collections import deque
global rCount, cCount
dr, dc = [0,0,1,-1], [1,-1,0,0]
def solution(places):
    global rCount, cCount
    rCount, cCount = len(places), len(places[0])

    answer = []
    for place in places:
        is위반 = False
        for r in range(rCount):
            for c in range(cCount):
                if place[r][c] == 'P':
                    if bfs((r,c), place):
                        is위반 = True
                if is위반:
                    break
            if is위반:
                break
        answer.append(1 if not is위반 else 0)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))


