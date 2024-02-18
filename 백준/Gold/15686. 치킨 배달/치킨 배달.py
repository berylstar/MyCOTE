from sys import stdin
input = stdin.readline

from itertools import combinations

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

chickens = []
houses = []
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
            curr = min(curr, abs(chickens[i][0] - house[0]) + abs(chickens[i][1] - house[1]))
        temp += curr

    answer = min(temp, answer)
print(answer)