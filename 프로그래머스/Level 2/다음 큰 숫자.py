def dectobin(n):
    tmp = ''
    while n > 0:
        tmp += str(n % 2)
        n //= 2
    return tmp[::-1]


def solution(n):
    answer = n

    while True:
        answer += 1

        if dectobin(answer).count('1') == dectobin(n).count('1'):
            break
    return answer
