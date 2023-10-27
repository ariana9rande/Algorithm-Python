def solution(dots):
    x = []
    y = []
    for i in dots:
        if i[0] not in x:
            x.append(i[0])
        if i[1] not in y:
            y.append(i[1])
    return abs((y[1] - y[0]) * (x[1] - x[0]))
