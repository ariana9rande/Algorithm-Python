def solution(s):
    answer = ''
    tmp = ''
    for i in range(len(s)):
        if i == 0 or s[i - 1] == ' ':
            tmp += s[i]
            if 97 <= ord(s[i]) <= 122:
                tmp = tmp.upper()
            answer += tmp
            tmp = ''
        else:
            tmp += s[i]
            tmp = tmp.lower()
            answer += tmp
            tmp = ''
    return answer
