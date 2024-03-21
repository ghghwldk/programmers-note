import math

def solution(arr):
    answer = arr[0]

    # 리스트를 순회하며 최소공배수를 계산
    for n in arr:
        answer = (n * answer) // math.gcd(n, answer)
    # 마지막 최소공배수 리턴
    return answer