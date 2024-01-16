from sys import stdin
input = stdin.readline

A, B = map(int, input().split())

dp = [0]
for i in range(1, 46):
    dp += [i for _ in range(i)]
    
print(sum(dp[A:B+1]))