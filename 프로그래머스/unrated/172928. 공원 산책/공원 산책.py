def solution(park, routes):
    N, M = len(park), len(park[0])
    for i in range(N):
        if 'S' in park[i]:
            x = i
            y = park[i].index('S')
            
    direction = { 'E' : [0, 1], 'W' : [0, -1], 'S' : [1, 0], 'N' : [-1, 0] }
    
    for route in routes:
        dx, dy = direction[route[0]]
        nx, ny = x, y
        
        for _ in range(int(route[2:])):
            nx += dx
            ny += dy
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
                
            if park[nx][ny] == 'X':
                break
        else:
            x, y = nx, ny
            
    return [x, y]