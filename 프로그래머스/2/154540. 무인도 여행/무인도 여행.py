from collections import deque
def solution(maps):
    N, M = len(maps), len(maps[0])
    
    maps = [[maps[i][j] for j in range(M)] for i in range(N)]
    answer = []
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    for i in range(N):
        for j in range(M):
            if not maps[i][j].isdigit():
                continue
                
            island = set()
            island.add((i, j))
            q = deque([[i, j]])
            
            while q:
                x, y = q.popleft()
                
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    
                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        continue
                    
                    if maps[nx][ny] != 'X' and (nx, ny) not in island:
                        q.append([nx, ny])
                        island.add((nx, ny))
                        
            now = 0
            for x,y in island:
                now += int(maps[x][y])
                maps[x][y] = 'X'
            answer.append(now)
            
    return sorted(answer) or [-1]