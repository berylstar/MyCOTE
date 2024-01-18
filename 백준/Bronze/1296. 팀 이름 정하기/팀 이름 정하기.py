from sys import stdin
input = stdin.readline

name = input().rstrip()
N = int(input())
li = sorted([input() for _ in range(N)])
max_p = max_i = 0
for i in range(N):
    L = name.count("L") + li[i].count("L")
    O = name.count("O") + li[i].count("O")
    V = name.count("V") + li[i].count("V")
    E = name.count("E") + li[i].count("E")
    p = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    if max_p < p:
        max_p = p
        max_i = i
print(li[max_i])