def solution(board, moves):
    answer = 0
    bucket = []
    for j in moves:
        i = 0
        while board[i][j - 1] == 0 and i < len(board) - 1:
            i += 1
        if board[i][j - 1] != 0:
            bucket.append(board[i][j - 1])
            board[i][j - 1] = 0
        for k in range(len(bucket) - 1):
            if bucket[k] == bucket[k + 1]:
                answer += 2
                del bucket[k]
                del bucket[k]
    return answer
