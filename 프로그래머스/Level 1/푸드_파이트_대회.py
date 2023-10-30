def solution(food):
    left = []

    for i in range(len(food)):
        left.append(str(i) * (food[i] // 2))

    answer = ''.join(left) + '0' + ''.join(sorted(left, reverse=True))
    return answer


food = [1, 3, 2, 3]
print(solution(food))