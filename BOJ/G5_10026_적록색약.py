from collections import deque

# 일반적인 / 적록색약 구분할 isNormal 파라미터 추가
def solution(board, isNormal):
    answer = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if not visited[i][j]:
                # board에서 방문되지 않은 좌표가 있다면 isNormal 값에 따라 dfs 호출
                if isNormal:
                    dfs(i, j, 1)
                else:
                    dfs(i, j, 0)
                answer += 1
    return answer

# 일반적인 / 적록색약 구분할 isNormal 파라미터 추가
def dfs(r, c, isNormal):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    stack = deque()
    stack.append([r, c])

    while stack:
        current = stack.pop()
        r = current[0]
        c = current[1]
        visited[r][c] = 1

        for direction in range(4):
            nr = r + dr[direction]
            nc = c + dc[direction]

            # 일반적인 경우 - board의 범위를 넘지 않고 탐색을 시작한 좌표와 같은 값의 좌표만 탐색
            if isNormal:
                if nr >= N or nc >= N or nr < 0 or nc < 0 or visited[nr][nc] or board[nr][nc] != board[r][c]:
                    continue
            # 적록색약 - 탐색을 시작한 좌표가 R or G일 경우 같은 값으로 취급
            else:
                if nr >= N or nc >= N or nr < 0 or nc < 0 or visited[nr][nc]:
                    continue

                if board[r][c] == 'B':
                    if board[nr][nc] != board[r][c]:
                        continue
                else:
                    if board[nr][nc] == 'B':
                        continue

            stack.append([nr, nc])

N = int(input())
board = [input() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
print(solution(board, 1), end=' ')
# dfs 한 번 수행 이후 visited 리스트 초기화 필요
visited = [[0] * N for _ in range(N)]
print(solution(board, 0))