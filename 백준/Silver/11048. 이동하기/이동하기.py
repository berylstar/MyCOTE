from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    miro[i][0] += miro[i-1][0]

for j in range(1, M):
    miro[0][j] += miro[0][j-1]

for i in range(1, N):
    for j in range(1, M):
        miro[i][j] += max(miro[i-1][j], miro[i][j-1], miro[i-1][j-1])

print(miro[-1][-1])