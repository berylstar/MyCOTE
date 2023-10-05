def solution(number, k):
    stack = []
    
    for s in number:
        while stack and k and int(stack[-1]) < int(s):
            stack.pop()
            k -= 1
        
        stack.append(s)
        
    for _ in range(k):
        stack.pop()
    
    return ''.join(stack)