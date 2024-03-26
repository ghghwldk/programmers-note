from collections import Counter

def solution(topping):
    answer = 0
    left = Counter(topping)
    right = set()

    for t in topping:
        left[t] -= 1
        right.add(t)

        if left[t] == 0:
            left.pop(t)

        if len(left) == len(right):
            answer += 1
    return answer