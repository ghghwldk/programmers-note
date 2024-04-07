# cap: 트럭이 실을 수 있는 재활용 택배의 개수
# n: 집의 수
# deliveries: 각 집에 배달할 재활용 택배상자 개수
# pickups: 각 집에서 수거할 상자개
def solution(cap, n, deliveries, pickups):
    distance = 0
    idx = 0
    while True:
        # idx += 1
        # if idx == 5:
        #     break
        # print('---------')
        # print('deliveries', deliveries)
        # print('pickups', pickups)

        if isEmpty(deliveries) and isEmpty(pickups):
            break
        # 두 개 중에 최대거리를 더해준다.
        maxIndex = max(getMaxIndex(deliveries), getMaxIndex(pickups))
        distance += (maxIndex+1)

        # cap만큼 deliveries와 pickups에서 차감한다.
        # 큰 인덱스부터 차감한다.
        cap만큼빼기(deliveries, cap)
        cap만큼빼기(pickups, cap)

    return distance * 2

def cap만큼빼기(arr, cap):
    # print(len(arr)-1)
    # print(cap)
    # print('before', arr)
    for i in range(len(arr)-1, -1, -1):
        if cap == 0:
            break
        # print(arr[i], cap)
        if arr[i] >= cap:
            arr[i] -= cap
            cap = 0
        else:
            cap -= arr[i]
            arr[i] = 0
    # print(arr)

def getMaxIndex(arr):
    maxIndex = 0
    if isEmpty(arr):
        return 0

    for i, item in enumerate(arr):
        if not item == 0:
            maxIndex = i
    return maxIndex

def isEmpty(arr):
    result = True
    for item in arr:
        if not item == 0:
            result = False
            break
    return result

# cap	n	deliveries	pickups	result
# 4	5	[1, 0, 3, 1, 2]	[0, 3, 0, 4, 0]	16
# 2	7	[1, 0, 2, 0, 1, 0, 2]	[0, 2, 0, 1, 0, 2, 0]	30

# print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))