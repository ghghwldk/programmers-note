def solution(n):
    answer = 0

    criteria = count1(n)
    while(True):
        n = n+1
        if criteria == count1(n):
            answer = n
            break

    return answer

def count1(n):
    count = 0
    while True:
        if n % 2:
            count += 1
        if n == 1:
            break
        n = n // 2
    return count