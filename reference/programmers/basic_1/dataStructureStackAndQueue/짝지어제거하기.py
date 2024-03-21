from collections import deque

def solution(s):
    if not len(s) % 2 == 0:
        return 0
    st = deque()

    for i in range(len(s)):
        current = s[i]
        # must check the size of the st
        # no need to compare
        if len(st) == 0:
            st.append(current)
        else:
            peek = st[len(st)-1]
            if peek == current:
                st.pop()
            else:
                st.append(current)
    return 1 if len(st) == 0 else 0