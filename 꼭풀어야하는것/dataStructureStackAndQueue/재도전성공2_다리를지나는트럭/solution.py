def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length

    while len(truck_weights)!=0:
        time+=1
        #미리 뺴주어야함 (1초가 지날 때마다 무조건 하나는 빠지므로)
        bridge.pop(0)

        #뺀 이후에 무엇을 넣을지만 고민하면 됨
        #만약 sum(bridge) + truck <= weight면 넣어준다.
        #sum함수에서 시간초과가 나니, 변수 설정하는것 필요! (5번 케이스)
        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        else: #아니면 0을 넣어줌
            bridge.append(0)

    #탈출 미리 했으니 후처리
    #브릿지 큐에 방금 마지막 트럭이 들어갔으므로, 브릿지 길이만큼 더해줘야함.
    time += bridge_length

    return time