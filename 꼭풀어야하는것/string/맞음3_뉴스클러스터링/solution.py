'''
비슷비슷한 제목의 기사가 많다.
>> 필요한 기사를 찾기가 어렵다.

개발의 방향 잡기 위해
>> 관련 기사 검색
>> 기사를 묶어서 보여주면 유용

묶는 기준
>> 자카드 유사도 = 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
>> 다중집합(원소의 중복 허용)에 확장
'''
def isAlpha(c):
    return True if (c >= 'a' and c<= 'z') else False

def getPairs(before):
    result = []
    for i in range(len(before)-1):
        front, back = before[i], before[i+1]
        if isAlpha(front) and isAlpha(back):
            result.append(front + back)
    return result

from collections import Counter
def solution(str1, str2):
    pairs1, pairs2 = getPairs(str1.lower()), getPairs(str2.lower())
    counter1, counter2 = Counter(pairs1), Counter(pairs2)
    # print('--pairs')
    # print(pairs1)
    # print(pairs2)
    set1, set2 = set(pairs1), set(pairs2)
    # print('--set')
    # print(set1)
    # print(set2)
    hap, kyo = set1 | set2, set1 & set2
    # print('--hapkyo')
    # print(hap)
    # print(kyo)
    sumHap, sumKyo = 0, 0
    for item in hap:
        sumHap += max(counter1[item], counter2[item])
    for item in kyo:
        sumKyo += min(counter1[item], counter2[item])

    return 65536 if sumHap == 0 else int(65536 * sumKyo / sumHap)