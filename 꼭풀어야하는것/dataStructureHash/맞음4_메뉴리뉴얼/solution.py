'''
단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다.
또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하기로 했습니다.
'''

def separate(s):
    l = list()
    for c in s:
        l.append(c)
    l = sorted(l)
    return l

def appendList(before, additional):
    for item in additional:
        before.append(item)
#[('X', 'Y'), ('W', 'X')]
def makeResult(before):
    result = []
    # print('-before', before)
    for item in before:
        s = ''
        for c in list(item):
            s = s+ c
        result.append(s)
    result = sorted(result)
    # print(result)
    return result
from collections import defaultdict
from itertools import combinations
def solution(orders, courses):
    # get candidates
    candidates = defaultdict(list)

    for i, course in enumerate(courses):
        temp = list()
        for order in orders:
            if len(order) < course:
                continue
            appendList(temp, list(combinations(separate(order), course)))

        temp = list(set(temp))
        if i == 0:
            candidates[course] = temp
        else:
            before = candidates[course]
            appendList(before, temp)
    # get most popular
    courses = [tuple(separate(order)) for order in orders]

    temps = []
    for k in candidates.keys():
        temp = list()
        #v는 list
        maxCount = -1
        for item in candidates[k]:

            count = 0

            for course in courses:
                if len(set(item) - set(course)) == 0:
                    # print(set(item), set(course))
                    count += 1
            # print('-count', count)
            if not count >= 2:
                continue

            if maxCount < count: # 갱신
                maxCount = count
                temp.clear()
                temp.append(item)
            elif maxCount == count:
                temp.append(item)
        if len(temp) > 0:
            appendList(temps, temp)
    return makeResult(temps)