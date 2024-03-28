visited = None
rCount, cCount = None, None
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

from collections import deque, defaultdict
def solution(land):
    global visited, rCount, cCount
    rCount, cCount = len(land), len(land[0])
    visited = [[False] * cCount for i in range(rCount)]
    surfaces = defaultdict(int)

    nextIdx = 2 # 0, 1은 index가 될 수 없다.
    for r in range(rCount):
        for c in range(cCount):
            q = deque()
            q.append((r, c))
            visited[r][c] = True

            surface = 0
            while q:
                popped = q.popleft()
                r, c = popped

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]

                    # print(nr, nc, r, c)
                    if nr < 0 or nc< 0 or nr >= rCount or nc >= cCount:
                        continue
                    if not land[nr][nc] == 1:
                        continue

                    # 방문
                    land[nr][nc] = nextIdx
                    q.append((nr, nc))
                    surface += 1
            if surface > 0:
                surfaces[nextIdx] = surface
                nextIdx += 1

    result = 0
    for c in range(cCount):
        visitedSet = set()
        for r in range(rCount):
            visitedSet.add(land[r][c])
        # get surface
        surface = 0
        for idx in visitedSet:
            surface += surfaces[idx]
        result = max(result, surface)
    return result