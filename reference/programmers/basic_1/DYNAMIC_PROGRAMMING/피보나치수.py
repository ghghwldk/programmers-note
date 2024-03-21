'''
[시간초과 발생]
재귀호출 발생 시 시간초과 발생
'''
def solution(n):
    a = 1
    b = 1
    if n == 1 or n == 2:
        return 1
    for i in range(1, n):
        a, b = b, b + a

    return a