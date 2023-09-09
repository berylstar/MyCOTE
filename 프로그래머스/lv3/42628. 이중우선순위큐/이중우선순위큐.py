import heapq
def solution(operations):
    q = []
    for op in operations:
        if op.startswith('I'):
            heapq.heappush(q, int(op[2:]))
            
        elif len(q) > 0:        
            if op == "D 1":
                q.remove(max(q))
                heapq.heapify(q)
            else:
                heapq.heappop(q)
            
    return [max(q), heapq.heappop(q)] if q else [0, 0]