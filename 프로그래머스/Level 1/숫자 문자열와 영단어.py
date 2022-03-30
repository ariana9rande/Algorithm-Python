def solution(s):
    x = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, j in enumerate(x):
        s = str(i).join(s.split(j))
    return int(s)
