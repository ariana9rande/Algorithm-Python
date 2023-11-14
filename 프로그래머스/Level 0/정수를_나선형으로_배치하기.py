def solution(n):
    answer = [[0] * n for _ in range(n)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r, c = 0, 0
    i = 1

    while i <= n * n:
        for direction in range(4):
            while True:
                nr = r + dr[direction]
                nc = c + dc[direction]

                if nr == n or nc == n or nr < 0 or nc < 0 or answer[nr][nc] != 0:
                    break
                else:
                    answer[r][c] = i
                    r = nr
                    c = nc
                    i += 1
        if i == n * n:
            answer[r][c] = i
            break
    return answer


n = int(input())
for row in solution(n):
    print(row)