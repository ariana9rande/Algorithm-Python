def solution(keymap, targets):
    dp = dict()
    answer = []
    # keymap 개수만큼 반복
    for map in keymap:
        # targets를 순회하면서
        for target in targets:
            # target의 글자마다
            for c in target:
                # 현재의 keymap에 있으면
                if c in map:
                    # dp에 없는 경우
                    if c not in dp:
                        # 현재 키맵에서 c를 입력할 때 필요한 클릭 회수 저장
                        dp[c] = map.index(c) + 1
                    # dp에 값이 있는 경우
                    else:
                        # 저장된 값과 비교해서 더 작은 값 저장
                        dp[c] = min(dp[c], map.index(c) + 1)

    # dp 갱신 완료 후
    # targets를 순회하면서
    for target in targets:
        # 클릭 회수 저장할 temp 변수
        temp = 0
        # -1 추가 여부 저장할 flag
        flag = True
        # target의 글자마자
        for c in target:
            # dp에 값이 없으면 flag -> false
            if c not in dp:
                flag = False
                break
            # dp에 저장된 회수를 더함
            else:
                temp += dp[c]
        # flag가 true면 temp값 추가 / false면 -1 추가
        if flag:
            answer.append(temp)
        else:
            answer.append(-1)

    return answer


keymap = ["ABCE"]
targets = ["ABDE"]
print(solution(keymap, targets))