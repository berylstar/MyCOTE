from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    N = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    
    if N > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    
    for j in range(2, N):
        preMax = max(dp[0][j-2], dp[1][j-2])
        dp[0][j] += max(dp[1][j-1], preMax)
        dp[1][j] += max(dp[0][j-1], preMax)

    print(max(dp[0][-1], dp[1][-1]))