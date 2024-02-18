from sys import stdin
input = stdin.readline

from itertools import combinations

L, C = map(int, input().split())
words = list(map(str, input().split()))

vowels = {'a', 'e', 'i', 'o', 'u'}
answer = set()
for comb in combinations(words, L):
    cnt = 0
    for v in vowels:
        if v in comb:
            cnt += 1

    if cnt < 1 or L - cnt < 2:
        continue

    answer.add(''.join(sorted(comb)))

print(*sorted(answer), sep="\n")