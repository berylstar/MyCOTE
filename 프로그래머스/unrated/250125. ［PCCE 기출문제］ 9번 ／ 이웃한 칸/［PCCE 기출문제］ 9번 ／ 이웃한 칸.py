def solution(board, h, w):
    answer = 0
    
    N = len(board)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]    
    
    target = board[h][w]
    
    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]
        
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        
        answer += board[nx][ny] == target
            
    return answer