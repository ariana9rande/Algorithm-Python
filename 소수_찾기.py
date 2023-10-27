def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def perm(depth, numbers, sel, check, answer):
    temp = ''.join(sel)
    while len(temp) != 0 and temp[0] == '0':
        temp = temp[1:]

    if len(temp) != 0 and temp not in answer:
        if isPrime(int(temp)):
            answer.append(temp)

    for i in range(len(numbers)):
        if check[i] == 0:
            check[i] = 1
            sel.append(numbers[i])
            # print("before", end=' ')
            # print("check:", check, end=' ')
            # print("sel:", sel)
            perm(depth + 1, numbers, sel, check, answer)
            check[i] = 0
            sel.pop()
            # print("after", end=' ')
            # print("check:", check, end=' ')
            # print("sel:", sel)


def solution(numbers):
    answer = []
    sel = []
    check = [0] * len(numbers)
    perm(0, numbers, sel, check, answer)
    print(answer)
    return len(answer)


numbers = "010101"
print(solution(numbers))