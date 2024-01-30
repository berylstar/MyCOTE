from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().split(',')))

for _ in range(K):
    for i in range(len(numbers) - 1):
        numbers[i] = numbers[i+1] - numbers[i]
    numbers.pop()
print(*numbers, sep=',')