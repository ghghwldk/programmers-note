from collections import deque

# popleft
q= deque()
q.append(1)
q.append(2)
q.append(3)

print(q)
while q:
    print(q.popleft())

# pop
q2= deque()
q2.append(1)
q2.append(2)
q2.append(3)

print(q2)
while q2:
    # bfs 사용 시 pop이 아닌 popleft 써야함을 명심할 것.
    print(q2.pop())