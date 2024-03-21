from collections import deque

# order: 택배 기사님이 원하는 상자 순서를 나타내는 정수 배열
def solution(order):
    answer = 1
    order = deque(order)
    stack = []
    result = []
    size = len(order)

    for i in range(1, size + 1):
        stack.append(i)  #박스를 서브 컨테이너에 옮긴다
        while stack:
            if order and stack[-1] == order[0]:  #서브 컨테이너에서 트럭으로 옮긴다
                num = stack.pop()
                order.popleft()
                result.append(num)
            else:  #만약 트럭으로 옮기는 순서가 잘못 됐다면 중지한다.
                break

    return len(result) #트럭에 실은 박스 갯수를 반환한다.