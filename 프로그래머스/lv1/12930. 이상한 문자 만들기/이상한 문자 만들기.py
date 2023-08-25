def solution(s):
    answer = ""
    j = 0
    for i, c in enumerate(s):
        if c == " ":
            j = -1
        else:
            if j % 2 == 0:
                c = c.upper()
            else:
                c = c.lower()
                
        j += 1
        answer += c
    return answer