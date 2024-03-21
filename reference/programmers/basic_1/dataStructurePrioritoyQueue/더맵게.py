from heapq import heapify, heappush, heappop

def solution(scoville, K):
    heapify(scoville)
    answer = 0

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        answer += 1
        min1, min2 = heappop(scoville), heappop(scoville)
        # insert new elements
        heappush(scoville, min1 + (min2* 2))


    return answer