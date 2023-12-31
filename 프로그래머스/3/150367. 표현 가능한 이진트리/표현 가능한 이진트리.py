def DFS(texts):
    if len(texts) <= 1:
        return True
    
    nodes = bin(len(texts) + 1)[2:]
    
    if '1' in nodes[1:]:
        dummies = (1 << len(nodes)) - int(nodes, 2)
        texts = '0' * dummies + texts
        
    N = len(texts) // 2
    
    if texts[N] == '0':
        if len(set(texts)) == 1:
            return True
        else:
            return False
    
    left = DFS(texts[:N])
    right = DFS(texts[N+1:])
    
    return left and right
    

def solution(numbers):
    answer = []
    for number in numbers:
        texts = bin(number)[2:]
        
        if DFS(texts) and texts != '0':
            answer.append(1)
        else:
            answer.append(0)
    return answer