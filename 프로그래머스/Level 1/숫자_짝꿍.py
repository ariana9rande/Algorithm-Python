# X Y에 공통으로 들어있는 정수들로 만들 수 있는 최대값
# 생각없이 하면 시간초과
# list.count 이용해서 x와 y에서 각 숫자가 들어있는 횟수 중 작은 값만큼 answer에 append
def solution(X, Y):
    answer = []
    X = list(X)
    Y = list(Y)
    cnt = []
    for i in range(10):
        cnt.append(min(X.count(str(i)), Y.count(str(i))))

    for i in range(len(cnt)):
        if cnt[i] != 0:
            answer.append(str(i) * cnt[i])

    if not answer:
        return "-1"
    if not ''.join(answer).replace("0", ""):
        return "0"

    return ''.join(sorted(answer, reverse=True))


X = "100"
Y = "123450"
print(solution(X, Y))