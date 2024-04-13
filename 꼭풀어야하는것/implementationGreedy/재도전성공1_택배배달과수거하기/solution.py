# cap: 트럭이 실을 수 있는 재활용 택배의 개수
# n: 집의 수
# deliveries: 각 집에 배달할 재활용 택배상자 개수
# pickups: 각 집에서 수거할 상자개
def solution(cap, n, deliveries, pickups):
    deliveries = 스택으로convert(deliveries)
    pickups = 스택으로convert(pickups)


    distance = 0
    while True:
        # idx += 1
        # if idx == 5:
        #     break
        # print('---------')
        # print('deliveries', deliveries)
        # print('pickups', pickups)

        if (not deliveries) and (not pickups):
            break

        maxD = -1
        maxP = -1

        # 두 개 중에 최대거리를 더해준다.
        # print('-----------')
        maxIndex = max(cap만큼빼기(deliveries, cap), cap만큼빼기(pickups, cap))
        distance += (maxIndex+1)

    return distance * 2

def 스택으로convert(before):
    after = []
    for i, value in enumerate(before):
        if not value == 0:
            after.append((i, value))
    return after

def cap만큼빼기(arr, cap):
    maxIdx = -1
    # print('cap만큼 빼기 전', arr)
    while arr and cap > 0:
        popped = arr.pop()
        i, value = popped

        if value >= cap:
            if not value == cap:
                arr.append((i, value - cap))
            cap = 0
        else:
            cap -= value
        maxIdx = max(maxIdx, i) # 비효율적인 코드. 일단~
    # print('cap만큼 빼고난 후', arr)

    return maxIdx


# cap	n	deliveries	pickups	result
# 4	5	[1, 0, 3, 1, 2]	[0, 3, 0, 4, 0]	16
# 2	7	[1, 0, 2, 0, 1, 0, 2]	[0, 2, 0, 1, 0, 2, 0]	30

# print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))