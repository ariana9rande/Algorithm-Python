def solution(x):
    temp = x
    sum_x = 0
    while temp > 0:
        sum_x += temp % 10
        temp //= 10
    answer = x % sum_x == 0
    return answer
