def solution(prices):
    answer = []
    count = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            count += 1
            if prices[j] < prices[i]:
                break
        answer.append(count)
        count = 0
    return answer
