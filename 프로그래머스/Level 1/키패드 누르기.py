def distance(x1, y1, x2, y2):
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    if pow(x2 - x1, 2) + pow(y2 - y1, 2) == 2:
        return 2
    elif pow(x2 - x1, 2) + pow(y2 - y1, 2) == 5:
        return 3
    elif pow(x2 - x1, 2) + pow(y2 - y1, 2) == 8 or pow(x2 - x1, 2) + pow(y2 - y1, 2) == 10:
        return 4
    else:
        return x2 - x1 + y2 - y1


def solution(numbers, hand):
    answer = ''
    location = [[1, 0], [0, 3], [1, 3], [2, 3], [0, 2], [1, 2], [2, 2], [0, 1], [1, 1], [2, 1]]
    l_present = [0, 0]
    r_present = [2, 0]
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            l_present = [location[i][0], location[i][1]]
        elif i in [3, 6, 9]:
            answer += 'R'
            r_present = [location[i][0], location[i][1]]
        else:
            if distance(location[i][0], location[i][1], l_present[0], l_present[1]) < distance(location[i][0], location[i][1], r_present[0], r_present[1]):
                answer += 'L'
                l_present = [location[i][0], location[i][1]]
            elif distance(location[i][0], location[i][1], r_present[0], r_present[1]) < distance(location[i][0], location[i][1], l_present[0], l_present[1]):
                answer += 'R'
                r_present = [location[i][0], location[i][1]]
            elif distance(location[i][0], location[i][1], l_present[0], l_present[1]) == distance(location[i][0], location[i][1], r_present[0], r_present[1]):
                if hand == 'left':
                    answer += 'L'
                    l_present = [location[i][0], location[i][1]]
                else:
                    answer += 'R'
                    r_present = [location[i][0], location[i][1]]
    return answer
