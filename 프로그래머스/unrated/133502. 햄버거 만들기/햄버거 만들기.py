def solution(ingredient):
    q = []
    answer = 0
    for i in ingredient:
        q.append(i)
        
        if len(q) >= 4 and q[-4:] == [1, 2, 3, 1]:
            answer += 1
            q.pop()
            q.pop()
            q.pop()
            q.pop()
            
    return answer