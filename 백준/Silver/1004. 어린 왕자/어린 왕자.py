from sys import stdin
input = stdin.readline

def CheckInPath(x, y, a, b, r):
    return (a - x) ** 2 + (b - y) ** 2 <= r ** 2

for _ in range(int(input())):

    x1, y1, x2, y2 = map(int, input().split())
    ret = 0

    for _ in range(int(input())):
        a, b, r = map(int, input().split())
        ret += int(CheckInPath(x1, y1, a, b, r) ^ CheckInPath(x2, y2, a, b, r))

    print(ret)