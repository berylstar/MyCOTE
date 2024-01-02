import sys
input = sys.stdin.readline

N = int(input())
dp = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]

for i in range(1, N):
    dp[i][1] += min(dp[i-1][2], dp[i-1][3])
    dp[i][2] += min(dp[i-1][1], dp[i-1][3])
    dp[i][3] += min(dp[i-1][1], dp[i-1][2])

print(min(dp[-1][1:4]))