def solution(k, m, score):
    apples = sorted(score, reverse=True)
    return sum(apples[i] * m for i in range(m-1, len(apples), m))