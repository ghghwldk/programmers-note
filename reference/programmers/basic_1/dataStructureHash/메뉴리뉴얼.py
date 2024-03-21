from itertools import combinations
from collections import Counter

def solution(orders, courses):
    answer = []
    course = sorted(courses)

    for course in courses:
        counter = Counter(getCombinated(course, orders))

        for key in counter.keys():
            value = counter[key]
            if value >= 2 and value == max(counter.values()):
                answer.append(key)
    return sorted(answer)

def getCombinated(course, orders):
    l = []
    for order in orders:
        combeds = list(combinations(order, course))
        for combed in combeds:
            l.append("".join(sorted(combed)))
    return l

