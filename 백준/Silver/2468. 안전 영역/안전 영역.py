from sys import stdin
input = stdin.readline

from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

d = {0:[1,0], 1:[-1,0], 2:[0,1], 3:[0,-1]}
answer = set()
answer.add(1)

for height in range(1, 100):
    curr = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = deque()
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] - height > 0 and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = True
                
                while q:
                    x, y = q.popleft()
                    
                    for k in range(4):
                        nx = x + d[k][0]
                        ny = y + d[k][1]
                        
                        if nx<0 or nx>=N or ny<0 or ny>=N:
                            continue
                        
                        if graph[nx][ny] - height > 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))

                curr += 1
    
    if curr > 0:
        answer.add(curr)
    else:
        break
print(max(answer))