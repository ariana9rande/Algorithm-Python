def solution(k, score):
    answer = []
    hallOfFame = []
    cnt = 0
    for i in score:
        if cnt < k:
            hallOfFame.append(i)
            cnt += 1
        else:
            if i > min(hallOfFame):
                hallOfFame[hallOfFame.index(min(hallOfFame))] = i
        answer.append(min(hallOfFame))
    return answer
