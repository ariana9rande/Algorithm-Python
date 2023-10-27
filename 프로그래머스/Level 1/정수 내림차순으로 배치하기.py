def solution(n):
    answer = ''
    data = [i for i in str(int(n))]
    sorted_data = sorted(data, reverse=True)
    for i in sorted_data:
        answer += i
    return int(answer)

#3번째줄에 str(n) -> str(int(n))으로 바꾸니까 성공함 이유는 모르겠음
