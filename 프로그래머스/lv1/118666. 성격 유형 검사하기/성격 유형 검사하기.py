def solution(survey, choices):
    cnt = [0, 0, 0, 0]
    t = ['RT', 'CF', 'JM', 'AN']
    
    for sv, ch in zip(survey, choices):
        if sv in t:
            cnt[t.index(sv)] += ch-4
        else:
            cnt[t.index(sv[::-1])] += 4-ch
            
    return ''.join(t[i][cnt[i] > 0] for i in range(4))