from itertools import permutations
def solution(k, dungeons):
    N = len(dungeons)
    answer = 0
    
    for case in permutations(range(N)):
        now = k
        temp = 0
        for i in case:
            if now < dungeons[i][0]:
                break
                
            now -= dungeons[i][1]
            temp += 1
                
        answer = max(answer, temp)
        
    return answer