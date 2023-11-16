def solution(a, b, c, d):
    arr = [a, b, c, d]
    arr = sorted(arr, key=lambda x: arr.count(x), reverse=True)
    for n in arr:
        if arr.count(n) == 4:
            return 1111 * n
        elif arr.count(n) == 3:
            temp = 0
            for tmp in arr:
                if arr.count(tmp) == 1:
                    temp = tmp
            return (10 * n + temp) ** 2
        elif arr.count(n) == 2:
            check = 2
            for tmp in arr:
                if arr.count(tmp) == 1:
                    check = 1
            if check == 1:
                temp = 1
                for tmp in arr:
                    if arr.count(tmp) == 1:
                        temp *= tmp
                return temp
            else:
                for tmp in arr:
                    if tmp != n:
                        return (n + tmp) * (n - tmp) if n > tmp else (n + tmp) * (tmp - n)
        else:
            return min(arr)


a = 1
b = 3
c = 2
d = 2
print(solution(a, b, c, d))