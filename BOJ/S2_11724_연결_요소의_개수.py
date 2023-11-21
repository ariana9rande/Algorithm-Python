from collections import deque
import sys

def solution(visited):
    answer = 0
    for i in range(1, N + 1):
        if i not in visited:
            dfs(i)
            answer += 1
    return answer

def dfs(v):
    stack = deque()
    stack.append(v)

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.append(current)
            # print(f"{current} appended")

            for item in adjList[current]:
                stack.append(item)
    # print("end")
    return


N, M = map(int, input().split())
# adjMatrix = [[0] * (N + 1) for _ in range(N + 1)]
adjList = [[] for _ in range(N + 1)]
visited = []
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    # adjMatrix[u][v] = 1
    # adjMatrix[v][u] = 1

    adjList[u].append(v)
    adjList[v].append(u)

# for row in adjMatrix:
#     print(row)
# print(adjList)

print(solution(visited))
