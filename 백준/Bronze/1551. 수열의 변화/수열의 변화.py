from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().split(',')))

for _ in range(K):
    for i in range(N - 1):
        numbers[i] = numbers[i+1] - numbers[i]
    numbers.pop()
    N -= 1
print(*numbers, sep=',')