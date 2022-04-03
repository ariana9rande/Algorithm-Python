def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return int(a * b / gcd(a, b))


def solution(arr):
    answer = 1
    for i in arr:
        answer = lcm(answer, i)
    return answer
