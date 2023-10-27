ans = [0 for _ in range(100001)]
ans[0] = 0
ans[1] = 1

def solution(n):
    for i in range(2, n + 1):
        ans[i] = (ans[i - 2] + ans[i - 1]) % 1234567
    return ans[n]
