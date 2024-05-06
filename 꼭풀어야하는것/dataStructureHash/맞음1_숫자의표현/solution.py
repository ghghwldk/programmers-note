def solution(n):
    h = {}
    summed = 0

    for i in range(0, n+1):
        summed += i
        h[summed] = None

    result = 0
    for k in sorted(h.keys(), reverse = True):
        target = k - n

        # if target in h.keys():
        #     result += 1
        '''in h로 작성해야 시간복잡도가 1이다.'''
        if target in h:
            result += 1
        if k < n:
            break
    return result


n = 15
print(solution(n))