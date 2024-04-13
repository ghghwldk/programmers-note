answer = []



def solution(n):
    hanoi(1,3,2,n)

    return answer

def hanoi(src, tgt, inter, n): # 인자 순서 넣어주는 게 좀 헷갈렸음.
    global answer

    if n == 1:
        answer.append([src, tgt])
    else:
        hanoi(src,inter,tgt,n-1)
        hanoi(src,tgt,inter,1)
        hanoi(inter,tgt,src,n-1)