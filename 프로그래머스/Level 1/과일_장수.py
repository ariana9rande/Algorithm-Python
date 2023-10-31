# 내림차순으로 정렬한 뒤 하나씩 리스트에 넣고 m개가 되면
# 리스트의 가격을 answer에 더한 뒤 리스트 초기화 후 반복
def solution(k, m, score):
    answer = 0
    temp = []
    i = 0
    for item in sorted(score, reverse=True):
        temp.append(item)
        i += 1
        if i == m:
            answer += min(temp) * m
            i = 0
            temp = []
    return answer


k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]

print(solution(k, m, score))