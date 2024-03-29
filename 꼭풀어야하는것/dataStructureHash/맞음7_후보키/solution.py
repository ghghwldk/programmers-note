from itertools import combinations
row = 0
col = 0
def solution(relation):
    global row
    global col
    row = len(relation)
    col = len(relation[0])


    candidates = getColumnCandidates()
    uniques = getUniques(candidates, relation)
    return getLenMinimum(uniques)
#     # 최소성
#     answer = set(unique)
#     for i in range(len(unique)):
#         for j in range(i + 1, len(unique)):
#             if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
#                 answer.discard(unique[j])

#     return len(answer)

def getLenMinimum(uniques):
    result = 0

    uniques = sorted(uniques, key= len)
    isSupers = [False for i in range(len(uniques))]
    for i in range(len(uniques)):
        if isSupers[i]:
            continue
        else:
            result += 1
        current = set(uniques[i])
        for j in range(i+1, len(uniques)):
            other = set(uniques[j])
            if len(current) == len(current & other):
                isSupers[j] = True
    return result

def getUniques(candidates, relation):
    global row
    global col

    result = []
    temp = []

    for candidate in candidates:
        tmp = [tuple([item[i] for i in candidate]) for item in relation]

        if len(set(tmp)) == row:
            result.append(candidate)
    return result


def getColumnCandidates():
    global col
    result = []
    temp = [i for i in range(col)]

    for i in range(1, col+1):
        for item in list(combinations(temp, i)):
            result.append(list(item))

    return result