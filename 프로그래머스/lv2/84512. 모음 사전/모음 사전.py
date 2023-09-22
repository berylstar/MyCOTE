from itertools import product
def solution(word):
    a = set()
    
    for i in range(1, 6):
        for j in product('AEIOU', repeat=i):
            a.add(''.join(j))
            
    d = {}
    for i, v in enumerate(sorted(a)):
        d[v] = i
    
    return d[word] + 1