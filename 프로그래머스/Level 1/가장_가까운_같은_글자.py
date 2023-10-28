def solution(s):
    visited = dict()
    answer = []
    for idx in range(len(s)):
        if s[idx] not in visited:
            visited[s[idx]] = idx
            answer.append(-1)
        else:
            answer.append(idx - visited[s[idx]])
            visited[s[idx]] = idx
    return answer


s = "banana"
print(solution(s))