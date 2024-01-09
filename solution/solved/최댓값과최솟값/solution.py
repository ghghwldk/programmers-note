# find out the minimum and maximum values among the numbers
def solution(s):
    l = list(map(int, s.split(' ')))

    l = sorted(l)

    return str(l[0]) + ' ' + str(l[len(l)-1])