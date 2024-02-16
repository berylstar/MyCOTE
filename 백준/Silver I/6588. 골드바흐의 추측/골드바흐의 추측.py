from sys import stdin
input = stdin.readline

sosu = [True for i in range(1000001)]

for i in range(2, int(1000001 ** 0.5) + 1):
    if not sosu[i]:
        continue

    for j in range(i + i, 1000001, i):
        sosu[j] = False

while True:
    N = int(input())

    if N == 0:
        break

    for i in range(3, N // 2 + 1, 2):
        if sosu[i] and sosu[N - i]:
            print(f"{N} = {i} + {N - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")