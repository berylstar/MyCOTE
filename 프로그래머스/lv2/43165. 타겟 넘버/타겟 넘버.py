from collections import deque
def solution(numbers, target):
    N = len(numbers)
    q = deque()
    q.append([0, []])
    answer = 0
    
    while q:
        i, count = q.popleft()
        
        if len(count) == N:
            if sum(count) == target:
                answer += 1
            continue
        
        q.append([i+1, count + [numbers[i]]])
        q.append([i+1, count + [-numbers[i]]])
        
    return answer