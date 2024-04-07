'''
최소피로도: 각 던전마다 탐험을 시작하기 위해 필요
소모피로도: 던전을 탐험 후 소모되는 피로도

탐험을 해야하는 던전이 여러개가 있을 때, 한 유저가 오늘 이 던전을 최대한 많이 탐험
'''

# k: 유저의 현재 피로도
# dungeons: 각 던전별 최소피로도, 소모피로도

from itertools import permutations
def solution(k, dungeons):
    indexes = list(range(0, len(dungeons)))
    cases = list(permutations(indexes, len(indexes)))

    maxCount = -1
    for case in cases:
        count = 0
        currentK = k

        for index in case:
            min피로도, 소모피로도 = dungeons[index][0], dungeons[index][1]
            # 최소피로도 비교
            # print(currentK, min피로도)
            if currentK >= min피로도:
                # 소모피로도만큼 소비
                count += 1
                currentK -= 소모피로도
            else:
                break
        maxCount = max(maxCount, count)

    # 유저가 탐험할 수 있는 최대 던전 수
    return maxCount

k = 80
dungeons = [[80,20],[50,40],[30,10]]
# print(solution(k, dungeons))