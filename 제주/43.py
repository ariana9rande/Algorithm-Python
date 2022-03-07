input_data = int(input())

answer = ''

while input_data > 0:
    answer += str(input_data % 2)
    input_data //= 2

for i in answer[::-1]:
    print(i, end='')
