import sys

queue = []
front = -1
back = -1

N = int(input())
for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        queue.append(int(cmd[1]))
        if front == -1:
            front = 0
        back += 1
    elif cmd[0] == 'front':
        if front == -1:
            print(-1)
        else:
            print(queue[front])
    elif cmd[0] == 'back':
        if back == -1:
            print(-1)
        else:
            print(queue[back])
    elif cmd[0] == 'size':
        if front == -1 and back == -1:
            print(0)
        else:
            print(back - front + 1)
    elif cmd[0] == 'empty':
        if front == -1 and back == -1:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'pop':
        if front == -1 or len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(front))
            if len(queue) == 0:
                front = -1
                back = -1
            if back > 0:
                back -= 1
