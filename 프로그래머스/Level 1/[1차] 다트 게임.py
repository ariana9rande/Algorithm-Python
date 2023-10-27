def solution(dartResult):
    answer = 0
    score = []
    count = 0
    for i in range(len(dartResult)):
        if dartResult[i] == 'S':
            if dartResult[i - 1] == '0' and dartResult[i - 2] == '1':
                score.append(int(dartResult[i - 2] + dartResult[i - 1]))
            else:
                score.append(int(dartResult[i - 1]))
            count += 1
        elif dartResult[i] == 'T':
            if dartResult[i - 1] == '0' and dartResult[i - 2] == '1':
                score.append(int(dartResult[i - 2] + dartResult[i - 1]) ** 3)
            else:
                score.append(int(dartResult[i - 1]) ** 3)
            count += 1
        elif dartResult[i] == 'D':
            if dartResult[i - 1] == '0' and dartResult[i - 2] == '1':
                score.append(int(dartResult[i - 2] + dartResult[i - 1]) ** 2)
            else:
                score.append(int(dartResult[i - 1]) ** 2)
            count += 1

        if dartResult[i] == '*':
            score[count - 1] *= 2
            if count > 1:
                score[count - 2] *= 2

        if dartResult[i] == '#':
            score[count - 1] *= -1

    for i in score:
        answer += i

    return answer
