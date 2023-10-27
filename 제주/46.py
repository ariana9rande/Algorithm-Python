def solution(data):
    data_sum = 0
    data_list = [int(i) for i in data]
    for i in data_list:
        data_sum += i
    return data_sum


a, b = map(int, input().split())
string = ''
for i in range(a, b + 1):
    string += str(i)

print(solution(string))
