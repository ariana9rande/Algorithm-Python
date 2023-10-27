def solution(sides):
    if sides[0] < sides[1]:
        a, b = sides[0], sides[1]
    else:
        a, b = sides[1], sides[0]

    answer = 2 * a - 1
    return answer
