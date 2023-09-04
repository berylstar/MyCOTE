def solution(X, Y):    
    answer = ''.join([i * min(X.count(i), Y.count(i)) for i in sorted(set(X) & set(Y), reverse=True)])
    
    if not answer:
        return '-1'
    if answer[0] == '0':
        return '0'
    else:
        return answer