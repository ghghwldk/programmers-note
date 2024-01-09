def solution(n):
    h = {}
    summed = 0

    for i in range(0, n+1):
        summed += i
        h[summed] = None

    result = 0
    for k in sorted(h.keys(), reverse = True):
        target = k - n
        # check directly from the dictionary
        if target in h:
            result += 1
        if k < n:
            break
    return result