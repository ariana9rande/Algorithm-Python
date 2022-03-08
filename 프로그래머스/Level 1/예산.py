def solution(cost, budget):
    sorted_cost = sorted(cost)
    check = 0
    answer = 0
    for i in sorted_cost:
        check += i
        answer += 1
        if check > budget:
            return answer - 1
        elif check == budget:
            return answer
    return answer
