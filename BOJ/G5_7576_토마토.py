from collections import deque
import sys

def bfs():
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    queue = deque()
    dist = 0

    # 탐색 전에 board[r][c] = 1인 좌표를 queue에 추가하고 시작
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                queue.append([i, j, dist])
                visited[i][j] = 1

    while queue:
        current = queue.popleft()
        r = current[0]
        c = current[1]
        dist = current[2]

        for direction in range(4):
            nr = r + dr[direction]
            nc = c + dc[direction]

            if nr == N or nc == M or nr < 0 or nc < 0 or board[nr][nc] == -1 or visited[nr][nc]:
                continue

            visited[nr][nc] = 1
            queue.append([nr, nc, dist + 1])

    # 탐색이 끝나고 값이 -1가 아닌데 방문하지 못한 좌표가 있는 경우 도달할 수 없는 경우이므로 -1 리턴
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != -1 and not visited[i][j]:
                return -1

    # 아니면 거리 리턴
    return dist


M, N = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
print(bfs())