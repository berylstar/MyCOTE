from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
square = [list(map(int, input().rstrip())) for _ in range(N)]
answer = 0

for d in range(1, min(N, M)):
    for i in range(N - d):
        for j in range(M - d):
            if square[i][j] == square[i][j+d] == square[i+d][j] == square[i+d][j+d]:
                answer = d
print((answer+1) * (answer+1))