def solution(A,B):
    # natural numbers!

    A = sorted(A)
    B = sorted(B, reverse = True)

    sum = 0
    for i in range(len(A)):
        sum += (A[i] * B[i])

    return sum