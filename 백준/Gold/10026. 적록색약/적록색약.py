from sys import stdin
input = stdin.readline

from collections import deque

d = {0:[1,0], 1:[-1,0], 2:[0,1], 3:[0,-1]}

N = int(input())
picture = [input().rstrip() for _ in range(N)]

q = deque()

def BFS(i ,j):
    q.append((i, j))

    visited[i][j] = True
    mark = picture[i][j]

    while q:
        x, y = q.popleft()
        
        for k in range(4):
            nx = x + d[k][0]
            ny = y + d[k][1]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
                
            if not visited[nx][ny] and picture[nx][ny] == mark:
                visited[nx][ny] = True
                q.append((nx, ny))

# 1. ALL
visited = [[False for _ in range(N)] for _ in range(N)]
answer_all = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:        
            BFS(i, j)
            answer_all += 1

# 2. R=G
visited = [[False for _ in range(N)] for _ in range(N)]
answer_rg = 0

for i in range(N):
    picture[i] = picture[i].replace('R', 'G')

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j)
            answer_rg += 1

print(answer_all, answer_rg)