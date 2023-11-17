from collections import deque

def solution(board):
    answer = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                dfs(i, j)
                answer += 1
    return answer

def dfs(r, c):
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    stack = deque()
    stack.append([r, c])

    while stack:
        current = stack.pop()
        cur_r = current[0]
        cur_c = current[1]
        board[cur_r][cur_c] = 0

        for direction in range(4):
            nr = cur_r + dr[direction]
            nc = cur_c + dc[direction]

            if nr >= N or nc >= M or nr < 0 or nc < 0 or board[nr][nc] != 1:
                continue

            stack.append([nr, nc])
    return

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    for _ in range(K):
        C, R = map(int, input().split())
        board[R][C] = 1

    print(solution(board))
