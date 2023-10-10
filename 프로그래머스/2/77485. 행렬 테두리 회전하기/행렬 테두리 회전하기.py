from collections import deque
def solution(rows, columns, queries):
    board = [[columns*i+j+1 for j in range(columns)] for i in range(rows)]
    answer = []
    
    for query in queries:
        x1, y1, x2, y2 = map(lambda x:x-1, query)
        
        q = deque()
        for i in range(y1, y2+1):
            q.append(board[x1][i])
        for i in range(x1+1, x2+1):
            q.append(board[i][y2])
        for i in reversed(range(y1, y2)):
            q.append(board[x2][i])
        for i in reversed(range(x1+1, x2)):
            q.append(board[i][y1])
            
        answer.append(min(q))

        q.appendleft(q.pop())
        
        for i in range(y1, y2+1):
            board[x1][i] = q.popleft()
        for i in range(x1+1, x2+1):
            board[i][y2] = q.popleft()
        for i in reversed(range(y1, y2)):
            board[x2][i] = q.popleft()
        for i in reversed(range(x1+1, x2)):
            board[i][y1] = q.popleft()
        
    return answer