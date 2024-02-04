from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0 for _ in range(N+2)]
for i in range(N+1):
    dp[i+1] = dp[i] + nums[i-1]

for _ in range(M):
    start, end = map(int, input().split())
    print(dp[end + 1] - dp[start])