# 1차 개선
from collections import deque
def find_start(col, row, board):
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'R':
                return deque([(i, j, 0)])

def solution(board):
    col, row = len(board[0]), len(board)
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[0 for _ in range(col)] for _ in range(row)]
    queue = find_start(col, row, board)

    while queue:
        current_node = queue.popleft()
        y, x, cnt = current_node

        for dy, dx in directions:
            ny, nx = y+dy, x+dx
            while 0 <= ny < row and 0 <= nx < col and board[ny][nx] != 'D':
                ny += dy
                nx += dx
            ny, nx = ny-dy, nx-dx

            if board[ny][nx] == 'G':
                return cnt+1

            if not visited[ny][nx]:
                visited[ny][nx] = 1
                queue.append((ny, nx, cnt+1))
    return -1
# 7.12ms, 10.3MB