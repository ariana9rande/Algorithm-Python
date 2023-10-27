def solution(n, m):
    answer = []
    if n > m:
        n, m = m, n

    for i in range(n, 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    i = m
    while True:
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break
        i += 1

    return answer
