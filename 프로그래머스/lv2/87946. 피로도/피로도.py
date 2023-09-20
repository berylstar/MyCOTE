## 1. Permutations
from itertools import permutations
def solution(k, dungeons):
    N = len(dungeons)
    answer = 0
    
    for case in permutations(range(N)):
        now = k
        temp = 0
        for i in case:
            if now < dungeons[i][0]:
                break
                
            now -= dungeons[i][1]
            temp += 1
                
        answer = max(answer, temp)
        
    return answer

## 2. DFS
def solution(k, dungeons):
    N = len(dungeons)
    answer = set()
    
    def DFS(k, count, visited):
        answer.add(count)
        
        for i in range(N):
            if k >= dungeons[i][0] and not visited[i]:
                DFS(k - dungeons[i][1], count + 1, [True if (visited[j] or i==j) else False for j in range(N)])
    
    DFS(k, 0, [False for _ in range(N)])
    
    return max(answer)

## 3. BFS
from collections import deque
def solution(k, dungeons):
    N = len(dungeons)
    answer = 0
    visited = [False for _ in range(N)]
    
    q = deque()
    q.append([k, 0, visited])
    
    while q:
        a, b, c = q.popleft()
        answer = max(answer, b)
        
        for i in range(N):
            if a >= dungeons[i][0] and not c[i]:
                new_visited = [True if c[j] or i==j else False for j in range(N)]
                q.append([a - dungeons[i][1], b + 1, new_visited])
                
    return answer