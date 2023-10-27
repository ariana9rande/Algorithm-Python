def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    count = 0
    zero_count = 0
    for i in lottos:
        if i == 0:
            zero_count += 1
            continue
        for j in win_nums:
            if i == j:
                count += 1
                continue
        
    answer = []
    answer.append(rank[count + zero_count])
    answer.append(rank[count])
    return answer
