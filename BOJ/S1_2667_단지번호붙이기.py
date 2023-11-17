from collections import deque

def solution(board):
    answer = []
    dfsResult = []

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                result = dfs(i, j)
                if result != 0:
                    dfsResult.append(result)

    answer.append(len(dfsResult))
    for item in sorted(dfsResult):
        answer.append(item)

    return answer

def dfs(r, c):
    count = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    stack = deque()
    stack.append([r, c])

    while stack:
        # print(f"stack = {stack}")
        current = stack.pop()
        r = current[0]
        c = current[1]

        if board[r][c] == 1:
            count += 1
        board[r][c] = 0
        # for row in board:
        #     print(row)
        # print(f"count = {count}")

        for direction in range(4):
            nr = r + dr[direction]
            nc = c + dc[direction]

            if nr >= N or nc >= N or nr < 0 or nc < 0 or board[nr][nc] != 1:
                continue

            stack.append([nr, nc])

    return count


N = int(input())
board = [list(map(int, ' '.join(input()).split())) for _ in range(N)]

# for row in board:
#     print(row)

for item in solution(board):
    print(item)