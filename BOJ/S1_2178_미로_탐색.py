from collections import deque
import sys

def solution(board, visited):
    return bfs(0, 0)

def bfs(r, c):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    queue = deque()
    dist = 1
    visited[r][c] = 1

    queue.append([r, c, dist])

    while queue:
        current = queue.popleft()
        r = current[0]
        c = current[1]
        dist = current[2]

        if r == N - 1 and c == M - 1:
            break

        for direction in range(4):
            nr = r + dr[direction]
            nc = c + dc[direction]

            if nr == N or nc == M or nr < 0 or nc < 0 or board[nr][nc] != 1 or visited[nr][nc] == 1:
                continue

            # 조건문을 통과해서 이미 방문할 게 확실한 좌표이므로 미리 방문처리
            # (안 하면 시간초과)
            visited[nr][nc] = 1
            queue.append([nr, nc, dist + 1])
    return dist


N, M = map(int, input().split())
board = [list(map(int, ' '.join(sys.stdin.readline()).split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
print(solution(board, visited))