max_num = -1
answer = []

def solution(n, info):
    # 어피치와 라이언의 점수배열을 보고 점수가 몇 점인지 구하는 함수
    def cal(appeach, lion):
        a_score, l_score = 0, 0
        for i in range(11):
            if appeach[i] == lion[i] == 0: continue
            elif appeach[i] > lion[i]:
                a_score += 10 - i
            else:
                l_score += 10 - i
        return a_score, l_score
    # dfs를 사용한 백트래킹 함수
    def dfs(lion, idx):
        global max_num, answer
        # 라이언의 배열에 숫자를 모두 채웠을 때, 점수 차가 최대인지 구하는 부분
        '''
        1. (라이언 점수 - 어피치 점수)가 최대이면 answer에 만들었던 라이언 배열을 추가
        2. 이전에 갱신된 max_num과 동일한 값이면 answer에 추가
        '''
        if idx == 11:
            a, l = 0, 0
            if sum(lion) == n:
                a, l = cal(info, lion)
            # 라이언이 남은 화살을 모두 과녘의 0점 배점인 곳에 맞힌 것
            elif sum(lion) < n:
                lion[-1] += (n - sum(lion))
                a, l = cal(info, lion)
            else:
                return

            if a < l:
                if max_num < (l-a):
                    max_num = (l-a)
                    answer = [lion[:]]
                elif max_num == (l-a):
                    answer.append(lion[:])
            return

        lion.append(info[idx]+1)
        dfs(lion, idx+1)
        lion.pop()

        lion.append(0)
        dfs(lion, idx+1)
        lion.pop()

    dfs([], 0)
    if not answer: return [-1]
    # 가장 낮은 점수를 더 많이 맞힌 경우
    answer.sort(key=lambda x: x[::-1], reverse=True)
    return answer[0]