def solution(id_list, report, k):
    banned = { _id:[] for _id in id_list}
    
    for rep in set(report):
        a, b = rep.split()
        
        banned[b].append(id_list.index(a))
        
    ans = [0 for _ in range(len(id_list))]
        
    for ban in banned.keys():
        if len(banned[ban]) >= k:
            for i in banned[ban]:
                ans[i] += 1
    
    return ans