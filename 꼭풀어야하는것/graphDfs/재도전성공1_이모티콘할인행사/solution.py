'''
[목표]
1. 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것
2. 이모티콘 판매액을 최대한 늘리는 것

[방식]
- n명의 카카오톡 사용자들에게 이모티콘 m개를 할인하여 판매
- 할인율은 다를 수 있음
-- 할인율은 10%, 20%, 30%, 40% 중 하나

[가입]
- 각 사용자들은 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매
- 각 사용자들은 자신의 기준에 따라 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면
- 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입
'''

cases = []
def dfs(temp, level):
    global cases
    if level > lenEmoticons:
        cases.append(temp[:])
        return

    for next할인율 in 할인율s:
        temp.append(next할인율)
        dfs(temp, level + 1)
        temp.pop()


from sys import setrecursionlimit

setrecursionlimit(int(1e6))
할인율s, lenEmoticons = [10, 20, 30, 40], -1

def solution(users, emoticons):
    global lenEmoticons
    lenEmoticons = len(emoticons)
    dfs([], 1)

    # case는 이모티콘할인율에 대한 모든 경우의 수 중 하나
    resultCase = []
    for case in cases:
        # print('----------------------')
        # print(case)
        총서비스가입, 총구매비용 = 0, 0
        for user in users:
            # 유저의 조건
            유저최저할인율, 유저최고가격 = user
            # 이모티콘과 case를 결합한 것과 user의 조건을 비교한다.
            l = [] # 구입할 이모티콘의 index
            for i, 이모티콘할인율 in enumerate(case):
                if 이모티콘할인율 >= 유저최저할인율:
                    l.append(i)
            예상비용 = int(sum([(100 - case[i]) * emoticons[i] / 100 for i in l]))
            # print(예상비용)
            if 예상비용 >= 유저최고가격:
                총서비스가입 += 1
            else:
                총구매비용 += 예상비용
        # print(총서비스가입, 총구매비용)
        resultCase.append([총서비스가입, 총구매비용])
        resultCase = sorted(resultCase, key= lambda x: (-x[0], -x[1]))
        if len(resultCase) > 1:
            # print(resultCase)
            resultCase.pop()
    # print(resultCase)
    return resultCase[0]
    # 행사 목적을 최대한으로 달성했을 때의 이모티콘 플러스 서비스 가입 수와 이모티콘 매출액
    # 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해주세요.

'''
users	emoticons	result
[[40, 10000], [25, 10000]]	[7000, 9000]	[1, 5400]
[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]	[1300, 1500, 1600, 4900]	[4, 13860]
'''
users, emoticons = [[40, 10000], [25, 10000]], [7000, 9000]
# users, emoticons = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]

solution(users, emoticons)