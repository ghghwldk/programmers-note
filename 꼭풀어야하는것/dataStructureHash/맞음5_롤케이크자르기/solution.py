from collections import Counter

def solution(toppings):
    answer = 0
    leftSet = set()
    leftCount = 0
    rightCount = len(set(toppings))
    rightCounter = Counter(toppings)

    for topping in toppings:
        # leftCount 증감
        if not topping in leftSet:
            leftCount += 1
            leftSet.add(topping)
        # rightCount 차감
        rightCounter[topping] -= 1
        if rightCounter[topping] == 0:
            rightCount -= 1
        # 비교
        if leftCount == rightCount:
            answer += 1
    return answer
