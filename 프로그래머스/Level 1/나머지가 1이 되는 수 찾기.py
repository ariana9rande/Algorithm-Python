def solution(n):
    i = n
    while i > 1:
        i -= 1
        if n % i == 1:
            answer = i
    return answer
