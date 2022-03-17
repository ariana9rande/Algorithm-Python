def solution(n, arr1, arr2):
    answer = []
    map1 = []
    string = ''
    map2 = []
    for i in arr1:
        temp = i
        while temp > 0:
            string += str(temp % 2)
            temp //= 2
        while len(string) < n:
            string += '0'
        map1.append(string[::-1])
        string = ''
    for i in arr2:
        temp = i
        while temp > 0:
            string += str(temp % 2)
            temp //= 2
        while len(string) < n:
            string += '0'
        map2.append(string[::-1])
        string = ''
    for i in range(len(map1)):
        for j in range(len(map1[i])):
            if map1[i][j] == '1' or map2[i][j] == '1':
                string += '#'
            else:
                string += ' '
        answer.append(string)
        string = ''
    return answer
