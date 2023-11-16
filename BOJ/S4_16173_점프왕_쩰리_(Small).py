def solution(n, board, visited):
    dr = [0, 1]
    dc = [1, 0]
    stack = []
    r, c = 0, 0
    # 스택에 시작점 추가
    stack.append(str(r) + " " + str(c))
    # 스택에 값이 있는 동안
    while stack:
        # 마지막 원소 pop 후 좌표 할당, 방문처리
        popped = stack.pop(-1)
        r = int(popped.split()[0])
        c = int(popped.split()[1])
        visited[r][c] = 1
        # 해당 좌표의 값만큼 한 방향으로 이동
        for direction in range(2):
            nr = r + board[r][c] * dr[direction]
            nc = c + board[r][c] * dc[direction]

            # 맵을 벗어나거나 방문한 좌표일 경우 반복
            if nr >= n or nc >= n or visited[nr][nc] == 1:
                continue
            # 목표에 도달한 경우 return 아니면 stack에 추가
            else:
                if board[r][c] == -1:
                    return "HaruHaru"
                stack.append(str(nr) + " " + str(nc))
        print(f"stack = {stack}")
        for row in visited:
            print(row)
    if board[r][c] == -1:
        return "HaruHaru"
    else:
        return "Hing"


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
print(solution(n, board, visited))