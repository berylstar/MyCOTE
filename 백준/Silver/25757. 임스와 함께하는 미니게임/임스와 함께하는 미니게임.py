from sys import stdin
input = stdin.readline

N, game = input().split()
print(len(set(input().rstrip() for _ in range(int(N))))//{'Y':1, 'F':2, 'O':3}[game])