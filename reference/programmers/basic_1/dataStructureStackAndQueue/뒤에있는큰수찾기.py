'''
완전탐색으로 진행하면, 시간초과 문제발생
>> 스택으로 해결
'''
def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer


