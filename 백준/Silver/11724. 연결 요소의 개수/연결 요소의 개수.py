from sys import stdin
input = stdin.readline

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
q = deque()
visited = [False for _ in range(N+1)]
answer = 0
for i in range(1, N+1):
    if visited[i]:
        continue
        
    answer += 1
    q.append(i)
    
    while q:
        curr = q.popleft()
    
        for nex in graph[curr]:
            if not visited[nex]:
                q.append(nex)
                visited[nex] = True
print(answer)