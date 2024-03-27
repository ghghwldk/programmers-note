import sys
sys.setrecursionlimit(1000000)

maps, visited = None, None
rCount, cCount = None, None
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def dfs(r, c):
    global visited
    result = 0 # 다음에 방문할 곳이 없으면, 0을 return해야한다.
    # 탈출조건
    if r<0  or c< 0 or r >= rCount or c >= cCount:
        return result
    if visited[r][c] == True:
        return result
    if maps[r][c] == 'X':
        return result

    # visited 처리
    visited[r][c] = True
    # 가능 시
    result += int(maps[r][c])
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        result += dfs(nr, nc)
    return result

def solution(m):
    # init
    init(m)
    # get result
    result = []
    for r in range(rCount):
        for c in range(cCount):
            total = dfs(r, c)
            if total > 0:
                result.append(total)
    return sorted(result) if len(result) > 0 else [-1]


def init(m):
    global maps, visited, rCount, cCount
    maps = m
    rCount, cCount = len(m), len(m[0])
    visited = [[False] * cCount for i in range(rCount)]
