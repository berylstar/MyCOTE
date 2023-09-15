def solution(elements):
    l = len(elements)
    elements += elements
    
    answer = []
    for i in range(1, l+1):
        for j in range(l):
            answer.append(sum(elements[j:j+i]))

    return len(set(answer))