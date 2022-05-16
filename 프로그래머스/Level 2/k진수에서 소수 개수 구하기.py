def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = ''
    while n > 0:
        num += str(n % k)
        n //= k
    num = num[::-1]

    for x in num.split('0'):
        if x == '':
            continue
        if(isPrime(int(x))):
            answer += 1

    return answer
