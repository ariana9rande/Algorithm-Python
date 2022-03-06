input_data = list(input().split())

max_value = 0
max_index = ''

for i in input_data:
	if input_data.count(i) > max_value:
		max_value = input_data.count(i)
		max_index = i

print(f"{max_index}(이)가 총 {max_value}표로 반장이 되었습니다.")
