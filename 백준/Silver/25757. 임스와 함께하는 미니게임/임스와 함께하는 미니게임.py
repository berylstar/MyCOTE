from sys import stdin
input = stdin.readline

games = {'Y':1, 'F':2, 'O':3}

N, game = input().split()
mans = set(input().rstrip() for _ in range(int(N)))
print(len(mans)//games[game])