#220404
/*def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        n = -1
        for j in range(len(arr2[0])):
            k = 0
            while k < len(arr1[0]):
                if k == 0:
                    answer[i].append(arr1[i][k] * arr2[k][j])
                    n += 1
                else:
                    answer[i][n] += arr1[i][k] * arr2[k][j]
                k += 1
    return answer*/

#220405
def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            tmp = 0
            for k in range(len(arr1[0])):
                tmp += arr1[i][k] * arr2[k][j]
            answer[i].append(tmp)
    return answer
