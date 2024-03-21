from collections import deque
def solution(x, y, n):
    answer = -1

    q = deque()

    q.append((x, 0))

    visited = set()

    while q:
        value, cnt = q.popleft()

        if value == y:
            answer = cnt
            break

        if value*3 <= y and not value*3 in visited:
            visited.add(value*3)
            q.append((value*3, cnt+1))
        if value*2 <= y and not value*2 in visited:
            visited.add(value*2)
            q.append((value*2, cnt+1))
        if value+n <= y and not value+n in visited:
            visited.add(value+n)
            q.append((value+n, cnt+1))

    return answer