import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())

box = []
for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int, input().split())))
    box.append(temp)

d = {0:[0,0,1], 1:[0,0,-1], 2:[0,1,0], 3:[0,-1,0], 4:[1,0,0], 5:[-1,0,0]}

q = deque()

for h in range(H):
    for x in range(N):
        for y in range(M):
            if box[h][x][y] == 1:
                q.append((x, y, h))

while q:
    x, y, h = q.popleft()

    for k in range(6):
        nx = x + d[k][0]
        ny = y + d[k][1]
        nh = h + d[k][2]

        if nx < 0 or nx >= N or ny < 0 or ny >= M or nh < 0 or nh >= H:
            continue

        if box[nh][nx][ny] != 0:
            continue

        box[nh][nx][ny] = box[h][x][y] + 1
        q.append((nx, ny, nh))

answer = 0

for h in range(H):
    for x in range(N):
        for y in range(M):
            if box[h][x][y] == 0:
                print(-1)
                exit(0)

        answer = max(answer, max(box[h][x]))

print(answer - 1)