def solution(places):
    answer = []
    for place in places:
        q = []
        for i,p in enumerate(place):
            for j in range(len(place)):
                if p[j] == "P":
                    q.append([i,j])
        if len(q) == 0:
            answer.append(1)
            continue
        if bfs(place, q):
            answer.append(1)
            continue
        answer.append(0)
    return answer

def bfs(graph, q):
    mX = [0,0,1,-1]
    mY = [1,-1,0,0]

    for c in q:
        queue = [[c[0], c[1], 0]]
        visited = [[False]*5 for i in range(5)]
        visited[c[0]][c[1]] = True
        while queue:
            cur = queue.pop()
            for i in range(4):
                nX = mX[i] + cur[0]
                nY = mY[i] + cur[1]
                if nX < 0 or nX >= 5 or nY < 0 or nY >= 5 or graph[nX][nY] == "X" or visited[nX][nY]:
                    continue
                if graph[nX][nY] == "P" and cur[2] <= 1:
                    return False
                if graph[nX][nY] == "O":
                    queue.append([nX,nY,cur[2]+1])
                    visited[nX][nY] = True

    return True