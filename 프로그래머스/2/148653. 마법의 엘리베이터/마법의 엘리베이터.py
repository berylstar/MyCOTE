import heapq
def solution(storey):
    q = []
    heapq.heappush(q, (storey, 0))
    
    answer = 100000001
    
    while q:
        ns, nc = heapq.heappop(q)
        
        if ns < 10:
            answer = min(answer, nc+ns, nc+(10-ns)+1)
            continue
            
        heapq.heappush(q, (ns//10, nc+ns % 10))
        heapq.heappush(q, (ns//10+1, nc+10-(ns % 10)))
        
    return answer