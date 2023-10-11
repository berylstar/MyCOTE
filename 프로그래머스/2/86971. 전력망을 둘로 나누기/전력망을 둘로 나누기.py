from collections import deque
def solution(n, wires):
    answers = []
    
    for i in range(len(wires)):
        graph = [[] for _ in range(n+1)]        
        for j in range(len(wires)):
            if j == i:
                continue
            graph[wires[j][0]].append(wires[j][1])
            graph[wires[j][1]].append(wires[j][0])
            
        visited = [False for _ in range(n+1)]
        q = deque([1])
        
        while q:
            now = q.popleft()
            
            visited[now] = True
            
            for k in graph[now]:
                if not visited[k]:
                    q.append(k)
                    
        answers.append(abs(n-2*visited.count(True)))
    return min(answers)