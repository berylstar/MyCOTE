from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    clothes = {}

    for _ in range(int(input())):
        A, B = input().split()

        clothes[B] = clothes.get(B, []) + [A]

    answer = 1
    for cloth in clothes.keys():
        answer *= len(clothes[cloth]) + 1
    print(answer - 1)