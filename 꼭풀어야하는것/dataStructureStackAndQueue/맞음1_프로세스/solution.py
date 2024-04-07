'''
1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
'''

# priorities: 현재 실행 대기 큐에 있는 프로세스의 중요도가 담긴 배열
# location: 몇번째로 실행되는지 알고싶은 프로세스의 위
from collections import deque
def solution(priorities, location):
    # priorities에다가 인덱스
    indexes = list(range(len(priorities)))
    pendingQ = deque(zip(priorities, indexes))

    priorities = deque(sorted(priorities, reverse= True))

    finished = []
    while pendingQ:
        target = priorities.popleft()

        popped = pendingQ.popleft()

        while True:
            poppedPriority, poppedIndex  = popped
            # target과 꺼낸 우선순위가 동일할 때까지 반복
            if target == poppedPriority:
                finished.append((poppedPriority, poppedIndex))
                break
            else:
                pendingQ.append(popped)
            popped = pendingQ.popleft()
        if poppedIndex == location:
            break

    # 문제 규칙에 따라 프로세스를 관리할 경우
    # 특정 프로세스가 몇 번째로 실행되는지 출력
    return len(finished)


# priorities, location =[1, 1, 9, 1, 1, 1], 0
priorities, location =[2, 1, 3, 2], 2
print(solution(priorities, location))