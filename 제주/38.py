input_data = input().split()

sorted_data = sorted(input_data, reverse=True)

count = 0

for i in range(len(sorted_data) - 1):

    if sorted_data[i] != sorted_data[i + 1]:
        count += 1

        if count == 3:
            break

print(i + 1) #리스트 인덱스 값이므로 +1
