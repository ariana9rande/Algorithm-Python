def solution(s, n):
    answer = ''
    for i in s:
        if 65 <= ord(i) <= 90 and 97 <= ord(i) + n <= 122:
            answer += chr(ord(i) + n - 26)
        elif 65 <= ord(i) + n <= 90 or 97 <= ord(i) + n <= 122:
            answer += chr(ord(i) + n)
        elif i == ' ':
            answer += i
        else:
            answer += chr(ord(i) + n - 26)
    return answer
