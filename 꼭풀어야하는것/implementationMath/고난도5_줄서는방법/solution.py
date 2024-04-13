def solution(targets):
    targets.sort(key=lambda x: x[1])

    cnt, end = 0, 0
    for s, e in targets:
        if s >= end:
            cnt += 1
            end = e
    return cnt