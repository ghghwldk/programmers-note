def solution(n,a,b):
    result = 1
    bigger, smaller = max(a,b), min(a,b)

    while(True):
        # to wirte the condition 'bigger % 2 == 0'
        # i have to write down the logic on the paper
        if bigger - smaller == 1 and bigger % 2 == 0:
            break
        else:
            result += 1
            bigger, smaller = getNext(bigger), getNext(smaller)
    return result

def getNext(previous):
    result = -1
    # even
    if previous % 2 == 0:
        result = previous // 2
    else:
        result = (previous+1) // 2

    return result