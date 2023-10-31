# goal에서 for문 돌리면 더 간결하게 해결 가능

def solution(cards1, cards2, goal):
    temp = []
    idx1 = 0
    idx2 = 0
    idx = 0

    # 둘 중 하나가 빌 때까지 각 리스트와 goal을 비교하면서 같을 경우
    # card에서 pop하고 temp에 append
    while len(cards1) > 0 and len(cards2) > 0:
        if cards1[idx1] == goal[idx]:
            temp.append(cards1.pop(idx1))
            idx += 1

        elif cards2[idx2] == goal[idx]:
            temp.append(cards2.pop(idx2))
            idx += 1

        # 두 리스트 모두 다를 경우 "No" return
        else:
            return "No"

        # while문 진행 중에 goal과 같아졌을 경우 "Yes" return
        if temp == goal:
            return "Yes"

    # while문 종료 후 temp와 goal이 같으면 "Yes" return
    if temp == goal:
        return "Yes"
    # 아닐 경우 남아 있는 리스트를 temp에 더한 뒤에 같으면 "Yes" return
    else:
        for item in cards1:
            temp.append(item)

        for item in cards2:
            temp.append(item)

        if temp == goal:
            return "Yes"

    return "No"


cards1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
cards2 = ["string", "or", "integer"]
goal = ["string", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(solution(cards1, cards2, goal))