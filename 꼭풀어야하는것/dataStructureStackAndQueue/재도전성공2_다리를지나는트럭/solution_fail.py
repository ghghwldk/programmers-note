'''
bridge_length: 다리에 올라갈 수 있는 트럭 수
weight: 다리가 견딜 수 있는 무게
truck_weights: 트럭별 무게
'''
from collections import deque
currentWeight = 0
arriveTarget = 0

def solution(bridge_length, weight, truck_weights):
    onBridges = []
    arriveTarget = len(truck_weights)
    # 무게, 잔여시간
    remains = [(weight, bridge_length) for weight in truck_weights]
    remains = deque(truck_weights)

    minTime = 0

    # 모든 트럭이 다리를 건널 때까지 진행
    # while True:
    for i in range(10):
        if len(remains) == 0:
            continue
        # decreaseTime
        onBridges = decreaseTime(onBridges)
        removeFirst(onBridges)
        if arriveTarget == 0:
            break

        addTruck(remains, weight, onBridges, bridge_length)

        print('i:', i, 'onBridges:', onBridges, 'arriveTarget:', arriveTarget)
    # 모든 트럭이 다리를 건너기 위한 최소시간
    return minTime

def addTruck(remains, weight, onBridges, bridgeLength):
    global currentWeight
    global arriveTarget

    if len(remains) == 0:
        return
    if currentWeight + remains[0] > weight:
        return
    head = remains.popleft()
    onBridges.append([head, bridgeLength])
    currentWeight += head
    arriveTarget -= 1

def decreaseTime(onBridges):
    result = []
    print('onBridges here')
    print(onBridges)
    # for onBridge in onBridges:
    # weight, remainTime = onBridge
    # result.append((weight, remainTime-1))
    # print(result)
    return result

def removeFirst(onBridges):
    global currentWeight

    onBridges = deque(onBridges)
    if len(onBridges) > 0:
        remainTime = onBridges[0][1]

        if remainTime == 0:
            currentWeight -= onBridges.popleft()