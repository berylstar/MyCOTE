import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

d = {0:[0, 1], 1:[0, -1], 2:[1, 0], 3:[-1, 0]}
q = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))
            
while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        
        if box[nx][ny] != 0:
            continue
            
        box[nx][ny] = box[x][y] + 1
        q.append((nx, ny))

answer = 0

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(box[i]))

print(answer - 1)