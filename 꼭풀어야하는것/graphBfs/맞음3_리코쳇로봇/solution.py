global rCount, cCount

dr, dc = [0,0, 1, -1], [1, -1, 0,0]
from collections import deque
def solution(board):
    global rCount, cCount
    rCount, cCount = len(board), len(board[0])

    visited = [[False] * cCount for i in range(rCount)]

    r, c = getFirstLocation(board)
    q = deque()
    # 마지막은 시작점으로부터의 거리
    q.append((r, c, 0))
    visited[r][c] = True

    while q:
        r, c, d = q.popleft()
        for i in range(4):
            nr, nc = getNextLocation((r, c), i, board)
            nd = d+1
            if visited[nr][nc]:
                continue

            if board[nr][nc] == 'G':
                return nd

            q.append((nr, nc, nd))
            visited[nr][nc] = True
    return -1

def getFirstLocation(board):
    for r in range(rCount):
        for c in range(cCount):
            if board[r][c] == 'R':
                return r,c


def getNextLocation(current, direction, board):
    r, c = current
    resultR, resultC = r, c

    while True:
        nr, nc = resultR + dr[direction], resultC + dc[direction]

        if nr < 0 or nc < 0 or nr >= rCount or nc >= cCount:
            break
        if board[nr][nc] == 'D':
            break
        # 움직였을 때, 가능하면 움직인 위치 변경
        resultR, resultC = nr, nc
    return resultR, resultC

