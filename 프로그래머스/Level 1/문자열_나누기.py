def solution(s):
    answer = []
    while s:
        sameCnt = 0
        diffCnt = 0
        x = s[0]
        temp = 0
        for i in range(len(s)):
            if s[i] == x:
                sameCnt += 1
            else:
                diffCnt += 1

            if sameCnt == diffCnt:
                temp = i
                break

        if sameCnt == diffCnt:
            answer.append(s[:temp + 1])
            s = s[temp + 1:]
        else:
            answer.append(s)
            break

    return len(answer)


s = "aaabbaccccabbaaabcd"
print(solution(s))