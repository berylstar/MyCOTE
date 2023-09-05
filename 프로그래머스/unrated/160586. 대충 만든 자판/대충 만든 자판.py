def solution(keymap, targets):
    dic = {}
    for key in keymap:
        for i, c in enumerate(key, start=1):
            dic[c] = min(dic.get(c, 101), i)
            
    answer = []
    
    for target in targets:
        temp = 0
        
        for c in target:
            if c in dic:
                temp += dic[c]
            else:
                temp = -1
                break
            
        answer.append(temp)
        
    return answer