def solution(s):
    answer = 0
    count = 0
    now = ''
    
    for c in s:
        now += c

        if c == now[0]:
            count += 1

        elif count != 0 and len(now) >= count * 2:
            now = ''
            count = 0
            answer += 1
            
    return answer + int(now != '')