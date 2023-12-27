import sys
input = sys.stdin.readline

A = int(input())
B = input().rstrip()
C = int(input())

if B == "+":
    print(A + C)
else:
    print(A * C)