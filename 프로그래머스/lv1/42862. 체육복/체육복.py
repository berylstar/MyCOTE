def solution(n, lost, reserve):
    lost, reserve = set(lost) - set(reserve), set(reserve) - set(lost)
    answer = n
    for st in sorted(lost):
                    
        if st-1 in reserve:
            reserve.remove(st-1)
            
        elif st+1 in reserve:
            reserve.remove(st+1)
            
        else:
            answer -= 1
            
    return answer       