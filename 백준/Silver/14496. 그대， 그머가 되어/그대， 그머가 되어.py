from sys import stdin
input = stdin.readline

from collections import deque

a, b = map(int, input().split())
N, M = map(int, input().split())

graph = [set() for _ in range(N+1)]
for _ in range(M):
    l, r = map(int, input().split())
    graph[l].add(r)
    graph[r].add(l)
    
if a == b:
    print(0)
    exit(0)
    
answer = set()
for start in graph[a]:
    q = deque()
    visited = [False for _ in range(N+1)]
    visited[start] = True
    q.append((start, 1))
    
    while q:
        now, count = q.popleft()
        
        if now == b:
            answer.add(count)
            break
        
        for nex in graph[now]:
            if not visited[nex]:
                q.append((nex, count + 1))
                visited[nex] = True
if answer:
    print(min(answer))
else:
    print(-1)