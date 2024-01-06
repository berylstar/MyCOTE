import sys
input = sys.stdin.readline
T = int(input())    
mans = [list(map(int, input().split())) for _ in range(T)]
answer = []
for i in range(T):
    count = 1
    for j in range(T):
        if mans[i][0] < mans[j][0] and mans[i][1] < mans[j][1]:
            count += 1
    answer.append(count)
print(*answer)