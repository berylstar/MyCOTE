def solution(babbling):
    d = {"ayaaya":"x", "yeye":"x", "woowoo":"x", "mama":"x", "aya":"0", "ye":"1", "woo":"2", "ma":"3"}
    answer = 0
    
    for b in babbling:
        for k in d.keys():
            b = b.replace(k, d[k])
        
        if b.isdigit():
            answer += 1
            
    return answer