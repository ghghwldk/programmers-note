
def solution(board):
    n = len(board)
    m = len(board[0])

    # 현재의 위치에서 가능한 최대 크기의 정사각형의 한 변의 길이를 dp에 저장한다.
    dp = [[0]*m for _ in range(n)]
    dp[0] = board[0]
    for i in range(1,n):
        dp[i][0] = board[i][0]

    # 2중 포문으로 연산
    for i in range(1, n):
        for j in range(1, m):
            '''
                현재의 위치에서 가능한 최대 크기의 정사각형의 한 변의 길이'는 가장 작은 값에 1을 더한 값이다! 
                (단, 현재 위치의 board값이 1일 때!)
            '''
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    # 최대 넓이 구하기
    answer = 0
    for i in range(n):
        temp = max(dp[i])
        answer = max(answer, temp)

    return answer**2