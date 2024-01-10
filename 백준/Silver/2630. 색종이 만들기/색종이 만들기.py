import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0]

def DFS(startX, startY, length):
    global answer

    count = [0, 0]

    for i in range(startX, startX + length):
        for j in range(startY, startY + length):
            count[paper[i][j]] += 1

    if count[0] == 0:
        answer[1] += 1
    elif count[1] == 0:
        answer[0] += 1
    else:
        DFS(startX, startY, length//2)
        DFS(startX + length//2, startY, length//2)
        DFS(startX, startY + length//2, length//2)
        DFS(startX + length//2, startY + length//2, length//2)

DFS(0, 0, N)

print(answer[0])
print(answer[1])