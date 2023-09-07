def solution(players, callings):
    pd = {v:i for i,v in enumerate(players)}
    rd = {i:v for i,v in enumerate(players)}
    
    for now in callings:
        nowRank = pd[now]
        front = rd[nowRank - 1]
        
        pd[now], pd[front], rd[nowRank], rd[nowRank - 1] = pd[front], pd[now], rd[nowRank-1], rd[nowRank]
        
    return [rd[i] for i in range(len(players))]