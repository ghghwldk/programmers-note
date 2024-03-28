'''
H-Index: 과학자의 생산성과 영향력

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상
나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
'''
from collections import Counter
def solution(citations):
    lenCitations = len(citations)
    counter = Counter(citations)
    citationSet = set(citations)

    conditions = sorted(list(range(lenCitations+1)), reverse=True)

    for condition in conditions:
        이상Count = get이상Count(citationSet, counter, condition)
        나머지 = lenCitations - 이상Count
        # print(condition, 이상Count, 나머지)
        if 이상Count >= condition and 나머지 <= condition:
            return condition

def get이상Count(citationSet, counter, condition):
    result = 0
    for item in citationSet:
        if item >= condition:
            result += counter[item]
    return result