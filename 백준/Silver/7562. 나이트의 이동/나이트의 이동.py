from sys import stdin
input = stdin.readline

from collections import deque

d = {0:[1,2], 1:[-1,2], 2:[1,-2], 3:[-1,-2],
     4:[2,1], 5:[-2,1], 6:[2,-1], 7:[-2,-1]}

for _ in range(int(input())):
    L = int(input())
    startX, startY = map(int, input().split())
    targetX, targetY = map(int, input().split())
    
    dp = [[-1 for _ in range(L)] for _ in range(L)]
    dp[startX][startY] = 0
    
    q = deque()
    q.append((startX, startY))
    
    while q:
        x, y = q.popleft()
        
        if x == targetX and y == targetY:
            print(dp[targetX][targetY])
            break
        
        for k in range(8):
            nx = x + d[k][0]
            ny = y + d[k][1]
            
            if nx<0 or nx>=L or ny<0 or ny>=L:
                continue
                
            if dp[nx][ny] < 0:
                dp[nx][ny] = dp[x][y] + 1
                q.append((nx, ny))