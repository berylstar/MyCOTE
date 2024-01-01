from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    numbers = list(map(int, input().split()))
    k = numbers[0]
    numbers = numbers[1:]

    if k == 0:
        break

    for comb in combinations(numbers, 6):
        print(*comb, sep=' ')
    print()