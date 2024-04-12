nextIdx, rCount, cCount, land, surfaces = None, None, None, None, None
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

from collections import deque, defaultdict
def solution(l):
    global rCount, cCount, nextIdx, land, surfaces
    land = l
    rCount, cCount = len(land), len(land[0])
    surfaces = defaultdict(int)
    nextIdx = 2 # 0, 1은 index가 될 수 없다.
    for r in range(rCount):
        for c in range(cCount):
            if not land[r][c] == 1:
                continue
            bfs(r, c)

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

def bfs(r, c):
    global nextIdx, surfaces
    q = deque()
    q.append((r, c))
    land[r][c] = nextIdx

    surface = 1
    while q:
        popped = q.popleft()
        r, c = popped

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nc< 0 or nr >= rCount or nc >= cCount:
                continue
            if not land[nr][nc] == 1:
                continue

            # 방문
            land[nr][nc] = nextIdx
            q.append((nr, nc))
            surface += 1
    surfaces[nextIdx] = surface
    nextIdx += 1
'''
land	result
[[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]	9
[[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]	16
'''
# print('solution', solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))
print('solution', solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))

