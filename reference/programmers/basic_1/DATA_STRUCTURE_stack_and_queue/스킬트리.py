# 문제를 분석해보면, 스킬트리는 앞에서부터 유효성을 확인 >> 큐 사용
from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        # 정석적인 스킬트리를 큐에 넣고, 하나씩 봅는다.
        queue = deque(skill)
        whether = True
        # for문을 통해 검증이 필요한 스킬트리를 하나하나 확인
        for s in tree:
            # skill에 저장되지 않은 스킬은 유효성 판단 필요x
            if s not in queue:
                continue
            else:
                # 선행스킬을 배우는 것
                if s == queue[0]:
                    queue.popleft()
                # 큐의 가장 앞에 있지 않다면, 다른 선행스킬을 배우지 않은 것
                else:
                    whether = False
                    break
        if whether:
            answer += 1

    return answer
