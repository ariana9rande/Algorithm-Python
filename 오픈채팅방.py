macro = ["님이 들어왔습니다.", "님이 나갔습니다."]

def solution(record):
    userList = sorted(set([item.split()[1] for item in record]))
    userDict = dict()
    logs = []
    for r in record:
        temp = r.split()
        if len(temp) == 3:
            userDict[temp[1]] = temp[2]
        if temp[0] != 'Change':
            logs.append(temp[:2])

    for i in range(len(logs)):
        if logs[i][0] == 'Enter':
            logs[i] = userDict[logs[i][1]] + macro[0]
        else:
            logs[i] = userDict[logs[i][1]] + macro[1]
    return logs


# uid로 구분
# uid 별로 마지막 change를 담은 str의 [2]값으로 모든 이름을 변경
# change가 없을 경우 해당 uid의 아무 str의 [2]값
# enter와 exit만 출력

record = ["Enter uid1234 Muzi",
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]
print(solution(record))