from collections import Counter

def solution(want, number, discount):
    condition = getCondition(want, number)
    return getAnswer(discount, condition)


def getAnswer(discount, condition):
    answer = 0

    for i in range(len(discount) - 9):
        if Counter(discount[i:i+10]) == condition:
            answer += 1

    return answer


def getCondition(want, number):
    condition = dict()
    for w, n in zip(want, number):
        condition[w] = n

    return condition