'''
요 것은 외우는 문제이다...
'''
def solution(sequence, k):
    answer = []
    start, end = 0,0
    currentSum = sequence[0]
    min_len = 1e9

    while start <= end < len(sequence):
        if currentSum == k :
            currentLen = end - start + 1

            if currentLen < min_len :
                min_len = currentLen
                answer = [start, end]

            currentSum -= sequence[start]
            start += 1
        else:
            if currentSum < k :
                end += 1
                if end < len(sequence) :
                    currentSum += sequence[end]
            else:
                currentSum -= sequence[start]
                start += 1
    return answer

