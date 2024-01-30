from sys import stdin
input = stdin.readline

N = int(input())
msg = input().rstrip()

arr = []
for i in range(0, len(msg), N):
    arr.append(list(msg[i:i+N]))

for i in range(len(arr)):
    if i % 2 != 0:
        data = list(reversed(arr[i]))
        arr[i] = data

print(''.join(arr[i][j] for j in range(N) for i in range(len(arr))))