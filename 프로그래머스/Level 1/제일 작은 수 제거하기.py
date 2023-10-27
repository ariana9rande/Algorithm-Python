def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
    arr.remove(min(arr))
    for i in arr:
        answer.append(i)

    return answer
