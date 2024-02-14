from sys import stdin
input = stdin.readline

from collections import deque

F, S, G, U, D = map(int, input().split()) # 최대, 현재, 목표, 위, 아래

q = deque()
sett = set()

q.append((S, 0))
sett.add(S)

while q:
    curr, count = q.popleft()
    
    if curr == G:
        print(count)
        exit(0)
    
    if curr - D > 0 and curr - D not in sett:
        q.append((curr - D, count + 1))
        sett.add(curr - D)
    if curr + U <= F and curr + U not in sett:
        q.append((curr + U, count + 1))
        sett.add(curr + U)
print("use the stairs")