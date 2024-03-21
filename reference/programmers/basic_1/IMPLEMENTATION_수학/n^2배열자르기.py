def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        # 해당 위치의 값
        value = max(i // n, i % n) + 1
        answer.append(value)

    return answer


'''
[시간초과]
def solution(n, left, right):
    answer = []

    for i in range(n):
        for j in range(n):
            answer.append(max(i + 1, j + 1))

    return answer[left:right + 1]
'''