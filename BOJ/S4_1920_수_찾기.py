def solution(arr, target):
    left = 0
    right = len(arr) - 1
    mid = len(arr) // 2

    while left <= right:
        if target == arr[mid]:
            return 1
        elif target < arr[mid]:
            right = mid - 1
        elif target >= arr[mid]:
            left = mid + 1
        mid = (left + right) // 2
    return 0


N = int(input())
list1 = sorted(list(map(int, input().split())))
M = int(input())
list2 = list(map(int, input().split()))

for item in list2:
    print(solution(list1, item))