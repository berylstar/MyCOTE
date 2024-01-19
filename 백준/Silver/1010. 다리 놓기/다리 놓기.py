from sys import stdin
input = stdin.readline

import math

for _ in range(int(input())):
    A, B = map(int, input().split())
    print(math.comb(B, A))