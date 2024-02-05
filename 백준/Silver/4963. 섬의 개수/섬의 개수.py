from sys import stdin
input = stdin.readline

from collections import deque

d = {0:[1,0], 1:[-1,0], 2:[0,1], 3:[0,-1], 4:[1,1], 5:[-1,1], 6:[1,-1], 7:[-1,-1]}

while True:
    w, h = map(int, input().split())

    if w == h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    q = deque()
    answer = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 0:
                continue

            answer += 1
            graph[i][j] = 0
            q.append((i, j))

            while q:
                x, y = q.popleft()

                for k in range(8):
                    nx = x + d[k][0]
                    ny = y + d[k][1]

                    if nx < 0 or nx >= h or ny < 0 or ny >= w:
                        continue

                    if graph[nx][ny] == 0:
                        continue

                    q.append((nx, ny))
                    graph[nx][ny] = 0
    print(answer)
