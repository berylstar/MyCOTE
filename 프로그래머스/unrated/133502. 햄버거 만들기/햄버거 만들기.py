def solution(ingredient):
    s = ""
    answer = 0
    for i in ingredient:
        s += str(i)
        
        if len(s) >= 4 and s[-4:] == "1231":
            answer += 1
            s = s[:-4]
            
    return answer