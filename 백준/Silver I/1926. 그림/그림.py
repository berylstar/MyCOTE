from sys import stdin
input = stdin.readline

from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

d = {0:[1,0], 1:[-1,0], 2:[0,1], 3:[0,-1]}
number = 0
maxx = 0
q = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] != 1:
            continue
            
        curr = 1
        q.append((i, j))
        graph[i][j] = 2
        
        while q:
            x, y = q.popleft()
            
            for k in range(4):
                nx = x + d[k][0]
                ny = y + d[k][1]
                
                if nx<0 or nx>=N or ny<0 or ny>=M:
                    continue
                
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 2
                    q.append((nx, ny))
                    curr += 1
                    
        maxx = max(curr, maxx)
        number += 1
        
print(number)
print(maxx)