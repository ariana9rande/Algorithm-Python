import itertools


def solution(nums):
    answer = 0
    combi = list(itertools.combinations(nums, 3))
    combi_sum = []
    for i in combi:
        combi_sum.append(i[0] + i[1] + i[2])

    count = 0
    for i in combi_sum:
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            answer += 1
        count = 0

    return answer
