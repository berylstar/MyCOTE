from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

answer = 0
for coin in reversed(A):
    answer += K // coin
    K %= coin
print(answer)