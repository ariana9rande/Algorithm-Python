from collections import deque

N, K = map(int, input().split())
dp = [-1] * 100001

queue = deque()
# queue에 시작점 넣고 방문처리
queue.append(N)
dp[N] = 0


while queue:
    current = queue.popleft()

    if current == K:
        print(dp[current])
        break

    # -1, +1, *2 돌면서
    for i in (current - 1, current + 1, current * 2):
        # i가 범위 내에 있고 방문하지 않았을 경우 -> 조건문 순서 중요(IndexError)
        if 0 <= i <= 100000 and dp[i] == -1:
            # dp리스트에 값 저장 하고 큐에 추가
            dp[i] = dp[current] + 1
            queue.append(i)