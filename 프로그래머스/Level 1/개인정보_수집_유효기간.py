def solution(today, terms, privacies):
    answer = []
    dic = dict()
    for item in terms:
        dic[item.split()[0]] = item.split()[1]

    for i in range(len(privacies)):
        year = int(privacies[i].split()[0].split('.')[0])
        month = int(privacies[i].split()[0].split('.')[1])
        day = int(privacies[i].split()[0].split('.')[2]) - 1
        if day == 0:
            month -= 1
            day = 28
        term = int(dic[privacies[i].split()[1]])

        today_year = int(today.split('.')[0])
        today_month = int(today.split('.')[1])
        today_day = int(today.split('.')[2])

        month += term
        if month > 12:
            year += month // 12
            month = month % 12

        if month == 0:
            year -= 1
            month = 12

        if year < today_year:
            answer.append(i + 1)
        elif year == today_year:
            if month < today_month:
                answer.append(i + 1)
            elif month == today_month:
                if day < today_day:
                    answer.append(i + 1)

    return answer


today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms, privacies))