from collections import deque
def solution(x, y, n):
    q = deque()
    q.append([x, 0])
    
    allset = set()
    
    while q:
        num, cnt = q.popleft()
        
        if num in allset or num > y:
            continue
        
        allset.add(num)
        
        if num == y:
            return cnt
        
        q.append([num + n, cnt + 1])
        q.append([num * 2, cnt + 1])
        q.append([num * 3, cnt + 1])
        
    return -1