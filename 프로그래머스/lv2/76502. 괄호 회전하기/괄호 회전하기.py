def CheckCorrect(s):
    stack = [0]
    
    for i in s:
        if i == ')' and stack[-1] == '(':
            stack.pop()
        elif i == ']' and stack[-1] == '[':
            stack.pop()
        elif i == '}' and stack[-1] == '{':
            stack.pop()
        else:
            stack.append(i)
    return True if stack.pop()==0 else False

def solution(s):    
    return sum(1 for i in range(len(s)) if CheckCorrect(s[i:] + s[:i]))