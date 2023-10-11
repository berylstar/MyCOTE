from collections import deque
def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    for rd in road:
        graph[rd[0]].append([rd[1], rd[2]])
        graph[rd[1]].append([rd[0], rd[2]])
        
    cost = [500001 for _ in range(N+1)]
    q = deque([[1,0]])
    
    while q:
        nowNode, nowCost = q.popleft()
        
        if cost[nowNode] < nowCost:
            continue
        
        cost[nowNode] = nowCost
        
        for nextNode, nextCost in graph[nowNode]:
            q.append([nextNode, nowCost + nextCost])
    
    return sum(1 for c in cost if c <= K)