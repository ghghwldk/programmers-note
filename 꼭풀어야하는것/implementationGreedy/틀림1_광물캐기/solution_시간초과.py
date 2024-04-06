'''
곡괭이 각 5개씩
각 곡괭이는 종류에 상관없이 광물 5개를 캔 후에는 더 이상 사용할 수 없다.

'''
'''
picks: 곡괭의 수 [dia, iron, stone]
minerals: 광
'''

def 필요한곡괭이만(picks):
    필요한곡괭이수 = len(minerals) // 5
    if not len(minerals) % 5 == 0:
        필요한곡괭이수 += 1
    result = []
    for i in range(3):
        if picks[i] <= 필요한곡괭이수:
            result.append(picks[i])
        else:
            result.append(필요한곡괭이수)
        필요한곡괭이수 -= result[i]
    return result
def get필요한곡괭이s(picks):
    필요한곡괭이s = []
    for i, pick in enumerate(picks):
        if i == 0:
            for i in range(pick):
                필요한곡괭이s.append('dia')
        elif i == 1:
            for i in range(pick):
                필요한곡괭이s.append('iron')
        else:
            for i in range(pick):
                필요한곡괭이s.append('stone')
    return 필요한곡괭이s

def getPartitions(minerals):
    result = []
    for i in range(0, len(minerals), 5):
        result.append(minerals[i:i+5])
    return result

def getCostPerPartition(partition, 곡괭이):
    cost = 0
    for mineral in partition:
        if 곡괭이 == 'dia':
            if mineral =='diamond':
                cost += 1
            elif mineral == 'iron':
                cost += 1
            elif mineral == 'stone':
                cost += 1
        elif 곡괭이 =='iron':
            if mineral =='diamond':
                cost += 5
            elif mineral == 'iron':
                cost += 1
            elif mineral == 'stone':
                cost += 1
        else:
            if mineral =='diamond':
                cost += 25
            elif mineral == 'iron':
                cost += 5
            elif mineral == 'stone':
                cost += 1
    return cost

from itertools import permutations
def solution(picks, minerals):
    picks = 필요한곡괭이만(picks)
    필요한곡괭이s = get필요한곡괭이s(picks)
    cases = permutations(필요한곡괭이s, len(필요한곡괭이s))

    partitions = getPartitions(minerals)

    minCost = 1e9
    for case in cases:
        cost = 0
        for i, 곡괭이 in enumerate(case):
            cost += getCostPerPartition(partitions[i], 곡괭이)
        minCost = min(minCost, cost)
    return minCost
# getCostPerPartition(partition, 곡괭이):


# picks =  [1, 3, 2]
# minerals =  ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]

#
picks = [0, 1, 1]
minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
print(solution(picks, minerals))