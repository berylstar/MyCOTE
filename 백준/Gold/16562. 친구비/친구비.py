import sys
input = sys.stdin.readline

from collections import deque

N, M, kk = map(int, input().split())
A = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x:int(x)-1, input().split())
    graph[a].append(b)
    graph[b].append(a)

waiting = sorted([[A[i], i] for i in range(len(A))], key=lambda x:(x[0], x[1]))
visited = [False for _ in range(N)]
k = kk

answer = 0
for money, index in waiting:
    if visited[index]:
        continue

    if k < money:
        break

    k -= money

    q = deque([index])
    while q:
        now = q.popleft()

        visited[now] = True

        for nxt in graph[now]:
            if not visited[nxt]:
                q.append(nxt)
else:
    answer = kk - k

print(answer or "Oh no")