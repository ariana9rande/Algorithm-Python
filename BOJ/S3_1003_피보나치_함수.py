# dp / 결과 저장할 리스트 생성
dp = [[0, 0]] * 41

def solution(n):
    return dp[n]

# n이 0 or 1인 경우의 결과 return
def fib(n):
    if n == 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]

# 입력값 범위인 40까지 dp 리스트 값 저장
for i in range(41):
    if i == 0 or i == 1:
        dp[i] = fib(i)
    elif dp[i] == [0, 0]:
        dp[i] = [dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1]]

T = int(input())
for _ in range(T):
    N = int(input())
    print(*solution(N))