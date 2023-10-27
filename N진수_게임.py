toHex = ['A', 'B', 'C', 'D', 'E', 'F']

def trans(num, n):
    result = []
    if num == 0:
        return '0'
    while num > 0:
        temp = num % n
        # print(f'{temp} = {num} % {n}')
        if temp >= 10:
            temp = toHex[temp - 10]
        result.append(str(temp))
        num //= n
    result.reverse()
    return ''.join(result)


# n진수 t개 문자열 return
# m명 중 p번째 순서
arr = []
answer = []
def solution(n, t, m, p):
    for i in range(t * m):
        arr.append(trans(i, n))
    string = ''.join(arr)

    for i in range(p - 1, m * t, m):
        answer.append(string[i])

    return ''.join(answer)


n = 16
t = 16
m = 2
p = 1

solution(n, t, m, p)

print(''.join(answer))

