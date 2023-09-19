def solution(progresses, speeds):
    temp = [(100 - progress) // speed + int((100-progress)%speed > 0) for progress, speed in zip(progresses, speeds)] + [1000]
    
    answer = []
    now = temp[0]
    cnt = 1
    
    for i, v in enumerate(temp[1:]):
        
        if v <= now:
            cnt += 1
        else:
            answer.append(cnt)
            now = temp[i+1]
            cnt = 1
            
    return answer