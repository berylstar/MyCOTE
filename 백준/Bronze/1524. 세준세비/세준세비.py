from sys import stdin
inut = stdin.readline

for _ in range(int(input())):
    input()

    N, M = map(int, input().split())
    sejun = sorted(map(int, input().split()), reverse=True)
    sebi = sorted(map(int, input().split()), reverse=True)

    while sejun and sebi:
        if sebi[-1] > sejun[-1]:
            sejun.pop()
        else:
            sebi.pop()

    if sejun:
        print("S")
    elif sebi:
        print("B")
    else:
        print("C")