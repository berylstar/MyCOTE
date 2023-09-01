def solution(k, m, score):
    apples = sorted(score, reverse=True)
    answer = 0
    i = m - 1
    while i < len(apples):
        answer += apples[i] * m
        i += m
    return answer