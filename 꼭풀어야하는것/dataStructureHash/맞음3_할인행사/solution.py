# 10일 동안 회원자격 부여
# 매일 한 가지 제품을 할인 & 하루에 하나씩만 구매가능

# 자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입


# want: 정현이가 원하는 제품을 나타내는 문자열 배열
# number: 정현이가 원하는 제품의 수량을 나타내는 정수배열
# discount: XYZ 마트에서 할인하는 제품을 나타내는 문자열 배열
from collections import Counter
def solution(want, number, discount):
    answer = 0

    condition = list(zip(want, number))

    # get answer
    current = Counter(discount[:10])
    if compare(current, condition):
        answer += 1

    # print(list(condition))
    for i in range(10, len(discount)):
        updateCurrent(current, i, discount)
        # print(i, current, list(condition))
        if compare(current, condition):
            answer += 1

    # 회원등록 날짜의 총일 수
    return answer

def updateCurrent(current, newLastIdx, discount):
    currentLast, beforeFirst = discount[newLastIdx], discount[newLastIdx - 1 -9]

    current[currentLast] = current[currentLast] + 1
    current[beforeFirst] = current[beforeFirst] - 1

# compare condition and current
def compare(current, conditions):
    # print('compare-')
    for i, condition in enumerate(conditions):
        if not condition[1] == current[condition[0]]:
            return False
    return True