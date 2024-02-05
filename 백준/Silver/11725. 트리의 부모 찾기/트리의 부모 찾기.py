from sys import stdin
input = stdin.readline

from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = [0 for _ in range(N+1)]
q = deque()
q.append(1)
while q:
    curr = q.popleft()
    
    for nex in graph[curr]:
        if answer[nex] == 0:
            answer[nex] = curr
            q.append(nex)

for i in range(2, N+1):
    print(answer[i])