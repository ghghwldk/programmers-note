# prices = [1, 2, 3, 2, 3, 1] return [5, 4, 1, 2, 1, 0]
def solution(prices):
    length = len(prices)

    # answer을 max값으로 초기화
    answer = [ i for i in range (length - 1, -1, -1)]

    # 주식 가격이 떨어질 경우 찾기
    stack = [0]
    for i in range (1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer


'''
[deque로도 풀이가능]

from collections import deque
def solution(prices):
    result = []                 # 결과값
    queue  = deque(prices)      # 주식가격 queue
    
    while queue:                # queue가 빈값이 아니면 while loop
        period = 0              # 가격이 떨어지지 않은 기간
        price = queue.popleft() # i번째 주식 가격 추출
        
        for after in queue:     # 미래의 가격 목록
            period += 1         # 가격이 떨어지지 않은 기간 + 1초
            if price > after:   # 미래에 가격이 떨어졌다면
                break           # break
        result.append(period)   # 유지된 기간 결과값에 저장
            
    return result               # 결과값 반환
'''