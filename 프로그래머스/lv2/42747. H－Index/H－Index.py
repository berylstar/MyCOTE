def solution(citations):
    n = len(citations)
    
    for i, v in enumerate(sorted(citations)):        
        if v >= n-i:
            return n-i
    return 0