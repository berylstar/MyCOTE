import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ys = [0, 0]
    for i in range(9):
        rounds = list(map(int, input().split()))
        ys[0] += rounds[0]
        ys[1] += rounds[1]
    if ys[0] > ys[1]:
        print("Yonsei")
    elif ys[0] < ys[1]:
        print("Korea")
    else:
        print("Draw")