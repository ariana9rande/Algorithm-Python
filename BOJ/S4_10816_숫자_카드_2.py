N = int(input())
arrN = sorted(list(map(int, input().split())))
dictN = dict()
for item in arrN:
    if item not in dictN:
        dictN[item] = 1
    else:
        dictN[item] += 1
M = int(input())
arrM = list(map(int, input().split()))

for item in arrM:
    start = 0
    end = len(arrN) - 1

    while start <= end:
        mid = (start + end) // 2

        if item == arrN[mid]:
            break
        if item < arrN[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if item == arrN[mid]:
        print(dictN[item], end=' ')
    else:
        print(0, end=' ')