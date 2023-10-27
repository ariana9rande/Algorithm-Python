def solution(n):
    answer = 0
    count = 0
    temp = ''
    while n > 0:
        temp += str(n % 3)
        n //= 3
    for i in temp[::-1]:
        answer += int(i) * (3 ** count)
        count += 1
    return answer
