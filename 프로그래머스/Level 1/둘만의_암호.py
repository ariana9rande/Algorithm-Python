def solution(s, skip, index):
    answer = []
    # s 순회하면서
    for item in s:
        # 글자의 유니코드값 저장
        temp = ord(item)
        # index 값만큼 반복
        for i in range(1, index + 1):
            # 증가시켰을 때 알파벳 범위 넘어가지 않도록 하면서 1 증가
            if temp + 1 > 122:
                temp -= 26
            temp += 1
            # 현재 글자가 skip에 있을 경우 1 증가
            while chr(temp) in skip:
                if temp + 1 > 122:
                    temp -= 26
                temp += 1
        answer.append(chr(temp))
    return ''.join(answer)


s = "a"
skip = "bcdefghijk"
index = 1
print(solution(s, skip, index))