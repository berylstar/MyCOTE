def solution(number, k):
    stack = []
    
    for s in number:
        
        while stack and k and int(stack[-1]) < int(s):
            stack.pop()
            k -= 1
        
        stack.append(s)
        
    while stack and k:
        stack.pop()
        k -= 1
    
    return ''.join(stack)