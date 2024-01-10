import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

graph = [list(map(int, input().rstrip())) for _ in range(N)]

d = {0:[1, 0], 1:[-1, 0], 2:[0, 1], 3:[0, -1]}

houses = []
numbering = 2

for i in range(N):
    for j in range(N):
        if graph[i][j] != 1:
            continue
            
        q = deque()
        q.append((i, j))
        graph[i][j] = numbering
        count = 1
        
        while q:
            x, y = q.popleft()
            
            for k in range(4):
                nx = x + d[k][0]
                ny = y + d[k][1]
                
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                    
                if graph[nx][ny] != 1:
                    continue
                    
                graph[nx][ny] = numbering
                count += 1
                q.append((nx, ny))
                
        houses.append(count)
        
print(len(houses))
for house in sorted(houses):
    print(house)