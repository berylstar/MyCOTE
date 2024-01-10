import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(N)]

d = {0:[1, 0], 1:[-1, 0], 2:[0, 1], 3:[0, -1]}

q = deque()
q.append((0, 0, 1))

while q:
    x, y, c = q.popleft()

    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if graph[nx][ny] == 0:
            continue

        if graph[nx][ny] == 1:
            graph[nx][ny] = c + 1
            q.append((nx, ny, c+1))
print(graph[-1][-1])