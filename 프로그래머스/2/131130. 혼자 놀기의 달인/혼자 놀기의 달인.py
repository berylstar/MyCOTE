def solution(cards):
    visited = [False for _ in range(len(cards))]
    answer = []
    
    for i in range(len(cards)):
        j = cards[i] - 1
        count = 0
        while not visited[j]:
            count += 1
            visited[j] = True
            j = cards[j] - 1
            
        answer.append(count)
    answer.sort()
    return answer[-1] * answer[-2]