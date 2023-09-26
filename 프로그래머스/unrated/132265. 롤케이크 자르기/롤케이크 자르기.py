from collections import Counter
def solution(topping):
    left = set()
    right = Counter(topping)
    answer = 0

    for v in topping:
        left.add(v)
        if right[v] == 1:
            del right[v]
        else:
            right[v] -= 1
        
        if len(left) == len(right):
            answer += 1
    
    return answer