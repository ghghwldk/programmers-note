# 멈춰둔 과제가 여러개일 경우, 가장 최근에 멈춘 과제부터 시작 >> 스택 사용
from collections import deque

def convert_time(s):
    h, m = map(int, s.split(':'))
    return h * 60 + m

def solution(plans):
    answer = []

    plans = [ (name, convert_time(start), int(playtime)) for name, start, playtime in plans]
    plans.sort(key = lambda x : x[1])

    assign_s = deque()
    left_time = 0

    for i in range(len(plans)):
        name, start, playtime = plans[i]

        while assign_s :
            _name, _playtime = assign_s.pop()
            if left_time >= _playtime :
                left_time -= _playtime
                answer.append(_name)
            else :
                assign_s.append((_name, _playtime - left_time))
                break

        assign_s.append((name, playtime))

        if i < len(plans)-1 :
            next_start = plans[i+1][1]
            left_time = next_start - start

    while assign_s :
        _name, _ = assign_s.pop()
        answer.append(_name)

    return answer