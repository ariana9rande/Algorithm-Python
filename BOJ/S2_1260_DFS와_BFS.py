from collections import deque

def dfs(visited):
    answer = []
    stack = deque()

    stack.append(V)

    while stack:
        popped = stack.pop()
        if visited[popped] == 0:
            answer.append(str(popped))
            visited[popped] = 1

        for item in sorted(adjList[popped], reverse=True):
            if visited[item] == 0:
                stack.append(item)

    return ' '.join(answer)

def bfs(visited):
    answer = []
    queue = deque()

    queue.append(V)
    while queue:
        popped = queue.popleft()
        if visited[popped] == 0:
            answer.append(str(popped))
            visited[popped] = 1

        for item in sorted(adjList[popped]):
            if visited[item] == 0:
                queue.append(item)

    return ' '.join(answer)


N, M, V = map(int, input().split())
adjMatrix = [[0] * (N + 1) for _ in range(N + 1)]
adjList = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    start, end = map(int, input().split())
    adjMatrix[start][end] = 1
    adjMatrix[end][start] = 1

    adjList[start].append(end)
    adjList[end].append(start)

# print("인접행렬")
# for row in adjMatrix:
#     print(row)
#
# print("인접리스트")
# print(adjList)

print(dfs(visited))
visited = [0] * (N + 1)
print(bfs(visited))