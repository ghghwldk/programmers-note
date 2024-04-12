
global currentWeight, waitings

# weight: 다리가 견딜 수 있는 무게
# bridgeLength: 다리길이
from collections import deque
def solution(bridge_length, weight, truck_weights):
    target, count, time = len(truck_weights), 0, 0
    global currentWeight, waitings, ons
    currentWeight, ons, waitings = 0, deque(), deque(truck_weights)

    # 1초마다 로직수행
    ## 제일 앞에 있는 트럭로직
    # 트럭의 남은 시간이 1인 경우
    while True:
        # 모든 트럭이 도착했을 경우

        time += 1

        ons = deque([(weight, time-1) for weight, time in ons])
        # 트럭의 남아 있는 시간이 1인 경우, 다리 위에서 내려온다.
        if ons:
            if ons[0][1] == 0:
                currentWeight -= ons.popleft()[0]
                count += 1

        if waitings:
            # 올라갈 수 있다면, 트럭이 다리 위에 올라간다.
            if waitings[0] + currentWeight <= weight:
                newWeight = waitings.popleft()
                ons.append((newWeight, bridge_length))
                currentWeight += newWeight

        # print('--------------')
        # print('ons: ', ons)
        # print('waitngs: ',waitings)
        # print('time: ', time)
        # print(currentWeight)
        if target == count:
            break
    return time


# print('result: ', solution(2, 10, [7,4,5,6]))
# print('result: ', solution(100, 100, [10]))
print('result: ', solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
'''
bridge_length	weight	truck_weights	return
2	10	[7,4,5,6]	8
100	100	[10]	101
100	100	[10,10,10,10,10,10,10,10,10,10]	110
'''