def solution(n):
    fact = 1
    i = 0
    while fact <= n:
        i += 1
        fact *= i
    return i - 1
