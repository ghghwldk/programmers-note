'''
https://ckd2806.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python-%EC%88%9C%EC%97%B4-%EC%A1%B0%ED%95%A9-%EC%BD%94%EB%93%9C%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
'''
l = ['a', 'b', 'c', 'd']
n = len(l)
r = 2
answer = []

def dfs(idx, list):
    # 전체를 돌았을 때
    if idx == n:
        # 해당 경우의 수의 요소 개수가 r개와 같다면
        if len(list) == r:
            # 답이다
            answer.append(list[:])
        #모두 돌았으니 정답이든 아니든 리턴해줌
        return
    # 자기 자신을 포함시킬 경우
    list.append(l[idx])
    dfs(idx+1, list)
    # 자기 자신을 포함시키지 않을 경우
    list.pop()
    dfs(idx+1, list)

dfs(0, [])
print(answer)