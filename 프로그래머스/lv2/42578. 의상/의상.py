def solution(clothes):
    d = {}
    for a, b in clothes:
        d[b] = d.get(b, 0) + 1
        
    answer = 1
    for i in d.values():
        answer *= (i + 1)
    return answer - 1