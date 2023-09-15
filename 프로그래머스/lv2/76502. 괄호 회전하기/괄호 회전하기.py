def CheckCorrect(s):
    stack = [0]
    d = {')':'(', ']':'[', '}':'{'}
    
    for i in s:
        if i in d.keys() and stack[-1] == d[i]:
            stack.pop()
        else:
            stack.append(i)
            
    return True if stack.pop()==0 else False

def solution(s):    
    return sum(1 for i in range(len(s)) if CheckCorrect(s[i:] + s[:i]))