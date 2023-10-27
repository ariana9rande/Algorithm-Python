def solution(arr):
    sum_arr = 0
    count = 0
    for i in arr:
        sum_arr += i
        count += 1

    return sum_arr / count
