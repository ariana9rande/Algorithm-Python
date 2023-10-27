def solution(box, n):
    answer = 1
    for i in box: // 가로 세로 높이를 각각 n으로 나눈 정수값을 answer에 곱함
        answer *= i // n
    return answer
