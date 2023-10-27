def solution(common):
    if common[1] ** 2 == common[0] * common[2] and common[0]:
        answer = common[-1] * (common[1] / common[0])
    else:
        answer = common[-1] + (common[1] - common[0])
    return answer
  
  # 그냥 생각나는대로 했더니 division by 0 오류나서 common[0]이 0이 아니라는 조건을 추가해야 되는데 그럼 for문 쓰기가 어려워져서
  # 등비중항으로 조건문 수정
