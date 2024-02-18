from sys import stdin
input = stdin.readline

from collections import deque
from itertools import combinations

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

chickens = deque()
houses = deque()
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            chickens.append((i, j))

answer = 2 * N * len(houses)
for comb in combinations(range(len(chickens)), M):
    temp = 0
    for house in houses:
        curr = 2 * N
        for i in comb:
            cx, cy = chickens[i][0], chickens[i][1]
            curr = min(curr, abs(cx - house[0]) + abs(cy - house[1]))
        temp += curr

    answer = min(temp, answer)
print(answer)