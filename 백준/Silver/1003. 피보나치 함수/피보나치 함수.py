import sys
input = sys.stdin.readline

dp = [[0, 0] for _ in range(41)]
dp[0][0] = 1
dp[1][1] = 1

for i in range(2, 41):
    dp[i] = list(map(lambda x,y:x+y, dp[i-1], dp[i-2]))

T = int(input())
for _ in range(T):
    N = int(input())
    print(*dp[N])