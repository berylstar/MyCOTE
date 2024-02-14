N = int(input())

dp = [0 for _ in range(10)]
dp[0] = 1

for _ in range(N):
    for i in range(1, 10):
        dp[i] += dp[i-1]

print(sum(dp) % 10007)