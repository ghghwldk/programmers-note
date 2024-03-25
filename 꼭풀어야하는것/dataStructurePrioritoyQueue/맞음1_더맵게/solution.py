# from heapq import heappush, heappop, heapify
import heapq
'''
모든 음식의 스코빌 지수를 K이상으로 변경
'''
def solution(h, K):
    heapq.heapify(h)
    answer = 0

    while True:
        # 스코빌 성립
        if h[0] >= K:
            break
        # mix: 성립하지 않을 경우
        ## 더 이상 섞지 못하는 경우
        if len(h) == 1:
            answer = -1
            break
        ## 섞을 수 있는 경우 섞기
        min1, min2 = heapq.heappop(h), heapq.heappop(h)
        mixed = min1 + min2 * 2
        heapq.heappush(h, mixed)
        ### 섞었으니 횟수추가
        answer += 1
    return answer