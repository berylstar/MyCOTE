import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [set() for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].add(B)
    graph[B].add(A)
for i in range(1, N+1):
    graph[i] = sorted(graph[i])
    
def CalcDistance(start):
    q = deque()
    q.append((start, 0))
    
    cost = [N+1 for _ in range(N+1)]
    cost[0] = 0
    
    while q:
        currNode, currCost = q.popleft()
        
        if currCost < cost[currNode]:
            cost[currNode] = currCost
        else:
            continue
        
        for nextNode in graph[currNode]:
            q.append((nextNode, currCost + 1))

    return sum(cost)

minCost = N*N
answer = 0

for i in range(1, N+1):
    curr = CalcDistance(i)

    if curr < minCost:
        answer = i
        minCost = curr

print(answer)