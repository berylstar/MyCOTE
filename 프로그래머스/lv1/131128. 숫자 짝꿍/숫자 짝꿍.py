from collections import Counter
def solution(X, Y):
    answer = ''.join([i * min(Counter(X)[i], Counter(Y)[i]) for i in sorted(set(X) & set(Y), reverse=True)])
    
    if not answer:
        return '-1'
    if answer[0] == '0':
        return '0'
    else:
        return answer