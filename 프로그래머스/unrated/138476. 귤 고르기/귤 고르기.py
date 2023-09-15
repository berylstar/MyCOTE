from collections import Counter
def solution(k, tangerine):
#     c = sorted(Counter(tangerine).values())
    
#     rem = len(tangerine) - k
#     answer = len(c)
    
#     for i in c:
#         if rem < i:
#             return answer
#         else:
#             rem -= i
#             answer -= 1

    answer = 0
    for v in sorted(Counter(tangerine).values(), reverse=True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer