'''
visited로 시간초과 해결

숫자 관련 bfs는 visited를 사용하지 않을 것이라고 생각했으나,
visited를 사용하지 않으면, 시간초과가 발생하여 오답
'''

from collections import deque
def solution(x, y, n):
    if x == y: return 0

    # using queue from now
    answer = 1e9

    visited = set()
    q = deque()
    q.append((x, 1))
    visited.add(x)

    while q:
        currentVal, count = q.popleft()
        nextVals = [currentVal + n, currentVal * 2, currentVal * 3]
        for nextVal in nextVals:
            if nextVal in visited:
                continue
            # print(currentVal, nextVal, count)
            if nextVal == y:
                return count
            if nextVal < y:
                q.append((nextVal, count + 1))
                visited.add(nextVal)
    return -1