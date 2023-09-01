def solution(k, m, score):
    apples = sorted(score, reverse=True)
    answer = 0
    # i = m - 1
    # while i < len(apples):
    #     answer += apples[i] * m
    #     i += m
    for i in range(m-1, len(apples), m):
        answer += apples[i] * m
    return answer