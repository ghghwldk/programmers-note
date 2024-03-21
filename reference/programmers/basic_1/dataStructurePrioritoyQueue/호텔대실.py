'''
heap is necessary to repeatedly remove the object with the highest(or lowest)
priority, or when insertions need to be interspersed with removals of the root node.
'''

from heapq import heappop, heappush


def format(book_time):
    s, e = book_time
    return (int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:]) + 10)

def getFormatted(book_times):
    return [format(book_time) for book_time in book_times]

def solution(book_times):
    book_times = getFormatted(book_times)
    book_times.sort(key= lambda e:(e[0], e[1]))

    # 사용정보를 저장하기 위한 heap을 선언한다.
    usingHeap = []
    # first element
    answer = 1
    heappush(usingHeap, book_times[0][1]) #end만 넣어서 push

    for i in range(1,len(book_times)):
        currentStart, currentEnd = book_times[i]
        if usingHeap[0] <= currentStart:
            heappop(usingHeap)
        else:
            answer += 1
        heappush(usingHeap, currentEnd)

    return answer