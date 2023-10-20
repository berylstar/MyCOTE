from collections import deque
def solution(picks, minerals):
    mineralDict = {"diamond":[1, 5, 25], "iron":[1, 1, 5], "stone":[1, 1, 1]}
    
    q = deque()
    q.append((picks, minerals, 0))

    answer = []
    
    while q:
        np, nm, nc = q.popleft()
        for i in range(3):
            cp = np
            cm = nm
            cc = nc
            
            if sum(cp) == 0:
                answer.append(cc)
                continue

            if cp[i] < 1:
                continue

            if len(cm) == 0:
                answer.append(cc)
                continue
            
            cc += sum(mineralDict[mineral][i] for mineral in cm[:5])
            
            cp = [cp[j]-1 if i==j else cp[j] for j in range(len(cp))]
            cm = cm[5:]
            
            q.append((cp, cm, cc))
            
    return min(answer)