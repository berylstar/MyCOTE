N, K = map(int, input().split())

q = [i for i in range(1, N + 1)]
index = 0
answer = []

while q:
    index = (index + K - 1) % len(q)
    answer.append(q[index])
    q.pop(index)
    
print('<', ', '.join(map(str, answer)), '>', sep='')