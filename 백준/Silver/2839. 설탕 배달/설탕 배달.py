N = int(input())
dp = [-1 for _ in range(5001)]
dp[3] = 1
dp[5] = 1

for i in range(6, N+1):
    a = dp[i-5] if dp[i-5] != -1 else dp[i]
    b = dp[i-3] if dp[i-3] != -1 else dp[i]

    if a > 0 and b > 0:
        dp[i] = min(a + 1, b + 1)
    elif a > 0 and b < 0:
        dp[i] = a + 1
    elif a < 0 and b > 0:
        dp[i] = b + 1
    
print(dp[N])