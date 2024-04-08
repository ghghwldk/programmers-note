'''
결승전 규칙은 전대회 우승자인 라이언에게 불리
>> 어피치가 n발 쏜 후 라이언이 n발 쏘기
>> 점수 계산

[점수 계산]
1. 10점 ~ 0점
2. 점수 가져가기
더 많은 화살을 쏜 사람이 해당 점수를 가져감
동점이면, 어피치가 가져감
0점이면, k점을 가져가지 않음
3. 최종점수
동점이면, 어피치가 우승

[현재상황]
어피치가 n발 쏜 후 라이언이 화살 쏠 차례
가장 큰 점수로 이기기 위해서는 어떻게 쏴야할 것인가?
'''

# 가장 낮은 점수? >> 이기고 나서 버리면 됨
# 이기기 위한 최소 개수 넣고 나서 가장 낮은 점수에 때려 넣으면 됨

# visited 필요 없다. >> 낮은 점수로만 향하면 됨
def dfs(남은화살, current, temp):
    global cases
    if 남은화살 <= 어피치[current]:
        return


    소진할양 = 어피치[current] + 1
    소진후 = 남은화살 - 소진할양

    갱신가능 = False
    for next in range(current+1, 11):
        if 소진후 > 어피치[next]:
            갱신가능 = True
        temp.append((current, 소진할양))
        dfs(소진후, next, temp)
        temp.pop()
    return

# n: 화살의 개수
# info: 어피치가 맞춘 과녘점수
cases = []
어피치 = []
from sys import setrecursionlimit
setrecursionlimit(int(1e9))
def solution(n, info):
    global 어피치
    어피치 = info

    # cases 구하기
    # for i in range(len(어피치)):
    for i in range(1):
        print('-----------')
        dfs(n, i,[])
    print(cases)


    # print(info)

    isPossible = False
    # 라이언이 가장 큰 점수로 이기기 위해 맞혀야하는 화살개수


    # 가장 작은 원소에 때려넣

    answer = None
    return  answer if isPossible else [-1]

solution(5, [2,1,1,1,0,0,0,0,0,0,0])

'''
n	info	result
5	[2,1,1,1,0,0,0,0,0,0,0]	[0,2,2,0,1,0,0,0,0,0,0]
1	[1,0,0,0,0,0,0,0,0,0,0]	[-1]
9	[0,0,1,2,0,1,1,1,1,1,1]	[1,1,2,0,1,2,2,0,0,0,0]
10	[0,0,0,0,0,0,0,0,3,4,3]	[1,1,1,1,1,1,1,1,0,0,2]
'''