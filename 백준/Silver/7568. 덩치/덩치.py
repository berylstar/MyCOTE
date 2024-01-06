import sys
input = sys.stdin.readline

mans = []
T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    mans.append((A, B, i))
    
answer = []
for i in range(T):
    count = 1
    for j in range(T):
        if mans[i][0] < mans[j][0] and mans[i][1] < mans[j][1]:
            count += 1
    answer.append(count)
print(*answer, sep=" ")