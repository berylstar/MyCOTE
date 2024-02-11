from sys import stdin
input = stdin.readline

N = int(input())
graph = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]

for i in range(1, N):
    for j in range(1, len(graph[i])-1):
        graph[i][j] += max(graph[i-1][j], graph[i-1][j-1])

print(max(graph[-1]))