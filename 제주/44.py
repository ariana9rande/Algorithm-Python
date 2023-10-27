input_data = int(input())
answer = 0

while input_data > 0:
    answer += input_data % 10
    input_data //= 10

print(answer)
