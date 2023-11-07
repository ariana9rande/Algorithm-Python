def solution(s):
    p_count = 0
    y_count = 0

    for i in s:
        if i == 'p' or i == 'P':
            p_count += 1
        elif i == 'y' or i == 'Y':
            y_count += 1

    return p_count == y_count
