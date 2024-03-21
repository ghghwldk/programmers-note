from collections import deque

def solution(s):
    queue = deque(s) # 큐 생성
    cnt = 0 # 카운트 초기화

    # 짝수인 경우
    if len(s) % 2 == 0:
        # 문자열 길이만큼 반복
        for i in range(len(s)):
            temp = queue.popleft() # 왼쪽을 뽑아서
            queue.append(temp)     # 오른쪽에 추가
            s = ''.join(queue)     # 문자열로 확인
            # 괄호 쌍이 문자열 안에 있으면 없어질 때까지 반복
            while '[]' in s or '()' in s or '{}' in s:
                if '[]' in s:
                    s = s.replace('[]','')
                if '()' in s:
                    s = s.replace('()','')
                if '{}' in s:
                    s = s.replace('{}','')
            # 문자열이 전부 공백으로 바뀌었으면 count
            if s == '': cnt += 1
        return cnt
    # 홀수인 경우
    else: return 0
