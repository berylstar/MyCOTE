import sys
input = sys.stdin.readline

T = int(input())
second = [300, 60, 10]
clicks = [0, 0, 0]

for i in range(3):
    clicks[i] = T // second[i]
    T %= second[i]
    
if T > 0:
    print(-1)
else:
    print(f"{clicks[0]} {clicks[1]} {clicks[2]}")