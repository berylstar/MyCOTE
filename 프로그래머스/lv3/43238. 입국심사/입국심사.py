def solution(n, times):
    answer = 0
    times.sort()
    left, right = 1, times[-1] * n
    
    while left <= right:
        mid = (left + right) // 2
        people = 0
        
        for time in times:
            people += mid // time
            
            if people >= n:
                right = mid - 1
                break
        else:
            left = mid + 1
            
    return left