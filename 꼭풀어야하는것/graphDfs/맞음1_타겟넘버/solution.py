t, maxStep, nums = None, None, None
count = 0

def solution(numbers, target):
    # 컴파일러에서 호출되는 solution함수에서도 값을 변경하려면 global 작성 필수
    global t, maxStep, nums

    t, maxStep, nums = target, len(numbers), numbers

    dfs(0, 0)

    return count

def dfs(before, step):
    global count
    if step == maxStep:
        if before == t:
            count += 1
        return

    nextVals = [before + nums[step], before - nums[step]]

    for nextVal in nextVals:
        dfs(nextVal, step+1)
