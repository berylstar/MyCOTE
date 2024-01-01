from itertools import combinations
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

print(sum(sum(1 for comb in combinations(numbers, i) if sum(comb) == S) for i in range(1, N+1)))