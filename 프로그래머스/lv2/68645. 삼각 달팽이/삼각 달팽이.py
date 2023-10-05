def solution(n):
    answer = [[0 for _ in range(i)] for i in range(1, n+1)]
    x, y = -1, 0
    direction = [[1, 0], [0, 1], [-1, -1]]
    move = 0
    num = 1
    
    for i in range(n):
        d = direction[i%3]
        
        for _ in range(n-i):
            x += d[0]
            y += d[1]
            
            answer[x][y] = num
            num += 1
            
    return sum(answer, [])