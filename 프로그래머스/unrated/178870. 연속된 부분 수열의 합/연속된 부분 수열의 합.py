from collections import deque
def solution(sequence, k):
    N = len(sequence)
    sequence.append(0)
    
    q = deque()
    _sum = sequence[0]
    
    answer = []
    
    l, r = 0, 1
    while l < N and r < N+1 and l <= r:
        if _sum < k:
            _sum += sequence[r]
            r += 1
        else:
            if _sum == k:
                answer.append([l, r-1])
            
            _sum -= sequence[l]
            l += 1
            
    return sorted(answer, key=lambda x:(x[1]-x[0]))[0]