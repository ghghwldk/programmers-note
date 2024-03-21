# 상하좌우 방향에 따른 행과 열 좌표의 변화를 나타내는 리스트
dr = (1, 0, -1, 0)
dc = (0, -1, 0, 1)

def solution(grid):
    answer = []  # 결과를 저장할 리스트

    # 그리드의 세로와 가로 길이를 가져옴
    rows, cols = len(grid), len(grid[0])

    # 4방향 방문 기록 리스트 : 4 * c * r
    visited = [[[False] * 4 for _ in range(cols)] for _ in range(rows)]

    # 모든 좌표에 대해 탐색
    for r in range(rows):
        for c in range(cols):
            # 해당 좌표에서 네 방향을 탐색
            for d in range(4):
                # 이미 방문한 좌표-방향일 경우 넘어감
                if visited[r][c][d]:
                    continue

                # 사용되지 않은 좌표-방향인 경우
                count = 0
                nr, nc = r, c
                # 빛을 이동시켜가며 탐색
                while not visited[nr][nc][d]:
                    visited[nr][nc][d] = True  # 방문한 좌표-방향으로 표시
                    count += 1
                    # 현재 좌표의 타입에 따라 방향 변경
                    if grid[nr][nc] == "S":  # S인 경우 방향 변경 없음
                        pass
                    elif grid[nr][nc] == "L":  # L인 경우 반시계 방향으로 변경
                        d = (d - 1) % 4
                    elif grid[nr][nc] == "R":  # R인 경우 시계 방향으로 변경
                        d = (d + 1) % 4

                    # 좌표가 격자를 벗어난 경우를 고려하여 좌표 이동
                    nr = (nr + dr[d]) % rows
                    nc = (nc + dc[d]) % cols

                # 탐색한 거리를 결과 리스트에 추가
                answer.append(count)
    # 결과를 오름차순으로 정렬
    answer = sorted(answer)
    return answer
