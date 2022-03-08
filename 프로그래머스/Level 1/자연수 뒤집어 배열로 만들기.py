def solution(n):
    data = [int(i) for i in str(n)]
    answer = []

    for i in data[::-1]:
        answer.append(i)
    return answer

#str int list 안 헷갈리게 조심
