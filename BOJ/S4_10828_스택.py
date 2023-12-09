import sys

stack = []
top = -1

N = int(input())
for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
        top += 1
    elif cmd[0] == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
    elif cmd[0] == 'size':
        print(top + 1)
    elif cmd[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            top -= 1
            print(stack.pop())
