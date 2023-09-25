def solution(numbers):
    stack = []
    answer = [-1 for _ in range(len(numbers))]
    
    for i, num in enumerate(numbers):
        while stack and stack[-1][1] < num:
            answer[stack.pop()[0]] = num
            
        stack.append([i, num])
    return answer