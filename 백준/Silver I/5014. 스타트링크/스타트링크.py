from sys import stdin
input = stdin.readline

from collections import deque

F, S, G, U, D = map(int, input().split()) # 최대, 현재, 목표, 위, 아래

q = deque()
q.append((S, 0))

visited = [False for _ in range(F+1)]
visited[S] = True

while q:
    curr, count = q.popleft()
    
    if curr == G:
        print(count)
        exit(0)
    
    if curr - D > 0 and not visited[curr - D]:
        q.append((curr - D, count + 1))
        visited[curr - D] = True
    if curr + U <= F and not visited[curr + U]:
        q.append((curr + U, count + 1))
        visited[curr + U] = True
print("use the stairs")