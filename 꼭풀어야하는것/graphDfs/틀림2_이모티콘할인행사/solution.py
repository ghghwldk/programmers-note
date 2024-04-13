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
def solution(users, emoticons):
    answer = [0, 0]
    data = [10 ,20, 30, 40]
    discount = []

    # 이모티콘 할인율 구하기
    def dfs(temp, depth):
        if depth == len(temp):
            discount.append(temp[:])
            return
        for d in data:
            temp[depth] += d
            dfs(temp, depth + 1)
            temp[depth] -= d

    dfs([0] * len(emoticons), 0)

    # 완전탐색
    for d in range(len(discount)):
        join, price = 0, [0] * len(users)
        for e in range(len(emoticons)):
            for u in range(len(users)):
                # 할인율을 만족하면 구매
                if users[u][0] <= discount[d][e]:
                    price[u] += emoticons[e] * (100 - discount[d][e]) / 100

        # 구매 금액에 따라 가입자 갱신
        for u in range(len(users)):
            if price[u] >= users[u][1]:
                join += 1
                price[u] = 0

        # 최대 가입자, 구매 금액 갱신
        if join >= answer[0]:
            if join == answer[0]:
                answer[1] = max(answer[1], sum(price))
            else:
                answer[1] = sum(price)
            answer[0] = join


    return answer