def solution(s):
    for i in s:
        if ord(i) < 48 or ord(i) > 57:
            return False
        if len(s) != 4 and len(s) != 6:
            return False
    return True
