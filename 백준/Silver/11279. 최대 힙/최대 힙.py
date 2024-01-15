from sys import stdin
input = stdin.readline

import heapq
Q = []

for _ in range(int(input())):
    msg = int(input())
    
    if msg == 0:
        print(-heapq.heappop(Q) if len(Q) > 0 else 0)
    else:
        heapq.heappush(Q, -msg)