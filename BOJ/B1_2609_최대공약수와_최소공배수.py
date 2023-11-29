def getGCD(a, b):
    answer = -1
    if a == b:
        return a
    else:
        for i in range(1, a + 1):
            if a % i == 0 and b % i == 0:
                answer = i
    return answer

def getLCM(a, b):
    if a == b:
        return a
    else:
        i = 1
        while True:
            if i % a == 0 and i % b == 0:
                answer = i
                break
            i += 1
    return answer

def solution(a, b):
    print(getGCD(a, b))
    print(getLCM(a, b))


A, B = map(int, input().split())
if A < B:
    solution(A, B)
else:
    solution(B, A)