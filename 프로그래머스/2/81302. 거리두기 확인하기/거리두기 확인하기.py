from collections import deque

def Check(place):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    isCorrect = True

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                q = deque([(i, j, 0)])
                s = set()
                s.add((i, j))

                while q:
                    x, y, c = q.popleft()
                    
                    if c > 1:
                        continue
                    
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        
                        if nx < 0 or nx > 4 or ny < 0 or ny > 4:
                            continue

                        if (nx, ny) in s:
                            continue
                        
                        if place[nx][ny] == 'X':
                            continue
                            
                        if place[nx][ny] == 'P':
                            isCorrect = False
                            break
                            
                        q.append((nx, ny, c+1))
                        s.add((nx, ny))

                
                if not isCorrect:
                    return 0
    
    return 1
                

def solution(places):    
    return [Check([list(p) for p in place]) for place in places]