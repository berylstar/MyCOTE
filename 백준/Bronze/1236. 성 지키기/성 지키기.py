from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
castle = [input().rstrip() for _ in range(N)]

answer = [0, 0]

for i in range(N):
    if 'X' not in castle[i]:
        answer[0] += 1

for j in range(M):
    for i in range(N):
        if castle[i][j] == 'X':
            break
    else:
        answer[1] += 1

print(max(answer))