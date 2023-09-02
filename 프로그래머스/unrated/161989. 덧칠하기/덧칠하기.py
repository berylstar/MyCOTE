def solution(n, m, section):
    answer = 0
    now = 0
    
    for sect in section:
        if now < sect:
            now = sect + m - 1
            answer += 1    
    return answer