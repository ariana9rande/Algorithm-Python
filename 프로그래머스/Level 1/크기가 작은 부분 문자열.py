def solution(t, p):
    answer = 0
    wordList = [] // 슬라이싱한 단어 담을 리스트
    for i in range(len(t) - len(p) + 1): // 인덱스 범위 넘어가지 않도록 p 길이에 따라 범위 설정 ex) 3글자면 마지막 인덱스 2칸 전까지
        wordList.append(t[i : i + len(p)]) // p길이만큼 슬라이싱해서 wordList에 저장
    for i in wordList: // wordList를 돌면서 p보다 작은 값이 있으면 answer 증가
        if i <= p:
            answer += 1
    return answer
