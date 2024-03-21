import sys
sys.setrecursionlimit(1000000)

idx = [[0,1],[1,0],[-1,0],[0,-1]]

def dfs(x, y, visited, matrix, food):

    visited[x][y] = True
    food = food + int(matrix[x][y])

    for each in idx:

        new_x = x + each[0]
        new_y = y + each[1]

        if 0 <= new_x < len(matrix) \
                and 0 <= new_y < len(matrix[0]) \
                and not visited[new_x][new_y] \
                and matrix[new_x][new_y] != 'X':

            food = dfs(new_x,new_y, visited, matrix, food)

    return food


def solution(maps):

    matrix = maps
    visited = [[False]*len(matrix[0]) for _ in range(len(matrix))]

    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 'X' and not visited[i][j]:
                tmp = dfs(i,j,visited, matrix,0)
                result.append(tmp)

    if not len(result):
        return [-1]
    else:
        return sorted(result)