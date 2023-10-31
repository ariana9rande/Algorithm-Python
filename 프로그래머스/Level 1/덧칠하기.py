def solution(n, m, section):
    answer = 1
    start = section[0]

    for item in section:
        if item > start + m - 1:
            answer += 1
            start = item

    return answer


n = 5
m = 4
section = [1, 3]

print(solution(n, m, section))
