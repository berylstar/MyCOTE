def Rev(num):
    return int(str(num)[::-1])

from sys import stdin
input = stdin.readline

A, B = map(int, input().split())
print(Rev(Rev(A) + Rev(B)))