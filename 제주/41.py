input_data = int(input())

count = 0

for i in range(1, input_data + 1):
    if input_data % i == 0:
        count += 1
        if count > 2:
            print('NO')
            break

if input_data == 1:
    print('NO')
elif i == input_data and count == 2:
    print('YES')
