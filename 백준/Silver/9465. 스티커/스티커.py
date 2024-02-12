from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    N = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0 for _ in range(N)] for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    
    if N > 1:
        dp[0][1] = dp[1][0] + stickers[0][1]
        dp[1][1] = dp[0][0] + stickers[1][1]
    
    for j in range(2, N):
        dp[0][j] = max(dp[1][j-1], dp[1][j-2], dp[0][j-2]) + stickers[0][j]
        dp[1][j] = max(dp[0][j-1], dp[1][j-2], dp[0][j-2]) + stickers[1][j]

    print(max(dp[0][-1], dp[1][-1]))