'''
https://ckd2806.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python-%EC%88%9C%EC%97%B4-%EC%A1%B0%ED%95%A9-%EC%BD%94%EB%93%9C%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
'''

l = ['a', 'b', 'c']
visited = [0 for _ in range(len(l))]
answer = []

def dfs(cnt, list):
    if cnt == len(l):
        answer.append(list[:])
        return

    for i, val in enumerate(l):
        # 만약 방문했다면 건너 뛰기(순열을 위함)
        if visited[i] == 1:
            continue
        # 현재까지의 list에 값을 추가하고, 방문 표시하기
        list.append(val)
        visited[i] = 1

        dfs(cnt+1, list)
        # 방금 전 list에 추가한 값과 방문 한 것을 되돌려주기
        list.pop()
        visited[i] = 0


dfs(0, [])
print(answer)