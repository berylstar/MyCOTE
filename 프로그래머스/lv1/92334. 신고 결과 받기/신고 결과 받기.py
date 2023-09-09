def solution(id_list, report, k):
    idxs = {v:i for i,v in enumerate(id_list)}
    ban = {_id:[] for _id in id_list}
    
    for repo in set(report):
        a, b = repo.split()
        ban[b] = ban.get(b, []) + [idxs[a]]
        
    answer = [0 for _ in range(len(id_list))]
        
    for b in ban:
        if len(ban[b]) >= k:
            for i in ban[b]:
                answer[i] += 1
    
    return answer