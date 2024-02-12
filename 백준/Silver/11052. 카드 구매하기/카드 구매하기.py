from sys import stdin
input = stdin.readline

N = int(input())
cards = [0] + list(map(int, input().split()))
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], cards[j] + dp[i-j])
print(dp[N])