'''
before following the 124 country's own rules
i have to implement the 3진법
'''

def samjin(n):
    result = ''
    n = n-1
    while n > 0:
        current = None
        if n % 3 == 0:
            current = '1'
        elif n%3 == 1:
            current = '2'
        elif n%3 == 2:
            current = '4'

        result = current + result
        n = n // 3
    return result


def solution(n):
    print(samjin(n))
    return samjin(n)