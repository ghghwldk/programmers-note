def solution(s):
    stack = []
    for i in range(len(s)):
        c = s[i]
        if len(stack) == 0:
            # 첫번째는 스택에서 마지막
            # char를 꺼내서 비교할 수 없으므로 생략
            stack.append(c)
        else:
            # 마지막 char를 꺼내지 않고 현재 char와 비교
            # 비교해서 동일하면, stack에서 pop
            last = stack[len(stack) - 1]
            if last == c:
                stack.pop()
            # 비교해서 동일하지 않으면, 현재 char를 stack에 넣어준다.
            else:
                stack.append(c)
        # print(stack)
    return 1 if len(stack) == 0 else 0
print(solution('baabaa'))
print(solution('cdcd'))
'''
baabaa	1
cdcd	0
'''