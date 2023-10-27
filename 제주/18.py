input_data = map(int, input().split())

data_sum = 0
count = 0

for i in input_data:
    data_sum += i
    count += 1

print(data_sum // count)
