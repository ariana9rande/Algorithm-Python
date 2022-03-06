data = int(input())

for i in range(data + 1):
    print(' ' * (data - i) + '*' * (i * 2 - 1))
