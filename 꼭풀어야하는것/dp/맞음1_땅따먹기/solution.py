'''
i'm moving down the rows one by one.
the same column cannot be touched consecutively.
'''
def solution(land):
    # to record the maximum score
    rCount, cCount = len(land), len(land[0])

    # step by step based on the row
    for r in range(1, rCount):
        for c in range(cCount):
            # get the maximum value of previous column on diffrent Column
            previousMax = 0
            for i in range(4):
                if i == c: continue
                previousMax = max(previousMax, land[r-1][i])

            land[r][c] = previousMax + land[r][c]
    # print(land)
    # maximum score i can win after moving to the last row.
    answer =0
    for i in range(4):
        answer = max(answer, land[rCount - 1][i])

    return answer