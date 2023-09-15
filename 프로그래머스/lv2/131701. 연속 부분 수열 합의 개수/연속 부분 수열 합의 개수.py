def solution(elements):
    l = len(elements)
    elements += elements
    return len(set([sum(elements[j:j+i]) for j in range(l) for i in range(1, l+1)]))