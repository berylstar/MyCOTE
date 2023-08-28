def solution(s):
    d = {}
    answer = []
    for i, v in enumerate(s):
        answer.append(i - d.get(v, (i+1)))
        d[v] = i
    return answer