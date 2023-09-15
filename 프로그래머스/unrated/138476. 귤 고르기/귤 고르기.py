from collections import Counter
def solution(k, tangerine):
    c = sorted(Counter(tangerine).items(), key=lambda x:x[1])
    
    rem = len(tangerine) - k
    answer = len(c)
    
    for i in c:
        if rem < i[1]:
            return answer
        else:
            rem -= i[1]
            answer -= 1