from sys import stdin
input = stdin.readline

N = int(input())
coin = list(reversed(list(map(int, input().split()))))

currMax = coin[0]
answer = 0
for i in range(1, N):
    if coin[i] > currMax:
        currMax = coin[i]
    else:
        answer += currMax - coin[i]
print(answer)