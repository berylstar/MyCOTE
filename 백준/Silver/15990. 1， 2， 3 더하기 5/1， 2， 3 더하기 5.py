from sys import stdin
input = stdin.readline

dp = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 1]]

for i in range(4, 100001):
    now = [
        (dp[i-1][1] + dp[i-1][2]) % 1000000009,
        (dp[i-2][0] + dp[i-2][2]) % 1000000009,
        (dp[i-3][0] + dp[i-3][1]) % 1000000009
    ]
    dp.append(now)

for _ in range(int(input())):
    print(sum(dp[int(input())]) % 1000000009)