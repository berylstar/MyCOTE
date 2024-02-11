from sys import stdin
input = stdin.readline

N = int(input())
rooms = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x:(x[1], x[0]))

answer = 0
curr = -1
for start, end in rooms:
    if start < curr:
        continue
    answer += 1
    curr = end
print(answer)