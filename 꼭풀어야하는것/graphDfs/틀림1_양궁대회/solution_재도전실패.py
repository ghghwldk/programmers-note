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

def compare(temp):
    isWin, 점수 = False, 0

    라, 어 = 0, 0
    for i in range(11):
        if temp[i] == 0 and 어피치[i] == 0:
            continue
        elif temp[i] > 어피치[i]:
            라 += (10-i)
        else:
            어 += (10-i)
    # print(라, 어, temp)
    isWin = 라 > 어
    점수 = 라

    return isWin, 점수
# visited 필요 없다. >> 낮은 점수로만 향하면 됨
def dfs(step, 남은화살, temp):
    # print(어피치)
    # print(step, 남은화살, temp)
    global result, lastScore
    if 남은화살 < 0:
        return
    if 남은화살 == 0 or step == maxStep:
        # 어피치점수와 비교해서 점수가 높은경우이만 진행
        temp = convert(temp, 남은화살)
        # print(getPoint(temp),temp)
        print(temp)
        isWin, 점수 = compare(temp)
        if isWin:

            if not result:
                result, lastScore = temp, 점수
            else:
                비교해서result업데이트(temp, 점수)
        return
    # print('step:', step, '남은화살:', 남은화살, temp)
    소진할양 = 어피치[step] + 1
    소진후 = 남은화살 - 소진할양
    for next in range(step+1, 11):
        temp.append((step, 소진할양))
        dfs(next, 소진후, temp)
        temp.pop()
    return

def 비교해서result업데이트(temp, 점수):
    global lastScore, result
    if lastScore > 점수:
        return
    elif lastScore < 점수:
        lastScore = 점수
        result = temp
    else:
        l1, l2 = result, temp
        print(l1, l2)
        for i in range(len(l1)-1, -1, -1):
            if l1[i] > l2[i]:
                result = l1
                break
def getPoint(l):
    point = 0
    for i, count in enumerate(l):
        point += (10-i) * count
    return point

def convert(before, 남은화살):
    l = [0] * 11
    for i, count in before:
        l[i] = count
    l[10] += 남은화살
    return l


# n: 화살의 개수
# info: 어피치가 맞춘 과녘점수
어피치, maxStep, result, totalN, lastScore = None, None, None, None, None
from sys import setrecursionlimit
setrecursionlimit(int(1e9))
def solution(n, info):
    global 어피치, maxStep, totalN
    maxStep, 어피치 = len(info) - 1, info

    totalN = n
    for i in range(len(어피치)):
        dfs(i, n,[])

    return result if result else [-1]

# solution(5, [2,1,1,1,0,0,0,0,0,0,0])
print('result:',solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
'''
n	info	result
5	[2,1,1,1,0,0,0,0,0,0,0]	[0,2,2,0,1,0,0,0,0,0,0]
1	[1,0,0,0,0,0,0,0,0,0,0]	[-1]
9	[0,0,1,2,0,1,1,1,1,1,1]	[1,1,2,0,1,2,2,0,0,0,0]
10	[0,0,0,0,0,0,0,0,3,4,3]	[1,1,1,1,1,1,1,1,0,0,2]
'''