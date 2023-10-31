def func(n, limit, power):
    cnt = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt += 1
            if cnt > limit:
                return power

    if n ** 0.5 % 1 != 0:
        cnt *= 2
    else:
        cnt = cnt * 2 - 1

    return cnt if cnt <= limit else power


def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        answer += func(i, limit, power)
    return answer


number = 5
limit = 3
power = 2

print(solution(number, limit, power))