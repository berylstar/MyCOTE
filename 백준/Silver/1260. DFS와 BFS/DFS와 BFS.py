import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
    
for i in range(1, N+1):
    graph[i] = sorted(graph[i])

dfs_visited = [False for _ in range(N+1)]
def DFS(start):
    global dfs_visited
    print(start, end=' ')
    dfs_visited[start] = True

    for i in graph[start]:
        if not dfs_visited[i]:
            DFS(i)

from collections import deque
def BFS(start):
    visited = [False for _ in range(N+1)]
    visited[start] = True
    q = deque()
    q.append(start)
    
    while q:
        curr = q.popleft()
        print(curr, end=' ')
        
        for i in graph[curr]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

    print()

DFS(V)
print()
BFS(V)