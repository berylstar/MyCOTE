from sys import stdin
input = stdin.readline

M, N, K = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    a, b, c, d = map(int, input().split())

    for i in range(b, d):
        for j in range(a, c):
            graph[i][j] = 1

from collections import deque
d = {0:[1,0], 1:[-1,0], 2:[0,1], 3:[0,-1]}
q = deque()
answer = []

for i in range(M):
    for j in range(N):
        if graph[i][j] > 0:
            continue

        curr = 1
        graph[i][j] = 1
        q.append((i, j))
        while q:
            x, y = q.popleft()

            for k in range(4):
                nx = x + d[k][0]
                ny = y + d[k][1]

                if nx<0 or nx>=M or ny<0 or ny>=N:
                    continue

                if graph[nx][ny] > 0:
                    continue

                q.append((nx, ny))
                graph[nx][ny] = 1
                curr += 1
                
        answer.append(curr)

print(len(answer))
print(*sorted(answer))