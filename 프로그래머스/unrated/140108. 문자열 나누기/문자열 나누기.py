def solution(s):
    answer = 0
    temp = [0, '']   # 갯수, 문자열
    
    for i, c in enumerate(s):
        temp[1] += c

        if c == temp[1][0]:
            temp[0] += 1

        elif temp[0] != 0 and len(temp[1]) >= temp[0] * 2:
            temp[1] = ''
            temp[0] = 0
            answer += 1
            
    return answer + int(temp[1] != '')