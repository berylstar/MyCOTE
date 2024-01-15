from sys import stdin
input = stdin.readline

import heapq
Q = []
for _ in range(int(input())):
    num = int(input())
    
    if num == 0:
        if len(Q) > 0:
            print(heapq.heappop(Q)[1])
        else:
            print(0)
    else:
        heapq.heappush(Q, (abs(num), num))