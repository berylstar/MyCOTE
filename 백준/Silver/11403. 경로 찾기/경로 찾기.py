from sys import stdin
input = stdin.readline

from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

q = deque()
for i in range(N):
    q.append(i)
    check = [0 for _ in range(N)]
    
    while q:
        now = q.popleft()
        
        for k in range(N):
            if check[k] == 0 and graph[now][k] == 1:
                q.append(k)
                check[k] = 1
                visited[i][k] = 1
                
for i in visited:
    print(*i)