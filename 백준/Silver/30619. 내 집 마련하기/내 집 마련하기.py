from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))

house = {A[i] : i for i in range(N)}

for z in range(int(input())):
    left, right = map(int, input().split())
    changers = sorted([house[i] for i in range(left, right+1)])
    answer = A[:]
    index = 0
    for num in range(left, right+1):
        answer[changers[index]] = num
        index += 1
    print(*answer)