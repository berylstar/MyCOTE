import sys
input = sys.stdin.readline
from collections import deque

d = {0:[0, 1], 1:[0, -1], 2:[1, 0], 3:[-1, 0]}

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()
    answer = 0
    for _ in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1
        
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                field[i][j] = 0
                q.append((i, j))
                
                while q:
                    x, y = q.popleft()
                    
                    for k in range(4):
                        nx = x + d[k][0]
                        ny = y + d[k][1]
                        
                        if nx < 0 or nx >= N or ny < 0 or ny >= M:
                            continue
                        
                        if field[nx][ny] == 1:
                            q.append((nx, ny))
                            field[nx][ny] = 0
                            
                answer += 1
                
    print(answer)
        