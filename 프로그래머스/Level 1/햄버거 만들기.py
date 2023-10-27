def solution(ingredient):
    answer = 0
    temp = []
    for i in ingredient:
        temp.append(i)
        if temp[-4:] == [1, 2, 3, 1]:
            answer += 1
            del temp[-4:]
    return answer
#배열 하나 만들어서 비교하는 방법으로 접근
