from sys import stdin
input = stdin.readline

N = int(input())
people = sorted(map(int, input().split()))
print(sum(sum(people[:i+1]) for i in range(N)))