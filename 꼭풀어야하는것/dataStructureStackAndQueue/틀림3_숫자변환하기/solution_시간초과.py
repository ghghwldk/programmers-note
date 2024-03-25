from collections import deque
def solution(x, y, n):
    if x == y: return 0

    # using queue from now
    answer = 1e9

    q = deque()
    q.append((x, 1))
    while q:
        currentVal, count = q.popleft()
        nextVals = [currentVal + n, currentVal * 2, currentVal * 3]
        for nextVal in nextVals:
            # print(currentVal, nextVal, count)
            if nextVal == y:
                return count
            if nextVal < y:
                q.append((nextVal, count + 1))
    return -1