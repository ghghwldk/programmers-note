'''
1x1: my team
5x5: other team
black space(0): cannot move through
white space(1): only move through
'''

def bfs(maps):
    rCount, cCount = len(maps), len(maps[0])
    start = (0, 0, 1)
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    visited = [[False] * cCount for i in range(rCount)]
    wall = 0
    minDistance = -1 # for the case there is no way to go to destination

    visited[start[0]][start[1]] = True
    q = deque()
    q.append(start)

    while q:
        current = q.popleft()
        # checking arrival on destination
        if not minDistance == -1:
            break
        for i in range(4):
            nr, nc, nDistance  = current[0] + dr[i], current[1] + dc[i], current[2] + 1

            # checking condition to restrict movement
            # must have to be checked prior to other condition for safe range of index
            if nr < 0 or nc < 0 or nr >= rCount or nc >= cCount:
                continue
            if maps[nr][nc] == wall:
                continue
            if visited[nr][nc]:
                continue
            # check destination
            if nr == rCount -1 and nc == cCount -1:
                # exit
                # for making result
                # for escaping while loop
                minDistance = nDistance
            else:
                visited[nr][nc] = True
                # print((nr, nc, nDistance))
                q.append((nr, nc, nDistance))
    return minDistance


from collections import deque
def solution(maps):
    answer = 0

    # minimum required for my character to arrive.
    # return -1 when there is no way to reach their camp.
    return bfs(maps)