from sys import stdin
input = stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

dic = {}

for num in numbers:
    dic[num] = dic.get(num, 0) + 1

answer = -1
for i in range(N+1):
    if dic.get(i, 0) == i:
        answer = max(answer, i)
print(answer)