def solution(answers):
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 1, 2, 3, 2, 4, 2, 5]
    list3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count1 = 0
    count2 = 0
    count3 = 0
    count = []
    for i in range(len(answers)):
        if answers[i] == list1[i % 5]:
            count1 += 1
        if answers[i] == list2[i % 8]:
            count2 += 1
        if answers[i] == list3[i % 10]:
            count3 += 1
    count.append(count1)
    count.append(count2)
    count.append(count3)
    answer = [i + 1 for i in range(len(count)) if count[i] == max(count)]
    answer.sort()
    return answer
