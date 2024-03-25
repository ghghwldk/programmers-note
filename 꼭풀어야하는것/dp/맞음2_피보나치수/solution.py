'''
[시간초과 발생]
재귀호출 발생 시 시간초과 발생
'''
def solution(n):
    before1, before2 = 0, 1

    current = -1
    for i in range(2, n+1):
        current = before1 + before2

        before1, before2 = before2, current

    return current % 1234567