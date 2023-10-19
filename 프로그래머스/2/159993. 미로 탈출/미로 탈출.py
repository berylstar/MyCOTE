from collections import deque
def bfs(start, end, maps):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    N, M = len(maps), len(maps[0])
    
    visited = [[False for _ in range(M)] for _ in range(N)]
    q = deque()
    flag = False
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] == start:      
                q.append((i, j, 0))    
                visited[i][j] = True
                flag = True
                break 
        if flag:
            break
                
    while q:
        x, y, c = q.popleft()
        
        if maps[x][y] == end:
            return c
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if maps[nx][ny] == 'X':
                continue
                
            if not visited[nx][ny]:
                q.append((nx, ny, c+1))
                visited[nx][ny] = True
                    
    return -1
            
def solution(maps):
    path1 = bfs('S', 'L', maps)
    path2 = bfs('L', 'E', maps)

    return path1 + path2 if path1 != -1 and path2 != -1 else -1