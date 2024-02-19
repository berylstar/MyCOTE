from sys import stdin
input = stdin.readline

from itertools import combinations

little = [int(input()) for _ in range(9)]

for comb in combinations(little, 7):
    if sum(comb) == 100:
        print(*sorted(comb), sep="\n")
        break