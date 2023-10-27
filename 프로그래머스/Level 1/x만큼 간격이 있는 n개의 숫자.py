def solution(x, n):
    answer = []
    if x != 0:
        for i in range(x, n * x + x, x):
            answer.append(i)
    else:
        for i in range(x, n):
            answer.append(x)
    return answer
