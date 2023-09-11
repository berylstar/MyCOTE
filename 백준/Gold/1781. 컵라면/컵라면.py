import sys
input = sys.stdin.readline

import heapq

N = int(input())
lit = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:(x[0], -x[1]))

q = []
for i in lit:
    heapq.heappush(q, i[1])
    if i[0] < len(q):
        heapq.heappop(q)
print(sum(q))