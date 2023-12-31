def DFS(texts):
    if len(texts) <= 1:
        return True
        
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

        nodes = len(texts) + 1
        need = bin(nodes)[3:]
        if '1' in need:
            texts = '0' * ((1 << len(need) + 1) - nodes) + texts
        
        answer.append(1 if DFS(texts) and texts != '0' else 0)
    return answer