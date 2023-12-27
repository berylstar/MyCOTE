import sys
input = sys.stdin.readline

V = int(input())
A = input().count('A')
if A > V - A:
    print('A')
elif A == V - A:
    print("Tie")
else:
    print('B')