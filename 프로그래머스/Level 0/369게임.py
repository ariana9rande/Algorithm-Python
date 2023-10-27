def solution(order):
    target = [3, 6, 9]
    answer = 0
    for i in str(order):
        if int(i) in target:
            answer += 1
    return answer
