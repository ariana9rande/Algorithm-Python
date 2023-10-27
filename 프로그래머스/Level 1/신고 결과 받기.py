def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = []
    banned = []
    mail = []
    for i in set(report):
        reported.append(i.split()[1])

    for i in set(reported):
        if reported.count(i) >= k:
            banned.append(i)

    for i in set(report):
        if i.split()[1] in banned:
            mail.append(i.split()[0])

    answer = [mail.count(i) for i in id_list]

    return answer
