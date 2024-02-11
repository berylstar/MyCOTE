from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
answer = set()

from collections import deque

q = deque()
q.append((A[0], 1, a, b, c, d)) # sum, index
while q:
    s, i, ca, cb, cc, cd = q.popleft()
    
    if i == N:
        answer.add(s)
        continue
    
    if ca > 0:
        q.append((s + A[i], i+1, ca-1, cb, cc, cd))
    if cb > 0:
        q.append((s - A[i], i+1, ca, cb-1, cc, cd))
    if cc > 0:
        q.append((s * A[i], i+1, ca, cb, cc-1, cd))
    if cd > 0:
        q.append((int(s / A[i]), i+1, ca, cb, cc, cd-1))

print(max(answer))
print(min(answer))