from collections import deque

def solution(s):
    left, right = '(', ')'

    st = deque()

    isCorrect = False
    for i in range(len(s)):
        current = s[i]

        # if stack is empty
        if len(st) == 0:
            # if current is righ parenthesis
            # the give string is incorrect parenthesis
            if current == right:
                isCorrect = False
                break
            else:
                st.append(current)
        else:
            peek = st[len(st)-1]
            if current == left:
                if peek == right:
                    isCorrect = False
                    break
                else:
                    st.append(current)
            elif current == right:
                if peek == left:
                    st.pop()
        # print(st)
        if i == len(s) -1 and len(st) == 0:
            isCorrect = True

    return isCorrect
