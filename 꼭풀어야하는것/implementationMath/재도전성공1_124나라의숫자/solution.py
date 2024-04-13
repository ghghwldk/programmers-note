def solution(n):
    result = ''
    count = 0
    while True:
        n, remain = n // 3, n % 3

        # print(n, remain)
        if remain > 0:
            result = str(remain) + result
        else:
            n -= 1
            result = '4' +result
        if n < 3:
            if n > 0:
                result = str(n) + result
            break
    return result

print(solution(15))

# n	result
# 1	1
# 2	2
# 3	4
# 4	11