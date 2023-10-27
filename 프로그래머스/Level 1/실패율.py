def solution(N, stages):
    answer = []
    stay = []
    temp = len(stages)
    ratio = []
    stages.sort()
    for i in range(1, len(stages) + 1):
        stay.append(stages.count(i))
        for j in range(stages.count(i)):
            stages.remove(i)

    for i in range(len(stay)):
        ratio.append(stay[i])

    for i in range(len(stay)):
        ratio[i] /= temp
        temp -= stay[i]
        if temp == 0:
            break

    ratio = ratio[:N]
    for i in range(len(ratio)):
        answer.append(ratio.index(max(ratio)) + 1)
        ratio[ratio.index(max(ratio))] = -1

    return answer
