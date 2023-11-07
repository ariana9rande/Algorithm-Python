
def solution(survey, choices):
    answer = []
    arr = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    score = dict()
    for i in range(len(survey)):
        if choices[i] < 4:
            if survey[i][0] in score:
                score[survey[i][0]] -= choices[i] - 4
            else:
                score[survey[i][0]] = abs(choices[i] - 4)
        elif choices[i] > 4:
            if survey[i][1] in score:
                score[survey[i][1]] += choices[i] - 4
            else:
                score[survey[i][1]] = choices[i] - 4

    for item in arr:
        if item not in score:
            score[item] = 0

    for i in range(0, len(arr), 2):
        left, right = arr[i], arr[i + 1]
        answer.append(left if score[left] > score[right]
                      else right if score[left] < score[right]
                      else left if ord(left) < ord(right) else right)

    return ''.join(answer)


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))
