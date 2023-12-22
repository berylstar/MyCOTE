from collections import deque
def solution(land):
    N, M = len(land), len(land[0])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    oil = {0:0}
    index = 10
    
    for i in range(M):        
        for j in range(N):
            if land[j][i] != 1:
                continue
                
            q = deque()
            q.append((j, i))
            
            count = 0
            
            while q:
                x, y = q.popleft()
                
                if land[x][y] != 1:
                    continue
                
                count += 1
                land[x][y] = index
                
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    
                    if nx<0 or nx>=N or ny<0 or ny>=M:
                        continue
                        
                    q.append((nx, ny))
                    
            oil[index] = count
            index += 1
        
    return max(sum(oil[c] for c in set(land[j][i] for j in range(N))) for i in range(M))