import sys
deque = []
front = -1
back = -1
N = int(input())
for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push_front':
        if len(deque) == 0:
            front = 0
        deque.insert(0, cmd[1])
        back += 1
    elif cmd[0] == 'push_back':
        if len(deque) == 0:
            front = 0
        deque.append(cmd[1])
        back += 1
    elif cmd[0] == 'pop_front':
        if front == -1:
            print(-1)
        else:
            print(deque.pop(0))
            back -= 1
            if len(deque) == 0:
                front = -1
                back = -1
    elif cmd[0] == 'pop_back':
        if back == -1:
            print(-1)
        else:
            print(deque.pop())
            back -= 1
            if len(deque) == 0:
                front = -1
                back = -1
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
    elif cmd[0] == 'front':
        if front == -1:
            print(-1)
        else:
            print(deque[front])
    elif cmd[0] == 'back':
        if back == -1:
            print(-1)
        else:
            print(deque[back])