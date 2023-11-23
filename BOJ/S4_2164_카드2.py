from collections import deque

def solution(n):
    queue = deque()
    # 1부터 n까지 queue에 삽입
    for i in range(1, n + 1):
        queue.append(i)

    # queue의 길이가 1이 될 때까지
    while len(queue) > 1:
        # 가장 위의 원소 삭제
        queue.popleft()
        # 가장 위의 원소를 가장 뒤로 이동
        queue.append(queue.popleft())

    # 마지막 남은 원소 return
    return queue.pop()


N = int(input())
print(solution(N))