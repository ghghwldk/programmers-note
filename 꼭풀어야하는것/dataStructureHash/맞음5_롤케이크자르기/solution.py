from collections import Counter

def solution(toppings):
    answer = 0
    leftDict = dict()
    leftCount = 0
    rightCount = len(set(toppings))
    rightCounter = Counter(toppings)

    for topping in toppings:
        # leftCount 증감
        if not topping in leftDict:
            leftCount += 1
            leftDict[topping] = None
        # rightCount 차감
        rightCounter[topping] -= 1
        if rightCounter[topping] == 0:
            rightCount -= 1
        # 비교
        if leftCount == rightCount:
            answer += 1
    return answer
